# COGNIFLOW v2 — PERSISTENT DATA SCHEMA (FINAL)

**Status**: AUTHORITATIVE — SCHEMA FREEZE FOR COGNIFLOW v2  
**Depends on**: 
- COGNIFLOW v1 schemas (Session, Derived_Signal)
- COGNIFLOW_v2_CANONICAL_DEFINITIONS_FINAL.md

---

## SCHEMA: Longitudinal_Delta

```sql
CREATE TABLE Longitudinal_Delta (
  delta_id UUID PRIMARY KEY,
  student_id VARCHAR NOT NULL,
  session_id UUID NOT NULL REFERENCES Session(session_id),
  signal_name VARCHAR NOT NULL,
  delta_direction VARCHAR NOT NULL,
  created_utc TIMESTAMP NOT NULL
);
```

---

## Field Justifications

### `delta_id`
- Unique identifier for this delta record
- Primary key

### `student_id`
- Associates delta with a student
- Required for filtering v2 outputs by student
- **Denormalized from Session**: Stored here to enable student-scoped queries without joining Session table

### `session_id`
- Links to the Session this delta was computed for
- Foreign key to Session table
- This is the "current comparison target" session (not baseline)

### `signal_name`
- Identifies which v1 signal this delta corresponds to
- Allowed values (enforced by application logic):
  - `"planning_latency_seconds"`
  - `"iteration_depth"`
  - `"rewrite_ratio"`
- **NOT** an enum in schema to avoid database-level coupling

### `delta_direction`
- Stores the locked language string representing delta direction
- Allowed values (enforced by application logic):
  - `"More than your previous attempts"`
  - `"Less than before"`
  - `"No change detected"`
- **NOT** an enum to preserve exact phrasing flexibility

### `created_utc`
- Timestamp when this delta was computed
- Used for auditing only (not displayed to users)

---

## Intentionally Omitted Fields

### Numeric Deltas
**Fields NOT included**:
- `delta_value` (numeric difference)
- `percent_change`
- `absolute_difference`

**Reason**: Violates constitutional rule against collapsing behavior into scores. Only directional language is stored.

---

### Baseline Values
**Fields NOT included**:
- `baseline_min`
- `baseline_max`
- `baseline_median`
- `baseline_session_ids`

**Reason**: Baseline is computed on-demand from first 3 v2-eligible sessions. Storing it would introduce update complexity and staleness risk.

---

### Current Signal Value
**Fields NOT included**:
- `current_value`

**Reason**: Current value exists in Derived_Signal table. Duplicating it introduces consistency risk.

---

### Confidence or Reliability Indicators
**Fields NOT included**:
- `confidence_score`
- `reliability_flag`
- `sample_size`

**Reason**: Explicitly prohibited by TDD constitutional rules.

---

### Comparison Metadata
**Fields NOT included**:
- `baseline_count`
- `comparison_method`
- `envelope_width`

**Reason**: Computation method is locked in canonical definitions. Storing metadata implies variability.

---

### Student or Session Metadata
**Fields NOT included**:
- `problem_id`
- `session_start_utc`
- `visibility_code`

**Reason**: All metadata available via foreign key to Session table. Denormalization serves no purpose.

---

### Aggregation or Trend Fields
**Fields NOT included**:
- `consecutive_increases`
- `trend_direction`
- `streak_length`

**Reason**: v2 performs single current-vs-baseline comparison only. No multi-session trend tracking.

---

### Cross-Student Fields
**Fields NOT included**:
- `cohort_id`
- `class_id`
- `percentile_rank`
- `normalized_delta`

**Reason**: v2 deltas are strictly self-referential. Cross-student comparison is constitutionally prohibited.

---

## Structural Invariants

### One Record Per Signal Per Session

A given `(session_id, signal_name)` pair may have at most **one** Longitudinal_Delta record.

If a signal has NULL baseline or NULL current value, **no record is created**.

---

### Student Isolation

All queries on Longitudinal_Delta **must** filter by `student_id`.

No global aggregation across students is permitted.

---

### No Baseline Sessions

Longitudinal_Delta records are **never** created for sessions that are part of a student's baseline (first 3 v2-eligible sessions).

Only sessions beyond baseline have delta records.

---

## Query Constraints

### Allowed Queries

```sql
-- Get all deltas for a student
SELECT * FROM Longitudinal_Delta WHERE student_id = ?;

-- Get deltas for a specific session
SELECT * FROM Longitudinal_Delta WHERE session_id = ?;

-- Get deltas for a specific signal and student
SELECT * FROM Longitudinal_Delta WHERE student_id = ? AND signal_name = ?;
```

---

### Forbidden Queries

```sql
-- Cross-student aggregation (FORBIDDEN)
SELECT signal_name, delta_direction, COUNT(*) 
FROM Longitudinal_Delta 
GROUP BY signal_name, delta_direction;

-- Percentile ranking (FORBIDDEN)
SELECT PERCENT_RANK() OVER (ORDER BY created_utc) FROM Longitudinal_Delta;

-- Global statistics (FORBIDDEN)
SELECT AVG(...) FROM Longitudinal_Delta;
```

---

## FINAL NOTE

This schema is minimal by design.

If a question cannot be answered without adding a new field, COGNIFLOW v2 does not answer that question.

---

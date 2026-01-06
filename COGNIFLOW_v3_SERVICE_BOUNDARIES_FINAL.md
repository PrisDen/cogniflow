# COGNIFLOW v3 — SERVICE BOUNDARIES (FINAL)

**Status**: AUTHORITATIVE — v3 SERVICE FREEZE  
**Depends on**:
- COGNIFLOW v1 Service Boundaries
- COGNIFLOW v2 Service Boundaries
- COGNIFLOW_v3_CANONICAL_DEFINITIONS_FINAL.md
- COGNIFLOW_v3_SCHEMA_FINAL.md
- COGNIFLOW_v3_STABILITY_COMPUTATIONAL_LOGIC_FINAL.md

---

## NEW SERVICE: Stability Assessment Service

### Service Name
`StabilityAssessmentService`

---

### Owned Data (Write)
- `Stability_Assessment` (all fields)

---

### Owned Data (Read)
- `Session` (read-only: `session_id`, `student_id`, `session_start_utc`, `insight_eligible`)
- `Derived_Signal` (read-only: `planning_latency_seconds`, `iteration_depth`, `rewrite_ratio`)

---

### Allowed Operations

#### `assess_stability(session_id: UUID) -> void`

**Steps**:
1. Read Session record for `session_id`
2. If `session.insight_eligible == false`, return (no stability assessed)
3. Read all Sessions for `session.student_id` where `insight_eligible == true`
4. Sort by `session_start_utc` ascending
5. If total count < 5, return (insufficient history for v3)
6. Select last 5 sessions as stability window
7. If `session_id` is not the most recent session, return (only most recent gets assessed)
8. Read Derived_Signal records for stability window session IDs
9. Read Derived_Signal record for `session_id` (current)
10. For each v3-eligible signal (`planning_latency_seconds`, `iteration_depth`, `rewrite_ratio`):
    - Extract window values (list of 5)
    - Extract current value
    - Call stability computation function
    - If result is not NULL, create Stability_Assessment record
11. Persist all non-NULL stability records

---

### Explicitly Forbidden Operations

#### Data Access
- Reading `Event` table (any field)
- Reading `Insight` table
- Reading `Longitudinal_Delta` table
- Modifying `Session`
- Modifying `Derived_Signal`
- Modifying `Event`
- Modifying `Insight`
- Modifying `Longitudinal_Delta`

#### Computation
- Computing numeric deviations
- Storing envelope bounds (min/max)
- Applying statistical tests
- Trend detection or volatility scoring
- Cross-student aggregation
- Difficulty normalization
- Comparing stability across students

#### Orchestration
- Triggering any other service
- Background jobs or async execution
- Retry logic or queuing
- Client-facing queries

---

## Execution Order Relative to v1/v2 Pipeline

### v1 Pipeline (Unchanged)
1. Event Ingestion Service
2. Session Finalization Service
3. Signal Computation Service
4. Event Retention Service
5. Insight Creation Service

### v2 Addition (Unchanged)
6. Longitudinal Delta Computation Service

### v3 Addition

**After** Longitudinal Delta Computation Service completes:

7. **Stability Assessment Service** (new)

### Trigger Condition

`StabilityAssessmentService` is invoked if and only if:
- Session is insight-eligible (`insight_eligible == true`)
- Derived_Signal record exists for session

If session is not insight-eligible, v3 is skipped entirely.

---

## Data Flow Diagram

```
v1 Pipeline Output:
  Session (with insight_eligible flag)
  Derived_Signal (with v1 signals)
  ↓
v2 Pipeline Output:
  Longitudinal_Delta (directional deltas)
  ↓
StabilityAssessmentService:
  Reads: Session, Derived_Signal
  Computes: Stability window envelope, current comparison
  Writes: Stability_Assessment (locked language strings only)
  ↓
v3 Output:
  Stability_Assessment records (0-3 per session)
```

---

## Service Isolation

### No Backward Dependencies

`StabilityAssessmentService` does NOT:
- Modify v1 or v2 data
- Trigger v1 or v2 services
- Require v1 or v2 services to know about v3

v1 and v2 pipelines are completely unaware of v3's existence.

---

### No Forward Dependencies

`StabilityAssessmentService` does NOT:
- Serve client requests directly
- Expose API endpoints
- Trigger output services

Output services read `Stability_Assessment` independently.

---

## Updated Output Service Access

### Student Output Service (Modified)

**New Read Access**:
- `Stability_Assessment` (filtered by `student_id`)

**New Operation**:
- Project stability labels for student's own sessions
- Expose stability strings only (no signal names)

**Format**:
```json
{
  "problem_id": "...",
  "session_start_utc": "...",
  "is_completed": true,
  "longitudinal_deltas": [...],
  "stability": [
    "Within your usual range",
    "Outside your usual range",
    "Within your usual range"
  ]
}
```

---

### Teacher Output Service (Modified)

**New Read Access**:
- `Stability_Assessment` (filtered by teacher scope)

**New Operation**:
- Display stability assessments with signal names

**Format**:
```json
{
  "student_id": "...",
  "problem_id": "...",
  "session_start_utc": "...",
  "cues": [...],
  "longitudinal_deltas": [...],
  "stability": [
    {
      "signal_name": "planning_latency_seconds",
      "stability_label": "Within your usual range"
    },
    {
      "signal_name": "iteration_depth",
      "stability_label": "Outside your usual range"
    }
  ]
}
```

---

### No New Output Services

v3 does not introduce new output services.

Existing Student and Teacher output services are extended to read `Stability_Assessment`.

---

## Structural Invariants

### Sliding Window Behavior

The stability window is defined as:
- **Most recent 5 v3-eligible sessions** for the student
- Window is computed fresh for each current session
- Window excludes the current session being assessed
- Window sessions must all have valid Derived_Signal records

If student has exactly 5 v3-eligible sessions total:
- First 4 sessions form window
- 5th (most recent) session is current → produces stability records

If student has 6+ sessions:
- Sessions [count-5, count-1] form window
- Session [count] is current → produces stability records

---

### Silence Rules

v3 **must remain silent** (no records created) when:

1. **Insufficient history**: Student has < 5 v3-eligible sessions
2. **Non-recent session**: Session is not the most recent v3-eligible session
3. **All NULLs in window**: All 5 window sessions have NULL for a given signal
4. **Current NULL**: Current session has NULL for a given signal
5. **Ineligible signal**: `error_transition_pattern` (always silent)
6. **Non-eligible session**: `insight_eligible == false`

Default: **silence** (no Stability_Assessment record created).

---

### Minimum Session Requirements

| Scenario | v1 Insights | v2 Deltas | v3 Stability |
|----------|-------------|-----------|--------------|
| 1 session | Yes (if eligible) | No | No |
| 2 sessions | Yes (if eligible) | No | No |
| 3 sessions | Yes (if eligible) | No | No |
| 4 sessions | Yes (if eligible) | Yes (current vs 3-baseline) | No |
| 5 sessions | Yes (if eligible) | Yes (current vs 3-baseline) | Yes (current vs 5-window) |
| 6+ sessions | Yes (if eligible) | Yes (current vs 3-baseline) | Yes (current vs 5-window) |

---

### Window vs Baseline Distinction

| Aspect | v2 Baseline | v3 Window |
|--------|-------------|-----------|
| Size | Fixed 3 sessions | Fixed 5 sessions |
| Selection | First 3 eligible | Last 5 eligible |
| Immutability | Immutable (never changes) | Recomputed per session |
| Current session | 4th onward | 6th onward (if 6+ exist) |

**Critical difference**: v3 uses a **sliding window** (last 5), not a fixed baseline.

---

## Structural Enforcement

### Import Restrictions

`StabilityAssessmentService` may import:
- `/schemas/session.schema`
- `/schemas/derived_signal.schema`
- `/schemas/stability_assessment.schema`
- `/v3_stability_logic/*` (stability computation functions)

`StabilityAssessmentService` must NOT import:
- `/schemas/event.schema`
- `/schemas/insight.schema`
- `/schemas/longitudinal_delta.schema`
- Any v1 or v2 service
- Any signal computation logic

---

### Execution Isolation

`StabilityAssessmentService` executes synchronously after v2 Longitudinal Delta Computation Service.

If it fails, v1 and v2 data remain intact.

---

## Cross-Version Interaction

### v3 and v2 Comparison

Both v2 and v3 may produce output for the same session:

**v2 output**: Directional delta vs first 3 sessions (immutable baseline)  
**v3 output**: Stability vs last 5 sessions (sliding window)

These are **independent and non-contradictory**:
- v2: "More than your previous attempts" (vs sessions 1-3)
- v3: "Within your usual range" (vs sessions 5-9)

Both statements can be true simultaneously.

---

### Data Independence

- v3 does NOT read v2 Longitudinal_Delta records
- v2 does NOT read v3 Stability_Assessment records
- Both read the same v1 Session and Derived_Signal data
- No mutual dependency

---

## Final Note

This service is the **only** v3-specific internal service.

All other v3 behavior is achieved by:
- Pure stability computation functions (no service)
- Extended read access for existing output services

---

## UNDEFINED IN v3

The following are explicitly undefined and must not be implemented:

1. **Trend consistency**: v3 compares current to recent window only
2. **Volatility scoring**: No measurement of fluctuation magnitude
3. **Stability over time**: No multi-window or historical trend analysis
4. **Difficulty adjustment**: No normalization by problem complexity
5. **Institutional aggregation**: No cross-student stability metrics
6. **Predictive modeling**: No forecasting future stability
7. **Explanation generation**: No interpretation of why behavior is inside/outside range

---

**END OF v3 SERVICE BOUNDARIES**

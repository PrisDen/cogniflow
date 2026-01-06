# COGNIFLOW v2 — SERVICE BOUNDARIES (FINAL)

**Status**: AUTHORITATIVE — v2 SERVICE FREEZE  
**Depends on**:
- COGNIFLOW v1 Service Boundaries
- COGNIFLOW_v2_CANONICAL_DEFINITIONS_FINAL.md
- COGNIFLOW_v2_SCHEMA_FINAL.md
- COGNIFLOW_v2_DELTA_LOGIC_FINAL.md

---

## NEW SERVICE: Longitudinal Delta Computation Service

### Service Name
`LongitudinalDeltaComputationService`

---

### Owned Data (Write)
- `Longitudinal_Delta` (all fields)

---

### Owned Data (Read)
- `Session` (read-only: `session_id`, `student_id`, `session_start_utc`, `insight_eligible`)
- `Derived_Signal` (read-only: all signal fields)

---

### Allowed Operations

#### `compute_longitudinal_deltas(session_id: UUID) -> void`

**Steps**:
1. Read Session record for `session_id`
2. If `session.insight_eligible == false`, return (no deltas computed)
3. Read all Sessions for `session.student_id` where `insight_eligible == true`
4. Sort by `session_start_utc` ascending
5. If total count < 4, return (insufficient history for v2)
6. Identify first 3 sessions as baseline
7. If `session_id` is in baseline, return (no deltas for baseline sessions)
8. If `session_id` is not the most recent session, return (only most recent gets deltas)
9. Read Derived_Signal records for baseline session IDs
10. Read Derived_Signal record for `session_id` (current)
11. For each v2-eligible signal (`planning_latency_seconds`, `iteration_depth`, `rewrite_ratio`):
    - Extract baseline values (list of 3)
    - Extract current value
    - Call delta computation function
    - If result is not NULL, create Longitudinal_Delta record
12. Persist all non-NULL delta records

---

### Explicitly Forbidden Operations

#### Data Access
- Reading `Event` table (any field)
- Reading `Insight` table
- Modifying `Session`
- Modifying `Derived_Signal`
- Modifying `Event`
- Modifying `Insight`

#### Computation
- Computing numeric deltas
- Storing baseline values in Longitudinal_Delta
- Applying thresholds or statistical tests
- Cross-student aggregation
- Difficulty normalization

#### Orchestration
- Triggering any other service
- Background jobs or async execution
- Retry logic or queuing
- Client-facing queries

---

## Execution Order Relative to v1 Pipeline

### v1 Pipeline (Unchanged)
1. Event Ingestion Service
2. Session Finalization Service
3. Signal Computation Service
4. Event Retention Service
5. Insight Creation Service

### v2 Addition

**After** Insight Creation Service completes:

6. **Longitudinal Delta Computation Service** (new)

### Trigger Condition

`LongitudinalDeltaComputationService` is invoked if and only if:
- Session is insight-eligible (`insight_eligible == true`)
- Derived_Signal record exists for session

If session is not insight-eligible, v2 is skipped entirely.

---

## Data Flow Diagram

```
v1 Pipeline Output:
  Session (with insight_eligible flag)
  Derived_Signal (with v1 signals)
  ↓
LongitudinalDeltaComputationService:
  Reads: Session, Derived_Signal
  Computes: Baseline envelope, current comparison
  Writes: Longitudinal_Delta (directional strings only)
  ↓
v2 Output:
  Longitudinal_Delta records (0-3 per session)
```

---

## Service Isolation

### No Backward Dependencies

`LongitudinalDeltaComputationService` does NOT:
- Modify v1 data
- Trigger v1 services
- Require v1 services to know about v2

v1 pipeline is completely unaware of v2's existence.

---

### No Forward Dependencies

`LongitudinalDeltaComputationService` does NOT:
- Serve client requests directly
- Expose API endpoints
- Trigger output services

Output services read `Longitudinal_Delta` independently.

---

## Updated Output Service Access

### Student Output Service (Modified)

**New Read Access**:
- `Longitudinal_Delta` (filtered by `student_id`)

**New Operation**:
- Project delta records for student's own sessions

---

### Teacher Output Service (Modified)

**New Read Access**:
- `Longitudinal_Delta` (filtered by teacher scope)

**New Operation**:
- Display delta strings alongside v1 insights

---

### No New Output Services

v2 does not introduce new output services.

Existing Student and Teacher output services are extended to read `Longitudinal_Delta`.

---

## Structural Enforcement

### Import Restrictions

`LongitudinalDeltaComputationService` may import:
- `/schemas/session.schema`
- `/schemas/derived_signal.schema`
- `/schemas/longitudinal_delta.schema`
- `/v2_delta_logic/*` (delta computation functions)

`LongitudinalDeltaComputationService` must NOT import:
- `/schemas/event.schema`
- `/schemas/insight.schema`
- Any v1 service
- Any signal computation logic

---

### Execution Isolation

`LongitudinalDeltaComputationService` executes synchronously after v1 Insight Creation Service.

If it fails, v1 data remains intact.

---

## Final Note

This service is the **only** v2-specific internal service.

All other v2 behavior is achieved by:
- Pure delta computation functions (no service)
- Extended read access for existing output services

---

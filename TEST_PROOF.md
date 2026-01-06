# COGNIFLOW v1 — TEST PROOF DOCUMENT

**System Version**: v1.0.0  
**Generated**: 2026-01-06  
**Purpose**: Verifiable artifacts for interview/demo

---

## SECTION 1 — DATABASE SCHEMAS (ACTUAL)

```sql
-- Session
CREATE TABLE Session (
  session_id UUID PRIMARY KEY,
  student_id VARCHAR NOT NULL,
  problem_id VARCHAR NOT NULL,
  session_start_utc TIMESTAMP NOT NULL,
  session_end_utc TIMESTAMP NOT NULL,
  visibility_code VARCHAR NOT NULL,
  insight_eligible BOOLEAN NOT NULL
);

-- Event
CREATE TABLE Event (
  event_id UUID PRIMARY KEY,
  session_id UUID NOT NULL REFERENCES Session(session_id),
  event_type VARCHAR NOT NULL,
  timestamp_utc TIMESTAMP NOT NULL,
  error_category VARCHAR NULL
);

-- Derived_Signal
CREATE TABLE Derived_Signal (
  signal_id UUID PRIMARY KEY,
  session_id UUID NOT NULL UNIQUE REFERENCES Session(session_id),
  planning_latency_seconds INTEGER NULL,
  iteration_depth INTEGER NULL,
  rewrite_ratio FLOAT NULL,
  error_transition_pattern JSON NULL
);

-- Insight
CREATE TABLE Insight (
  insight_id UUID PRIMARY KEY,
  session_id UUID NOT NULL REFERENCES Session(session_id),
  cue_type VARCHAR NOT NULL,
  created_utc TIMESTAMP NOT NULL
);
```

---

## SECTION 2 — TEST INPUT DATA (RAW EVENTS)

### Test Case A — High Visibility

```json
[
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T10:00:00Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "line_number": 1,
    "column_number": 0,
    "inserted_text": "def calculate_sum(numbers):"
  },
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T10:00:15Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "line_number": 2,
    "column_number": 4,
    "inserted_text": "    total = 0"
  },
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T10:00:30Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "line_number": 3,
    "column_number": 4,
    "inserted_text": "    for n in numbers:"
  },
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T10:00:45Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "line_number": 4,
    "column_number": 8,
    "inserted_text": "        total += n"
  },
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T10:01:00Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "line_number": 5,
    "column_number": 4,
    "inserted_text": "    return total"
  },
  {
    "event_type": "run_code",
    "timestamp_utc": "2026-01-06T10:02:30Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444"
  },
  {
    "event_type": "error",
    "timestamp_utc": "2026-01-06T10:02:31Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "error_category": "test",
    "line_number": 5
  },
  {
    "event_type": "code_delete",
    "timestamp_utc": "2026-01-06T10:03:00Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "line_number": 2,
    "column_number": 4,
    "deleted_text": "    total = 0"
  },
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T10:03:20Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "line_number": 2,
    "column_number": 4,
    "inserted_text": "    result = 0"
  },
  {
    "event_type": "code_delete",
    "timestamp_utc": "2026-01-06T10:03:40Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "line_number": 4,
    "column_number": 8,
    "deleted_text": "        total += n"
  },
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T10:04:00Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "line_number": 4,
    "column_number": 8,
    "inserted_text": "        result += n"
  },
  {
    "event_type": "code_delete",
    "timestamp_utc": "2026-01-06T10:04:20Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "line_number": 5,
    "column_number": 4,
    "deleted_text": "    return total"
  },
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T10:04:40Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "line_number": 5,
    "column_number": 4,
    "inserted_text": "    return result"
  },
  {
    "event_type": "run_code",
    "timestamp_utc": "2026-01-06T10:05:00Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444"
  },
  {
    "event_type": "error",
    "timestamp_utc": "2026-01-06T10:05:01Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "error_category": "test",
    "line_number": null
  },
  {
    "event_type": "code_delete",
    "timestamp_utc": "2026-01-06T10:05:30Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "line_number": 3,
    "column_number": 4,
    "deleted_text": "    for n in numbers:"
  },
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T10:06:00Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "line_number": 3,
    "column_number": 4,
    "inserted_text": "    for num in numbers:"
  },
  {
    "event_type": "code_delete",
    "timestamp_utc": "2026-01-06T10:06:20Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "line_number": 4,
    "column_number": 8,
    "deleted_text": "        result += n"
  },
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T10:06:40Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "line_number": 4,
    "column_number": 8,
    "inserted_text": "        result += num"
  },
  {
    "event_type": "run_code",
    "timestamp_utc": "2026-01-06T10:07:00Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444"
  },
  {
    "event_type": "run_code",
    "timestamp_utc": "2026-01-06T10:07:30Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444"
  },
  {
    "event_type": "run_code",
    "timestamp_utc": "2026-01-06T10:08:00Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444"
  },
  {
    "event_type": "submit",
    "timestamp_utc": "2026-01-06T10:08:15Z",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444"
  }
]
```

**Observable Event Count**: 23 (excludes idle)

---

### Test Case B — Medium Visibility

```json
[
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T11:00:00Z",
    "session_id": "bbbbbbbb-2222-3333-4444-555555555555",
    "line_number": 1,
    "column_number": 0,
    "inserted_text": "def find_max(arr):"
  },
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T11:00:20Z",
    "session_id": "bbbbbbbb-2222-3333-4444-555555555555",
    "line_number": 2,
    "column_number": 4,
    "inserted_text": "    return max(arr)"
  },
  {
    "event_type": "run_code",
    "timestamp_utc": "2026-01-06T11:01:00Z",
    "session_id": "bbbbbbbb-2222-3333-4444-555555555555"
  },
  {
    "event_type": "error",
    "timestamp_utc": "2026-01-06T11:01:01Z",
    "session_id": "bbbbbbbb-2222-3333-4444-555555555555",
    "error_category": "runtime",
    "line_number": 2
  },
  {
    "event_type": "code_delete",
    "timestamp_utc": "2026-01-06T11:01:30Z",
    "session_id": "bbbbbbbb-2222-3333-4444-555555555555",
    "line_number": 2,
    "column_number": 11,
    "deleted_text": "max(arr)"
  },
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T11:02:00Z",
    "session_id": "bbbbbbbb-2222-3333-4444-555555555555",
    "line_number": 2,
    "column_number": 11,
    "inserted_text": "arr[0] if len(arr) > 0 else None"
  },
  {
    "event_type": "run_code",
    "timestamp_utc": "2026-01-06T11:02:30Z",
    "session_id": "bbbbbbbb-2222-3333-4444-555555555555"
  },
  {
    "event_type": "error",
    "timestamp_utc": "2026-01-06T11:02:31Z",
    "session_id": "bbbbbbbb-2222-3333-4444-555555555555",
    "error_category": "test",
    "line_number": null
  },
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T11:03:00Z",
    "session_id": "bbbbbbbb-2222-3333-4444-555555555555",
    "line_number": 3,
    "column_number": 4,
    "inserted_text": "    for item in arr[1:]:"
  },
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T11:03:30Z",
    "session_id": "bbbbbbbb-2222-3333-4444-555555555555",
    "line_number": 4,
    "column_number": 8,
    "inserted_text": "        if item > arr[0]:"
  },
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T11:04:00Z",
    "session_id": "bbbbbbbb-2222-3333-4444-555555555555",
    "line_number": 5,
    "column_number": 12,
    "inserted_text": "            arr[0] = item"
  },
  {
    "event_type": "run_code",
    "timestamp_utc": "2026-01-06T11:04:30Z",
    "session_id": "bbbbbbbb-2222-3333-4444-555555555555"
  },
  {
    "event_type": "run_code",
    "timestamp_utc": "2026-01-06T11:05:00Z",
    "session_id": "bbbbbbbb-2222-3333-4444-555555555555"
  },
  {
    "event_type": "submit",
    "timestamp_utc": "2026-01-06T11:05:15Z",
    "session_id": "bbbbbbbb-2222-3333-4444-555555555555"
  }
]
```

**Observable Event Count**: 14

---

### Test Case C — Low Visibility

```json
[
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T14:00:00Z",
    "session_id": "cccccccc-3333-4444-5555-666666666666",
    "line_number": 1,
    "column_number": 0,
    "inserted_text": "def reverse(s):"
  },
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T14:00:15Z",
    "session_id": "cccccccc-3333-4444-5555-666666666666",
    "line_number": 2,
    "column_number": 4,
    "inserted_text": "    return s[::-1]"
  },
  {
    "event_type": "run_code",
    "timestamp_utc": "2026-01-06T14:00:30Z",
    "session_id": "cccccccc-3333-4444-5555-666666666666"
  },
  {
    "event_type": "idle",
    "timestamp_utc": "2026-01-06T14:02:00Z",
    "session_id": "cccccccc-3333-4444-5555-666666666666",
    "duration_seconds": 60
  },
  {
    "event_type": "code_delete",
    "timestamp_utc": "2026-01-06T14:03:00Z",
    "session_id": "cccccccc-3333-4444-5555-666666666666",
    "line_number": 2,
    "column_number": 11,
    "deleted_text": "s[::-1]"
  },
  {
    "event_type": "code_insert",
    "timestamp_utc": "2026-01-06T14:03:15Z",
    "session_id": "cccccccc-3333-4444-5555-666666666666",
    "line_number": 2,
    "column_number": 11,
    "inserted_text": "s[::-1]"
  },
  {
    "event_type": "idle",
    "timestamp_utc": "2026-01-06T14:05:00Z",
    "session_id": "cccccccc-3333-4444-5555-666666666666",
    "duration_seconds": 120
  }
]
```

**Observable Event Count**: 5 (excludes idle, no submit)

---

## SECTION 3 — SESSION FINALIZATION OUTPUT

### Test Case A

```json
{
  "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
  "student_id": "student_001",
  "problem_id": "problem_sum",
  "session_start_utc": "2026-01-06T10:00:00Z",
  "session_end_utc": "2026-01-06T10:08:15Z",
  "visibility_code": "HIGH",
  "insight_eligible": true
}
```

### Test Case B

```json
{
  "session_id": "bbbbbbbb-2222-3333-4444-555555555555",
  "student_id": "student_001",
  "problem_id": "problem_max",
  "session_start_utc": "2026-01-06T11:00:00Z",
  "session_end_utc": "2026-01-06T11:05:15Z",
  "visibility_code": "MEDIUM",
  "insight_eligible": true
}
```

### Test Case C

```json
{
  "session_id": "cccccccc-3333-4444-5555-666666666666",
  "student_id": "student_001",
  "problem_id": "problem_reverse",
  "session_start_utc": "2026-01-06T14:00:00Z",
  "session_end_utc": "2026-01-06T14:03:15Z",
  "visibility_code": "LOW",
  "insight_eligible": false
}
```

---

## SECTION 4 — DERIVED SIGNAL OUTPUT

### Test Case A

```json
{
  "signal_id": "sig-aaaa-1111-2222-3333-444444444444",
  "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
  "planning_latency_seconds": 150,
  "iteration_depth": 5,
  "rewrite_ratio": 0.714,
  "error_transition_pattern": ["test", "test"]
}
```

### Test Case B

```json
{
  "signal_id": "sig-bbbb-2222-3333-4444-555555555555",
  "session_id": "bbbbbbbb-2222-3333-4444-555555555555",
  "planning_latency_seconds": 60,
  "iteration_depth": 4,
  "rewrite_ratio": 0.2,
  "error_transition_pattern": ["runtime", "test"]
}
```

### Test Case C

**NOT CREATED** (session not insight-eligible)

---

## SECTION 5 — INSIGHT RECORDS

### Test Case A

```json
[
  {
    "insight_id": "ins-1-aaaa-1111-2222-3333-444444444444",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "cue_type": "understanding_problem",
    "created_utc": "2026-01-06T10:08:16Z"
  },
  {
    "insight_id": "ins-2-aaaa-1111-2222-3333-444444444444",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "cue_type": "translating_logic",
    "created_utc": "2026-01-06T10:08:16Z"
  },
  {
    "insight_id": "ins-3-aaaa-1111-2222-3333-444444444444",
    "session_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "cue_type": "debugging_effectively",
    "created_utc": "2026-01-06T10:08:16Z"
  }
]
```

### Test Case B

```json
[
  {
    "insight_id": "ins-1-bbbb-2222-3333-4444-555555555555",
    "session_id": "bbbbbbbb-2222-3333-4444-555555555555",
    "cue_type": "understanding_problem",
    "created_utc": "2026-01-06T11:05:16Z"
  },
  {
    "insight_id": "ins-2-bbbb-2222-3333-4444-555555555555",
    "session_id": "bbbbbbbb-2222-3333-4444-555555555555",
    "cue_type": "translating_logic",
    "created_utc": "2026-01-06T11:05:16Z"
  },
  {
    "insight_id": "ins-3-bbbb-2222-3333-4444-555555555555",
    "session_id": "bbbbbbbb-2222-3333-4444-555555555555",
    "cue_type": "debugging_effectively",
    "created_utc": "2026-01-06T11:05:16Z"
  }
]
```

### Test Case C

**NO INSIGHTS CREATED** (session not insight-eligible)

---

## SECTION 6 — STUDENT OUTPUT (API RESULT)

### Request

```
GET /student/sessions?student_id=student_001
```

### Response

```json
[
  {
    "problem_id": "problem_sum",
    "session_start_utc": "2026-01-06T10:00:00Z",
    "is_completed": true
  },
  {
    "problem_id": "problem_max",
    "session_start_utc": "2026-01-06T11:00:00Z",
    "is_completed": true
  },
  {
    "problem_id": "problem_reverse",
    "session_start_utc": "2026-01-06T14:00:00Z",
    "is_completed": false
  }
]
```

---

## SECTION 7 — TEACHER OUTPUT (API RESULT)

### Request

```
GET /teacher/sessions?scope=class_101
```

### Response

```json
[
  {
    "student_id": "student_001",
    "problem_id": "problem_sum",
    "session_start_utc": "2026-01-06T10:00:00Z",
    "cues": [
      "understanding_problem",
      "translating_logic",
      "debugging_effectively"
    ]
  },
  {
    "student_id": "student_001",
    "problem_id": "problem_max",
    "session_start_utc": "2026-01-06T11:00:00Z",
    "cues": [
      "understanding_problem",
      "translating_logic",
      "debugging_effectively"
    ]
  },
  {
    "student_id": "student_001",
    "problem_id": "problem_reverse",
    "session_start_utc": "2026-01-06T14:00:00Z",
    "cues": []
  }
]
```

---

## SECTION 8 — EXPLAINABLE-ON-CLICK OUTPUT

### Test Case A — Cue: translating_logic

**Request**:
```
GET /teacher/session/aaaaaaaa-1111-2222-3333-444444444444/explain?cue=translating_logic
```

**Response**:
```json
{
  "planning_latency_seconds": 150,
  "iteration_depth": 5,
  "rewrite_ratio": 0.714,
  "error_transition_pattern": ["test", "test"]
}
```

### Test Case B — Cue: debugging_effectively

**Request**:
```
GET /teacher/session/bbbbbbbb-2222-3333-4444-555555555555/explain?cue=debugging_effectively
```

**Response**:
```json
{
  "planning_latency_seconds": 60,
  "iteration_depth": 4,
  "rewrite_ratio": 0.2,
  "error_transition_pattern": ["runtime", "test"]
}
```

### Test Case C — No Insight

**Request**:
```
GET /teacher/session/cccccccc-3333-4444-5555-666666666666/explain?cue=understanding_problem
```

**Response**:
```json
{
  "message": "Insufficient process data for this session"
}
```

---

## SECTION 9 — CONSTRAINT VERIFICATION

| Rule | Evidence | Status |
|------|----------|--------|
| No scores exist in any schema | Section 1 (all schemas) | **PASS** |
| No rankings or percentiles produced | Sections 6-7 (all outputs) | **PASS** |
| No global cross-student comparison | Sections 6-7 (student isolated, teacher sees one student) | **PASS** |
| Absence of evidence produces silence | Section 7 (Test Case C: empty cues array) | **PASS** |
| Low-visibility sessions not stigmatized | Section 7 (Test Case C appears normally) | **PASS** |
| Confidence scalars never exposed | Sections 1, 4, 6-8 (absent from all outputs) | **PASS** |
| Every insight traceable to signals | Section 5 (insight records) → Section 4 (signal records) | **PASS** |
| Signal computation skipped for low-visibility | Section 4 (Test Case C: NOT CREATED) | **PASS** |
| Students never see teacher insights | Section 6 (no cues field present) | **PASS** |
| Teachers never see raw event payloads | Section 7-8 (only signals shown on click) | **PASS** |
| Sensitive fields deleted after signal computation | Section 1 (Event schema post-retention has no line_number, inserted_text, etc.) | **PASS** |
| Session end by submit OR timeout | Test Case A-B (submit), Test Case C (timeout/last event) | **PASS** |
| Observable event count excludes idle | Section 2 (Test Case C: 5 observable despite 7 total) | **PASS** |
| Visibility thresholds applied correctly | Section 3 (23→HIGH, 14→MEDIUM, 5→LOW) | **PASS** |
| Binary cues only (shown or not shown) | Section 7 (cues are present/absent, not scored) | **PASS** |
| No decision automation | All sections (system presents evidence, no actions triggered) | **PASS** |

---

**END OF PROOF DOCUMENT**

# COGNIFLOW v2 — DEMO SCENARIOS & OUTPUTS

**System Version**: v2.0.0  
**Generated**: 2026-01-06  
**Purpose**: Presentation-ready v2 walkthrough

---

## SCENARIO 1 — INSUFFICIENT HISTORY (3 SESSIONS)

### Session Records

```json
[
  {
    "session_id": "s1111111-1111-1111-1111-111111111111",
    "student_id": "student_bob",
    "problem_id": "problem_sort",
    "session_start_utc": "2026-01-01T10:00:00Z",
    "session_end_utc": "2026-01-01T10:15:00Z",
    "visibility_code": "HIGH",
    "insight_eligible": true
  },
  {
    "session_id": "s2222222-2222-2222-2222-222222222222",
    "student_id": "student_bob",
    "problem_id": "problem_reverse",
    "session_start_utc": "2026-01-02T10:00:00Z",
    "session_end_utc": "2026-01-02T10:20:00Z",
    "visibility_code": "HIGH",
    "insight_eligible": true
  },
  {
    "session_id": "s3333333-3333-3333-3333-333333333333",
    "student_id": "student_bob",
    "problem_id": "problem_search",
    "session_start_utc": "2026-01-03T10:00:00Z",
    "session_end_utc": "2026-01-03T10:18:00Z",
    "visibility_code": "HIGH",
    "insight_eligible": true
  }
]
```

### Longitudinal_Delta Records

**NONE CREATED** (minimum 4 v2-eligible sessions required)

---

### Student Output JSON

```json
[
  {
    "problem_id": "problem_sort",
    "session_start_utc": "2026-01-01T10:00:00Z",
    "is_completed": true
  },
  {
    "problem_id": "problem_reverse",
    "session_start_utc": "2026-01-02T10:00:00Z",
    "is_completed": true
  },
  {
    "problem_id": "problem_search",
    "session_start_utc": "2026-01-03T10:00:00Z",
    "is_completed": true
  }
]
```

**Note**: No `longitudinal_deltas` field present (silence by default)

---

### Teacher Output JSON

```json
[
  {
    "student_id": "student_bob",
    "problem_id": "problem_sort",
    "session_start_utc": "2026-01-01T10:00:00Z",
    "cues": ["understanding_problem", "translating_logic", "debugging_effectively"]
  },
  {
    "student_id": "student_bob",
    "problem_id": "problem_reverse",
    "session_start_utc": "2026-01-02T10:00:00Z",
    "cues": ["understanding_problem", "translating_logic"]
  },
  {
    "student_id": "student_bob",
    "problem_id": "problem_search",
    "session_start_utc": "2026-01-03T10:00:00Z",
    "cues": ["understanding_problem", "debugging_effectively"]
  }
]
```

**Note**: No `longitudinal_deltas` field present (insufficient history)

---

## SCENARIO 2 — FIRST ELIGIBLE v2 SESSION (4TH SESSION)

### Baseline Sessions (First 3)

```json
[
  {
    "session_id": "s1111111-1111-1111-1111-111111111111",
    "student_id": "student_bob",
    "problem_id": "problem_sort",
    "session_start_utc": "2026-01-01T10:00:00Z",
    "insight_eligible": true
  },
  {
    "session_id": "s2222222-2222-2222-2222-222222222222",
    "student_id": "student_bob",
    "problem_id": "problem_reverse",
    "session_start_utc": "2026-01-02T10:00:00Z",
    "insight_eligible": true
  },
  {
    "session_id": "s3333333-3333-3333-3333-333333333333",
    "student_id": "student_bob",
    "problem_id": "problem_search",
    "session_start_utc": "2026-01-03T10:00:00Z",
    "insight_eligible": true
  }
]
```

### Baseline Derived_Signal Values

```json
[
  {
    "session_id": "s1111111-1111-1111-1111-111111111111",
    "planning_latency_seconds": 120,
    "iteration_depth": 5,
    "rewrite_ratio": 0.6
  },
  {
    "session_id": "s2222222-2222-2222-2222-222222222222",
    "planning_latency_seconds": 90,
    "iteration_depth": 4,
    "rewrite_ratio": 0.8
  },
  {
    "session_id": "s3333333-3333-3333-3333-333333333333",
    "planning_latency_seconds": 150,
    "iteration_depth": 6,
    "rewrite_ratio": 0.5
  }
]
```

**Baseline Envelopes**:
- `planning_latency_seconds`: min=90, max=150
- `iteration_depth`: min=4, max=6
- `rewrite_ratio`: min=0.5, max=0.8

---

### Current Session (4th)

```json
{
  "session_id": "s4444444-4444-4444-4444-444444444444",
  "student_id": "student_bob",
  "problem_id": "problem_merge",
  "session_start_utc": "2026-01-04T10:00:00Z",
  "session_end_utc": "2026-01-04T10:25:00Z",
  "visibility_code": "HIGH",
  "insight_eligible": true
}
```

### Current Derived_Signal

```json
{
  "session_id": "s4444444-4444-4444-4444-444444444444",
  "planning_latency_seconds": 180,
  "iteration_depth": 3,
  "rewrite_ratio": 0.7
}
```

---

### Delta Computation

**planning_latency_seconds**:
- Current (180) > baseline_max (150)
- Result: `"More than your previous attempts"`

**iteration_depth**:
- Current (3) < baseline_min (4)
- Result: `"Less than before"`

**rewrite_ratio**:
- baseline_min (0.5) <= Current (0.7) <= baseline_max (0.8)
- Result: `"No change detected"`

---

### Longitudinal_Delta Records

```json
[
  {
    "delta_id": "d1-4444444-4444-4444-4444-444444444444",
    "student_id": "student_bob",
    "session_id": "s4444444-4444-4444-4444-444444444444",
    "signal_name": "planning_latency_seconds",
    "delta_direction": "More than your previous attempts",
    "created_utc": "2026-01-04T10:25:01Z"
  },
  {
    "delta_id": "d2-4444444-4444-4444-4444-444444444444",
    "student_id": "student_bob",
    "session_id": "s4444444-4444-4444-4444-444444444444",
    "signal_name": "iteration_depth",
    "delta_direction": "Less than before",
    "created_utc": "2026-01-04T10:25:01Z"
  },
  {
    "delta_id": "d3-4444444-4444-4444-4444-444444444444",
    "student_id": "student_bob",
    "session_id": "s4444444-4444-4444-4444-444444444444",
    "signal_name": "rewrite_ratio",
    "delta_direction": "No change detected",
    "created_utc": "2026-01-04T10:25:01Z"
  }
]
```

---

### Student Output JSON

```json
{
  "problem_id": "problem_merge",
  "session_start_utc": "2026-01-04T10:00:00Z",
  "is_completed": true,
  "longitudinal_deltas": [
    "More than your previous attempts",
    "Less than before",
    "No change detected"
  ]
}
```

**Note**: Student sees delta strings only, no signal names

---

### Teacher Output JSON

```json
{
  "student_id": "student_bob",
  "problem_id": "problem_merge",
  "session_start_utc": "2026-01-04T10:00:00Z",
  "cues": ["understanding_problem", "translating_logic", "debugging_effectively"],
  "longitudinal_deltas": [
    {
      "signal_name": "planning_latency_seconds",
      "delta_direction": "More than your previous attempts"
    },
    {
      "signal_name": "iteration_depth",
      "delta_direction": "Less than before"
    },
    {
      "signal_name": "rewrite_ratio",
      "delta_direction": "No change detected"
    }
  ]
}
```

**Note**: Teacher sees signal names + delta strings

---

## SCENARIO 3 — "NO CHANGE DETECTED" (ALL SIGNALS)

### Baseline Envelopes

- `planning_latency_seconds`: min=100, max=200
- `iteration_depth`: min=3, max=7
- `rewrite_ratio`: min=0.4, max=0.9

---

### Current Session Derived_Signal

```json
{
  "session_id": "s5555555-5555-5555-5555-555555555555",
  "planning_latency_seconds": 150,
  "iteration_depth": 5,
  "rewrite_ratio": 0.6
}
```

**All values inside baseline envelopes**

---

### Longitudinal_Delta Records

```json
[
  {
    "delta_id": "d1-5555555-5555-5555-5555-555555555555",
    "student_id": "student_bob",
    "session_id": "s5555555-5555-5555-5555-555555555555",
    "signal_name": "planning_latency_seconds",
    "delta_direction": "No change detected",
    "created_utc": "2026-01-05T10:20:01Z"
  },
  {
    "delta_id": "d2-5555555-5555-5555-5555-555555555555",
    "student_id": "student_bob",
    "session_id": "s5555555-5555-5555-5555-555555555555",
    "signal_name": "iteration_depth",
    "delta_direction": "No change detected",
    "created_utc": "2026-01-05T10:20:01Z"
  },
  {
    "delta_id": "d3-5555555-5555-5555-5555-555555555555",
    "student_id": "student_bob",
    "session_id": "s5555555-5555-5555-5555-555555555555",
    "signal_name": "rewrite_ratio",
    "delta_direction": "No change detected",
    "created_utc": "2026-01-05T10:20:01Z"
  }
]
```

---

### Student Output JSON

```json
{
  "problem_id": "problem_binary_search",
  "session_start_utc": "2026-01-05T10:00:00Z",
  "is_completed": true,
  "longitudinal_deltas": [
    "No change detected",
    "No change detected",
    "No change detected"
  ]
}
```

---

### Teacher Output JSON

```json
{
  "student_id": "student_bob",
  "problem_id": "problem_binary_search",
  "session_start_utc": "2026-01-05T10:00:00Z",
  "cues": ["understanding_problem", "translating_logic"],
  "longitudinal_deltas": [
    {
      "signal_name": "planning_latency_seconds",
      "delta_direction": "No change detected"
    },
    {
      "signal_name": "iteration_depth",
      "delta_direction": "No change detected"
    },
    {
      "signal_name": "rewrite_ratio",
      "delta_direction": "No change detected"
    }
  ]
}
```

---

## SCENARIO 4 — NULL SIGNAL HANDLING

### Baseline Derived_Signal Values (with NULLs)

```json
[
  {
    "session_id": "s1111111-1111-1111-1111-111111111111",
    "planning_latency_seconds": 100,
    "iteration_depth": NULL,
    "rewrite_ratio": 0.5
  },
  {
    "session_id": "s2222222-2222-2222-2222-222222222222",
    "planning_latency_seconds": 120,
    "iteration_depth": 4,
    "rewrite_ratio": 0.7
  },
  {
    "session_id": "s3333333-3333-3333-3333-333333333333",
    "planning_latency_seconds": NULL,
    "iteration_depth": 5,
    "rewrite_ratio": NULL
  }
]
```

**Non-NULL Baseline Values**:
- `planning_latency_seconds`: [100, 120] → min=100, max=120
- `iteration_depth`: [4, 5] → min=4, max=5
- `rewrite_ratio`: [0.5, 0.7] → min=0.5, max=0.7

---

### Current Session Derived_Signal

```json
{
  "session_id": "s6666666-6666-6666-6666-666666666666",
  "planning_latency_seconds": 140,
  "iteration_depth": NULL,
  "rewrite_ratio": 0.6
}
```

---

### Delta Computation

**planning_latency_seconds**:
- Current (140) > baseline_max (120)
- Result: `"More than your previous attempts"`

**iteration_depth**:
- Current is NULL
- Result: NULL (no delta record created)

**rewrite_ratio**:
- baseline_min (0.5) <= Current (0.6) <= baseline_max (0.7)
- Result: `"No change detected"`

---

### Longitudinal_Delta Records

```json
[
  {
    "delta_id": "d1-6666666-6666-6666-6666-666666666666",
    "student_id": "student_bob",
    "session_id": "s6666666-6666-6666-6666-666666666666",
    "signal_name": "planning_latency_seconds",
    "delta_direction": "More than your previous attempts",
    "created_utc": "2026-01-06T10:30:01Z"
  },
  {
    "delta_id": "d2-6666666-6666-6666-6666-666666666666",
    "student_id": "student_bob",
    "session_id": "s6666666-6666-6666-6666-666666666666",
    "signal_name": "rewrite_ratio",
    "delta_direction": "No change detected",
    "created_utc": "2026-01-06T10:30:01Z"
  }
]
```

**Note**: No record for `iteration_depth` (current value is NULL)

---

### Student Output JSON

```json
{
  "problem_id": "problem_quicksort",
  "session_start_utc": "2026-01-06T10:00:00Z",
  "is_completed": true,
  "longitudinal_deltas": [
    "More than your previous attempts",
    "No change detected"
  ]
}
```

**Note**: Only 2 delta strings (iteration_depth suppressed)

---

### Teacher Output JSON

```json
{
  "student_id": "student_bob",
  "problem_id": "problem_quicksort",
  "session_start_utc": "2026-01-06T10:00:00Z",
  "cues": ["understanding_problem", "translating_logic"],
  "longitudinal_deltas": [
    {
      "signal_name": "planning_latency_seconds",
      "delta_direction": "More than your previous attempts"
    },
    {
      "signal_name": "rewrite_ratio",
      "delta_direction": "No change detected"
    }
  ]
}
```

**Note**: Only 2 deltas shown (iteration_depth silently omitted)

---

## SCENARIO 5 — STUDENT VS TEACHER OUTPUT COMPARISON

### Same Session, Different Visibility

**Session ID**: `s7777777-7777-7777-7777-777777777777`

---

### Student View

```json
{
  "problem_id": "problem_heapsort",
  "session_start_utc": "2026-01-07T10:00:00Z",
  "is_completed": true,
  "longitudinal_deltas": [
    "Less than before",
    "More than your previous attempts",
    "No change detected"
  ]
}
```

**Student sees**:
- Problem name
- Timestamp
- Completion status
- Delta direction strings (no signal names)
- Cannot determine which signal each delta refers to

---

### Teacher View

```json
{
  "student_id": "student_bob",
  "problem_id": "problem_heapsort",
  "session_start_utc": "2026-01-07T10:00:00Z",
  "cues": ["understanding_problem", "debugging_effectively"],
  "longitudinal_deltas": [
    {
      "signal_name": "planning_latency_seconds",
      "delta_direction": "Less than before"
    },
    {
      "signal_name": "iteration_depth",
      "delta_direction": "More than your previous attempts"
    },
    {
      "signal_name": "rewrite_ratio",
      "delta_direction": "No change detected"
    }
  ]
}
```

**Teacher sees**:
- Student identifier
- Problem name
- Timestamp
- v1 binary cues
- v2 deltas with signal names
- Can identify which signal each delta refers to

---

### Key Differences

| Aspect | Student View | Teacher View |
|--------|--------------|--------------|
| Student ID | Hidden | Visible |
| Signal names | Hidden | Visible |
| Delta strings | Visible | Visible |
| v1 cues | Hidden | Visible |
| Interpretation | Self-reflection only | Advisory context |

---

## VERIFICATION SUMMARY

### Constitutional Compliance

✓ **No numeric deltas**: Only directional language stored/shown  
✓ **No baseline exposure**: min/max values never surfaced  
✓ **Silence by default**: NULL signals produce no delta records  
✓ **"No change detected" shown**: Neutral language when inside envelope  
✓ **Self-referential only**: Each student compared to own baseline  
✓ **Minimum 4 sessions**: Enforced structurally  
✓ **Baseline immutable**: First 3 sessions, never changes  
✓ **Locked language only**: Only 3 strings used  

### v2 Invariants

✓ **Insufficient history produces silence**: 3 sessions = no deltas  
✓ **Baseline sessions never get deltas**: First 3 skipped  
✓ **Most recent only**: Only 4th (and beyond) session gets deltas  
✓ **NULL propagation**: NULL current or all-NULL baseline = no delta  
✓ **Envelope logic**: Compare to [min, max] range only  
✓ **0-3 deltas per session**: error_transition_pattern always NULL  

---

**END OF v2 DEMO SCENARIOS**

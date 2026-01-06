# COGNIFLOW v3 — DEMO SCENARIOS & VERIFICATION

**System Version**: v3.0.0  
**Generated**: 2026-01-06  
**Purpose**: Verification artifact demonstrating v3 constitutional compliance

---

## SCENARIO 1 — INSUFFICIENT HISTORY (4 SESSIONS, SILENCE)

### 1. Scenario Description

Student has exactly 4 insight-eligible sessions; v3 requires minimum 5 for stability assessment.

---

### 2. Session Records

```json
[
  {
    "session_id": "s1111111-1111-1111-1111-111111111111",
    "student_id": "student_alice",
    "problem_id": "problem_sort",
    "session_start_utc": "2026-01-01T10:00:00Z",
    "session_end_utc": "2026-01-01T10:15:00Z",
    "visibility_code": "HIGH",
    "insight_eligible": true
  },
  {
    "session_id": "s2222222-2222-2222-2222-222222222222",
    "student_id": "student_alice",
    "problem_id": "problem_reverse",
    "session_start_utc": "2026-01-02T10:00:00Z",
    "session_end_utc": "2026-01-02T10:20:00Z",
    "visibility_code": "HIGH",
    "insight_eligible": true
  },
  {
    "session_id": "s3333333-3333-3333-3333-333333333333",
    "student_id": "student_alice",
    "problem_id": "problem_search",
    "session_start_utc": "2026-01-03T10:00:00Z",
    "session_end_utc": "2026-01-03T10:18:00Z",
    "visibility_code": "HIGH",
    "insight_eligible": true
  },
  {
    "session_id": "s4444444-4444-4444-4444-444444444444",
    "student_id": "student_alice",
    "problem_id": "problem_merge",
    "session_start_utc": "2026-01-04T10:00:00Z",
    "session_end_utc": "2026-01-04T10:25:00Z",
    "visibility_code": "HIGH",
    "insight_eligible": true
  }
]
```

---

### 3. Derived_Signal Records

```json
[
  {
    "signal_id": "sig1-1111111-1111-1111-1111-111111111111",
    "session_id": "s1111111-1111-1111-1111-111111111111",
    "planning_latency_seconds": 120,
    "iteration_depth": 5,
    "rewrite_ratio": 0.6,
    "error_transition_pattern": ["syntax", "logic"]
  },
  {
    "signal_id": "sig2-2222222-2222-2222-2222-222222222222",
    "session_id": "s2222222-2222-2222-2222-222222222222",
    "planning_latency_seconds": 90,
    "iteration_depth": 4,
    "rewrite_ratio": 0.8,
    "error_transition_pattern": ["syntax"]
  },
  {
    "signal_id": "sig3-3333333-3333-3333-3333-333333333333",
    "session_id": "s3333333-3333-3333-3333-333333333333",
    "planning_latency_seconds": 150,
    "iteration_depth": 6,
    "rewrite_ratio": 0.5,
    "error_transition_pattern": []
  },
  {
    "signal_id": "sig4-4444444-4444-4444-4444-444444444444",
    "session_id": "s4444444-4444-4444-4444-444444444444",
    "planning_latency_seconds": 180,
    "iteration_depth": 3,
    "rewrite_ratio": 0.7,
    "error_transition_pattern": ["syntax", "logic", "runtime"]
  }
]
```

---

### 4. Stability Window Computation

**Total v3-eligible sessions**: 4  
**Required for v3**: 5

**Result**: Student is NOT v3-eligible. No stability window can be constructed.

---

### 5. Stability_Assessment Records

**NONE CREATED** — Insufficient history (minimum 5 v3-eligible sessions required)

---

### 6. Student Output JSON

```json
{
  "problem_id": "problem_merge",
  "session_start_utc": "2026-01-04T10:00:00Z",
  "is_completed": true
}
```

**Note**: No `stability` field present (v3 silent by design)

---

### 7. Teacher Output JSON

```json
{
  "student_id": "student_alice",
  "problem_id": "problem_merge",
  "session_start_utc": "2026-01-04T10:00:00Z",
  "cues": ["understanding_problem", "translating_logic", "debugging_effectively"]
}
```

**Note**: No `stability` field present (v3 silent)

---

### 8. Verification Checklist

- ✓ **v3 eligibility respected**: Student has 4 sessions, requires 5
- ✓ **Silence rules respected**: No Stability_Assessment records created
- ✓ **No forbidden fields exposed**: No stability field in outputs
- ✓ **No interpretation added**: System remains completely silent

---

## SCENARIO 2 — FIRST STABILITY ASSESSMENT (5TH SESSION)

### 1. Scenario Description

Student has exactly 5 insight-eligible sessions; session 5 produces first stability assessment.

---

### 2. Session Records

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
  },
  {
    "session_id": "s4444444-4444-4444-4444-444444444444",
    "student_id": "student_bob",
    "problem_id": "problem_merge",
    "session_start_utc": "2026-01-04T10:00:00Z",
    "insight_eligible": true
  },
  {
    "session_id": "s5555555-5555-5555-5555-555555555555",
    "student_id": "student_bob",
    "problem_id": "problem_quicksort",
    "session_start_utc": "2026-01-05T10:00:00Z",
    "insight_eligible": true
  }
]
```

---

### 3. Derived_Signal Records

```json
[
  {
    "session_id": "s1111111-1111-1111-1111-111111111111",
    "planning_latency_seconds": 100,
    "iteration_depth": 4,
    "rewrite_ratio": 0.5
  },
  {
    "session_id": "s2222222-2222-2222-2222-222222222222",
    "planning_latency_seconds": 120,
    "iteration_depth": 5,
    "rewrite_ratio": 0.6
  },
  {
    "session_id": "s3333333-3333-3333-3333-333333333333",
    "planning_latency_seconds": 110,
    "iteration_depth": 6,
    "rewrite_ratio": 0.7
  },
  {
    "session_id": "s4444444-4444-4444-4444-444444444444",
    "planning_latency_seconds": 90,
    "iteration_depth": 3,
    "rewrite_ratio": 0.4
  },
  {
    "session_id": "s5555555-5555-5555-5555-555555555555",
    "planning_latency_seconds": 105,
    "iteration_depth": 5,
    "rewrite_ratio": 0.55
  }
]
```

---

### 4. Stability Window Computation

**Total v3-eligible sessions**: 5  
**Window sessions**: First 4 sessions (s1 through s4)  
**Current session**: s5555555 (most recent)

**planning_latency_seconds window**: [100, 120, 110, 90]  
- Non-NULL values: [100, 120, 110, 90]
- envelope_min = 90
- envelope_max = 120
- Current value: 105
- **Result**: 90 <= 105 <= 120 → "Within your usual range"

**iteration_depth window**: [4, 5, 6, 3]  
- Non-NULL values: [4, 5, 6, 3]
- envelope_min = 3
- envelope_max = 6
- Current value: 5
- **Result**: 3 <= 5 <= 6 → "Within your usual range"

**rewrite_ratio window**: [0.5, 0.6, 0.7, 0.4]  
- Non-NULL values: [0.5, 0.6, 0.7, 0.4]
- envelope_min = 0.4
- envelope_max = 0.7
- Current value: 0.55
- **Result**: 0.4 <= 0.55 <= 0.7 → "Within your usual range"

---

### 5. Stability_Assessment Records

```json
[
  {
    "stability_id": "stab1-5555555-5555-5555-5555-555555555555",
    "student_id": "student_bob",
    "session_id": "s5555555-5555-5555-5555-555555555555",
    "signal_name": "planning_latency_seconds",
    "stability_label": "Within your usual range",
    "created_utc": "2026-01-05T10:20:01Z"
  },
  {
    "stability_id": "stab2-5555555-5555-5555-5555-555555555555",
    "student_id": "student_bob",
    "session_id": "s5555555-5555-5555-5555-555555555555",
    "signal_name": "iteration_depth",
    "stability_label": "Within your usual range",
    "created_utc": "2026-01-05T10:20:01Z"
  },
  {
    "stability_id": "stab3-5555555-5555-5555-5555-555555555555",
    "student_id": "student_bob",
    "session_id": "s5555555-5555-5555-5555-555555555555",
    "signal_name": "rewrite_ratio",
    "stability_label": "Within your usual range",
    "created_utc": "2026-01-05T10:20:01Z"
  }
]
```

---

### 6. Student Output JSON

```json
{
  "problem_id": "problem_quicksort",
  "session_start_utc": "2026-01-05T10:00:00Z",
  "is_completed": true,
  "stability": [
    "Within your usual range",
    "Within your usual range",
    "Within your usual range"
  ]
}
```

**Note**: Student sees stability labels only, no signal names

---

### 7. Teacher Output JSON

```json
{
  "student_id": "student_bob",
  "problem_id": "problem_quicksort",
  "session_start_utc": "2026-01-05T10:00:00Z",
  "cues": ["understanding_problem", "translating_logic"],
  "stability": [
    {
      "signal_name": "planning_latency_seconds",
      "stability_label": "Within your usual range"
    },
    {
      "signal_name": "iteration_depth",
      "stability_label": "Within your usual range"
    },
    {
      "signal_name": "rewrite_ratio",
      "stability_label": "Within your usual range"
    }
  ]
}
```

**Note**: Teacher sees signal names paired with stability labels

---

### 8. Verification Checklist

- ✓ **v3 eligibility respected**: Student has exactly 5 sessions, threshold met
- ✓ **Silence rules respected**: All signals computable, all records created
- ✓ **No forbidden fields exposed**: No numeric values, envelopes, or window metadata shown
- ✓ **No interpretation added**: Only locked strings used

---

## SCENARIO 3 — "WITHIN YOUR USUAL RANGE" (ALL SIGNALS)

### 1. Scenario Description

All current signal values fall within stability window envelope.

---

### 2. Session Records (Window + Current)

**Window sessions**: 6 total sessions (last 5 form window)  
**Current session**: Session 6 (most recent)

---

### 3. Derived_Signal Records

**Window values (sessions 2-6 act as window for session 7)**:

```json
[
  {
    "session_id": "s1111111-1111-1111-1111-111111111111",
    "planning_latency_seconds": 80,
    "iteration_depth": 2,
    "rewrite_ratio": 0.3
  },
  {
    "session_id": "s2222222-2222-2222-2222-222222222222",
    "planning_latency_seconds": 95,
    "iteration_depth": 4,
    "rewrite_ratio": 0.45
  },
  {
    "session_id": "s3333333-3333-3333-3333-333333333333",
    "planning_latency_seconds": 110,
    "iteration_depth": 5,
    "rewrite_ratio": 0.55
  },
  {
    "session_id": "s4444444-4444-4444-4444-444444444444",
    "planning_latency_seconds": 105,
    "iteration_depth": 6,
    "rewrite_ratio": 0.65
  },
  {
    "session_id": "s5555555-5555-5555-5555-555555555555",
    "planning_latency_seconds": 120,
    "iteration_depth": 7,
    "rewrite_ratio": 0.75
  },
  {
    "session_id": "s6666666-6666-6666-6666-666666666666",
    "planning_latency_seconds": 100,
    "iteration_depth": 5,
    "rewrite_ratio": 0.60
  }
]
```

---

### 4. Stability Window Computation

**Window sessions**: s2 through s6 (last 5 sessions before current)  
**Current session**: s6666666

**planning_latency_seconds**:
- Window: [95, 110, 105, 120, 100]
- envelope_min = 95, envelope_max = 120
- Current: 100
- **Result**: 95 <= 100 <= 120 → "Within your usual range"

**iteration_depth**:
- Window: [4, 5, 6, 7, 5]
- envelope_min = 4, envelope_max = 7
- Current: 5
- **Result**: 4 <= 5 <= 7 → "Within your usual range"

**rewrite_ratio**:
- Window: [0.45, 0.55, 0.65, 0.75, 0.60]
- envelope_min = 0.45, envelope_max = 0.75
- Current: 0.60
- **Result**: 0.45 <= 0.60 <= 0.75 → "Within your usual range"

---

### 5. Stability_Assessment Records

```json
[
  {
    "stability_id": "stab1-6666666-6666-6666-6666-666666666666",
    "student_id": "student_carol",
    "session_id": "s6666666-6666-6666-6666-666666666666",
    "signal_name": "planning_latency_seconds",
    "stability_label": "Within your usual range",
    "created_utc": "2026-01-06T10:30:01Z"
  },
  {
    "stability_id": "stab2-6666666-6666-6666-6666-666666666666",
    "student_id": "student_carol",
    "session_id": "s6666666-6666-6666-6666-666666666666",
    "signal_name": "iteration_depth",
    "stability_label": "Within your usual range",
    "created_utc": "2026-01-06T10:30:01Z"
  },
  {
    "stability_id": "stab3-6666666-6666-6666-6666-666666666666",
    "student_id": "student_carol",
    "session_id": "s6666666-6666-6666-6666-666666666666",
    "signal_name": "rewrite_ratio",
    "stability_label": "Within your usual range",
    "created_utc": "2026-01-06T10:30:01Z"
  }
]
```

---

### 6. Student Output JSON

```json
{
  "problem_id": "problem_binary_search",
  "session_start_utc": "2026-01-06T10:00:00Z",
  "is_completed": true,
  "stability": [
    "Within your usual range",
    "Within your usual range",
    "Within your usual range"
  ]
}
```

---

### 7. Teacher Output JSON

```json
{
  "student_id": "student_carol",
  "problem_id": "problem_binary_search",
  "session_start_utc": "2026-01-06T10:00:00Z",
  "cues": ["understanding_problem", "debugging_effectively"],
  "stability": [
    {
      "signal_name": "planning_latency_seconds",
      "stability_label": "Within your usual range"
    },
    {
      "signal_name": "iteration_depth",
      "stability_label": "Within your usual range"
    },
    {
      "signal_name": "rewrite_ratio",
      "stability_label": "Within your usual range"
    }
  ]
}
```

---

### 8. Verification Checklist

- ✓ **v3 eligibility respected**: All signals computable
- ✓ **Silence rules respected**: All records created (no silence needed)
- ✓ **No forbidden fields exposed**: Only locked strings shown
- ✓ **No interpretation added**: "Within your usual range" used exclusively

---

## SCENARIO 4 — "OUTSIDE YOUR USUAL RANGE" (MIXED RESULTS)

### 1. Scenario Description

Current values demonstrate mix of within-range and outside-range signals.

---

### 2. Session Records

Student has 7 total v3-eligible sessions; session 7 is current.

---

### 3. Derived_Signal Records

**Stability window (sessions 2-6)**:

```json
[
  {
    "session_id": "s2222222-2222-2222-2222-222222222222",
    "planning_latency_seconds": 100,
    "iteration_depth": 5,
    "rewrite_ratio": 0.5
  },
  {
    "session_id": "s3333333-3333-3333-3333-333333333333",
    "planning_latency_seconds": 110,
    "iteration_depth": 6,
    "rewrite_ratio": 0.6
  },
  {
    "session_id": "s4444444-4444-4444-4444-444444444444",
    "planning_latency_seconds": 105,
    "iteration_depth": 5,
    "rewrite_ratio": 0.55
  },
  {
    "session_id": "s5555555-5555-5555-5555-555555555555",
    "planning_latency_seconds": 115,
    "iteration_depth": 7,
    "rewrite_ratio": 0.65
  },
  {
    "session_id": "s6666666-6666-6666-6666-666666666666",
    "planning_latency_seconds": 95,
    "iteration_depth": 4,
    "rewrite_ratio": 0.45
  }
]
```

**Current session**:

```json
{
  "session_id": "s7777777-7777-7777-7777-777777777777",
  "planning_latency_seconds": 200,
  "iteration_depth": 6,
  "rewrite_ratio": 0.3
}
```

---

### 4. Stability Window Computation

**Window sessions**: s2 through s6  
**Current session**: s7777777

**planning_latency_seconds**:
- Window: [100, 110, 105, 115, 95]
- envelope_min = 95, envelope_max = 115
- Current: 200
- **Result**: 200 > 115 → "Outside your usual range"

**iteration_depth**:
- Window: [5, 6, 5, 7, 4]
- envelope_min = 4, envelope_max = 7
- Current: 6
- **Result**: 4 <= 6 <= 7 → "Within your usual range"

**rewrite_ratio**:
- Window: [0.5, 0.6, 0.55, 0.65, 0.45]
- envelope_min = 0.45, envelope_max = 0.65
- Current: 0.3
- **Result**: 0.3 < 0.45 → "Outside your usual range"

---

### 5. Stability_Assessment Records

```json
[
  {
    "stability_id": "stab1-7777777-7777-7777-7777-777777777777",
    "student_id": "student_dave",
    "session_id": "s7777777-7777-7777-7777-777777777777",
    "signal_name": "planning_latency_seconds",
    "stability_label": "Outside your usual range",
    "created_utc": "2026-01-07T10:40:01Z"
  },
  {
    "stability_id": "stab2-7777777-7777-7777-7777-777777777777",
    "student_id": "student_dave",
    "session_id": "s7777777-7777-7777-7777-777777777777",
    "signal_name": "iteration_depth",
    "stability_label": "Within your usual range",
    "created_utc": "2026-01-07T10:40:01Z"
  },
  {
    "stability_id": "stab3-7777777-7777-7777-7777-777777777777",
    "student_id": "student_dave",
    "session_id": "s7777777-7777-7777-7777-777777777777",
    "signal_name": "rewrite_ratio",
    "stability_label": "Outside your usual range",
    "created_utc": "2026-01-07T10:40:01Z"
  }
]
```

---

### 6. Student Output JSON

```json
{
  "problem_id": "problem_heapsort",
  "session_start_utc": "2026-01-07T10:00:00Z",
  "is_completed": true,
  "stability": [
    "Outside your usual range",
    "Within your usual range",
    "Outside your usual range"
  ]
}
```

**Note**: Student sees labels but cannot identify which signal each refers to

---

### 7. Teacher Output JSON

```json
{
  "student_id": "student_dave",
  "problem_id": "problem_heapsort",
  "session_start_utc": "2026-01-07T10:00:00Z",
  "cues": ["understanding_problem", "translating_logic", "debugging_effectively"],
  "stability": [
    {
      "signal_name": "planning_latency_seconds",
      "stability_label": "Outside your usual range"
    },
    {
      "signal_name": "iteration_depth",
      "stability_label": "Within your usual range"
    },
    {
      "signal_name": "rewrite_ratio",
      "stability_label": "Outside your usual range"
    }
  ]
}
```

**Note**: Teacher can identify that planning_latency and rewrite_ratio are outside range, iteration_depth within

---

### 8. Verification Checklist

- ✓ **v3 eligibility respected**: All signals computable
- ✓ **Silence rules respected**: All records created
- ✓ **No forbidden fields exposed**: No numeric deviations or envelope bounds shown
- ✓ **No interpretation added**: Only locked strings used, no explanation of why outside range

---

## SCENARIO 5 — NULL HANDLING (FORCED SILENCE)

### 1. Scenario Description

Current session has NULL for one signal; that signal produces no Stability_Assessment record.

---

### 2. Session Records

Student has 6 v3-eligible sessions; session 6 is current.

---

### 3. Derived_Signal Records

**Stability window (sessions 1-5)**:

```json
[
  {
    "session_id": "s1111111-1111-1111-1111-111111111111",
    "planning_latency_seconds": 100,
    "iteration_depth": 5,
    "rewrite_ratio": 0.5
  },
  {
    "session_id": "s2222222-2222-2222-2222-222222222222",
    "planning_latency_seconds": 120,
    "iteration_depth": 6,
    "rewrite_ratio": 0.6
  },
  {
    "session_id": "s3333333-3333-3333-3333-333333333333",
    "planning_latency_seconds": 110,
    "iteration_depth": null,
    "rewrite_ratio": 0.55
  },
  {
    "session_id": "s4444444-4444-4444-4444-444444444444",
    "planning_latency_seconds": 115,
    "iteration_depth": 7,
    "rewrite_ratio": 0.65
  },
  {
    "session_id": "s5555555-5555-5555-5555-555555555555",
    "planning_latency_seconds": 105,
    "iteration_depth": 5,
    "rewrite_ratio": 0.58
  }
]
```

**Current session**:

```json
{
  "session_id": "s6666666-6666-6666-6666-666666666666",
  "planning_latency_seconds": 108,
  "iteration_depth": null,
  "rewrite_ratio": 0.62
}
```

---

### 4. Stability Window Computation

**Window sessions**: s1 through s5  
**Current session**: s6666666

**planning_latency_seconds**:
- Window: [100, 120, 110, 115, 105]
- Non-NULL values: [100, 120, 110, 115, 105]
- envelope_min = 100, envelope_max = 120
- Current: 108
- **Result**: 100 <= 108 <= 120 → "Within your usual range"

**iteration_depth**:
- Window: [5, 6, NULL, 7, 5]
- Non-NULL values: [5, 6, 7, 5]
- envelope_min = 5, envelope_max = 7
- Current: NULL
- **Result**: NULL → NO RECORD CREATED (forced silence)

**rewrite_ratio**:
- Window: [0.5, 0.6, 0.55, 0.65, 0.58]
- Non-NULL values: [0.5, 0.6, 0.55, 0.65, 0.58]
- envelope_min = 0.5, envelope_max = 0.65
- Current: 0.62
- **Result**: 0.5 <= 0.62 <= 0.65 → "Within your usual range"

**Why NULL causes silence**: Current value is NULL; v3 canonical rules specify NULL current → return NULL (no record).

---

### 5. Stability_Assessment Records

```json
[
  {
    "stability_id": "stab1-6666666-6666-6666-6666-666666666666",
    "student_id": "student_eve",
    "session_id": "s6666666-6666-6666-6666-666666666666",
    "signal_name": "planning_latency_seconds",
    "stability_label": "Within your usual range",
    "created_utc": "2026-01-08T10:50:01Z"
  },
  {
    "stability_id": "stab3-6666666-6666-6666-6666-666666666666",
    "student_id": "student_eve",
    "session_id": "s6666666-6666-6666-6666-666666666666",
    "signal_name": "rewrite_ratio",
    "stability_label": "Within your usual range",
    "created_utc": "2026-01-08T10:50:01Z"
  }
]
```

**Note**: NO record for `iteration_depth` (current value is NULL)

---

### 6. Student Output JSON

```json
{
  "problem_id": "problem_radix_sort",
  "session_start_utc": "2026-01-08T10:00:00Z",
  "is_completed": true,
  "stability": [
    "Within your usual range",
    "Within your usual range"
  ]
}
```

**Note**: Only 2 stability labels (iteration_depth silently omitted)

---

### 7. Teacher Output JSON

```json
{
  "student_id": "student_eve",
  "problem_id": "problem_radix_sort",
  "session_start_utc": "2026-01-08T10:00:00Z",
  "cues": ["understanding_problem", "debugging_effectively"],
  "stability": [
    {
      "signal_name": "planning_latency_seconds",
      "stability_label": "Within your usual range"
    },
    {
      "signal_name": "rewrite_ratio",
      "stability_label": "Within your usual range"
    }
  ]
}
```

**Note**: iteration_depth not shown (partial stability output)

---

### 8. Verification Checklist

- ✓ **v3 eligibility respected**: Partial eligibility enforced per signal
- ✓ **Silence rules respected**: NULL current → no record for that signal
- ✓ **No forbidden fields exposed**: No explanation shown for missing signal
- ✓ **No interpretation added**: System silently omits iteration_depth, no "not enough data" message

---

## SCENARIO 6 — v2 + v3 TOGETHER (NON-CONTRADICTION PROOF)

### 1. Scenario Description

Same session produces both v2 Longitudinal_Delta and v3 Stability_Assessment records; demonstrates coexistence.

---

### 2. Session Records

Student has 6 v3-eligible sessions.

**Baseline for v2** (first 3 sessions):
```json
[
  {
    "session_id": "s1111111-1111-1111-1111-111111111111",
    "student_id": "student_frank",
    "session_start_utc": "2026-01-01T10:00:00Z",
    "insight_eligible": true
  },
  {
    "session_id": "s2222222-2222-2222-2222-222222222222",
    "student_id": "student_frank",
    "session_start_utc": "2026-01-02T10:00:00Z",
    "insight_eligible": true
  },
  {
    "session_id": "s3333333-3333-3333-3333-333333333333",
    "student_id": "student_frank",
    "session_start_utc": "2026-01-03T10:00:00Z",
    "insight_eligible": true
  }
]
```

**Additional sessions**:
```json
[
  {
    "session_id": "s4444444-4444-4444-4444-444444444444",
    "student_id": "student_frank",
    "session_start_utc": "2026-01-04T10:00:00Z",
    "insight_eligible": true
  },
  {
    "session_id": "s5555555-5555-5555-5555-555555555555",
    "student_id": "student_frank",
    "session_start_utc": "2026-01-05T10:00:00Z",
    "insight_eligible": true
  },
  {
    "session_id": "s6666666-6666-6666-6666-666666666666",
    "student_id": "student_frank",
    "session_start_utc": "2026-01-06T10:00:00Z",
    "insight_eligible": true
  }
]
```

---

### 3. Derived_Signal Records

```json
[
  {
    "session_id": "s1111111-1111-1111-1111-111111111111",
    "planning_latency_seconds": 80,
    "iteration_depth": 3,
    "rewrite_ratio": 0.4
  },
  {
    "session_id": "s2222222-2222-2222-2222-222222222222",
    "planning_latency_seconds": 90,
    "iteration_depth": 4,
    "rewrite_ratio": 0.5
  },
  {
    "session_id": "s3333333-3333-3333-3333-333333333333",
    "planning_latency_seconds": 100,
    "iteration_depth": 5,
    "rewrite_ratio": 0.6
  },
  {
    "session_id": "s4444444-4444-4444-4444-444444444444",
    "planning_latency_seconds": 110,
    "iteration_depth": 6,
    "rewrite_ratio": 0.7
  },
  {
    "session_id": "s5555555-5555-5555-5555-555555555555",
    "planning_latency_seconds": 120,
    "iteration_depth": 7,
    "rewrite_ratio": 0.8
  },
  {
    "session_id": "s6666666-6666-6666-6666-666666666666",
    "planning_latency_seconds": 115,
    "iteration_depth": 5,
    "rewrite_ratio": 0.65
  }
]
```

---

### 4. v2 Baseline Computation (Session 6)

**v2 baseline** (first 3 sessions): s1, s2, s3  
**Current session for v2**: s6666666

**planning_latency_seconds**:
- Baseline: [80, 90, 100]
- baseline_min = 80, baseline_max = 100
- Current: 115
- **v2 Result**: 115 > 100 → "More than your previous attempts"

**iteration_depth**:
- Baseline: [3, 4, 5]
- baseline_min = 3, baseline_max = 5
- Current: 5
- **v2 Result**: 3 <= 5 <= 5 → "No change detected"

**rewrite_ratio**:
- Baseline: [0.4, 0.5, 0.6]
- baseline_min = 0.4, baseline_max = 0.6
- Current: 0.65
- **v2 Result**: 0.65 > 0.6 → "More than your previous attempts"

---

### 5. v3 Stability Window Computation (Session 6)

**v3 window** (last 5 sessions before current): s1, s2, s3, s4, s5  
**Current session for v3**: s6666666

**planning_latency_seconds**:
- Window: [80, 90, 100, 110, 120]
- envelope_min = 80, envelope_max = 120
- Current: 115
- **v3 Result**: 80 <= 115 <= 120 → "Within your usual range"

**iteration_depth**:
- Window: [3, 4, 5, 6, 7]
- envelope_min = 3, envelope_max = 7
- Current: 5
- **v3 Result**: 3 <= 5 <= 7 → "Within your usual range"

**rewrite_ratio**:
- Window: [0.4, 0.5, 0.6, 0.7, 0.8]
- envelope_min = 0.4, envelope_max = 0.8
- Current: 0.65
- **v3 Result**: 0.4 <= 0.65 <= 0.8 → "Within your usual range"

---

### 6. Longitudinal_Delta Records (v2)

```json
[
  {
    "delta_id": "d1-6666666-6666-6666-6666-666666666666",
    "student_id": "student_frank",
    "session_id": "s6666666-6666-6666-6666-666666666666",
    "signal_name": "planning_latency_seconds",
    "delta_direction": "More than your previous attempts",
    "created_utc": "2026-01-06T11:00:00Z"
  },
  {
    "delta_id": "d2-6666666-6666-6666-6666-666666666666",
    "student_id": "student_frank",
    "session_id": "s6666666-6666-6666-6666-666666666666",
    "signal_name": "iteration_depth",
    "delta_direction": "No change detected",
    "created_utc": "2026-01-06T11:00:00Z"
  },
  {
    "delta_id": "d3-6666666-6666-6666-6666-666666666666",
    "student_id": "student_frank",
    "session_id": "s6666666-6666-6666-6666-666666666666",
    "signal_name": "rewrite_ratio",
    "delta_direction": "More than your previous attempts",
    "created_utc": "2026-01-06T11:00:00Z"
  }
]
```

---

### 7. Stability_Assessment Records (v3)

```json
[
  {
    "stability_id": "stab1-6666666-6666-6666-6666-666666666666",
    "student_id": "student_frank",
    "session_id": "s6666666-6666-6666-6666-666666666666",
    "signal_name": "planning_latency_seconds",
    "stability_label": "Within your usual range",
    "created_utc": "2026-01-06T11:00:01Z"
  },
  {
    "stability_id": "stab2-6666666-6666-6666-6666-666666666666",
    "student_id": "student_frank",
    "session_id": "s6666666-6666-6666-6666-666666666666",
    "signal_name": "iteration_depth",
    "stability_label": "Within your usual range",
    "created_utc": "2026-01-06T11:00:01Z"
  },
  {
    "stability_id": "stab3-6666666-6666-6666-6666-666666666666",
    "student_id": "student_frank",
    "session_id": "s6666666-6666-6666-6666-666666666666",
    "signal_name": "rewrite_ratio",
    "stability_label": "Within your usual range",
    "created_utc": "2026-01-06T11:00:01Z"
  }
]
```

---

### 8. Non-Contradiction Proof

**planning_latency_seconds**:
- v2 says: "More than your previous attempts" (vs first 3: 80-100)
- v3 says: "Within your usual range" (vs last 5: 80-120)
- **Both true**: Value 115 exceeds early baseline but within recent window

**iteration_depth**:
- v2 says: "No change detected" (vs first 3: 3-5)
- v3 says: "Within your usual range" (vs last 5: 3-7)
- **Both true**: Value 5 is at top of v2 baseline, middle of v3 window

**rewrite_ratio**:
- v2 says: "More than your previous attempts" (vs first 3: 0.4-0.6)
- v3 says: "Within your usual range" (vs last 5: 0.4-0.8)
- **Both true**: Value 0.65 exceeds early baseline but within recent window

**Key insight**: v2 compares against immutable first 3 sessions; v3 compares against sliding last 5 sessions. No contradiction exists.

---

### 9. Student Output JSON

```json
{
  "problem_id": "problem_dijkstra",
  "session_start_utc": "2026-01-06T10:00:00Z",
  "is_completed": true,
  "longitudinal_deltas": [
    "More than your previous attempts",
    "No change detected",
    "More than your previous attempts"
  ],
  "stability": [
    "Within your usual range",
    "Within your usual range",
    "Within your usual range"
  ]
}
```

**Note**: Both v2 and v3 outputs coexist; student sees both delta strings and stability labels

---

### 10. Teacher Output JSON

```json
{
  "student_id": "student_frank",
  "problem_id": "problem_dijkstra",
  "session_start_utc": "2026-01-06T10:00:00Z",
  "cues": ["understanding_problem", "translating_logic"],
  "longitudinal_deltas": [
    {
      "signal_name": "planning_latency_seconds",
      "delta_direction": "More than your previous attempts"
    },
    {
      "signal_name": "iteration_depth",
      "delta_direction": "No change detected"
    },
    {
      "signal_name": "rewrite_ratio",
      "delta_direction": "More than your previous attempts"
    }
  ],
  "stability": [
    {
      "signal_name": "planning_latency_seconds",
      "stability_label": "Within your usual range"
    },
    {
      "signal_name": "iteration_depth",
      "stability_label": "Within your usual range"
    },
    {
      "signal_name": "rewrite_ratio",
      "stability_label": "Within your usual range"
    }
  ]
}
```

**Note**: Teacher sees both v2 deltas and v3 stability with signal names for interpretive context

---

### 11. Verification Checklist

- ✓ **v3 eligibility respected**: Student has 6 sessions, both v2 and v3 eligible
- ✓ **Silence rules respected**: All records created for both systems
- ✓ **No forbidden fields exposed**: Only locked language strings shown
- ✓ **No interpretation added**: No explanation of why outputs differ
- ✓ **Non-contradiction demonstrated**: v2 uses first 3 baseline, v3 uses last 5 window
- ✓ **Independent computation**: Neither system reads the other's records

---

## VERIFICATION SUMMARY

### Constitutional Compliance

✓ **No numeric values exposed**: Only locked strings in Stability_Assessment  
✓ **No envelope bounds stored**: min/max computed transiently, never persisted  
✓ **Silence by default**: NULL current or insufficient history → no records  
✓ **Locked language only**: "Within your usual range" / "Outside your usual range" exclusively  
✓ **Self-referential only**: Each student compared to own window  
✓ **Minimum 5 sessions**: Enforced structurally  
✓ **Sliding window**: Last 5 sessions recomputed per assessment  
✓ **No cross-student data**: No class_id, cohort_id, or percentiles

### v3 Structural Invariants

✓ **Insufficient history produces silence**: 4 sessions = no stability (Scenario 1)  
✓ **Window sessions never assessed**: Only most recent gets stability records  
✓ **5th session threshold**: First stability at exactly 5 sessions (Scenario 2)  
✓ **NULL propagation**: NULL current = no record for that signal (Scenario 5)  
✓ **Envelope logic**: Compare to [min, max] range only  
✓ **0-3 records per session**: error_transition_pattern always silent  
✓ **v2/v3 independence**: Both operate on v1 data, no mutual dependency (Scenario 6)

### Comparison Window Differences

| Aspect | v2 Baseline | v3 Window |
|--------|-------------|-----------|
| Size | Fixed 3 sessions | Fixed 5 sessions |
| Selection | First 3 eligible | Last 5 eligible |
| Immutability | Immutable (never changes) | Recomputed per session |
| Minimum sessions | 4 (3 baseline + 1 current) | 5 (4 window + 1 current) |
| First eligibility | Session 4 | Session 5 |

---

**END OF v3 DEMO SCENARIOS**

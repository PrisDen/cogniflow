# COGNIFLOW v2 — DELTA COMPUTATION LOGIC (FINAL)

**Status**: AUTHORITATIVE — v2 DELTA LOGIC FREEZE  
**Depends on**: COGNIFLOW_v2_CANONICAL_DEFINITIONS_FINAL.md

---

## Global Rules

- All functions are pure and stateless
- Input: baseline values (list), current value
- Output: locked language string OR NULL
- NULL propagation follows canonical definitions
- No thresholds, no scoring, no interpretation

---

## Function 1: compute_planning_latency_delta

### Signature
```
function compute_planning_latency_delta(
  baseline_values: List[Integer | NULL],
  current_value: Integer | NULL
) -> String | NULL
```

### Logic
```
if current_value IS NULL:
  return NULL

non_null_baseline = FILTER(baseline_values, WHERE value IS NOT NULL)

if LENGTH(non_null_baseline) == 0:
  return NULL

baseline_min = MIN(non_null_baseline)
baseline_max = MAX(non_null_baseline)

if current_value > baseline_max:
  return "More than your previous attempts"

if current_value < baseline_min:
  return "Less than before"

if baseline_min <= current_value <= baseline_max:
  return "No change detected"
```

### Edge Cases
- Empty baseline list → NULL
- All NULL baseline values → NULL
- Current value NULL → NULL
- Single non-NULL baseline value → min == max (range collapses to point)

---

## Function 2: compute_iteration_depth_delta

### Signature
```
function compute_iteration_depth_delta(
  baseline_values: List[Integer | NULL],
  current_value: Integer | NULL
) -> String | NULL
```

### Logic
```
if current_value IS NULL:
  return NULL

non_null_baseline = FILTER(baseline_values, WHERE value IS NOT NULL)

if LENGTH(non_null_baseline) == 0:
  return NULL

baseline_min = MIN(non_null_baseline)
baseline_max = MAX(non_null_baseline)

if current_value > baseline_max:
  return "More than your previous attempts"

if current_value < baseline_min:
  return "Less than before"

if baseline_min <= current_value <= baseline_max:
  return "No change detected"
```

### Edge Cases
- Empty baseline list → NULL
- All NULL baseline values → NULL
- Current value NULL → NULL
- Single non-NULL baseline value → min == max (range collapses to point)

---

## Function 3: compute_rewrite_ratio_delta

### Signature
```
function compute_rewrite_ratio_delta(
  baseline_values: List[Float | NULL],
  current_value: Float | NULL
) -> String | NULL
```

### Logic
```
if current_value IS NULL:
  return NULL

non_null_baseline = FILTER(baseline_values, WHERE value IS NOT NULL)

if LENGTH(non_null_baseline) == 0:
  return NULL

baseline_min = MIN(non_null_baseline)
baseline_max = MAX(non_null_baseline)

if current_value > baseline_max:
  return "More than your previous attempts"

if current_value < baseline_min:
  return "Less than before"

if baseline_min <= current_value <= baseline_max:
  return "No change detected"
```

### Edge Cases
- Empty baseline list → NULL
- All NULL baseline values → NULL
- Current value NULL → NULL
- Single non-NULL baseline value → min == max (range collapses to point)
- Floating-point equality: use `<=` and `>=` to handle precision

---

## Function 4: compute_error_transition_pattern_delta

### Signature
```
function compute_error_transition_pattern_delta(
  baseline_values: List[List[String] | NULL],
  current_value: List[String] | NULL
) -> String | NULL
```

### Logic
```
return NULL
```

### Reason
UNDEFINED BY DESIGN per canonical definitions.

No mechanical, non-judgmental comparison exists for categorical sequences.

---

## Exhaustive Edge Cases

### Empty Baseline
```
baseline_values = []
current_value = 100

Result: NULL
```

---

### All NULL Baseline
```
baseline_values = [NULL, NULL, NULL]
current_value = 100

Result: NULL
```

---

### Some NULL Baseline
```
baseline_values = [NULL, 50, 100]
current_value = 75

non_null_baseline = [50, 100]
baseline_min = 50
baseline_max = 100
current_value (75) is between 50 and 100

Result: "No change detected"
```

---

### NULL Current Value
```
baseline_values = [50, 75, 100]
current_value = NULL

Result: NULL
```

---

### Exact Match to Baseline Min
```
baseline_values = [50, 75, 100]
current_value = 50

baseline_min = 50
baseline_max = 100
50 >= 50 AND 50 <= 100

Result: "No change detected"
```

---

### Exact Match to Baseline Max
```
baseline_values = [50, 75, 100]
current_value = 100

baseline_min = 50
baseline_max = 100
100 >= 50 AND 100 <= 100

Result: "No change detected"
```

---

### Above Baseline
```
baseline_values = [50, 75, 100]
current_value = 150

baseline_min = 50
baseline_max = 100
150 > 100

Result: "More than your previous attempts"
```

---

### Below Baseline
```
baseline_values = [50, 75, 100]
current_value = 25

baseline_min = 50
baseline_max = 100
25 < 50

Result: "Less than before"
```

---

### Single Baseline Value
```
baseline_values = [NULL, 75, NULL]
current_value = 75

non_null_baseline = [75]
baseline_min = 75
baseline_max = 75
75 >= 75 AND 75 <= 75

Result: "No change detected"
```

---

### Single Baseline Value (Above)
```
baseline_values = [NULL, 75, NULL]
current_value = 100

non_null_baseline = [75]
baseline_min = 75
baseline_max = 75
100 > 75

Result: "More than your previous attempts"
```

---

### Single Baseline Value (Below)
```
baseline_values = [NULL, 75, NULL]
current_value = 50

non_null_baseline = [75]
baseline_min = 75
baseline_max = 75
50 < 75

Result: "Less than before"
```

---

## Forbidden Patterns

The following are explicitly forbidden in delta computation:

- Computing numeric delta (`current - baseline_min`)
- Computing percent change (`(current - baseline) / baseline * 100`)
- Applying thresholds ("if delta > 10% then...")
- Normalizing by difficulty or problem complexity
- Aggregating across students
- Using median, mean, or mode instead of min/max
- Introducing "significance" testing
- Adding confidence intervals
- Smoothing or dampening fluctuations

---

## Final Invariant

If baseline envelope cannot be computed OR current value is NULL:

**Return NULL** (delta record is not created).

Silence is the correct output for insufficient evidence.

---

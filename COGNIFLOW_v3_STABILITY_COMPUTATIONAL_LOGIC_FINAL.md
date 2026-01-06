COGNIFLOW v3 — STABILITY COMPUTATION LOGIC (FINAL)

Status: AUTHORITATIVE — LOGIC FREEZE
Depends on: COGNIFLOW v3 Canonical Definitions

⸻

GLOBAL RULES
	•	All functions are pure
	•	No side effects
	•	No DB access
	•	No thresholds
	•	No statistics beyond min/max
	•	Return locked string or NULL only

⸻

Allowed Output Strings (EXHAUSTIVE)
	1.	"Within your usual range"
	2.	"Outside your usual range"

Anything else is forbidden.

⸻

Function 1: planning latency stability

Signature

compute_planning_latency_stability(
  recent_values: List[Integer | NULL],
  current_value: Integer | NULL
) -> String | NULL

Logic

if current_value IS NULL:
  return NULL

non_null = FILTER(recent_values, value IS NOT NULL)

if LENGTH(non_null) < 5:
  return NULL

min_val = MIN(non_null)
max_val = MAX(non_null)

if min_val <= current_value <= max_val:
  return "Within your usual range"

return "Outside your usual range"


⸻

Function 2: iteration depth stability

Signature

compute_iteration_depth_stability(
  recent_values: List[Integer | NULL],
  current_value: Integer | NULL
) -> String | NULL

Logic

(identical structure — intentionally duplicated)

if current_value IS NULL:
  return NULL

non_null = FILTER(recent_values, value IS NOT NULL)

if LENGTH(non_null) < 5:
  return NULL

min_val = MIN(non_null)
max_val = MAX(non_null)

if min_val <= current_value <= max_val:
  return "Within your usual range"

return "Outside your usual range"


⸻

Function 3: rewrite ratio stability

Signature

compute_rewrite_ratio_stability(
  recent_values: List[Float | NULL],
  current_value: Float | NULL
) -> String | NULL

Logic

if current_value IS NULL:
  return NULL

non_null = FILTER(recent_values, value IS NOT NULL)

if LENGTH(non_null) < 5:
  return NULL

min_val = MIN(non_null)
max_val = MAX(non_null)

if min_val <= current_value <= max_val:
  return "Within your usual range"

return "Outside your usual range"


⸻

Function 4: error transition pattern

Signature

compute_error_transition_pattern_stability(...) -> NULL

Logic

return NULL

Reason: categorical sequences cannot be compared without judgment.

⸻

SILENCE CONDITIONS (VERY IMPORTANT)

The function returns NULL (no record created) if:
	•	Fewer than 5 prior sessions exist
	•	All prior values are NULL
	•	Current value is NULL
	•	Signal is error_transition_pattern

NULL ≠ failure
NULL = design choice

⸻


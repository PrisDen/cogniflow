COGNIFLOW v1 — SIGNAL COMPUTATION LOGIC (FINAL)

Status: AUTHORITATIVE — SIGNAL LOGIC FREEZE FOR COGNIFLOW v1
Depends on:
	•	COGNIFLOW TDD
	•	COGNIFLOW_v1_CANONICAL_DEFINITIONS_FINAL.md
	•	COGNIFLOW_v1_SCHEMA_FINAL.md

This document supersedes all prior signal logic drafts, agent outputs, and chat responses.

⸻

Global Rules (Non-Negotiable)
	•	All signal computations are pure, stateless functions
	•	Signals are computed only for insight-eligible sessions
	•	Functions must not infer intent, ability, or quality
	•	If a signal cannot be computed mechanically, return NULL
	•	Absence of evidence must never be collapsed into a value
	•	No thresholds, heuristics, or confidence math are permitted

If a function is not called (e.g., session is not insight-eligible),
no signal value exists.

⸻

Signal 1: planning_latency_seconds

Function Signature

compute_planning_latency(
  events: List[Event],
  session_start_utc: Timestamp
) -> Integer | NULL

Required Input
	•	Ordered or unordered list of retained Event records
	•	Session start timestamp

Computation Steps
	1.	Filter events where event_type = 'run_code'
	2.	If no such events exist, return NULL
	3.	Sort filtered events by timestamp_utc ascending
	4.	Select the first event
	5.	Compute time difference in seconds:

first_run_timestamp - session_start_utc


	6.	Truncate fractional seconds
	7.	Return integer value

Null Conditions
	•	No run_code events exist

⸻

Signal 2: iteration_depth

Function Signature

compute_iteration_depth(
  events: List[Event]
) -> Integer | NULL

Required Input
	•	List of retained Event records

Computation Steps
	1.	Filter events where event_type = 'run_code'
	2.	Count number of filtered events
	3.	If count = 0, return NULL
	4.	Return count as integer

Null Conditions
	•	No run_code events exist

⸻

Signal 3: rewrite_ratio

Function Signature

compute_rewrite_ratio(
  events: List[Event]
) -> Float | NULL

Required Input
	•	List of retained Event records

Computation Steps
	1.	Filter events where event_type = 'code_insert'
	2.	Count records → insert_count
	3.	Filter events where event_type = 'code_delete'
	4.	Count records → delete_count
	5.	If insert_count = 0, return NULL
	6.	Compute:

delete_count / insert_count


	7.	Return result as floating-point number

Null Conditions
	•	No code_insert events exist

⸻

Signal 4: error_transition_pattern

Function Signature

compute_error_transition_pattern(
  events: List[Event]
) -> List[String] | NULL

Required Input
	•	List of retained Event records

Computation Steps
	1.	Filter events where:
	•	event_type = 'error'
	•	error_category IS NOT NULL
	2.	If no such events exist, return an empty list
	3.	Sort filtered events by timestamp_utc ascending
	4.	Extract error_category from each event in order
	5.	Return ordered list of category strings

Null Conditions
	•	Signal computation is not executed (e.g., session not insight-eligible)

Notes
	•	Empty list ([]) means: signal computed, zero categorized errors observed
	•	NULL means: signal does not exist

⸻

Explicitly Undefined Signals

The following signal is UNDEFINED BY DESIGN and must not be implemented in v1:
	•	structural_convergence

Any attempt to compute it would require semantic or structural inference, which is prohibited.

⸻

Forbidden Patterns (Global)

The following are explicitly forbidden in all signal logic:
	•	Returning 0 to represent absence
	•	Inferring difficulty, struggle, or success
	•	Combining signals
	•	Normalization or scaling
	•	Confidence or reliability calculations
	•	Session-to-session comparisons
	•	Cross-student aggregation

⸻

Final Invariant

If a question cannot be answered using only:
	•	event presence
	•	event order
	•	event counts
	•	timestamps

then Cogniflow v1 does not answer it.

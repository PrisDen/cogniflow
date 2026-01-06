COGNIFLOW v3 — CANONICAL DEFINITIONS (FINAL)

Status: AUTHORITATIVE — v3 SPECIFICATION
Depends on: v1 (Session, Derived_Signal), v2 (Longitudinal_Delta)
Scope: Pattern Stability (self-referential only)

⸻

1. v3 PURPOSE (NON-NEGOTIABLE)

v3 answers one question only:

Is the current session within the student’s usual working range, or outside it?

v3 does not evaluate quality, improvement, regression, or compare students.

⸻

2. v3 ELIGIBILITY

Session v3-Eligibility

A session is v3-eligible iff:

session.insight_eligible == true
AND
Derived_Signal exists for session

Student v3-Eligibility

A student is v3-eligible iff:

COUNT(v3-eligible sessions for student_id) >= 5

If not eligible → v3 REMAINS SILENT.

⸻

3. STABILITY WINDOW (BASELINE)

Window Construction

For each signal independently:
	1.	Filter sessions where:
	•	session.student_id == target_student_id
	•	session is v3-eligible
	2.	Sort by session_start_utc ascending
	3.	Select the last 5 sessions → stability window
	4.	The window is immutable per computation (no rolling mid-computation)

Window Size
	•	Fixed at 5 sessions
	•	Fewer than 5 → silence

⸻

4. COMPARISON TARGET
	•	The current comparison target is the most recent v3-eligible session
	•	Only one session is evaluated at a time
	•	If the most recent session is within the window but lacks computable signals → silence for that signal

⸻

5. SIGNALS CONSIDERED

v3 applies to:
	•	planning_latency_seconds
	•	iteration_depth
	•	rewrite_ratio

Explicitly excluded:
	•	error_transition_pattern (UNDEFINED BY DESIGN)

⸻

6. STABILITY ENVELOPE

For each signal:

window_values = values from the 5-session window
non_null = FILTER(window_values, value IS NOT NULL)

if LENGTH(non_null) == 0:
  envelope = NULL
else:
  envelope_min = MIN(non_null)
  envelope_max = MAX(non_null)


⸻

7. v3 STABILITY LOGIC (LOCKED)

Output Language (EXHAUSTIVE)

Only the following strings are permitted:
	1.	“Within your usual range”
	2.	“Outside your usual range”

Decision Rules

if current_value IS NULL:
  return NULL

if envelope IS NULL:
  return NULL

if envelope_min <= current_value <= envelope_max:
  return "Within your usual range"
else:
  return "Outside your usual range"

No other outcomes are allowed.

⸻

8. NULL & SILENCE RULES

v3 must remain silent if:
	•	Student has < 5 v3-eligible sessions
	•	Current value is NULL
	•	All window values are NULL
	•	Signal is not v3-eligible
	•	Session is not the most recent v3-eligible session

Silence means no record created and no UI element shown.

⸻

9. INSIGHT CREATION (v3)

Record Creation
	•	One record per signal per eligible session
	•	Only when output is non-NULL
	•	No records for baseline-only or ineligible sessions

Prohibitions

v3 must not:
	•	Store numeric values
	•	Store envelope bounds
	•	Store counts, percentages, or trends
	•	Use thresholds beyond min/max
	•	Compare across students
	•	Rank or order signals

⸻

10. USER VISIBILITY

Student View
	•	Sees strings only
	•	No signal names
	•	No numbers
	•	Silence if nothing applies

Teacher View
	•	Sees:
	•	signal_name
	•	stability (one of the two strings)
	•	Still no numbers or scores

⸻

11. FINAL INVARIANTS
	•	v3 is self-referential only
	•	v3 is range-based, not score-based
	•	v3 is observational, not evaluative
	•	v3 cannot be repurposed for grading, ranking, or surveillance

⸻

UNDEFINED BY DESIGN (v3)

The following are explicitly out of scope:
	•	Trend detection
	•	Stability over time
	•	Volatility scoring
	•	Difficulty normalization
	•	Any interpretation of why behavior changed

⸻

END OF v3 CANONICAL DEFINITIONS


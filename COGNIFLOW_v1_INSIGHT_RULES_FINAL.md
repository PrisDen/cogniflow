COGNIFLOW v1 — INSIGHT INSTANTIATION RULES (FINAL)

Status: AUTHORITATIVE — INSIGHT RULES FREEZE FOR COGNIFLOW v1
Depends on:
	•	COGNIFLOW TDD
	•	COGNIFLOW_v1_CANONICAL_DEFINITIONS_FINAL.md
	•	COGNIFLOW_v1_SCHEMA_FINAL.md
	•	COGNIFLOW_v1_SIGNAL_LOGIC_FINAL.md

This document supersedes all prior insight rule drafts, agent outputs, and chat responses.

⸻

Core Principle (v1)

In Cogniflow v1, teacher-facing cues do not indicate problems, quality, or ability.

They indicate presence of observable evidence in a specific dimension of problem-solving.

A cue answers only:

“Is there concrete, observable session evidence in this dimension that a human may choose to examine?”

It does not answer:
	•	whether the behavior was good or bad
	•	whether the student succeeded or failed
	•	whether intervention is required

⸻

Global Eligibility Rules

An Insight record may be created only if all conditions below are met:
	1.	Session is marked insight_eligible = true
	2.	Session visibility is High or Medium (mechanically enforced upstream)
	3.	Required signal computation was executed
	4.	Required signal value is not NULL

If any condition fails, no Insight record is created.

Absence of Insight is neutral and non-actionable.

⸻

Cue 1: “Understanding the problem”

Evidence Dimension

Early execution behavior (transition from problem reading to first execution).

Required Inputs
	•	planning_latency_seconds

Create Insight IF
	•	planning_latency_seconds IS NOT NULL

This indicates:
	•	There is observable evidence related to how the student moved from reading to execution.

Do NOT Create Insight IF
	•	planning_latency_seconds IS NULL
	•	Session is not insight-eligible

No interpretation of speed, delay, or quality is performed.

⸻

Cue 2: “Translating logic into code”

Evidence Dimension

Code-writing and revision activity.

Required Inputs
	•	rewrite_ratio
	•	iteration_depth

Create Insight IF
	•	rewrite_ratio IS NOT NULL
OR
	•	iteration_depth IS NOT NULL

This indicates:
	•	There is observable evidence related to how the student translated ideas into code.

No assessment of correctness, efficiency, or struggle is made.

Do NOT Create Insight IF
	•	Both rewrite_ratio and iteration_depth are NULL
	•	Session is not insight-eligible

⸻

Cue 3: “Debugging effectively”

Evidence Dimension

Error encounter and handling activity.

Required Inputs
	•	error_transition_pattern

Create Insight IF
	•	error_transition_pattern IS NOT NULL

Notes:
	•	An empty list ([]) counts as computed evidence.
	•	NULL means no evidence exists in this dimension.

Do NOT Create Insight IF
	•	error_transition_pattern IS NULL
	•	Session is not insight-eligible

No judgment is made about effectiveness, success, or failure.

⸻

Explicit Non-Rules (Forbidden in v1)

The following are explicitly forbidden:
	•	Thresholds of any kind
	•	Directional judgments (e.g., high/low, good/bad)
	•	Single-session intervention logic
	•	Confidence or reliability math
	•	Cross-session or cross-student comparison
	•	Suppression or prioritization of cues
	•	Automatic recommendations or actions

⸻

Invariant

If a cue exists, it means only one thing:

“There is observable session evidence in this dimension.”

Nothing more.

Nothing less.

⸻

Final Lock

If future changes require:
	•	thresholds
	•	deltas
	•	trends
	•	interpretation

they belong to v2 or later and must not modify this file.

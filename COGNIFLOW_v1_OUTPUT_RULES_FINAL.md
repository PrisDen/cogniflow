COGNIFLOW v1 — ROLE-BASED DATA VISIBILITY RULES (FINAL)

Status: AUTHORITATIVE — OUTPUT RULES FREEZE FOR COGNIFLOW v1
Depends on:
	•	COGNIFLOW TDD
	•	COGNIFLOW_v1_CANONICAL_DEFINITIONS_FINAL.md
	•	COGNIFLOW_v1_SCHEMA_FINAL.md
	•	COGNIFLOW_v1_SIGNAL_LOGIC_FINAL.md
	•	COGNIFLOW_v1_INSIGHT_RULES_FINAL.md

This document supersedes all prior visibility drafts, agent outputs, and chat responses.

⸻

ROLE 1: Student (Viewing Own Data Only)

Visible Entities
	•	Session (own sessions only)

Session — Visible Fields
	•	problem_id
	•	session_start_utc
	•	Derived: completion status (computed server-side from presence of a submit event)

Session — Explicitly Hidden Fields
	•	session_id
	•	student_id
	•	session_end_utc
	•	visibility_code
	•	insight_eligible

Event
	•	Not visible to the student under any circumstance

Derived_Signal
	•	No access

Insight
	•	No access

Forbidden Views
	•	Other students’ data
	•	Teacher dashboards
	•	Insight records
	•	Signal values
	•	Event details or counts
	•	Session comparisons (self or cross-student)
	•	Class or cohort distributions
	•	Any ordering or ranking

⸻

ROLE 2: Teacher

Visible Entities
	•	Session (within teacher’s scope)
	•	Insight (for insight-eligible sessions only)

Session — Visible Fields (List View)
	•	student_id
	•	problem_id
	•	session_start_utc
	•	Derived: cue presence (binary existence of Insight records)

Session — Explicitly Hidden Fields (List View)
	•	session_id
	•	session_end_utc
	•	visibility_code
	•	insight_eligible

Explainable-on-Click (Detail View)

Available only when a cue exists and is clicked.

Visible via Explainable-on-Click
	•	Signal values from Derived_Signal:
	•	planning_latency_seconds
	•	iteration_depth
	•	rewrite_ratio
	•	error_transition_pattern

Explicitly Hidden via Explainable-on-Click
	•	Individual event records or timestamps
	•	Event counts of any kind
	•	Code content
	•	Inserted/deleted text
	•	Line or column numbers
	•	Idle durations
	•	Session duration
	•	Confidence or reliability values (do not exist)

Insight — Visible Fields
	•	cue_type (displayed as a binary checkbox; presence only)

Insight — Explicitly Hidden Fields
	•	insight_id
	•	session_id
	•	created_utc

Low-Visibility Session Handling

For sessions where insight_eligible = false:
	•	Session appears in list with student identifier, problem name, and start timestamp
	•	No cues shown (cue area blank)
	•	Clicking shows: “Insufficient process data for this session”
	•	No signals, events, or explanations are revealed

Forbidden Views
	•	Raw event payloads
	•	Sortable student lists
	•	Side-by-side student comparisons
	•	Exportable tables
	•	Cross-student rankings or percentiles
	•	Session-to-session deltas (until v2)
	•	Confidence or reliability indicators
	•	Event timestamps
	•	Code content

⸻

ROLE 3: Institution

Visible Entities
	•	UNDEFINED IN v1

Institutional views are explicitly out of scope for v1 and are introduced in v2 only.

Forbidden Views (When Implemented in v2)
	•	Individual students or identifiers
	•	Teacher comparisons
	•	Performance rankings
	•	Any data reversible to individual identification

⸻

CROSS-ROLE INVARIANTS

Never Visible to Any Role
	•	Confidence scalars (do not exist)
	•	structural_convergence (undefined by design)
	•	Raw event payloads after retention
	•	session_id values (internal only)
	•	visibility_code values (server-internal)
	•	insight_eligible boolean (server-internal)

Prohibited Query Patterns (All Roles)
	•	Stable ordering for ranking (e.g., ORDER BY on comparable fields)
	•	Percentile or rank calculations
	•	Cross-student joins for comparison
	•	Global aggregation for normalization
	•	Time-series analysis spanning students (until v2)

⸻

FINAL CONSTRAINT

If a field, view, or query enables:
	•	ranking students
	•	comparing students to each other
	•	making judgments about ability or quality
	•	circumventing visibility rules

it is forbidden regardless of role.

⸻

End of v1 Output Rules.

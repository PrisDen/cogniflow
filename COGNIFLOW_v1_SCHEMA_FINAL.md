COGNIFLOW v1 — PERSISTENT DATA SCHEMA (FINAL)

Status: AUTHORITATIVE — SCHEMA FREEZE FOR COGNIFLOW v1
Depends on:
	•	COGNIFLOW TDD (Constitutional Specification)
	•	COGNIFLOW_v1_CANONICAL_DEFINITIONS_FINAL.md

This document supersedes all prior schema drafts, agent outputs, and chat responses.

⸻

SCHEMA 1: Session

Session {
  session_id:        UUID PRIMARY KEY,
  student_id:        STRING NOT NULL,
  problem_id:        STRING NOT NULL,
  session_start_utc: TIMESTAMP NOT NULL,
  session_end_utc:   TIMESTAMP NOT NULL,
  visibility_code:   STRING NOT NULL,
  insight_eligible:  BOOLEAN NOT NULL
}

Field Justification
	•	session_id: Unique identifier per session.
	•	student_id: Associates session to a student; format intentionally unspecified.
	•	problem_id: Enforces “one problem per session” (v1 scope).
	•	session_start_utc: Timestamp of first qualifying session event.
	•	session_end_utc: Timestamp when first session end condition occurs.
	•	visibility_code: Opaque server-defined code representing process visibility.
	•	insight_eligible: Mechanical guard preventing Insight creation for ineligible sessions.

Properties
	•	visibility_code values are:
	•	Defined server-side only
	•	Non-ordered
	•	Never exposed via API
	•	Never displayed verbatim
	•	insight_eligible is derived mechanically from visibility rules and has no semantic meaning.

Intentionally Omitted
	•	Duration fields
	•	Event counts
	•	Completion status
	•	Difficulty or outcome indicators
	•	Auto-increment IDs
	•	Ranking or ordering keys

⸻

SCHEMA 2: Event (Post-Retention Form)

Event {
  event_id:       UUID PRIMARY KEY,
  session_id:     UUID NOT NULL REFERENCES Session(session_id),
  event_type:     STRING NOT NULL,
  timestamp_utc:  TIMESTAMP NOT NULL,
  error_category: STRING NULL
}

Field Justification
	•	event_id: Unique identifier for retained event record.
	•	session_id: Associates event with a session.
	•	event_type: One of the allowed event types after retention.
	•	timestamp_utc: Event occurrence time.
	•	error_category: Present only when event_type is error.

Intentionally Omitted
	•	Inserted/deleted text
	•	Line or column numbers
	•	Idle duration
	•	Sequence numbers
	•	Stack traces or messages

All omitted fields are deleted synchronously per Canonical v1 Definitions.

⸻

SCHEMA 3: Derived_Signal

Derived_Signal {
  signal_id:                UUID PRIMARY KEY,
  session_id:               UUID NOT NULL UNIQUE REFERENCES Session(session_id),
  planning_latency_seconds: INTEGER NULL,
  iteration_depth:          INTEGER NULL,
  rewrite_ratio:            FLOAT NULL,
  error_transition_pattern: JSON NULL
}

Field Justification
	•	signal_id: Unique identifier.
	•	session_id: One-to-one relationship with Session.
	•	planning_latency_seconds: Null when not computable.
	•	iteration_depth: Null when signal not applicable.
	•	rewrite_ratio: Null when undefined.
	•	error_transition_pattern: Null when not applicable; empty list only when computed with zero errors.

Properties
	•	Derived_Signal records exist only for insight-eligible sessions.
	•	All fields are nullable to avoid forced interpretation.

Intentionally Omitted
	•	structural_convergence (UNDEFINED BY DESIGN)
	•	Confidence or reliability values
	•	Computation timestamps
	•	Aggregates or trend indicators

⸻

SCHEMA 4: Insight (Teacher-Facing)

Insight {
  insight_id:   UUID PRIMARY KEY,
  session_id:   UUID NOT NULL REFERENCES Session(session_id),
  cue_type:     STRING NOT NULL,
  created_utc:  TIMESTAMP NOT NULL
}

Field Justification
	•	insight_id: Unique identifier.
	•	session_id: Associates insight to a specific session.
	•	cue_type: Identifies which binary cue is shown.
	•	created_utc: Time of insight instantiation.

Structural Invariants
	•	Insight records must not exist for sessions where insight_eligible = false.
	•	Multiple Insight records may exist per session (multiple cues).

Intentionally Omitted
	•	Confidence or reliability indicators
	•	Priority, severity, or status fields
	•	Teacher identifiers
	•	Resolution or enforcement flags

⸻

SCHEMA 5: Student-Facing Session Record

No separate persistent schema.

Student-facing data is a filtered projection of existing schemas:

From Session and Event, scoped to the authenticated student.

Properties
	•	No duplication of persistent state
	•	No additional fields introduced
	•	Presentation logic only

⸻

GLOBAL SCHEMA OMISSIONS (APPLY TO ALL)

The following are intentionally absent across all schemas:
	•	Scores, ranks, percentiles
	•	Cohort, class, or group identifiers
	•	Difficulty normalization fields
	•	Auto-increment or ordered IDs
	•	Flags implying evaluation or enforcement
	•	Soft-delete markers
	•	Audit or author fields
	•	Versioning or migration hooks

⸻

FINAL NOTE

These schemas are minimal by design.

If a question cannot be answered without adding a new field,
Cogniflow v1 does not answer that question.

⸻

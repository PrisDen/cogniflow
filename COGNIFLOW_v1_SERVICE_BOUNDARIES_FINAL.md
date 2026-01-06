COGNIFLOW v1 — SERVICE BOUNDARIES (FINAL)

Status: AUTHORITATIVE — SERVICE BOUNDARIES FREEZE FOR COGNIFLOW v1
Depends on:
	•	COGNIFLOW TDD
	•	COGNIFLOW_v1_SCHEMA_FINAL.md
	•	COGNIFLOW_v1_SIGNAL_LOGIC_FINAL.md
	•	COGNIFLOW_v1_INSIGHT_RULES_FINAL.md
	•	COGNIFLOW_v1_OUTPUT_RULES_FINAL.md

This document supersedes all prior service-boundary drafts, agent outputs, and chat responses.

⸻

SERVICE 1: Event Ingestion Service

Owned Data (Write)
	•	Event (full payloads, pre-retention form)
	•	Session (create and update only)

Owned Data (Read)
	•	Session (own writes only)

Allowed Operations
	•	Receive event payloads from client
	•	Validate event schema
	•	Determine session start conditions
	•	Create new Session records
	•	Determine session end conditions
	•	Update Session.session_end_utc
	•	Persist full Event payloads
	•	Trigger session finalization

Explicitly Forbidden Operations
	•	Compute signals
	•	Compute visibility levels
	•	Create Insight records
	•	Delete or redact event fields
	•	Read Derived_Signal
	•	Read Insight
	•	Serve client queries

⸻

SERVICE 2: Session Finalization Service

Owned Data (Write)
	•	Session.visibility_code
	•	Session.insight_eligible

Owned Data (Read)
	•	Event (read-only, pre-deletion)

Allowed Operations
	•	Count total observable events (without categorizing by type)
	•	Compute visibility level using server-side constants
	•	Set visibility_code
	•	Set insight_eligible
	•	Trigger signal computation
	•	Trigger event retention

Explicitly Forbidden Operations
	•	Categorize or analyze events by type
	•	Modify event records
	•	Create Insight records
	•	Compute signals directly
	•	Serve client queries

⸻

SERVICE 3: Signal Computation Service

Owned Data (Write)
	•	Derived_Signal (all fields)

Owned Data (Read)
	•	Event (read-only, pre-deletion)
	•	Session (read-only: session_start_utc, session_end_utc)

Allowed Operations
	•	Read full event payloads
	•	Execute pure signal computation functions
	•	Persist computed signals to Derived_Signal
	•	Return computation completion status

Explicitly Forbidden Operations
	•	Modify Event records
	•	Modify Session records
	•	Create Insight records
	•	Compute visibility levels
	•	Delete event fields
	•	Serve client queries
	•	Store intermediate or derived state

⸻

SERVICE 4: Event Retention Service

Owned Data (Write)
	•	Event (delete and modify only)

Owned Data (Read)
	•	Event (own writes only)

Allowed Operations
	•	Delete sensitive fields from Event records
	•	Retain only:
	•	event_id
	•	session_id
	•	event_type
	•	timestamp_utc
	•	error_category
	•	Execute synchronously at session end
	•	Confirm deletion completion

Explicitly Forbidden Operations
	•	Read Derived_Signal
	•	Read Insight
	•	Create or modify any other schema
	•	Archive deleted fields
	•	Delay or queue deletion
	•	Serve client queries

⸻

SERVICE 5: Insight Creation Service

Owned Data (Write)
	•	Insight (all fields)

Owned Data (Read)
	•	Session (session_id, insight_eligible)
	•	Derived_Signal (all fields)

Allowed Operations
	•	Read Derived_Signal records
	•	Check signal NULL / non-NULL status
	•	Create Insight records when rules are satisfied
	•	Set cue_type
	•	Set created_utc

Explicitly Forbidden Operations
	•	Read Event records (pre- or post-retention)
	•	Modify Session or Derived_Signal
	•	Compute signals
	•	Apply thresholds or confidence logic
	•	Create insights for insight_eligible = false sessions
	•	Serve client queries

⸻

SERVICE 6: Student Output Service

Owned Data (Read)
	•	Session (filtered by authenticated student_id, includes derived completion status)

Allowed Operations
	•	Filter sessions by authenticated student
	•	Project allowed fields only
	•	Serve filtered data to student clients

Explicitly Forbidden Operations
	•	Read Event
	•	Read Derived_Signal
	•	Read Insight
	•	Read internal fields (visibility_code, insight_eligible, session_id)
	•	Expose event details
	•	Write any data
	•	Read other students’ data
	•	Perform aggregation or comparison

⸻

SERVICE 7: Teacher Output Service

Owned Data (Read)
	•	Session (within teacher scope)
	•	Insight
	•	Derived_Signal (explainable-on-click only)

Allowed Operations
	•	Filter sessions by teacher scope
	•	Project allowed fields only
	•	Read Insight records for cue display
	•	On click: read associated Derived_Signal values
	•	Serve filtered data to teacher clients

Explicitly Forbidden Operations
	•	Read Event records (pre- or post-retention)
	•	Read internal fields (visibility_code, insight_eligible, session_id)
	•	Expose confidence values (do not exist)
	•	Sort or order students stably
	•	Export bulk data
	•	Aggregate across students
	•	Write any data

⸻

CROSS-SERVICE CONSTRAINTS

Orchestration Requirement

For each session, services must execute in the following strict order:
	1.	Event Ingestion Service
	2.	Session Finalization Service
	3.	Signal Computation Service
	4.	Event Retention Service
	5.	Insight Creation Service

Steps 2–5 must complete synchronously before the session is queryable by any output service.

⸻

Structural Enforcement
	•	Signal Computation Service has no write access to Event
	•	Insight Creation Service has no read access to Event
	•	Output Services have no write access to any schema
	•	Event Retention Service has no read access to Derived_Signal or Insight

⸻

No Shared State

Services must not share:
	•	In-memory caches of restricted fields
	•	Confidence or reliability state
	•	Cross-student aggregates
	•	Ordering keys

⸻

EXPLICITLY NOT REQUIRED IN v1

The following services are not defined and must not be implemented in v1:
	•	Institutional reporting service (v2 scope)
	•	Cross-session analysis service (v2 scope)
	•	ML or clustering service (v3 scope)
	•	Audit or compliance service
	•	Background job schedulers
	•	Caching or cache-invalidation services

⸻

End of v1 Service Boundaries.

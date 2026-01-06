COGNIFLOW_v1_API_SURFACE_FINAL.md

Status: AUTHORITATIVE — API SURFACE FREEZE FOR COGNIFLOW v1

Response - 
COGNIFLOW v1 SERVICE-TO-SERVICE INTERFACES
SERVICE 1: Event Ingestion Service
Callable By
Client (browser/editor)
Exposed Operations
ingest_event (synchronous)
Data Direction
Write: Event, Session
Call Restrictions
Not callable by any internal service
Not callable by output services
SERVICE 2: Session Finalization Service
Callable By
Event Ingestion Service (trigger only)
Exposed Operations
finalize_session (synchronous)
Data Direction
Read: Event
Write: Session.visibility_code, Session.insight_eligible
Trigger: Signal Computation Service (next in chain)
Call Restrictions
Must not be callable by client
Must not be callable by output services
Must not be callable after signal computation
SERVICE 3: Signal Computation Service
Callable By
Session Finalization Service (trigger only)
Exposed Operations
compute_signals (synchronous)
Data Direction
Read: Event, Session
Write: Derived_Signal
Trigger: Event Retention Service (next in chain)
Call Restrictions
Must not be callable by client
Must not be callable by output services
Must not be callable before session finalization
Must complete before Event Retention begins
SERVICE 4: Event Retention Service
Callable By
Signal Computation Service (trigger only)
Exposed Operations
retain_events (synchronous)
Data Direction
Write: Event (delete fields only)
Trigger: Insight Creation Service (next in chain)
Call Restrictions
Must not be callable by client
Must not be callable by output services
Must not expose read interfaces
Must not be callable before signal computation completes
SERVICE 5: Insight Creation Service
Callable By
Event Retention Service (trigger only)
Exposed Operations
create_insights (synchronous)
Data Direction
Read: Session.insight_eligible, Derived_Signal
Write: Insight
Call Restrictions
Must not be callable by client
Must not be callable by output services
Must not be callable before event retention completes
Must not be callable before signal computation completes
SERVICE 6: Student Output Service
Callable By
Client (authenticated student only)
Exposed Operations
get_student_sessions (synchronous)
Data Direction
Read: Session (filtered)
Call Restrictions
Not callable by any internal service
Not callable by other output services
Must not be callable until session finalization chain completes
SERVICE 7: Teacher Output Service
Callable By
Client (authenticated teacher only)
Exposed Operations
get_teacher_sessions (synchronous)
get_session_explanation (synchronous)
Data Direction
Read: Session, Insight, Derived_Signal (explainable-on-click only)
Call Restrictions
Not callable by any internal service
Not callable by other output services
Must not be callable until session finalization chain completes
GLOBAL INTERFACE CONSTRAINTS
Synchronous Execution Chain
All services in the finalization chain (Services 2-5) must execute synchronously in strict order for each session.

No Backward Calls
Services must not call services earlier in the execution order:

Event Retention → Signal Computation (forbidden)
Insight Creation → Event Retention (forbidden)
Insight Creation → Signal Computation (forbidden)
Output Services → any internal service (forbidden)
No Cross-Session Calls
No service may trigger operations on sessions other than the one currently being processed.

No Asynchronous Triggers in v1
All triggers in the finalization chain are synchronous. Background jobs, queues, or retry mechanisms are forbidden.

Client Isolation
Clients may only call:

Event Ingestion Service (to submit events)
Student Output Service (authenticated students only)
Teacher Output Service (authenticated teachers only)
Clients must never call:

Session Finalization Service
Signal Computation Service
Event Retention Service
Insight Creation Service
EXPLICITLY FORBIDDEN INTERFACES
The following interfaces must NOT exist in v1:

Data Export Interfaces
No bulk export operations
No CSV/JSON serialization endpoints
No cross-student aggregation queries
Administrative Interfaces
No manual insight creation
No signal recomputation
No visibility override
No event replay or restoration
Cross-Service Data Access
Signal Computation may not query Insight
Insight Creation may not query Event
Output Services may not trigger internal services
Event Retention may not be queried for deleted data
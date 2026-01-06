COGNIFLOW v1 PROJECT STRUCTURE

Status: AUTHORITATIVE — PROJECT STRUCTURE FREEZE FOR COGNIFLOW v1


cogniflow-v1/
├── schemas/
│   ├── session.schema
│   ├── event.schema
│   ├── derived_signal.schema
│   └── insight.schema
│
├── signal_logic/
│   ├── planning_latency.compute
│   ├── iteration_depth.compute
│   ├── rewrite_ratio.compute
│   └── error_transition_pattern.compute
│
├── insight_rules/
│   ├── understanding_problem.rule
│   ├── translating_logic.rule
│   └── debugging_effectively.rule
│
├── services/
│   ├── event_ingestion/
│   │   └── ingestion.service
│   │
│   ├── session_finalization/
│   │   └── finalization.service
│   │
│   ├── signal_computation/
│   │   └── computation.service
│   │
│   ├── event_retention/
│   │   └── retention.service
│   │
│   ├── insight_creation/
│   │   └── creation.service
│   │
│   └── output/
│       ├── student.output
│       └── teacher.output
│
└── tests/
    ├── signal_logic/
    ├── insight_rules/
    └── services/
/schemas
Responsibility:

Define persistent data structures only
No logic or computation
Allowed Imports:

None (pure schema definitions)
Forbidden Imports:

Any service
Any logic module
Any other schema
/signal_logic
Responsibility:

Pure signal computation functions
Stateless transformations of Event lists to signal values
Allowed Imports:

None (must be dependency-free)
Forbidden Imports:

/schemas (cannot know about persistence)
/services (cannot know about services)
/insight_rules (cannot know about insights)
Other signal logic modules (each must be independent)
/insight_rules
Responsibility:

Binary insight creation rules
Signal null-checking logic only
Allowed Imports:

None (operates on abstract signal presence/absence)
Forbidden Imports:

/schemas/event.schema
/signal_logic (receives computed values, does not compute)
/services
/services/event_ingestion
Responsibility:

Receive events from client
Validate event schema
Persist Event records
Create and update Session records
Allowed Imports:

/schemas/event.schema
/schemas/session.schema
Forbidden Imports:

/signal_logic
/insight_rules
/schemas/derived_signal.schema
/schemas/insight.schema
Other services
/services/session_finalization
Responsibility:

Count events
Compute visibility level
Set visibility_code and insight_eligible
Allowed Imports:

/schemas/session.schema
/schemas/event.schema (read-only)
Forbidden Imports:

/signal_logic
/insight_rules
/schemas/derived_signal.schema
/schemas/insight.schema
Other services (except trigger interfaces)
/services/signal_computation
Responsibility:

Orchestrate signal computation
Persist results to Derived_Signal
Allowed Imports:

/schemas/event.schema (read-only)
/schemas/session.schema (read-only)
/schemas/derived_signal.schema (write)
/signal_logic/* (all compute modules)
Forbidden Imports:

/insight_rules
/schemas/insight.schema
Other services (except trigger interfaces)
/services/event_retention
Responsibility:

Delete sensitive fields from Event records
Execute synchronously
Allowed Imports:

/schemas/event.schema (write-only for deletion)
Forbidden Imports:

/signal_logic
/insight_rules
/schemas/derived_signal.schema
/schemas/insight.schema
/schemas/session.schema
Other services (except trigger interfaces)
/services/insight_creation
Responsibility:

Apply insight rules
Create Insight records
Allowed Imports:

/schemas/session.schema (read: insight_eligible)
/schemas/derived_signal.schema (read-only)
/schemas/insight.schema (write)
/insight_rules/* (all rule modules)
Forbidden Imports:

/schemas/event.schema
/signal_logic
Other services
/services/output/student.output
Responsibility:

Filter and project Session data for students
Expose pre-derived completion status from Session

Allowed Imports:

/schemas/session.schema (read-only, filtered projection)
Forbidden Imports:

/schemas/event.schema
/schemas/derived_signal.schema
/schemas/insight.schema
/signal_logic
/insight_rules
All other services
/services/output/teacher.output
Responsibility:

Filter and project Session data for teachers
Expose Insight cues
Serve signal values on explainable-on-click
Allowed Imports:

/schemas/session.schema (read-only, filtered projection)
/schemas/insight.schema (read-only)
/schemas/derived_signal.schema (read-only, explainable-on-click only)
Forbidden Imports:

/schemas/event.schema
/signal_logic
/insight_rules
All other services
/tests
Responsibility:

Mirror production structure
Verify boundaries are not violated
Allowed Imports:

Same as module under test
No additional access paths
Forbidden Imports:

Anything forbidden by module under test
Cross-boundary test helpers that bypass constraints
GLOBAL STRUCTURAL CONSTRAINTS
Import Direction Rule
Imports must flow in execution order only:

Services 1→2→3→4→5 (no backward imports)
Output services import schemas only
Pure logic (/signal_logic, /insight_rules) imports nothing
Isolation Enforcement
/signal_logic has zero dependencies
/insight_rules has zero dependencies
/services/event_retention cannot be imported (write-only service)
/services/output/* cannot be imported by internal services
No Shared Utilities
No /common or /utils directory
No shared helpers that bypass boundaries
Duplication is preferable to boundary violation
VERIFICATION
A correct implementation must satisfy:

/signal_logic can be tested without database
/insight_rules can be tested without Event schema
Output services cannot trigger internal services (no import path exists)
Event Retention cannot read Derived_Signal (no import path exists)

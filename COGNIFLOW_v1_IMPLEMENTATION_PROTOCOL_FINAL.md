Status: AUTHORITATIVE — IMPLEMENTATION PROTOCOL FREEZE FOR COGNIFLOW v1

COGNIFLOW v1 IMPLEMENTATION ORDER
STEP 1: Schema Definitions
Allowed Files
/schemas/session.schema
/schemas/event.schema
/schemas/derived_signal.schema
/schemas/insight.schema
Preconditions
None
Forbidden at This Step
Any imports between schemas
Any logic or computation
Any default values implying judgment
Validation Checks
All field types specified
No circular references
No computed fields
No ranking or ordering keys present
STEP 2: Signal Logic Modules
Allowed Files
/signal_logic/planning_latency.compute
/signal_logic/iteration_depth.compute
/signal_logic/rewrite_ratio.compute
/signal_logic/error_transition_pattern.compute
Preconditions
Step 1 complete (schemas exist for reference, but not imported)
Forbidden at This Step
Any imports (including schemas)
Any persistence logic
Any thresholds or confidence math
Cross-signal dependencies
Validation Checks
Each module has zero dependencies
Each function is pure (same input → same output)
NULL conditions match canonical definitions
No interpretation of ability or intent in logic
STEP 3: Insight Rules Modules
Allowed Files
/insight_rules/understanding_problem.rule
/insight_rules/translating_logic.rule
/insight_rules/debugging_effectively.rule
Preconditions
Step 1 complete
Forbidden at This Step
Importing /schemas/event.schema
Importing /signal_logic
Any computation (only null-checking)
Any thresholds
Validation Checks
Each rule has zero dependencies
Rules check only signal NULL status
No evaluation of signal values
No cross-rule dependencies
STEP 4: Event Ingestion Service
Allowed Files
/services/event_ingestion/ingestion.service
Preconditions
Step 1 complete
/schemas/event.schema exists
/schemas/session.schema exists
Forbidden at This Step
Importing signal logic
Importing insight rules
Computing visibility or signals
Triggering downstream services (not yet implemented)
Validation Checks
Imports only allowed schemas
Validates event schema
Creates Session records correctly
Session start/end conditions match canonical definitions
STEP 5: Session Finalization Service
Allowed Files
/services/session_finalization/finalization.service
Preconditions
Step 1 complete
Step 4 complete
Forbidden at This Step
Importing signal logic
Importing insight rules
Computing signals
Categorizing events by type (only counts total)
Validation Checks
Imports only allowed schemas
Event counting matches canonical definition (excludes idle)
Visibility assignment uses server-side constants correctly
Sets insight_eligible correctly
STEP 6: Signal Computation Service
Allowed Files
/services/signal_computation/computation.service
Preconditions
Step 1 complete
Step 2 complete (all signal logic modules)
Step 5 complete
Forbidden at This Step
Importing insight rules
Importing /schemas/insight.schema
Modifying Event or Session records
Creating Insight records
Validation Checks
Imports all signal logic modules
Reads Event records (pre-retention)
Calls signal functions correctly
Persists to Derived_Signal only
Handles NULL returns correctly
STEP 7: Event Retention Service
Allowed Files
/services/event_retention/retention.service
Preconditions
Step 1 complete
Step 6 complete
Forbidden at This Step
Importing signal logic
Importing insight rules
Importing other schemas (except Event)
Archiving deleted fields
Async deletion or queueing
Validation Checks
Deletes specified fields synchronously
Retains only allowed fields per canonical definition
Deletion is irreversible
No read interfaces exposed
STEP 8: Insight Creation Service
Allowed Files
/services/insight_creation/creation.service
Preconditions
Step 1 complete
Step 3 complete (all insight rules)
Step 7 complete
Forbidden at This Step
Importing /schemas/event.schema
Importing signal logic
Reading Event records
Computing signals
Creating insights for insight_eligible = false
Validation Checks
Imports only allowed schemas
Imports all insight rules
Reads Derived_Signal correctly
Creates Insight records only when rules satisfied
Respects insight_eligible flag
STEP 9: Student Output Service
Allowed Files
/services/output/student.output
Preconditions
Step 1 complete
Step 8 complete (full pipeline functional)
Forbidden at This Step
Importing Event schema
Importing Derived_Signal schema
Importing Insight schema
Importing signal logic or insight rules
Importing internal services
Reading other students' data
Validation Checks
Imports only Session schema
Filters by authenticated student_id
Projects only allowed fields
Hides all internal fields
Completion status computed correctly
STEP 10: Teacher Output Service
Allowed Files
/services/output/teacher.output
Preconditions
Step 1 complete
Step 8 complete
Forbidden at This Step
Importing Event schema
Importing signal logic or insight rules
Importing internal services
Exposing internal fields
Enabling sortable student lists
Validation Checks
Imports only allowed schemas
Filters by teacher scope
Projects only allowed fields
Explainable-on-click reveals only specified data
Low-visibility sessions handled correctly
No cross-student comparison possible
STEP 11: Tests (Optional, Per Module)
Allowed Files
/tests/signal_logic/* (after Step 2)
/tests/insight_rules/* (after Step 3)
/tests/services/* (after corresponding service steps)
Preconditions
Production module under test exists
Forbidden at This Step
Importing anything forbidden by module under test
Test helpers that bypass boundaries
Shared test utilities across boundary layers
Validation Checks
Test imports mirror production imports
No additional access paths created
Boundary violations caught by tests
Pure modules testable without database
GLOBAL VALIDATION (After All Steps)
Required Checks
No backward imports in service chain
Signal logic has zero dependencies
Insight rules have zero dependencies
Event Retention not importable
Output services not callable by internal services
No circular dependencies
All forbidden imports verified absent
Integration Validation
Full pipeline (Steps 4→5→6→7→8) executes synchronously
Output services (Steps 9-10) cannot trigger internal services
Low-visibility sessions produce no insights
Cross-student comparison structurally impossible
LOCK
Once Step 10 is complete and validated, no additional files may be added to v1.
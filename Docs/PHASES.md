# Cogniflow Development Phases

This document tracks the incremental development of Cogniflow from first principles to a working MVP.

---

## Phase 1: Backend Skeleton

**Goal**: Establish minimal application structure.

**Completed**:
- FastAPI app with health check
- Configuration management via Pydantic
- Database engine setup (no side effects on import)
- Dependency structure (`requirements.txt`)

---

## Phase 2: Authentication

**Goal**: Enable individual student accounts with email verification.

**Completed**:
- User persistence (email, password hash, verification status)
- Email verification token persistence (OTP-based, 15-minute expiration)
- Password hashing with bcrypt
- JWT-based login (24-hour token expiration)
- API routes: signup, verify-email, login
- Dev-mode OTP logging (console output when `ENV=development`)

**Explicit non-goals**:
- No password reset
- No institutional roles
- No MFA

---

## Phase 3: Sessions & Prompts

**Goal**: Track coding sessions and provide neutral prompts.

**Completed**:
- Session persistence (one prompt per session)
- Start/end session endpoints
- Prompt catalog model
- Random prompt endpoint

**Explicit non-goals**:
- No automatic session closing
- No prompt difficulty or tagging

---

## Phase 4: Execution & Event Capture (CURRENT BASELINE)

**Goal**: Execute Python code and capture run/error events.

**Completed**:
- RunEvent persistence (links to session)
- ErrorEvent persistence (links to run)
- Code execution via subprocess (2-second timeout)
- Execution endpoint captures stdout/stderr and logs events

**Explicit non-goals**:
- No grading or correctness checking
- No sandboxing beyond timeout
- No signal computation or analytics

---

## Status

**Phase 4 is the current baseline.**

This represents a complete, minimal backend for Cogniflow v1. No AI, no ML, no analytics. The system observes and records; it does not interpret or judge.

Future phases will introduce signal computation, but only after this foundation is stable and trusted.

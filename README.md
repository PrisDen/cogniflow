# Cogniflow

A cognitive observability system for programming education.

Cogniflow is built to help students see how they learn to program. It observes the process of writing code—sessions, runs, errors, and patterns—without converting that visibility into grades, rankings, or surveillance. The system is designed for individual learners, not institutions. It exists to support reflection, not evaluation.

This project rejects the idea that learning should be measured by single metrics or compared across students. Instead, it assumes that programming is a process worth observing on its own terms, and that students should own the data about how they work.

---

## Current Status

**Phase 4 Complete**: Backend MVP  
The foundation is stable and ready for baseline commit. Authentication, sessions, execution, and event capture are implemented. No AI, no ML, no analytics.

---

## Architecture Overview

Cogniflow v1 consists of:

- **Users & Email Verification**  
  Individual student accounts with email-based verification. Password hashing via bcrypt. JWT-based authentication.

- **Sessions**  
  Each session is tied to a single coding prompt. Sessions have explicit start and end boundaries.

- **Prompt Catalog**  
  Neutral coding questions that serve as starting points. Prompts are not assignments or tests.

- **Code Execution**  
  Subprocess-based Python execution with timeout. No grading. Output and errors are captured as-is.

- **Run & Error Events**  
  Every code run is recorded. Errors are logged without judgment. Events are primitives for future signal computation.

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy Core
- PostgreSQL
- Pydantic

---

## How to Run Locally

1. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

2. Set environment variables in `.env`:
   ```
   DATABASE_URL=postgresql://user:pass@localhost/cogniflow
   SECRET_KEY=your-secret-key
   ENV=development
   ```

3. Initialize database tables (manually via psql or a migration tool).

4. Run the server:
   ```bash
   uvicorn backend.app.main:app --reload
   ```

5. Access the API at `http://localhost:8000`.

---

## Philosophy

Cogniflow observes **process over outcomes**. It does not grade code, rank students, or predict success. It exists to make learning visible without converting visibility into control.

---

## License

To be determined.

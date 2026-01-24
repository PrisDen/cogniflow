import subprocess
from datetime import datetime

from fastapi import APIRouter, HTTPException
from sqlalchemy import insert

from app.config import settings
from app.db import get_engine
from app.models.events import error_events, run_events
from app.schemas.events import ExecuteRequest, ExecuteResponse

router = APIRouter(prefix="/execute", tags=["execute"])


@router.post("", response_model=ExecuteResponse)
def execute_code(request: ExecuteRequest):
    """
    Execute Python code and capture run/error events.
    
    Runs code via subprocess with 2-second timeout. Always creates a RunEvent.
    Creates ErrorEvent if stderr is non-empty. Does NOT grade correctness,
    sandbox filesystem access, or validate code quality.
    """
    engine = get_engine(settings.database_url)
    
    try:
        result = subprocess.run(
            ["python", "-c", request.code],
            capture_output=True,
            text=True,
            timeout=2
        )
        
        stdout = result.stdout
        stderr = result.stderr
        
    except subprocess.TimeoutExpired:
        stderr = "Execution timed out after 2 seconds"
        stdout = ""
    except Exception as e:
        stderr = str(e)
        stdout = ""
    
    with engine.connect() as conn:
        run_result = conn.execute(
            insert(run_events).values(
                session_id=request.session_id,
                executed_at=datetime.utcnow()
            ).returning(run_events.c.id)
        )
        run_id = run_result.fetchone()[0]
        
        if stderr:
            conn.execute(
                insert(error_events).values(
                    run_id=run_id,
                    error_message=stderr,
                    occurred_at=datetime.utcnow()
                )
            )
        
        conn.commit()
    
    if stderr:
        return ExecuteResponse(output=stderr, error=True)
    else:
        return ExecuteResponse(output=stdout, error=False)

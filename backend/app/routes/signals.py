from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.config import settings
from app.db import get_engine
from app.models.events import error_events, run_events
from app.models.sessions import sessions
from app.schemas.signals import Signal, SignalsResponse

router = APIRouter(prefix="/sessions", tags=["signals"])


@router.get("/{session_id}/signals", response_model=SignalsResponse)
def get_session_signals(session_id: int):
    """
    Compute v1 signals for a single session.
    
    Signals are descriptive summaries of observable activity. They describe
    what happened, not quality or ability. Computed on-demand from run_events,
    error_events, and session data. Does NOT store signals, compare across
    sessions, or infer intent.
    """
    engine = get_engine(settings.database_url)
    
    with engine.connect() as conn:
        session = conn.execute(
            select(sessions).where(sessions.c.id == session_id)
        ).first()
        
        if not session:
            raise HTTPException(status_code=404, detail="Session not found")
        
        runs = conn.execute(
            select(run_events).where(run_events.c.session_id == session_id)
            .order_by(run_events.c.executed_at)
        ).fetchall()
        
        errors = conn.execute(
            select(error_events)
            .join(run_events, error_events.c.run_id == run_events.c.id)
            .where(run_events.c.session_id == session_id)
            .order_by(error_events.c.occurred_at)
        ).fetchall()
    
    signals = []
    
    run_count = len(runs)
    
    if run_count == 1:
        signals.append(Signal(
            key="run_count",
            value=run_count,
            description="You ran your code once during this session."
        ))
    elif run_count > 1:
        signals.append(Signal(
            key="run_count",
            value=run_count,
            description="You ran your code multiple times during this session."
        ))
    
    if run_count > 1:
        signals.append(Signal(
            key="repeated_execution",
            value=True,
            description="The code was executed more than once during this session."
        ))
    
    if len(errors) > 0:
        signals.append(Signal(
            key="errors_present",
            value=True,
            description="Errors occurred during this session."
        ))
        
        first_error_time = errors[0].occurred_at
        runs_after_error = [r for r in runs if r.executed_at > first_error_time]
        
        if len(runs_after_error) > 0:
            signals.append(Signal(
                key="error_followed_by_run",
                value=True,
                description="After an error occurred, the code was run again."
            ))
    
    if session.ended_at is not None:
        duration_seconds = (session.ended_at - session.started_at).total_seconds()
        duration_minutes = round(duration_seconds / 60)
        
        signals.append(Signal(
            key="session_duration_minutes",
            value=duration_minutes,
            description=f"This session lasted {duration_minutes} minutes."
        ))
    
    if run_count > 0:
        first_run_time = runs[0].executed_at
        time_to_first_seconds = (first_run_time - session.started_at).total_seconds()
        time_to_first_minutes = round(time_to_first_seconds / 60)
        
        signals.append(Signal(
            key="time_to_first_run_minutes",
            value=time_to_first_minutes,
            description=f"The first code execution occurred after {time_to_first_minutes} minutes."
        ))
    
    return SignalsResponse(
        session_id=session_id,
        signals=signals
    )

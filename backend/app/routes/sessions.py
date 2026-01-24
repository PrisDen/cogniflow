from datetime import datetime

from fastapi import APIRouter, HTTPException
from sqlalchemy import insert, select, update

from app.config import settings
from app.db import get_engine
from app.models.sessions import sessions
from app.schemas.sessions import (
    EndSessionRequest,
    EndSessionResponse,
    StartSessionRequest,
    StartSessionResponse,
)

router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.post("/start", response_model=StartSessionResponse)
def start_session(request: StartSessionRequest):
    """
    Start a new coding session tied to a prompt.
    
    Each session is bound to exactly one prompt question. Does NOT validate
    user_id, check for existing open sessions, or auto-close previous sessions.
    """
    engine = get_engine(settings.database_url)
    
    with engine.connect() as conn:
        result = conn.execute(
            insert(sessions).values(
                user_id=request.user_id,
                prompt_text=request.prompt_text,
                started_at=datetime.utcnow(),
                ended_at=None
            ).returning(sessions.c.id, sessions.c.started_at)
        )
        row = result.fetchone()
        conn.commit()
    
    return StartSessionResponse(
        session_id=row[0],
        started_at=row[1]
    )


@router.post("/end", response_model=EndSessionResponse)
def end_session(request: EndSessionRequest):
    """
    End an active coding session.
    
    Sets ended_at timestamp. Prevents double-ending. Does NOT compute session
    duration, analyze activity, or generate summaries.
    """
    engine = get_engine(settings.database_url)
    
    with engine.connect() as conn:
        existing = conn.execute(
            select(sessions).where(sessions.c.id == request.session_id)
        ).first()
        
        if not existing:
            raise HTTPException(status_code=404, detail="Session not found")
        
        if existing.ended_at is not None:
            raise HTTPException(status_code=400, detail="Session already ended")
        
        ended_at = datetime.utcnow()
        
        conn.execute(
            update(sessions).where(sessions.c.id == request.session_id).values(
                ended_at=ended_at
            )
        )
        
        conn.commit()
    
    return EndSessionResponse(
        session_id=request.session_id,
        ended_at=ended_at
    )

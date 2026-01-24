from datetime import datetime

from pydantic import BaseModel


class StartSessionRequest(BaseModel):
    user_id: int
    prompt_text: str


class StartSessionResponse(BaseModel):
    session_id: int
    started_at: datetime


class EndSessionRequest(BaseModel):
    session_id: int


class EndSessionResponse(BaseModel):
    session_id: int
    ended_at: datetime

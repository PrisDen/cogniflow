from typing import Any, List

from pydantic import BaseModel

class Signal(BaseModel):
    key: str
    value: Any
    description: str

class SignalsResponse(BaseModel):
    session_id: int
    signals: List[Signal]
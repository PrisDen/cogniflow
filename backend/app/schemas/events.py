from pydantic import BaseModel


class ExecuteRequest(BaseModel):
    session_id: int
    code: str


class ExecuteResponse(BaseModel):
    output: str
    error: bool

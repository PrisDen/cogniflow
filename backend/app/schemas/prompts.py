from pydantic import BaseModel


class PromptResponse(BaseModel):
    id: int
    text: str

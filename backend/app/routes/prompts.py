from fastapi import APIRouter, HTTPException
from sqlalchemy import func, select

from app.config import settings
from app.db import get_engine
from app.models.prompts import prompts
from app.schemas.prompts import PromptResponse

router = APIRouter(prefix="/prompts", tags=["prompts"])


@router.get("/random", response_model=PromptResponse)
def get_random_prompt():
    """
    Fetch a random coding prompt from the catalog.
    
    Returns a single neutral question to start a session. Does NOT filter by
    difficulty, personalize to user, or track prompt history.
    """
    engine = get_engine(settings.database_url)
    
    with engine.connect() as conn:
        result = conn.execute(
            select(prompts).order_by(func.random()).limit(1)
        ).first()
        
        if not result:
            raise HTTPException(status_code=404, detail="No prompts available")
    
    return PromptResponse(
        id=result.id,
        text=result.text
    )

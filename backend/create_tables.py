from app.db import get_engine
from app.config import settings

from app.models.users import users
from app.models.sessions import sessions
from app.models.prompts import prompts
from app.models.events import run_events, error_events
from app.models.email_verification import email_verification_tokens

from sqlalchemy import MetaData

metadata = MetaData()

# Attach all tables to metadata
for table in [
    users,
    sessions,
    prompts,
    run_events,
    error_events,
    email_verification_tokens,
]:
    table.tometadata(metadata)

engine = get_engine(settings.database_url)

metadata.create_all(engine)

print("✅ All tables created")
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, MetaData, String, Table

metadata = MetaData()

sessions = Table(
    "sessions",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey("users.id"), nullable=False),
    Column("prompt_text", String, nullable=False),
    Column("started_at", DateTime, default=datetime.utcnow, nullable=False),
    Column("ended_at", DateTime, nullable=True),
)

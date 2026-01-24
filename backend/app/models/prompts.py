from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table

metadata = MetaData()

prompts = Table(
    "prompts",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("text", String, nullable=False),
    Column("created_at", DateTime, default=datetime.utcnow, nullable=False),
)

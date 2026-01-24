from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, MetaData, Table, Text

metadata = MetaData()

run_events = Table(
    "run_events",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("session_id", Integer, ForeignKey("sessions.id"), nullable=False),
    Column("executed_at", DateTime, default=datetime.utcnow, nullable=False),
)

error_events = Table(
    "error_events",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("run_id", Integer, ForeignKey("run_events.id"), nullable=False),
    Column("error_message", Text, nullable=False),
    Column("occurred_at", DateTime, default=datetime.utcnow, nullable=False),
)

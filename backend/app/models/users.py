from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, MetaData, String, Table

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("email", String(255), unique=True, nullable=False),
    Column("password_hash", String(255), nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
    Column("created_at", DateTime, default=datetime.utcnow, nullable=False),
)

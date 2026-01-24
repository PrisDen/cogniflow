from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, MetaData, String, Table

metadata = MetaData()

email_verification_tokens = Table(
    "email_verification_tokens",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey("users.id"), nullable=False),
    Column("otp_code", String(6), nullable=False),
    Column("expires_at", DateTime, nullable=False),
    Column("used", Boolean, default=False, nullable=False),
)

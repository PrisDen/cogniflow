from fastapi import APIRouter, HTTPException
from sqlalchemy import select, insert, update
from datetime import datetime, timedelta
import secrets
import os

from app.schemas.auth import (
    SignupRequest,
    SignupResponse,
    VerifyEmailRequest,
    VerifyEmailResponse,
    LoginRequest,
    LoginResponse
)
from app.security.auth import hash_password, verify_password, create_access_token
from app.models.users import users
from app.models.email_verification import email_verification_tokens
from app.db import get_engine
from app.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=SignupResponse)
def signup(request: SignupRequest):
    """
    Create a new user account with email verification.
    
    Generates a 6-digit OTP with 15-minute expiration. In development mode,
    the OTP is printed to console. Does NOT send emails. Does NOT validate
    email domain or password strength beyond basic requirements.
    """
    engine = get_engine(settings.database_url)
    
    with engine.connect() as conn:
        existing = conn.execute(
            select(users).where(users.c.email == request.email)
        ).first()
        
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        password_hash = hash_password(request.password)
        
        result = conn.execute(
            insert(users).values(
                email=request.email,
                password_hash=password_hash,
                is_verified=False,
                created_at=datetime.utcnow()
            ).returning(users.c.id)
        )
        user_id = result.fetchone()[0]
        
        otp_code = ''.join([str(secrets.randbelow(10)) for _ in range(6)])
        expires_at = datetime.utcnow() + timedelta(minutes=15)
        
        conn.execute(
            insert(email_verification_tokens).values(
                user_id=user_id,
                otp_code=otp_code,
                expires_at=expires_at,
                used=False
            )
        )
        
        conn.commit()
        
        if os.getenv("ENV") == "development":
            print(f"[DEV MODE] OTP for {request.email}: {otp_code}")
    
    return SignupResponse(
        email=request.email,
        message="Signup successful. Check your email for verification code."
    )


@router.post("/verify-email", response_model=VerifyEmailResponse)
def verify_email(request: VerifyEmailRequest):
    """
    Verify user email using OTP code.
    
    Validates OTP exists, has not expired, and has not been used. Marks user
    as verified. Does NOT allow re-verification or OTP regeneration.
    """
    engine = get_engine(settings.database_url)
    
    with engine.connect() as conn:
        user = conn.execute(
            select(users).where(users.c.email == request.email)
        ).first()
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        token = conn.execute(
            select(email_verification_tokens).where(
                email_verification_tokens.c.user_id == user.id,
                email_verification_tokens.c.otp_code == request.otp,
                email_verification_tokens.c.used == False
            )
        ).first()
        
        if not token:
            raise HTTPException(status_code=400, detail="Invalid OTP")
        
        if token.expires_at < datetime.utcnow():
            raise HTTPException(status_code=400, detail="OTP expired")
        
        conn.execute(
            update(users).where(users.c.id == user.id).values(is_verified=True)
        )
        
        conn.execute(
            update(email_verification_tokens).where(
                email_verification_tokens.c.id == token.id
            ).values(used=True)
        )
        
        conn.commit()
    
    return VerifyEmailResponse(message="Email verified successfully")


@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):
    """
    Authenticate user and return JWT access token.
    
    Requires verified email. Returns 24-hour JWT token. Does NOT implement
    refresh tokens, session storage, or device tracking.
    """
    engine = get_engine(settings.database_url)
    
    with engine.connect() as conn:
        user = conn.execute(
            select(users).where(users.c.email == request.email)
        ).first()
        
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        if not user.is_verified:
            raise HTTPException(status_code=403, detail="Email not verified")
        
        if not verify_password(request.password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        access_token = create_access_token(user.id)
    
    return LoginResponse(access_token=access_token, token_type="bearer")

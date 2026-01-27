from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, sessions, execute, prompts, signals

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(sessions.router)
app.include_router(execute.router)
app.include_router(prompts.router)
app.include_router(signals.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}

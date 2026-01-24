from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.middleware.sessions import SessionMiddleware
from contextlib import asynccontextmanager
import os
import time
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
import uvicorn

from app.api.auth.routes import auth_router
from app.api.oauth.routes import oauth_router
from app.core.database import engine, Base
from app.core.config import settings

# Create database tables
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: wait for DB to be ready, then create tables
    max_attempts = int(os.environ.get("DB_BOOT_WAIT_ATTEMPTS", "30"))
    sleep_seconds = float(os.environ.get("DB_BOOT_WAIT_SLEEP", "2"))
    allow_start_without_db = os.environ.get("ALLOW_START_WITHOUT_DB", "false").lower() in {"1", "true", "yes"}

    db_ready = False
    for attempt in range(1, max_attempts + 1):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            db_ready = True
            break
        except OperationalError:
            if attempt == max_attempts:
                if allow_start_without_db:
                    break
                raise
            time.sleep(sleep_seconds)

    if db_ready:
        Base.metadata.create_all(bind=engine)
    yield
    # Shutdown
    pass

app = FastAPI(
    title="Shadiejo Authentication API",
    description="FastAPI application with user authentication and OAuth",
    version="1.0.0",
    lifespan=lifespan
)

# Add session middleware for OAuth
app.add_middleware(SessionMiddleware, secret_key=settings.secret_key)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Include routers
app.include_router(auth_router)
app.include_router(oauth_router)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/signup", response_class=HTMLResponse)
async def signup_page(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/signup", response_class=HTMLResponse)
async def signup_form_submit(request: Request):
    """Handle form submission from signup page"""
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/signup", status_code=302)

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/verification-success", response_class=HTMLResponse)
async def verification_success_page(request: Request):
    return templates.TemplateResponse("verification_success.html", {"request": request})

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Shadiejo API is running"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=port,
        reload=True
    )

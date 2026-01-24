#!/usr/bin/env python3
"""
Startup script for Shadiejo FastAPI application
"""

import os
import uvicorn
from app.main import app

if __name__ == "__main__":
    print("🚀 Starting Shadiejo FastAPI Application...")
    print("📱 Frontend: http://localhost:8080")
    print("📚 API Docs: http://localhost:8080/docs")
    print("🔧 Admin Panel: http://localhost:8080/redoc")
    print("=" * 50)
    
    port = int(os.environ.get("PORT", "8080"))
    uvicorn.run(app, host="0.0.0.0", port=port, reload=True, log_level="info")
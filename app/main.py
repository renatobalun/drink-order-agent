from fastapi import FastAPI
import os
from fastapi.middleware.cors import CORSMiddleware
import logging

import uvicorn
from routers import chat
# from app.routers

app = FastAPI()

environment = os.getenv("ENVIRONMENT", "dev")

if environment == "dev":
    logger = logging.getLogger("uvicorn")
    logger.warning("Running in development mode - allowing CORS for all origins")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["POST", "GET"],
        allow_headers="*",
        expose_headers=["X-Additional-Metadata", "Access-Control-Allow-Origin"],
    )
    
app.include_router(chat.router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", reload=True)
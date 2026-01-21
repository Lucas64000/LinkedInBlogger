"""FastAPI application - main entry point with health endpoint."""

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import structlog
from fastapi import FastAPI
from fastapi.responses import JSONResponse

log = structlog.get_logger()


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan context manager for startup/shutdown events."""
    log.info("app_startup", message="AI Dev Radar starting up")
    yield
    log.info("app_shutdown", message="AI Dev Radar shutting down")


app = FastAPI(
    title="AI Dev Radar",
    description="AI-powered tool to discover trending AI/dev topics and generate LinkedIn posts",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/health")
async def health_check() -> JSONResponse:
    """Health check endpoint - returns 200 OK when the app is running."""
    return JSONResponse(status_code=200, content={"status": "ok"})

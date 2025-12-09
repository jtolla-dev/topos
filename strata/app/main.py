import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import admin, ingest, query

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

app = FastAPI(
    title="Strata API",
    description="AI data plane for enterprise file systems",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingest.router, prefix="/v0/ingest", tags=["ingest"])
app.include_router(query.router, prefix="/v0", tags=["query"])
app.include_router(admin.router, prefix="/v0/admin", tags=["admin"])


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}

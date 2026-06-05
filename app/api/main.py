from fastapi import FastAPI

from app.api.routes.investigation import (
    router as investigation_router,
)

app = FastAPI( title="HermesGuardian API", version="0.1.0", )

app.include_router(
    investigation_router
)


@app.get("/")
def health_check():

    return {
        "service": "HermesGuardian",
        "status": "healthy",
    }
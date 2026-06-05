from fastapi import FastAPI

app = FastAPI(
    title="HermesGuardian API",
    version="0.1.0",
)


@app.get("/")
def health_check():

    return {
        "service": "HermesGuardian",
        "status": "healthy",
    }
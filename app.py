from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI(
    title="ASI Deploy API",
    description="Artificial Super Intelligence deployment project - API service",
    version="0.1.0"
)

# Root endpoint
@app.get("/")
def root():
    return {"message": "🚀 ASI Deploy API is running successfully"}

# Example health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok", "service": "ASI-deploy"}


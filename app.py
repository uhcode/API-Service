import uvicorn
from fastapi import FastAPI

from routes.weather import weather_route

app = FastAPI(
    title="January API",
    description="API for anyone, anywhere, anytime",
    version="0.0.1",
    docs_url="/",
    redoc_url=None,
)

app.include_router(weather_route)

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
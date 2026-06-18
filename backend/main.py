from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from mundial_router import router as mundial_router
from weather_router import router as weather_router

app = FastAPI(title="Backend Modo Mundial 2026")

# CORS para permitir tu frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://francisco2424.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(mundial_router)
app.include_router(weather_router)

@app.get("/")
def root():
    return {"status": "Backend Modo Mundial 2026 activo"}

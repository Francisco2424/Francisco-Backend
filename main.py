from fastapi import FastAPI
from weather_router import router as weather_router

app = FastAPI(title="FranciscoMallea_Automatizaciones_Backend")

# Registrar rutas
app.include_router(weather_router)

@app.get("/")
def root():
    return {"message": "Backend de Francisco Mallea funcionando correctamente"}

from fastapi import APIRouter, Query
import requests
import os

router = APIRouter(prefix="/api", tags=["Weather"])

@router.get("/weather")
def get_weather(city: str = Query(...), country: str = Query(...)):
    api_key = os.getenv("OPENWEATHER_KEY")
    if not api_key:
        return {"error": "API key no configurada en Render"}

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city},{country}&appid={api_key}&units=metric&lang=es"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        # Si OpenWeather responde error
        if response.status_code != 200:
            return {"error": data.get("message", "No se pudo obtener el clima")}

        # Validación segura
        if "main" not in data or "weather" not in data:
            return {"error": "Datos incompletos desde OpenWeather"}

        return {
            "city": data.get("name", city),
            "country": data.get("sys", {}).get("country", country),
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
        }

    except Exception as e:
        return {"error": f"Error al consultar OpenWeather: {str(e)}"}

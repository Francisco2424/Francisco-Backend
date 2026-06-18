from fastapi import APIRouter, Query
import requests
import os

router = APIRouter(prefix="/api", tags=["Weather"])

@router.get("/weather")
def get_weather(city: str = Query(...), country: str = Query(...)):
    api_key = os.getenv("OPENWEATHER_KEY")
    if not api_key:
        return {"error": "API key no configurada en Render"}

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "No se pudo obtener el clima"}

    data = response.json()
    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }

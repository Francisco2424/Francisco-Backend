from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter()

BASE_PATH = Path(__file__).resolve().parent

def cargar_json(nombre):
    with open(BASE_PATH / nombre, "r", encoding="utf-8") as f:
        return json.load(f)

@router.get("/mundial/grupos")
def obtener_grupos():
    return cargar_json("grupos.json")

@router.get("/mundial/jugadores/{codigo_pais}")
def obtener_jugadores(codigo_pais: str):
    data = cargar_json("jugadores.json")
    codigo_pais = codigo_pais.upper()

    for pais in data["jugadores"]:
        if pais["codigo_pais"] == codigo_pais:
            return pais

    return {"error": "País no encontrado"}

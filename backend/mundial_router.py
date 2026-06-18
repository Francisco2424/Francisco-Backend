from fastapi import APIRouter
import os
import json

router = APIRouter(prefix="/mundial", tags=["Mundial"])

# Ruta base absoluta (siempre apunta al backend)
BASE = os.path.join(os.path.dirname(__file__), "datos", "mundial")

def leer_json(nombre):
    ruta = os.path.join(BASE, nombre)
    if not os.path.exists(ruta):
        return {"error": f"Archivo {nombre} no encontrado en {ruta}"}
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

@router.get("/selecciones")
def obtener_selecciones():
    return leer_json("selecciones.json")

@router.get("/jugadores")
def obtener_jugadores():
    return leer_json("jugadores.json")

@router.get("/grupos")
def obtener_grupos():
    return leer_json("grupos.json")

@router.get("/partidos")
def obtener_partidos():
    return leer_json("partidos.json")

@router.get("/estadisticas")
def obtener_estadisticas():
    return leer_json("estadisticas.json")

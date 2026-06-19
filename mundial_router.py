from fastapi import APIRouter
import os
import json

router = APIRouter(prefix="/mundial", tags=["Mundial"])

# Ruta base absoluta (backend/data/mundial)
BASE = os.path.join(os.path.dirname(__file__), "data", "mundial")

def leer_json(nombre):
    ruta = os.path.join(BASE, nombre)
    if not os.path.exists(ruta):
        return {"error": f"Archivo {nombre} no encontrado en {ruta}"}
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

# ------------------------------------------------------------
# 1. SELECCIONES
# ------------------------------------------------------------
@router.get("/selecciones")
def obtener_selecciones():
    return leer_json("selecciones.json")

# ------------------------------------------------------------
# 2. GRUPOS (con estadísticas completas)
# ------------------------------------------------------------
@router.get("/grupos")
def obtener_grupos():
    return leer_json("grupos.json")

# ------------------------------------------------------------
# 3. PARTIDOS
# ------------------------------------------------------------
@router.get("/partidos")
def obtener_partidos():
    return leer_json("partidos.json")

# ------------------------------------------------------------
# 4. ESTADÍSTICAS POR SELECCIÓN
# ------------------------------------------------------------
@router.get("/estadisticas")
def obtener_estadisticas():
    return leer_json("estadisticas.json")

# ------------------------------------------------------------
# 5. GOLEADORES DEL TORNEO
# ------------------------------------------------------------
@router.get("/goleadores")
def obtener_goleadores():
    return leer_json("goleadores.json")

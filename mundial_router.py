from fastapi import APIRouter
import os
import json

router = APIRouter(prefix="/mundial", tags=["Mundial"])

# Ruta base absoluta (siempre apunta al backend)
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
    data = leer_json("selecciones.json")
    return {"selecciones": data}

# ------------------------------------------------------------
# 2. JUGADORES
# ------------------------------------------------------------
@router.get("/jugadores")
def obtener_jugadores():
    data = leer_json("jugadores.json")
    return {"jugadores": data}

# ------------------------------------------------------------
# 3. GRUPOS
# ------------------------------------------------------------
@router.get("/grupos")
def obtener_grupos():
    data = leer_json("grupos.json")
    return {"grupos": data}

# ------------------------------------------------------------
# 4. PARTIDOS
# ------------------------------------------------------------
@router.get("/partidos")
def obtener_partidos():
    data = leer_json("partidos.json")
    return {"partidos": data}

# ------------------------------------------------------------
# 5. ESTADISTICAS
# ------------------------------------------------------------
@router.get("/estadisticas")
def obtener_estadisticas():
    data = leer_json("estadisticas.json")
    return {"estadisticas": data}

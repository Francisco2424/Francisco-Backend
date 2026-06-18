import json
import os

BASE = os.path.join(os.path.dirname(__file__), "..", "data", "mundial")

def guardar(nombre, data):
    os.makedirs(BASE, exist_ok=True)
    ruta = os.path.join(BASE, nombre)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def procesar_datos(data):
    partidos = data.get("matches", [])

    # Extraer grupos y equipos únicos
    grupos = {}
    selecciones = set()

    for partido in partidos:
        grupo = partido.get("group")
        equipo1 = partido.get("team1")
        equipo2 = partido.get("team2")

        if grupo:
            grupos.setdefault(grupo, set()).update([equipo1, equipo2])
        selecciones.update([equipo1, equipo2])

    # Convertir a listas ordenadas
    grupos_lista = [{"grupo": g, "equipos": sorted(list(e))} for g, e in grupos.items()]
    selecciones_lista = sorted(list(selecciones))

    # Estadísticas básicas por selección
    estadisticas = {team: {"partidos": 0} for team in selecciones_lista}
    for partido in partidos:
        for team in [partido.get("team1"), partido.get("team2")]:
            if team in estadisticas:
                estadisticas[team]["partidos"] += 1

    # Guardar los archivos JSON
    guardar("grupos.json", grupos_lista)
    guardar("selecciones.json", selecciones_lista)
    guardar("partidos.json", partidos)
    guardar("estadisticas.json", estadisticas)

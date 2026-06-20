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

    # ============================
    # EXTRAER SELECCIONES Y GRUPOS
    # ============================

    grupos_dict = {}
    selecciones = set()

    for partido in partidos:
        grupo = partido.get("group")
        t1 = partido.get("team1")
        t2 = partido.get("team2")

        if grupo:
            grupos_dict.setdefault(grupo, set()).update([t1, t2])

        selecciones.update([t1, t2])

    selecciones_lista = sorted(list(selecciones))

    # ============================
    # ESTADÍSTICAS POR SELECCIÓN
    # ============================

    estadisticas = {
        team: {
            "pj": 0,
            "pg": 0,
            "pe": 0,
            "pp": 0,
            "gf": 0,
            "gc": 0,
            "dg": 0,
            "puntos": 0
        }
        for team in selecciones_lista
    }

    for partido in partidos:
        t1 = partido.get("team1")
        t2 = partido.get("team2")
        score = partido.get("score", {})
        ft = score.get("ft")

        # Si el partido no tiene resultado, saltar
        if not ft:
            continue

        g1, g2 = ft

        # PJ
        estadisticas[t1]["pj"] += 1
        estadisticas[t2]["pj"] += 1

        # GF / GC
        estadisticas[t1]["gf"] += g1
        estadisticas[t1]["gc"] += g2
        estadisticas[t2]["gf"] += g2
        estadisticas[t2]["gc"] += g1

        # PG / PE / PP / Puntos
        if g1 > g2:
            estadisticas[t1]["pg"] += 1
            estadisticas[t1]["puntos"] += 3
            estadisticas[t2]["pp"] += 1
        elif g1 < g2:
            estadisticas[t2]["pg"] += 1
            estadisticas[t2]["puntos"] += 3
            estadisticas[t1]["pp"] += 1
        else:
            estadisticas[t1]["pe"] += 1
            estadisticas[t2]["pe"] += 1
            estadisticas[t1]["puntos"] += 1
            estadisticas[t2]["puntos"] += 1

    # Diferencia de gol
    for team, stats in estadisticas.items():
        stats["dg"] = stats["gf"] - stats["gc"]

    guardar("estadisticas.json", estadisticas)

    # ============================
    # GOLEADORES DEL TORNEO
    # ============================

    goleadores = {}  # { "Jugador": cantidad_goles }

    for partido in partidos:
        # Goles del equipo 1
        for g in partido.get("goals1", []):
            nombre = g.get("name")
            if not nombre:
                continue

            # Autogol → NO suma al jugador
            if g.get("owngoal"):
                continue

            # Penal → también suma como gol normal
            goleadores[nombre] = goleadores.get(nombre, 0) + 1

        # Goles del equipo 2
        for g in partido.get("goals2", []):
            nombre = g.get("name")
            if not nombre:
                continue

            if g.get("owngoal"):
                continue

            goleadores[nombre] = goleadores.get(nombre, 0) + 1

    # Ordenar goleadores por cantidad de goles
    goleadores_ordenados = sorted(
        goleadores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    guardar("goleadores.json", goleadores_ordenados)

    # ============================
    # GRUPOS CON ESTADÍSTICAS
    # ============================

    grupos_lista = []

    for grupo, equipos in grupos_dict.items():
        equipos_estad = []

        for team in sorted(equipos):
            equipos_estad.append({
                "nombre": team,
                **estadisticas[team]  # Inserta pj, pg, pe, pp, gf, gc, dg, puntos
            })

        # Ordenar por puntos, DG, GF
        equipos_estad = sorted(
            equipos_estad,
            key=lambda x: (x["puntos"], x["dg"], x["gf"]),
            reverse=True
        )

        grupos_lista.append({
            "grupo": grupo,
            "paises": equipos_estad
        })

    guardar("grupos.json", grupos_lista)

    # ============================
    # GUARDAR SELECCIONES Y PARTIDOS
    # ============================

    guardar("selecciones.json", selecciones_lista)
    guardar("partidos.json", partidos)

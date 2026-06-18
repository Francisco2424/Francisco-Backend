import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# ============================
# CONFIGURACIÓN
# ============================

land_ids = {
    "México": 76,
    "Sudáfrica": 195,
    "Corea del Sur": 55,
    "Rep. Checa": 163,
    "Canadá": 23,
    "Bosnia": 17,
    "Qatar": 153,
    "Suiza": 37,
    "Brasil": 26,
    "Marruecos": 107,
    "Haití": 82,
    "Escocia": 98,
    "USA": 184,
    "Paraguay": 128,
    "Australia": 4,
    "Turquía": 174,
    "Alemania": 40,
    "Curazao": 66,
    "Costa de Marfil": 38,
    "Ecuador": 70,
    "Países Bajos": 122,
    "Japón": 56,
    "Suecia": 147,
    "Túnez": 174,
    "Bélgica": 19,
    "Egipto": 62,
    "Irán": 65,
    "Nueva Zelanda": 89,
    "España": 157,
    "Cabo Verde": 185,
    "Arabia Saudí": 185,
    "Uruguay": 179,
    "Francia": 50,
    "Senegal": 149,
    "Irak": 64,
    "Noruega": 142,
    "Argentina": 11,
    "Argelia": 3,
    "Austria": 5,
    "Jordania": 83,
    "Portugal": 136,
    "RD Congo": 37,
    "Uzbekistán": 236,
    "Colombia": 83,
    "Inglaterra": 189,
    "Croacia": 37,
    "Ghana": 54,
    "Panamá": 157
}

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# ============================
# EXTRAER JUGADORES
# ============================

def obtener_convocados(url):
    r = requests.get(url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    tabla = soup.find("table", {"class": "items"})
    if not tabla:
        return []

    jugadores = []
    filas = tabla.find_all("tr", {"class": ["odd", "even"]})

    for fila in filas:
        cols = fila.find_all("td")
        if len(cols) < 5:
            continue

        a = cols[1].find("a")
        span = cols[1].find("span")

        nombre = a.get_text(strip=True) if a else ""
        posicion = span.get_text(strip=True) if span else ""

        dorsal = cols[0].get_text(strip=True)
        edad = cols[2].get_text(strip=True)
        club = cols[3].get_text(strip=True)
        valor = cols[4].get_text(strip=True)

        jugadores.append([nombre, dorsal, edad, posicion, club, valor])

    return jugadores

# ============================
# GENERAR EXCEL
# ============================

def main():
    with pd.ExcelWriter("convocados_mundial.xlsx", engine="openpyxl") as writer:
        for pais, lid in land_ids.items():

            print(f"\n🔎 Extrayendo: {pais} (land_id={lid})")

            url = f"https://www.transfermarkt.com/spieler/land_id/{lid}"
            print(f"→ URL: {url}")

            jugadores = obtener_convocados(url)
            print(f"  → {len(jugadores)} jugadores extraídos")

            if len(jugadores) == 0:
                continue

            df = pd.DataFrame(jugadores, columns=[
                "Jugador", "Dorsal", "Edad", "Posición", "Club", "Valor de mercado"
            ])

            df.to_excel(writer, sheet_name=pais[:31], index=False)
            time.sleep(1)

    print("\n✅ Excel generado correctamente: convocados_mundial.xlsx")


if __name__ == "__main__":
    main()

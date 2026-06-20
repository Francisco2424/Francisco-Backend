import requests
import json
from procesar_json import procesar_datos

# URL del dataset oficial del Mundial 2026 (openfootball)
URL = "https://raw.githubusercontent.com/openfootball/worldcup.json/master/2026/worldcup.json"

def actualizar():
    print("Descargando datos del Mundial 2026...")
    r = requests.get(URL)

    if r.status_code != 200:
        print("Error al descargar los datos:", r.status_code)
        return

    data = r.json()
    print("Datos descargados correctamente.")

    print("Procesando datos...")
    procesar_datos(data)
    print("Proceso completado. JSON generados en /data/mundial/")

if __name__ == "__main__":
    actualizar()

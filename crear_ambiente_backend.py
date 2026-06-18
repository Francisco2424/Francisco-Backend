import os
import json

# Ruta base del proyecto
BASE = r"C:\Francisco\2026\Independiente - Proyectos Varios\Paginas Web\ModoMundial2026\Proyectomundial"

# Estructura de carpetas
carpetas = [
    os.path.join(BASE, "backend"),
    os.path.join(BASE, "backend", "data"),
    os.path.join(BASE, "backend", "data", "mundial"),
    os.path.join(BASE, "backend", "mundial_updater"),
]

# Archivos base
archivos = {
    os.path.join(BASE, "backend", "main.py"): "# main.py — punto de entrada del backend\n",
    os.path.join(BASE, "backend", "mundial_router.py"): "# mundial_router.py — rutas del Mundial\n",
    os.path.join(BASE, "backend", "weather_router.py"): "# weather_router.py — rutas del clima\n",
    os.path.join(BASE, "backend", "requirements.txt"): "fastapi\nuvicorn\n",
    os.path.join(BASE, "backend", "mundial_updater", "procesar_json.py"): "# procesar_json.py — procesamiento de datos del Mundial\n",
    os.path.join(BASE, "backend", "mundial_updater", "update_mundial.py"): "# update_mundial.py — actualización automática de datos\n",
}

# Archivos JSON base
json_archivos = {
    "grupos.json": {"grupos": []},
    "selecciones.json": [],
    "jugadores.json": [],
    "partidos.json": [],
    "estadisticas.json": {},
}

# Crear carpetas
for carpeta in carpetas:
    os.makedirs(carpeta, exist_ok=True)
    print(f"✅ Carpeta creada: {carpeta}")

# Crear archivos base
for ruta, contenido in archivos.items():
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)
    print(f"📄 Archivo creado: {ruta}")

# Crear archivos JSON vacíos
for nombre, contenido in json_archivos.items():
    ruta = os.path.join(BASE, "backend", "data", "mundial", nombre)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(contenido, f, indent=2, ensure_ascii=False)
    print(f"🧩 JSON creado: {ruta}")

print("\n🎯 Ambiente del backend creado correctamente.")

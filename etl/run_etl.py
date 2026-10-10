"""
Punto de entrada unico del pipeline ETL de SolarBI.

Ejecuta en orden:
    1. Silver: aplica reglas de calidad a data/bronze/telemetria.csv
       y escribe data/silver/lectura_5min.csv.
    2. Gold:   carga la silver a PostgreSQL y construye el fact
       dwh.fact_energia_dia con energia diaria por dispositivo.

Es idempotente: correrlo dos veces produce los mismos conteos.

Uso:
    uv run python etl/run_etl.py

Programacion diaria (ejemplo cron, Linux):
    0 0 * * * cd /ruta/al/repo && /usr/bin/python etl/run_etl.py

Programacion diaria (Windows, Programador de tareas):
    Accion: python.exe
    Argumentos: E:\\ruta\\al\\repo\\etl\\run_etl.py
    Desencadenador: Diario a las 00:00
"""

import subprocess
import sys
from pathlib import Path

ETL_DIR = Path(__file__).parent


def correr(nombre: str) -> None:
    print(f">>> Ejecutando {nombre}")
    resultado = subprocess.run(
        [sys.executable, str(ETL_DIR / nombre)],
        check=False,
    )
    if resultado.returncode != 0:
        sys.exit(f"Fallo {nombre} con codigo {resultado.returncode}")


def main() -> None:
    print(">>> PASO 1/2: SILVER")
    correr("silver.py")
    print()
    print(">>> PASO 2/2: GOLD")
    correr("gold.py")
    print()
    print("Pipeline ETL completado.")


if __name__ == "__main__":
    main()

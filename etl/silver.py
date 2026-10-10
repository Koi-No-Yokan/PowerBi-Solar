"""
Capa Silver: aplica reglas de calidad a la telemetria cruda (Bronze)
y produce un dataset limpio listo para la capa Gold.

Reglas aplicadas (en orden):
    1. Datos faltantes en columnas criticas.
    2. Rango fisico valido (potencia, irradiancia, temperatura).
    3. Duplicados por (ts, dispositivo_id).

Salida: data/silver/lectura_5min.csv
"""

from pathlib import Path
import pandas as pd

BRONZE = Path("data/bronze/telemetria.csv")
SILVER = Path("data/silver/lectura_5min.csv")

RANGO_POTENCIA_AC_KW = (0.0, 6.0)        # inversor de 5 kWp. Se da un margen según la potencia establecida para el inversor en kW, dejando margen para posibles picos de energía
RANGO_IRRADIANCIA = (0.0, 1500.0) # W/m2
RANGO_TEMPERATURA_MODULO = (-20.0, 85.0) # grados C

COLUMNAS_CRITICAS = ["p_ac_kw", "irradiancia_wm2", "temp_modulo_c"]


def main() -> None:
    SILVER.parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(BRONZE)
    total_leidas = len(df)

    df["ts"] = pd.to_datetime(df["ts"], errors="coerce")
    for col in COLUMNAS_CRITICAS:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Regla 1: Verifica que no hay registros en el dataframe vacios
    mask_faltantes = df[COLUMNAS_CRITICAS + ["ts"]].isna().any(axis=1)
    rech_faltantes = int(mask_faltantes.sum())
    df = df.loc[~mask_faltantes].copy()

    # Regla 2: Identifica que los datos presentes en el archivo original esten dentro de los rangos definidos como físicamente viables
    mask_rango = (
        df["p_ac_kw"].between(*RANGO_POTENCIA_AC_KW) # Identifica que la potencia esté en el rango soportado por el inversor
        & df["irradiancia_wm2"].between(*RANGO_IRRADIANCIA)
        & df["temp_modulo_c"].between(*RANGO_TEMPERATURA_MODULO)
    )
    rech_rango = int((~mask_rango).sum())
    df = df.loc[mask_rango].copy()

    # Regla 3: Elimina los registro duplicados en el data source
    mask_dup = df.duplicated(subset=["ts", "dispositivo_id"], keep="first")
    rech_duplicados = int(mask_dup.sum())
    df = df.loc[~mask_dup].copy()

    df = df.sort_values(["dispositivo_id", "ts"]).reset_index(drop=True)
    df.to_csv(SILVER, index=False)

    validas = len(df)
    pct_validos = (validas / total_leidas * 100) if total_leidas else 0.0

    print("=" * 48)
    print("REPORTE DE CALIDAD - CAPA SILVER")
    print("=" * 48)
    print(f"Filas leidas:              {total_leidas:>6}")
    print(f"Rechazadas (faltantes):    {rech_faltantes:>6}")
    print(f"Rechazadas (rango):        {rech_rango:>6}")
    print(f"Rechazadas (duplicados):   {rech_duplicados:>6}")
    print(f"Filas validas:             {validas:>6}")
    print(f"% datos validos:           {pct_validos:>6.2f}%")
    print("=" * 48)
    print(f"Salida: {SILVER}")


if __name__ == "__main__":
    main()

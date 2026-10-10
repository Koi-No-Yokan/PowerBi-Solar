# Nombre el proyecto: Solarbi-Jimenez-Valencia

## Integrantes del equipo:

- Joseph Santiago Jimenez Jimenez [joseph.jimenez108@pascualbravo.edu.co]
- Miguel Angel Valencia Velez [miguel.valencia664@pascualbravo.edu.co]

## Descripción del curso

**Curso**: 2026-02 Grupo 01 INTELIGENCIA DE NEGOCIOS BI GRUPO 01 ANALITICA DE DATOS
**Docente**: RAMIRO GRISALES MONTOYA

## Descripción del trabajo

Consulta y práctica guiada del proyecto **SolarBI Pascual**, con enfoque en el
monitoreo operativo de una planta solar (Grupo 01). El trabajo compara **Power
BI** y **Grafana** sobre un mismo conjunto de datos y da los primeros pasos en
tres pilares del proyecto:

- **Gobernanza de datos**: roles, contrato de datos, RLS y marco legal.
- **Automatización ETL**: simulación de telemetría, reglas de calidad y carga
  idempotente en PostgreSQL siguiendo las capas Bronze → Silver → Gold.
- **IoT**: arquitectura por capas, MQTT y la pila abierta de monitoreo.

Todo el flujo se controla con Git y se entrega en este repositorio público.

## Práctica

### Requisitos

- Python 3.12 (gestionado con [uv](https://docs.astral.sh/uv/)).
- PostgreSQL 16 corriendo en `localhost:5432`.
- Power BI Desktop.
- Grafana OSS (local o en Docker).

### Pasos para reproducir

```bash
# 1. Clonar el repositorio e instalar dependencias
git clone <url-del-repo>
cd <carpeta>
uv sync

# 2. Configurar credenciales de PostgreSQL
cp .env.example .env
# editar .env con la contraseña real

# 3. Crear la base de datos
psql -U postgres -c "CREATE DATABASE solarbi;"

# 4. Generar la telemetría cruda (capa Bronze)
uv run python etl/simulador.py

# 5. Ejecutar el pipeline completo (Silver + Gold)
uv run python etl/run_etl.py

# 6. Verificar idempotencia (correr dos veces, los conteos no cambian)
uv run python etl/run_etl.py
```

Después:

- Abrir `powerbi/solarbi.pbix` en Power BI Desktop.
- Importar `grafana/dashboard.json` en Grafana (Dashboard → Import).

### Estructura del repositorio

```
.
├── README.md
├── .gitignore
├── .env.example
├── pyproject.toml / uv.lock       # dependencias Python
├── doc/                           # PDF de la consulta y material de apoyo
├── data/
│   ├── bronze/                    # telemetría cruda generada por el simulador
│   └── silver/                    # datos limpios tras reglas de calidad
├── etl/
│   ├── simulador.py               # genera telemetría cruda
│   ├── silver.py                  # aplica reglas de calidad
│   ├── gold.py                    # UPSERT a PostgreSQL
│   └── run_etl.py                 # punto de entrada único (silver + gold)
├── sql/
│   └── 01_schema.sql              # schemas y tablas
├── powerbi/
│   └── solarbi.pbix               # cuadro de mando directivo
└── grafana/
    └── dashboard.json             # tablero operativo
```

## Responsabilidades

| Integrante | Aportes principales |
| :--- | :--- |
| Joseph Santiago Jimenez Jimenez | Parte A (consulta): bloques de gobernanza e IoT. Tablero en Grafana. Documento PDF final. |
| Miguel Angel Valencia Velez | Parte A (consulta): bloques de Power BI/Grafana, ETL y control de versiones. Pipeline ETL (simulador, silver, gold). Cuadro de mando en Power BI. Estructura del repositorio. |

> La tabla refleja la coordinación general; ambos integrantes revisaron y
> aprobaron el trabajo completo antes de la entrega.
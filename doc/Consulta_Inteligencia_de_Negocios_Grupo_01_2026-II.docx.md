**INSTITUCIÓN UNIVERSITARIA PASCUAL BRAVO**

Estrategia de Articulación EnContexto · Departamento de Sistemas Digitales

**Trabajo de consulta en parejas**

**SolarBI Pascual: Power BI y Grafana, gobernanza de datos, automatización ETL e IoT**

Inteligencia de Negocios · Grupo 01 · Semestre 2026-II · Docente: Ramiro Grisales Montoya

# **1\. Propósito**

En SolarBI el cuadro de mando final se construye en Power BI. Sin embargo, en la industria el monitoreo de plantas y equipos suele hacerse con Grafana. En esta consulta compararán las dos herramientas sobre los mismos datos y darán sus primeros pasos en tres temas que sostienen el proyecto: gobernanza de datos, automatización de procesos ETL e Internet de las Cosas (IoT), trabajando con control de versiones en GitHub.

**Enfoque del Grupo 01:** monitoreo operativo. Su práctica se centra en la potencia en el tiempo y en la detección de fallas.

# **2\. Ficha del trabajo**

| Campo | Contenido |
| :---- | :---- |
| **Curso / Grupo** | Inteligencia de Negocios · Grupo 01 |
| **Modalidad** | Parejas (dos integrantes). Una sola entrega por pareja. |
| **Tiempo disponible** | Dos (2) días a partir de la publicación en Google Classroom. |
| **Fecha límite** | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| **Valor** | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |
| **Articulación** | Proyecto de Aula SolarBI Pascual. Prepara el Entregable III (esquema estrella y flujo ETL, semana 12\) y el Entregable V (cuadro de mando, semana 16). |
| **Entrega** | Un archivo PDF central \+ repositorio en GitHub con los archivos de soporte. |

Indicadores de resultado de aprendizaje que moviliza: U2-a (lago de datos), U2-b (calidad de datos), U2-d (flujos ETL), U3-d (indicadores de desempeño), U3-e (cuadros de mando) y U2-e (responsabilidad frente a la información).

# **3\. Parte A · Consulta**

Respondan cada pregunta con sus propias palabras, en máximo 120 palabras, aplicándola al caso SolarBI e indicando la fuente. Las tablas, los diagramas y los fragmentos de código no cuentan en el límite.

## **Bloque 1 · Power BI y Grafana**

**D1.**¿Qué es Grafana? Describan sus componentes: data sources, panels, dashboards, variables y alerting. Diferencien Grafana OSS de Grafana Cloud.

**D2.**Elaboren una tabla comparativa Power BI vs. Grafana con mínimo 8 criterios: propósito principal, usuario típico, conexión a los datos, modelo semántico y lenguaje (DAX frente a la consulta del origen), actualización y tiempo real, alertas, licenciamiento y costo, y control de acceso.

**D3.**Diferencien un dashboard operativo, uno analítico y uno estratégico. Clasifiquen cada KPI mínimo del proyecto (energía, yield y Performance Ratio, ahorro, disponibilidad y alarmas, porcentaje de datos válidos) e indiquen en cuál de las dos herramientas lo publicarían y por qué.

**D4.**Grafana con PostgreSQL: ¿cómo debe ser una consulta de series de tiempo y para qué sirven las macros \$\_\_timeFilter y \$\_\_timeGroup? Escriban la consulta de la potencia promedio por hora.

**D5.**Alertas: comparen Grafana Alerting (alert rules y contact points) con las alertas de datos del servicio de Power BI. Propongan una regla de alerta útil para la planta y el canal por el que se notificaría.

## **Bloque 2 · Gobernanza de datos (data governance)**

**G1.**Definan data governance y diferéncienla de data management y de data quality. Tomen como referencia el marco DAMA-DMBOK.

**G2.**Expliquen los roles data owner, data steward y data custodian. Relaciónenlos con los roles del equipo en el proyecto (data engineer, data modeler, BI analyst y product owner).

**G3.**El contrato de datos (data contract) del proyecto como instrumento de gobernanza: ¿qué debe incluir (esquema, unidades, frecuencia, responsable, niveles de calidad)? ¿Qué le pasa al cuadro de mando si la fuente cambia un campo sin avisar?

**G4.**Seguridad a nivel de fila (row-level security, RLS) en Power BI: roles y filtros DAX. Den el ejemplo de un responsable que solo ve su sitio. ¿Cuál es el mecanismo equivalente de control de acceso en Grafana (organizaciones, equipos y permisos por carpeta o dashboard)?

**G5.**Ley 1581 de 2012 (protección de datos personales en Colombia): ¿los datos de SolarBI son personales? ¿Qué cambiaría si el tablero mostrara qué operador atendió cada alarma? Fijen la postura del equipo frente al manejo responsable de la información.

## **Bloque 3 · Automatización de procesos ETL**

**E1.**Diferencien ETL de ELT y ubiquen cada paso en las capas Bronze, Silver y Gold del proyecto. ¿Power Query es una herramienta ETL? Argumenten.

**E2.**Comparen carga completa (full load) y carga incremental. ¿Qué significa que una carga sea idempotente y cómo se logra en fact\_energia\_dia con su clave primaria (fecha\_key, dispositivo\_key) y un UPSERT?

**E3.**Elaboren una tabla comparativa de tres formas de automatizar un flujo: cron (o el Programador de tareas de Windows), Apache Airflow y la actualización programada de Power BI. Incluyan qué es, qué automatiza cada una y cuándo conviene.

**E4.**Query folding en Power Query: ¿qué es, por qué mejora el rendimiento y cómo se verifica si un paso se está plegando hacia PostgreSQL?

## **Bloque 4 · Internet de las Cosas (IoT)**

**I1.**Describan la arquitectura IoT por capas: dispositivo, gateway (edge), red o broker, almacenamiento y aplicación. Dibujen cómo viaja una lectura del inversor hasta llegar a un visual del tablero, indicando en qué capa (Bronze, Silver, Gold) queda en cada momento.

**I2.**Expliquen MQTT: modelo publish/subscribe, broker, topic y niveles de QoS (0, 1 y 2). Propongan la jerarquía de topics de la planta, por ejemplo pascualbravo/solar/\<sitio\>/\<dispositivo\>/\<variable\>.

**I3.**Describan una pila abierta típica de monitoreo IoT: Mosquitto, Telegraf, una base de series de tiempo (InfluxDB o TimescaleDB) y Grafana. ¿Qué papel cumple cada componente y dónde encajaría PostgreSQL?

**I4.**Procesamiento por lotes (batch) frente a flujo continuo (streaming). La telemetría llega cada 5 minutos y fact\_energia\_dia tiene granularidad diaria: ¿qué se gana y qué se pierde al agregar? ¿Qué herramienta atiende mejor cada granularidad?

## **Bloque 5 · Control de versiones**

**V1.**Diferencien Git de GitHub y definan repository, commit, branch y pull request. Un archivo .pbix es binario: ¿qué problema genera en Git y qué resuelve el formato Power BI Project (.pbip)? ¿Cómo se versiona un dashboard de Grafana?

# **4\. Parte B · Práctica guiada: los mismos datos en dos herramientas**

Construirán un flujo pequeño pero completo: datos crudos de un dispositivo simulado, limpieza con reglas de calidad, carga en PostgreSQL y dos visualizaciones sobre esa misma base, una en Power BI y otra en Grafana.

## **Paso 1 · Bronze: datos crudos**

Usen el dataset del contrato de datos del curso o, si lo prefieren, este simulador base (etl/simulador.py), que genera 3 días de telemetría de un inversor de 5 kWp con anomalías inyectadas. El archivo de Bronze no se modifica.

import csv, math, os, random  
from datetime import datetime, timedelta  
   
inicio \= datetime(2026, 10, 5, 0, 0\)  
os.makedirs("data/bronze", exist\_ok=True)  
   
with open("data/bronze/telemetria.csv", "w", newline="", encoding="utf-8") as f:  
    w \= csv.writer(f)  
    w.writerow(\["ts", "dispositivo\_id", "p\_ac\_kw", "irradiancia\_wm2", "temp\_modulo\_c"\])  
    for i in range(3 \* 288):                          \# 3 dias, cada 5 min  
        ts \= inicio \+ timedelta(minutes=5 \* i)  
        sol \= max(0.0, math.sin(math.pi \* (ts.hour \+ ts.minute / 60 \- 6\) / 12))  
        irr \= round(1000 \* sol \* random.uniform(0.7, 1.0), 1\)  
        p\_ac \= round(5.0 \* irr / 1000 \* random.uniform(0.80, 0.90), 3\)  
        fila \= \[ts.isoformat(sep=" "), 1, p\_ac, irr, round(22 \+ 30 \* sol, 1)\]  
        r \= random.random()  
        if r \< 0.02:  
            fila\[2\] \= \-1                              \# anomalia: potencia negativa  
        elif r \< 0.04:  
            fila\[3\] \= ""                              \# anomalia: dato faltante  
        w.writerow(fila)  
        if r \> 0.98:  
            w.writerow(fila)                          \# anomalia: fila duplicada

## **Paso 2 · Silver: reglas de calidad**

Con Python (pandas) o con SQL, apliquen mínimo tres reglas de calidad: rango físico válido, duplicados y datos faltantes. Reporten filas leídas, filas rechazadas por cada regla, filas válidas y el porcentaje de datos válidos.

## **Paso 3 · Gold: carga en PostgreSQL**

* Carguen las lecturas limpias de 5 minutos en una tabla silver.lectura\_5min.

* Carguen el resumen diario en una tabla con la estructura de dwh.fact\_energia\_dia (como mínimo: fecha, dispositivo, energia\_kwh y pct\_datos\_validos). Recuerden que la energía de cada intervalo es la potencia por 5/60 de hora.

* Dejen todo en un solo punto de entrada (etl/run\_etl.py) que se ejecute con un único comando. Ejecútenlo dos veces y demuestren que los conteos no cambian (carga idempotente).

* Escriban, sin necesidad de implementarla, la expresión cron (o la configuración del Programador de tareas) que lanzaría ese comando cada día a la medianoche.

## **Paso 4 · Power BI**

Conecten Power BI Desktop a PostgreSQL y construyan una página con: una tarjeta con la energía total (kWh), un gráfico de líneas con la energía diaria y una tarjeta con el porcentaje de datos válidos. Las cifras deben salir de medidas DAX, no de columnas arrastradas.

## **Paso 5 · Grafana**

Instalen Grafana OSS en su equipo (instalador o Docker), agreguen PostgreSQL como data source y construyan un dashboard con:

* Un panel de series de tiempo con la potencia p\_ac\_kw cada 5 minutos, usando \$\_\_timeFilter en la consulta.

* Un umbral (threshold) o una regla de alerta que se active cuando la potencia sea cero entre las 9:00 y las 15:00.

* Un panel tipo stat con la energía del día seleccionado.

* Exporten el dashboard como JSON y guárdenlo en el repositorio.

Si no logran instalar Grafana, documenten el error con capturas, expliquen qué intentaron y exploren los tableros de ejemplo de play.grafana.org para sustentar su comparación. Esta ruta alterna se evalúa con menor puntaje en el criterio de tableros.

## **Paso 6 · Reflexión**

En máximo 10 líneas: con los mismos datos, ¿qué resolvió mejor cada herramienta?, ¿qué les costó más?, ¿cuál usarían para el operador de la planta y cuál para un directivo?

**Evidencias de la Parte B en el PDF:** una captura por paso con una explicación de dos o tres líneas, incluidas las capturas de los dos tableros. El código va en el repositorio, no pegado completo en el PDF.

# **5\. Parte C · Repositorio en GitHub**

Todo el trabajo se desarrolla y se entrega integrado a un repositorio en GitHub. Este repositorio no es de un solo uso: será la base sobre la que continuarán los siguientes trabajos del proyecto hasta el final del semestre.

* Un integrante crea el repositorio **público** con el nombre solarbi-apellido1-apellido2.

* Agrega a su compañero como **colaborador** (Settings → Collaborators → Add people). El compañero debe aceptar la invitación antes de la entrega.

* Los dos integrantes deben aportar: mínimo **3 commits por persona**, con mensajes descriptivos (no "update" ni "cambios").

* El README.md incluye: nombres completos, curso y grupo, descripción del trabajo, pasos para reproducir la práctica y una tabla breve de quién hizo qué.

* Incluyan un .gitignore. **Nunca** suban contraseñas ni cadenas de conexión; usen variables de entorno o un archivo .env excluido del repositorio.

Estructura mínima del repositorio:

solarbi-apellido1-apellido2/  
├── README.md  
├── .gitignore  
├── docs/       PDF de la consulta  
├── data/       bronze/ (crudo) y silver/ (limpio)  
├── etl/        simulador.py, run\_etl.py  
├── sql/        tablas y cargas en PostgreSQL  
├── powerbi/    archivo .pbix o proyecto .pbip  
└── grafana/    dashboard.json exportado

**Evidencias que deben aparecer en el PDF:** enlace al repositorio, captura de la sección Collaborators con los dos integrantes y captura del historial de commits donde se vean ambos autores.

# **6\. Condiciones de entrega**

* El archivo central es **un único PDF**. La revisión y la calificación se hacen sobre ese PDF: lo que no esté allí no se evalúa.

* El nombre del archivo lleva los **nombres y apellidos completos de los dos integrantes**, así: NombreCompleto1\_NombreCompleto2\_Consulta\_BI\_G01.pdf.

* Contenido del PDF, en este orden: portada (nombres completos, curso, grupo y fecha), Parte A con cada respuesta identificada por su código, Parte B con las capturas y explicaciones, Parte C con el enlace y las capturas de GitHub, y referencias.

* Los demás archivos (scripts, SQL, datos de muestra y otros que requieran) pueden adjuntarse en la entrega y deben estar también en el repositorio.

* Se sube una sola vez por pareja en Google Classroom, con el enlace al repositorio en el comentario de la entrega.

* Extensión sugerida del PDF: máximo 18 páginas. Mínimo 5 fuentes consultadas, citadas en el texto y listadas al final.

# **7\. Rúbrica de evaluación**

| Criterio | Descriptor de nivel alto | Peso |
| :---- | :---- | ----- |
| **Consulta (Parte A)** | Respuestas correctas, en palabras propias, aplicadas a SolarBI y con fuentes confiables citadas. | 35% |
| **Flujo ETL (Parte B)** | Reglas de calidad documentadas, carga idempotente en PostgreSQL con un solo comando y métricas de calidad reportadas. | 20% |
| **Tableros (Parte B)** | Power BI con medidas DAX y Grafana con consulta de series de tiempo, ambos sobre la misma base, y una reflexión comparativa bien argumentada. | 20% |
| **GitHub (Parte C)** | Repositorio ordenado, README reproducible, compañero como colaborador y commits de ambos integrantes. | 15% |
| **Presentación y ética** | PDF con el nombre exigido, bien organizado, con referencias y sin credenciales expuestas. | 10% |

# **8\. Proyección del trabajo**

Esta consulta es el primero de una serie de trabajos que, de aquí al final del semestre, estarán ligados al proyecto SolarBI Pascual. Lo que construyan aquí (repositorio, flujo ETL y datos simulados) se reutiliza en el Entregable III (esquema estrella y flujo ETL) y en el cuadro de mando final.

Con base en estas entregas se identificarán los trabajos con mayor potencial para continuar hacia el PIA y la ruta EnContexto. Trabajen pensando en que su repositorio puede ser el punto de partida de ese proyecto.

# **9\. English corner**

Vocabulario técnico de este trabajo: data governance, data steward, data contract, data lineage, single source of truth, row-level security, data source, panel, time series, alert rule, threshold, real-time monitoring, scheduled refresh, incremental load, idempotent, orchestration, broker, topic, payload, version control, commit, pull request.

Frase para el README: "One governed dataset, two views: Grafana for real-time operations and Power BI for business decisions."
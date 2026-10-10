-- Esquema de la capa Gold para SolarBI.
-- Crea los schemas y tablas usados por el ETL. Es idempotente: puede
-- ejecutarse multiples veces sin romper nada (IF NOT EXISTS).

CREATE SCHEMA IF NOT EXISTS silver;
CREATE SCHEMA IF NOT EXISTS dwh;

-- Capa silver: lecturas limpias cada 5 minutos.
CREATE TABLE IF NOT EXISTS silver.lectura_5min (
    ts              TIMESTAMP NOT NULL,
    dispositivo_id  INT       NOT NULL,
    p_ac_kw         NUMERIC(6,3),
    irradiancia_wm2 NUMERIC(7,1),
    temp_modulo_c   NUMERIC(5,1),
    PRIMARY KEY (ts, dispositivo_id)
);

-- Capa gold: fact de energia diaria por dispositivo.
CREATE TABLE IF NOT EXISTS dwh.fact_energia_dia (
    fecha_key         DATE          NOT NULL,
    dispositivo_key   INT           NOT NULL,
    energia_kwh       NUMERIC(10,3) NOT NULL,
    pct_datos_validos NUMERIC(5,2)  NOT NULL,
    PRIMARY KEY (fecha_key, dispositivo_key)
);

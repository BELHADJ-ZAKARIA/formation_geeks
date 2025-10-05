CREATE TABLE IF NOT EXISTS public.country_data (
  id         SERIAL PRIMARY KEY,
  name       TEXT NOT NULL UNIQUE,
  capital    TEXT,
  flag       TEXT,
  subregion  TEXT,
  population BIGINT
);
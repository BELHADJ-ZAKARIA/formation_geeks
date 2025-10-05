import random
import requests
from countries_db import get_conn
from contextlib import contextmanager

API_URL = "https://restcountries.com/v3.1/all?fields=name,capital,flags,subregion,population"
HEADERS = {"User-Agent": "CountrySeeder/1.0"}

@contextmanager
def db_cursor():
    conn = None
    try:
        conn = get_conn()
        with conn:
            with conn.cursor() as cur:
                yield cur
    finally:
        if conn:
            conn.close()

def ensure_schema():
    schema_sql = """
    CREATE TABLE IF NOT EXISTS public.country_data (
      id         SERIAL PRIMARY KEY,
      name       TEXT NOT NULL UNIQUE,
      capital    TEXT,
      flag       TEXT,
      subregion  TEXT,
      population BIGINT
    );
    """
    with db_cursor() as cur:
        cur.execute(schema_sql)

# ---------- API + normalization ----------
def normalize(country):
    """Map REST Countries object to our row tuple."""
    name_obj = country.get("name") or {}
    name = name_obj.get("common") or name_obj.get("official")
    capital_val = country.get("capital")
    capital = (
        capital_val[0] if isinstance(capital_val, list) and capital_val
        else (capital_val if isinstance(capital_val, str) else None)
    )
    flags = country.get("flags") or {}
    flag = flags.get("svg") or flags.get("png")  # prefer SVG, then PNG
    subregion = country.get("subregion")
    population = country.get("population")
    return (name, capital, flag, subregion, population)

def fetch_random_rows(count=10):
    r = requests.get(API_URL, headers=HEADERS, timeout=30)
    r.raise_for_status()
    data = r.json()
    sample_size = min(count, len(data))
    picked = random.sample(data, k=sample_size)
    rows = [normalize(c) for c in picked]
    # Drop any rows without a name (should be rare)
    return [r for r in rows if r[0]]

# ---------- Insert / Upsert ----------
UPSERT_SQL = """
INSERT INTO public.country_data (name, capital, flag, subregion, population)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (name) DO UPDATE SET
  capital    = EXCLUDED.capital,
  flag       = EXCLUDED.flag,
  subregion  = EXCLUDED.subregion,
  population = EXCLUDED.population;
"""

def seed_random_countries(count=10):
    print(f"\n--- Fetching {count} Random Countries ---")
    ensure_schema()
    rows = fetch_random_rows(count)
    if not rows:
        print("No rows to insert.")
        return 0
    with db_cursor() as cur:
        cur.executemany(UPSERT_SQL, rows)
    print(f"✓ Upserted {len(rows)} countries into public.country_data")
    return len(rows)

# ---------- Optional: show a preview ----------
def show_top_by_population(limit=20):
    ensure_schema()
    with db_cursor() as cur:
        cur.execute("""
            SELECT name, capital, subregion, population
            FROM public.country_data
            ORDER BY population DESC NULLS LAST
            LIMIT %s;
        """, (limit,))
        rows = cur.fetchall()
    if not rows:
        print("\nNo country data found.")
        return
    # Format pretty table
    name_w = max(max((len(r[0]) for r in rows), default=12), len("Country Name"))
    cap_w  = max(max((len(r[1] or '-') for r in rows), default=7), len("Capital"))
    sub_w  = max(max((len(r[2] or '-') for r in rows), default=9), len("Subregion"))
    header = f"| {'Country Name':<{name_w}} | {'Capital':<{cap_w}} | {'Subregion':<{sub_w}} | {'Population':>12} |"
    print("\n" + "="*len(header))
    print("STORED COUNTRY DATA (Top by Population)")
    print("="*len(header))
    print(header)
    print("-"*len(header))
    for name, capital, subregion, population in rows:
        pop_str = f"{population:,}" if population is not None else "-"
        print(f"| {name:<{name_w}} | {capital or '-':<{cap_w}} | {subregion or '-':<{sub_w}} | {pop_str:>12} |")
    print("="*len(header))

if __name__ == "__main__":
    seed_random_countries(10)
    show_top_by_population(20)
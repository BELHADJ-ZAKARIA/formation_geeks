import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_conn():
    try:
        conn = psycopg2.connect(
            host=os.getenv("HOST"),
            port=os.getenv("PORT"),
            database=os.getenv("DATABASE"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD")
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database connection error: Please check DB_CONFIG in countries_db.py. Error details: {e}")
        return None
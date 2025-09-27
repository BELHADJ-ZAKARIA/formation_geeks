""" Database connection """

import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()


def get_db_connection():
    """ Connect to the database """

    try:
        conn = psycopg2.connect(
            host=os.getenv("HOST"),
            port=os.getenv("PORT"),
            database=os.getenv("DATABASE"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            cursor_factory=RealDictCursor
        )
    except psycopg2.OperationalError as e:
        print(e)
        return None
    # pylint: disable=W0718
    except Exception as e:
        print(e)
        return None

    return conn

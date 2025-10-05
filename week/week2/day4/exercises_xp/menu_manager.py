# 3. menu_manager.py 

import psycopg2
from dotenv import load_dotenv
from menu_item import connect_db, MenuItem


load_dotenv()

class MenuManager:
    @classmethod
    def get_by_name(cls, item_name):
        conn = connect_db()
        if conn is None:
            return None

        try:
            cursor = conn.cursor()
            sql = "SELECT item_name, item_price FROM Menu_Items WHERE item_name = %s;"
            cursor.execute(sql, (item_name,))
            record = cursor.fetchone()

            if record:
                return MenuItem(record[0], record[1])
            else:
                return None

        except psycopg2.Error as e:
            print(f"Database error fetching item by name: {e}")
            return None
        finally:
            if conn:
                conn.close()

    @classmethod
    def all_items(cls):
        conn = connect_db()
        if conn is None:
            return []

        items_list = []
        try:
            cursor = conn.cursor()
            sql = "SELECT item_name, item_price FROM Menu_Items ORDER BY item_name;"
            cursor.execute(sql)
            records = cursor.fetchall()

            for record in records:
                items_list.append(MenuItem(record[0], record[1]))

            return items_list

        except psycopg2.Error as e:
            print(f"Database error fetching all items: {e}")
            return []
        finally:
            if conn:
                conn.close()
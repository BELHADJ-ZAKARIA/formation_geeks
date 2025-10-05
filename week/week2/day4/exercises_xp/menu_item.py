#Part I:
# 2. menu_item.py

import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def connect_db():
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
        print(f"Database connection error: Please check DB_CONFIG in menu_item.py. Error details: {e}")
        return None

class MenuItem:
    def __init__(self, item_name, item_price):
        try:
            self.name = str(item_name).strip()
            self.price = int(item_price)
        except ValueError:
            raise ValueError("Item price must be a valid integer.")

        if not self.name:
            raise ValueError("Item name cannot be empty.")

    def save(self):
        conn = connect_db()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            sql = "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s);"
            cursor.execute(sql, (self.name, self.price))
            conn.commit()
            return True
        except psycopg2.IntegrityError:
            print(f"Error saving item: Item '{self.name}' already exists.")
            conn.rollback()
            return False
        except psycopg2.Error as e:
            print(f"Database error during save: {e}")
            conn.rollback()
            return False
        finally:
            if conn:
                conn.close()

    def delete(self):
        conn = connect_db()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            sql = "DELETE FROM Menu_Items WHERE item_name = %s;"
            cursor.execute(sql, (self.name,))
            deleted_rows = cursor.rowcount
            conn.commit()

            return deleted_rows > 0

        except psycopg2.Error as e:
            print(f"Database error during delete: {e}")
            conn.rollback()
            return False
        finally:
            if conn:
                conn.close()

    def update(self, new_name=None, new_price=None):
        conn = connect_db()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            updates = []
            params = []

        
            if new_name is not None and new_name.strip():
                updates.append("item_name = %s")
                params.append(new_name.strip())

            
            if new_price is not None:
                try:
                    price_int = int(new_price)
                    updates.append("item_price = %s")
                    params.append(price_int)
                except ValueError:
                    print("Update aborted: New price must be an integer.")
                    return False

            if not updates:
                print("No valid fields provided for update.")
                return False


            params.append(self.name)

        
            sql = f"UPDATE Menu_Items SET {', '.join(updates)} WHERE item_name = %s;"

            cursor.execute(sql, tuple(params))
            updated_rows = cursor.rowcount
            conn.commit()

            if updated_rows > 0:
                if new_name is not None and new_name.strip():
                    self.name = new_name.strip()
                if new_price is not None:
                    self.price = int(new_price)
                return True
            else:
                return False

        except psycopg2.IntegrityError:
            print(f"Error updating item: New name '{new_name}' might already exist.")
            conn.rollback()
            return False
        except psycopg2.Error as e:
            print(f"Database error during update: {e}")
            conn.rollback()
            return False
        finally:
            if conn:
                conn.close()
import sqlite3
from constants import DB_PATH

sql_create_table_users = """
    CREATE TABLE IF NOT EXISTS users 
(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone_number TEXT NOT NULL,
        password TEXT NOT NULL
);
"""

def db_init():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_create_table_users)
    except Exception as ex:
        print(f"An error occurred while initializing the database: {ex}")
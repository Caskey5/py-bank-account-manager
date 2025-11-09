from typing import List
from constants import DB_PATH
import sqlite3

from models.user import User


sql_create_user_table = """
    INSERT INTO users (first_name, last_name, email, phone_number, password)
    VALUES (?, ?, ?, ?, ?)
"""

class SignUpRepository:
    def __init__(self, user: User):
        self.user = user

    def _add_user_to_db(self, user: User) -> int:
        if isinstance(user, User):
            params = (user.first_name, user.last_name, user.email, user.phone_number, user.password)
        else:
            return None
        
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(sql_create_user_table, params)
                return cursor.lastrowid
        except Exception as ex:
            print(f'Dogodila se greska {ex}! ')
            return None
                   
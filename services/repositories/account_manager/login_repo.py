
import sqlite3

from constants import DB_PATH


sql_authenticate_user = """
    SELECT * FROM users WHERE email = ? AND password = ?

"""

class Login:
    def __init__(
            self,
            email, 
            password
):
            self.email = email
            self.password = password       

class LoginRepository:
    def __init__(self, user: Login):
        self.user = user

    def authenticate_user(self, login: Login):
        params = (login.email, login.password)
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute(sql_authenticate_user, params)
                user_data = cursor.fetchone()
                if user_data:
                    # Vracamo user_id (prvi element iz rezultata)
                    return user_data[0]  # id je na poziciji 0
                return None

        except Exception as ex:
            print(f'An error occurred during authentication: {ex}')
            return None
        
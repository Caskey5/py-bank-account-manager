


import sqlite3

from constants import DB_PATH


def account_balance(user_id):
    """Prikazuje trenutni balance korisnika"""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
            result = cursor.fetchone()
            if result:
                balance = result[0]
                print(f"\nYour current balance is: €{balance:.2f}")
            else:
                print("\nUser not found!")
    except Exception as ex:
        print(f"An error occurred while fetching balance: {ex}")

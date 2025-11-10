


import sqlite3

from constants import DB_PATH


def deposit(user_id):
    """Dodaje novac na racun korisnika"""
    try:
        amount = float(input("Enter the amount to deposit: €"))
        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            # Trenutni balance
            cursor.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
            result = cursor.fetchone()
            if result:
                current_balance = result[0]
                new_balance = current_balance + amount
                # Azuriraj balance
                cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (new_balance, user_id))
                conn.commit()
                print(f"\nDeposit successful! Your new balance is: €{new_balance:.2f}")
            else:
                print("\nUser not found!")
    except ValueError:
        print("Invalid amount! Please enter a valid number.")
    except Exception as ex:
        print(f"An error occurred during deposit: {ex}")
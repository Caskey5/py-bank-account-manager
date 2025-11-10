


from dbm import sqlite3

from constants import DB_PATH


def withdraw(user_id):
    """Povlaci novac sa racuna korisnika"""
    try:
        amount = float(input("Enter the amount to withdraw: €"))
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
                if current_balance < amount:
                    print(f"\nInsufficient funds! Your current balance is: €{current_balance:.2f}")
                    return

                new_balance = current_balance - amount
                # Azuriraj balance
                cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (new_balance, user_id))
                conn.commit()
                print(f"\nWithdrawal successful! Your new balance is: €{new_balance:.2f}")
            else:
                print("\nUser not found!")
    except ValueError:
        print("Invalid amount! Please enter a valid number.")
    except Exception as ex:
        print(f"An error occurred during withdrawal: {ex}")

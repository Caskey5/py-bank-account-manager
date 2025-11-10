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


def bank_menu(user_id):
    print("Welcome to the Bank Menu!")
    while True:
        print("\nOptions:")
        print("1. View Account Balance")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            print("Viewing account balance...")
            account_balance(user_id)
        elif choice == '2':
            print("Depositing funds...")
            deposit(user_id)
        elif choice == '3':
            print("Withdrawing funds...")
            withdraw(user_id)
        elif choice == '4':
            print("Exiting Bank Menu.")
            break
        else:
            print("Invalid option. Please try again.")
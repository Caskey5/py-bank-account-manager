from services.repositories.bank_manager.balance_repo import account_balance
from services.repositories.bank_manager.deposit_repo import deposit
from services.repositories.bank_manager.withdraw_repo import withdraw


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
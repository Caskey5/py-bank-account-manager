


def account_balance():
    pass

def deposit():
    pass

def withdraw():
    pass


def bank_menu():
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
            account_balance()
        elif choice == '2':
            print("Depositing funds...")
            deposit()
        elif choice == '3':
            print("Withdrawing funds...")
            withdraw()
        elif choice == '4':
            print("Exiting Bank Menu.")
            break
        else:
            print("Invalid option. Please try again.")
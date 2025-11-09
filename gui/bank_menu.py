


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
            # Here you would call the view balance functionality
        elif choice == '2':
            print("Depositing funds...")
            # Here you would call the deposit functionality
        elif choice == '3':
            print("Withdrawing funds...")
            # Here you would call the withdraw functionality
        elif choice == '4':
            print("Exiting Bank Menu.")
            break
        else:
            print("Invalid option. Please try again.")

from gui.bank_menu import bank_menu
from models.user import User
from services.repositories.login_repo import LoginRepository
from services.repositories.signup_repo import SignUpRepository


def create_user():
    # Kreiraj korisnika
    first_name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    phone_number = input("Enter your phone number: ")
    password = input("Enter your password: ")
    new_user = User(first_name, last_name, email, phone_number, password)
    # Dodaj korisnika u bazu podataka
    new_user_to_db = SignUpRepository(new_user)
    new_user_to_db._add_user_to_db(new_user)

def user_exists():
    # Proveri da li korisnik postoji
    email = input("Enter email: ")
    password = input("Enter password: ")

    login_user = User("", "", email, "", password)
    login_user_repo = LoginRepository(login_user)
    if login_user_repo.authenticate_user(login_user):
        print("Seccuess!")
        bank_menu()
    else:
        print("Something went wrong!")    

    
def account_manager_menu():
    print("Account Manager Menu")
    
    while True:
        print("\nOptions:")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            print("Creating a new account...")
            create_user()
        elif choice == '2':
            print("Logging in...")
            user_exists()
        elif choice == '3':
            print("Exiting Account Manager Menu.")
            break
        else:
            print("Invalid option. Please try again.")
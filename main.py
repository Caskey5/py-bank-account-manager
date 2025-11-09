from services.repositories.db_init import db_init
from services.repositories.signup_repo import SignUpRepository, User
from gui.account_manager_menu import account_manager_menu




def main():
    account_manager_menu()
    
if __name__ == "__main__":
    db_init()
    main()

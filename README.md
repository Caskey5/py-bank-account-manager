A Python application for creating, updating, deleting users and accounts, as well as viewing account balances.
A simple Python application for managing bank users and accounts, featuring user registration, login, and account management through a graphical interface.
Managing users and accounts.


## Project structure

Paths are relative to repository root.

```
├── .gitattributes
├── .gitignore
├── constants.py
├── main.py
├── README.md
├── data_store/
│   └── users.db
├── gui/
│   ├── account_manager_menu.py
│   ├── bank_menu.py
│   ├── account_manager_menu.cpython-314.pyc
│   └── bank_menu.cpython-314.pyc
├── models/
│   ├── user.py
│   ├── __init__.py
│   ├── user.cpython-314.pyc
│   └── __init__.cpython-314.pyc
└── services/
   ├── __init__.py
   ├── .gitignore
   └── repositories/
      ├── db_init.py
      ├── account_manager/
      │   ├── login_repo.py
      │   └── signup_repo.py
      └── bank_manager/
         ├── balance_repo.py
         ├── deposit_repo.py
         └── withdraw_repo.py
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Caskey5/py-bank-account-manager.git
   ```
2. Navigate to the project directory and create a virtual environment:
   ```bash
   cd py-bank-account-manager
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main application:

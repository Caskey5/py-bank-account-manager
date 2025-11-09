A Python application for creating, updating, deleting users and accounts, as well as viewing account balances.
A simple Python application for managing bank users and accounts, featuring user registration, login, and account management through a graphical interface.
Managing users and accounts.


* Simple Bank Managing app:

```
.
├── .gitattributes           # Git configuration for attributes
├── .gitignore               # Specifies files/folders to ignore in git
├── constants.py             # Stores application-wide constants
├── main.py                  # Main entry point for the application
├── README.md               # Project documentation
│
├── data_store              # Contains database and persistent storage
│   └── users.db           # SQLite database for user/account data
│
├── gui                     # Graphical user interface components
│   ├── account_manager_menu.py  # Account management GUI
│   └── bank_menu.py            # Main bank menu GUI
│
├── models                  # Data models for users and accounts
│   ├── user.py            # User model definition
│   └── __init__.py
│
└── services               # Business logic and service layer
    ├── __init__.py
    └── repositories      # Database access and repository classes
        ├── db_init.py    # Database initialization scripts
        ├── login_repo.py  # Handles login-related DB operations
        ├── signup_repo.py # Handles signup-related DB operations
        └── __init__.py
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/py-bank-account-manager.git
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

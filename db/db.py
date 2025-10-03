import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# Connect to databases
ConnectUsersDB = sqlite3.connect(os.path.join(DATA_DIR, "users.db"))
ConnectBooksDB = sqlite3.connect(os.path.join(DATA_DIR, "books.db"))
ConnectAccountsDB = sqlite3.connect(os.path.join(DATA_DIR, "accounts.db"))

UsersDB = ConnectUsersDB.cursor()
BooksDB = ConnectBooksDB.cursor()
AccountsDB = ConnectAccountsDB.cursor()

# Create books table
BooksDB.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        genre TEXT,
        isbn TEXT,
        isTaken BOOLEAN
    )
""")

# Create users table
UsersDB.execute("""
    CREATE TABLE IF NOT EXISTS users(
        uid INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        age INTEGER,
        address TEXT
    )
""")

# Create staffs table
AccountsDB.execute("""
    CREATE TABLE IF NOT EXISTS accounts(\
        uid INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        role TEXT
    )
""")

# Commit changes
ConnectUsersDB.commit()
ConnectBooksDB.commit()
ConnectAccountsDB.commit()

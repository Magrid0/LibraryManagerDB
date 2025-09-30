import sqlite3
from pyfiglet import Figlet

ConnectUsersDB = sqlite3.connect("users.db")
ConnectBooksDB = sqlite3.connect("books.db")

UsersDB = ConnectUsersDB.cursor()
BooksDB = ConnectBooksDB.cursor()

# Create books table.
BooksDB.execute("""
	CREATE TABLE IF NOT EXISTS books(
		id INTEGER PRIMARY KEY,
		title TEXT,
		author TEXT,
		isbn TEXT,
		isTaken BOOLEAN
	)
""")

# Create users table.
UsersDB.execute("""
	CREATE TABLE IF NOT EXISTS users(
		uid INTEGER PRIMARY KEY,
		name TEXT,
		surname TEXT,
		age INTEGER,
		address TEXT
	)
""")

# Starting text
def figPrint(text):
	f = Figlet(font='slant')
	print(f.renderText(text))

def clearScreen():
	print("\033c")

# Add new user.
def addUser():
	uid = 0
	name = input("Insert new user's name: ")
	surname = input("Insert new user's surname: ")
	age = input("Insert new user's age: ")
	address = input("Insert new user's address: ")
	
	UsersDB.execute("INSERT INTO users (name, surname, age, address) VALUES (?, ?, ?, ?)", (name, surname, age, address))
	ConnectUsersDB.commit()
	
# Add new book.
def addBook():
	id = 0	
	title = input("Insert new book's title: ")
	author = input("Insert new book's author: ")
	isbn = input("Insert new book's isbn: ")
	isTaken = False

	BooksDB.execute("INSERT INTO books (title, author, isbn, isTaken) VALUES (?, ?, ?, ?)", (title, author, isbn, isTaken) )
	ConnectBooksDB.commit()

# Display all users.
def displayUsers():
	conn = sqlite3.connect("users.db")
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM users")
	rows = cursor.fetchall()
	if rows:
		for row in rows:
			print(row)
		input("Press ENTER to continue...")
	else:
		print("No users found.")
	conn.close()

# Display all books.
def displayBooks():
	conn = sqlite3.connect("books.db")
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM books")
	rows = cursor.fetchall()
	if rows:
		for row in rows:
			print(row)
		input("Press ENTER to continue...")
	else:
		print("No books found.")
	conn.close()

# Delete user.
def delUser():
	# UsersDB.execute("""
	# 	DELETE FROM users
	#	
	# """)
	pass

# Delete book.
def delBook():
	# BooksDB.execute("""
	# 	DELETE FROM books
	#
	# """)
	pass

# Selection Menu.
def menu():
	while True:
		clearScreen()
		figPrint('Library Manager')
		print("1. Books menu\n2. Users menu\n0. Exit")
		choice = int(input("Select: "))
	
		match choice:
			case 1: booksMenu()
			case 2: usersMenu()
			case 0: exit(0)
			case _: print("Invalid selection.")

# Books Menu.
def booksMenu():
	while True:
		clearScreen()
		figPrint('Books Menu')
		print("1. Add book\n2. Remove book\n3. List all books\n0. Back")
		choice = int(input("Select: "))

		match choice:
			case 1: addBook()
			case 2: delBook()
			case 3: displayBooks()
			case 0: menu()
			case _: print("Invalid selection.")

# Users Menu.
def usersMenu():
	while True:
		clearScreen()
		figPrint('Users Menu')
		print("1. Add user\n2. Remove user\n3. List all users\n0. Back")
		choice = int(input("Select: "))

		match choice:
			case 1: addUser()
			case 2: delUser()
			case 3: displayUsers()
			case 0: menu()
			case _: print("Invalid selection.")

clearScreen() # Clear the terminal.
menu()		  # Display the menu.

# Close db.
ConnectUsersDB.close()
ConnectBooksDB.close()

from scripts.utils import clearScreen, figPrint
from scripts.books import addBook, displayBooks, delBook, searchBook
from scripts.users import addUser, displayUsers, delUser, searchUser
from db.db import ConnectUsersDB, ConnectBooksDB

def menu():
    while True:
        clearScreen()
        figPrint('Library Manager')
        print("1. Books menu\n2. Users menu\n0. Exit")
        choice = int(input("Select: "))
    
        match choice:
            case 1: booksMenu()
            case 2: usersMenu()
            case 0: exitProgram()
            case _: print("Invalid selection.")

def booksMenu():
	while True:
		clearScreen()
		figPrint('Books Menu')
		print("1. Add book\n2. Remove book\n3. List all books\n4. Search for a book\n0. Back")
		choice = int(input("Select: "))

		match choice:
			case 1: addBook()
			case 2: delBook()
			case 3: displayBooks()
			case 4: searchBook()
			case 0: return
			case _: print("Invalid selection.")

def usersMenu():
    while True:
        clearScreen()
        figPrint('Users Menu')
        print("1. Add user\n2. Remove user\n3. List all users\n4. Search user\n0. Back")
        choice = int(input("Select: "))

        match choice:
            case 1: addUser()
            case 2: delUser()
            case 3: displayUsers()
            case 4: searchUser()
            case 0: return
            case _: print("Invalid selection.")

def exitProgram():
    ConnectUsersDB.close()
    ConnectBooksDB.close()
    exit(0)

if __name__ == "__main__":
    clearScreen()
    menu()


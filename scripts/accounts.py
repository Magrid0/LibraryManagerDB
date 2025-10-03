from db.db import ConnectAccountsDB, AccountsDB
from scripts.utils import figPrint, clearScreen

def searchAccount(username):
	AccountsDB.execute(
		"SELECT username FROM accounts WHERE username LIKE ?", (username,)
	)
	rows = AccountsDB.fetchall()
	
	if rows:
		return 200
	else:
		return 404


def login():
	while True:
		clearScreen()
		figPrint('Login')
		username = input("Username: ")
		result = int(searchAccount(username))
		if result == 200:
			passwd = input("Password: ")
		elif result == 404:
			print("User not found.")
			input("Press ENTER to continue...")
		else:
			input("An error has occurred.\nPress ENTER to continue")
			print("Login Done.")
			input("press Enter")

def register():
    while True:
		clearScreen()
		figPrint('Register')
		username = input("Username: ")
		passwd = input("Password: ")

def guest():
	pass

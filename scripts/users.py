from db.db import ConnectUsersDB, UsersDB

def addUser():
    name = input("Insert new user's name: ")
    surname = input("Insert new user's surname: ")
    age = input("Insert new user's age: ")
    address = input("Insert new user's address: ")
    
    UsersDB.execute(
        "INSERT INTO users (name, surname, age, address) VALUES (?, ?, ?, ?)",
        (name, surname, age, address)
    )
    ConnectUsersDB.commit()

def displayUsers():
    UsersDB.execute("SELECT * FROM users")
    rows = UsersDB.fetchall()
    if rows:
        for row in rows:
            print(row)
        input("Press ENTER to continue...")
    else:
        print("No users found.")

def delUser():
	search_query = input("What user to delete?: ")

	# Search by partial match
	UsersDB.execute("""SELECT * FROM users WHERE name LIKE ? OR surname LIKE ?""" , ('%' + search_query + '%','%' + search_query + '%',))
	rows = UsersDB.fetchall()

	if not rows:
		print("No user found.")
		input("Press ENTER to continue...")
		return
	
	# Show results
	print(f"\nFound {len(rows)} matching users:")
	for row in rows:
		print(f"[{row[0]}] {row[1]} {row[2]}, {row[3]}yo, living @ {row[4]}")
		
	# Ask which one to delete
	try:
		user_id = int(input("\nEnter the ID of the user to delete: "))
	except ValueError:
		print("Invalid input.")
		input("Press ENTER to continue...")
		return

	# Delete by ID
	UsersDB.execute("DELETE FROM users WHERE uid = ?", (user_id,))
	ConnectUsersDB.commit()

	print("User deleted successfully.")
	input("Press ENTER to continue...")

def searchUser():
    search_query = input("What user are you searching for?: ")
	
    # Search the db	
    UsersDB.execute("SELECT uid, name, surname, age, address FROM users WHERE name LIKE ? OR surname LIKE ? OR age LIKE ? OR address LIKE ?", ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%','%' + search_query + '%',))
    rows = UsersDB.fetchall()

    if not rows:
        print("No user found.")
        input("Press ENTER to continue...")
        return

    # Show results
    print(f"\nFound {len(rows)} matching users:")
    for row in rows:
        print(f"[{row[0]}] {row[1]} {row[2]}, {row[3]}yo, living @ {row[4]}")
	
    input("Press ENTER to continue...")

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
    pass


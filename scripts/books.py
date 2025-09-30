from db.db import ConnectBooksDB, BooksDB

def addBook():
    title = input("Insert new book's title: ")
    author = input("Insert new book's author: ")
    isbn = input("Insert new book's isbn: ")
    isTaken = False

    BooksDB.execute(
        "INSERT INTO books (title, author, isbn, isTaken) VALUES (?, ?, ?, ?)",
        (title, author, isbn, isTaken)
    )
    ConnectBooksDB.commit()

def displayBooks():
    BooksDB.execute("SELECT * FROM books")
    rows = BooksDB.fetchall()
    if rows:
        for row in rows:
            print(row)
        input("Press ENTER to continue...")
    else:
        print("No books found.")

def delBook():
    # later: add search logic here
    pass


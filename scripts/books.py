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
    search_query = input("What book to delete?: ")

    # Search by partial title
    BooksDB.execute("SELECT id, title, author FROM books WHERE title LIKE ?", ('%' + search_query + '%',))
    rows = BooksDB.fetchall()

    if not rows:
        print("No books found.")
        input("Press ENTER to continue...")
        return

    # Show results
    print("\nMatching books:")
    for row in rows:
        print(f"[{row[0]}] {row[1]} by {row[2]}")

    # Ask which one to delete
    try:
        book_id = int(input("\nEnter the ID of the book to delete: "))
    except ValueError:
        print("Invalid input.")
        input("Press ENTER to continue...")
        return

    # Delete by ID
    BooksDB.execute("DELETE FROM books WHERE id = ?", (book_id,))
    ConnectBooksDB.commit()

    print("Book deleted successfully.")
    input("Press ENTER to continue...")


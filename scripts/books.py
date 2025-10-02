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
        input("Press ENTER to continue...")

def delBook():
    search_query = input("What book to delete?: ")

    # Search by partial title
    BooksDB.execute("SELECT id, title, author, isbn FROM books WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ?", ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%',))
    rows = BooksDB.fetchall()

    if not rows:
        print("No books found.")
        input("Press ENTER to continue...")
        return

    # Show results
    print(f"\nFound {len(rows)} matching books:")
    for row in rows:
        print(f"[{row[0]}] {row[1]} by {row[2]} (ISBN: {row[3]})")

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

def searchBook():
    search_query = input("What book/author are you searching for?: ")
	
    # Search the db	
    BooksDB.execute("SELECT id, title, author, isbn FROM books WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ?", ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%',))
    rows = BooksDB.fetchall()

    if not rows:
        print("No books found.")
        input("Press ENTER to continue...")
        return

    # Show results
    print(f"\nFound {len(rows)} matching books:")
    for row in rows:
        print(f"[{row[0]}] {row[1]} by {row[2]} (ISBN: {row[3]})")
	
    input("Press ENTER to continue...")

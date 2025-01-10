class Book:
    def __init__(self, title, author, ISBN, price):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.price = price

    def display_book(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.ISBN}")
        print(f"Price: {self.price}")

book1 = Book("Python Programming", "John Doe", "123456789", 19.99)
book2 = Book("Data Science for Beginners", "Jane Smith", "987654321", 29.99)

book1.display_book()
book2.display_book()

import sqlite3
conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()

# Create a table to store book information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        title TEXT,
        author TEXT,
        ISBN TEXT,
        price REAL
    )
''')

# Insert some books into the database
cursor.execute('''
    INSERT INTO books (title, author, ISBN, price) VALUES
    ('Python Programming', 'John Doe', '123456789', 19.99),
    ('Data Science for Beginners', 'Jane Smith', '987654321', 29.99)
''')

conn.commit()
conn.close()

conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()

# Retrieve all books from the database
cursor.execute("SELECT * FROM books")
books = cursor.fetchall()

# Display all books
for book in books:
    print(f"Title: {book[0]}, Author: {book[1]}, ISBN: {book[2]}, Price: {book[3]}")

# Close the connection
conn.close()

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    ISBN = input("Enter ISBN number: ")
    price = float(input("Enter book price: ")

    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()

    # Insert the new book into the database
    cursor.execute('''
        INSERT INTO books (title, author, ISBN, price) VALUES
        (?, ?, ?, ?)
    ''', (title, author, ISBN, price))

    # Commit and close
    conn.commit()
    conn.close()

# Call the function to add a book
add_book()








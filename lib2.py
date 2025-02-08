import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText

# Dictionary to store books instead of a database
library_books = []

# Function to borrow a book
def borrow_book(title, book_type, borrower, email):
    borrow_date = datetime.now().strftime("%Y-%m-%d")
    return_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

    book_entry = {
        "title": title,
        "book_type": book_type,
        "borrower": borrower,
        "borrow_date": borrow_date,
        "return_date": return_date,
        "email": email
    }
    
    library_books.append(book_entry)
    print(f"Book '{title}' borrowed by {borrower}. Due on {return_date}.")

# Function to return a book
def return_book(title, borrower):
    global library_books
    library_books = [book for book in library_books if not (book["title"] == title and book["borrower"] == borrower)]
    print(f"Book '{title}' returned by {borrower}.")

# Function to check overdue books and send reminders
def send_reminders():
    today = datetime.now().strftime("%Y-%m-%d")
    
    for book in library_books:
        if book["return_date"] < today:
            print(f"Reminder: {book['borrower']} has overdue book '{book['title']}' due on {book['return_date']}.")
            send_email(book["email"], book["title"], book["borrower"], book["return_date"])

# Function to simulate sending email
def send_email(to_email, book_title, borrower, return_date):
    print(f"Sending email to {to_email}...")
    print(f"Subject: Library Book Return Reminder")
    print(f"Dear {borrower},\n\nThe book '{book_title}' was due on {return_date}. Please return it as soon as possible.\n\nBest regards,\nLibrary Management\n")

# Testing the functions
borrow_book("The Great Gatsby", "Fiction", "Alice", "alice@example.com")
borrow_book("1984", "Dystopian", "Bob", "bob@example.com")

print("\nCurrent Library Records:", library_books)

return_book("The Great Gatsby", "Alice")

print("\nUpdated Library Records:", library_books)

# Simulate overdue reminder (manually setting an overdue date)
library_books[0]["return_date"] = "2024-02-01"  # Set past date
send_reminders()

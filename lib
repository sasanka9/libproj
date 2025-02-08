import sqlite3
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText

# Database setup
def init_db():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY,
                        title TEXT,
                        book_type TEXT,
                        borrower TEXT,
                        borrow_date TEXT,
                        return_date TEXT,
                        email TEXT
                    )''')
    conn.commit()
    conn.close()

# Function to add a book entry
def borrow_book(title, book_type, borrower, email):
    borrow_date = datetime.now().strftime("%Y-%m-%d")
    return_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, book_type, borrower, borrow_date, return_date, email) VALUES (?, ?, ?, ?, ?, ?)",
                   (title, book_type, borrower, borrow_date, return_date, email))
    conn.commit()
    conn.close()
    print(f"Book '{title}' borrowed by {borrower}. Due on {return_date}.")

# Function to return a book
def return_book(title, borrower):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE title=? AND borrower=?", (title, borrower))
    conn.commit()
    conn.close()
    print(f"Book '{title}' returned by {borrower}.")

# Function to check overdue books and send reminders
def send_reminders():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, borrower, return_date, email FROM books")
    books = cursor.fetchall()
    conn.close()
    
    today = datetime.now().strftime("%Y-%m-%d")
    for book in books:
        title, borrower, return_date, email = book
        if return_date < today:
            send_email(email, title, borrower, return_date)

# Function to send email
def send_email(to_email, book_title, borrower, return_date):
    from_email = "your_email@example.com"
    password = "your_email_password"
    subject = "Library Book Return Reminder"
    body = (f"Dear {borrower},\n\n"
            f"The book '{book_title}' borrowed from the library was due on {return_date}.\n"
            f"Please return it as soon as possible to avoid any penalties.\n\n"
            f"Best regards,\nLibrary Management")
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    
    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print(f"Reminder email sent to {borrower} ({to_email}) for book '{book_title}'.")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

if __name__ == "__main__":
    init_db()
    # Example Usage
    # borrow_book("The Great Gatsby", "Fiction", "Alice", "alice@example.com")
    # return_book("The Great Gatsby", "Alice")
    # send_reminders()

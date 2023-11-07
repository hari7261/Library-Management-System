import os
import datetime

# Function to get student information
def get_student_info():
    student_name = input("Enter student name: ")
    roll_no = input("Enter student roll number: ")
    return f"{student_name},{roll_no}"

# Function to get book information
def get_book_info():
    book_name = input("Enter book name: ")
    book_id = input("Enter book ID: ")
    return f"{book_name},{book_id}"

# Function to add a book
def add_book():
    book_info = get_book_info()
    with open("books.txt", "a") as file:
        file.write(book_info + "\n")
    print("Book added successfully!")

# Function to update a book
def update_book():
    book_id = input("Enter book ID to update: ")
    new_book_info = get_book_info()
    updated_data = []
    found = False

    with open("books.txt", "r") as file:
        for line in file:
            book_data = line.strip().split(',')
            if book_data[1] == book_id:
                updated_data.append(new_book_info)
                found = True
            else:
                updated_data.append(line)

    if found:
        with open("books.txt", "w") as file:
            for line in updated_data:
                file.write(line)
        print("Book updated successfully!")
    else:
        print("Book not found.")

# Function to delete a book
def delete_book():
    book_id = input("Enter book ID to delete: ")
    books_to_keep = []
    found = False

    with open("books.txt", "r") as file:
        for line in file:
            book_data = line.strip().split(',')
            if book_data[1] == book_id:
                found = True
            else:
                books_to_keep.append(line)

    if found:
        with open("books.txt", "w") as file:
            for line in books_to_keep:
                file.write(line)
        print("Book deleted successfully!")
    else:
        print("Book not found.")

# Function to display all books
def display_books():
    with open("books.txt", "r") as file:
        print("List of Books:")
        for line in file:
            book_data = line.strip().split(',')
            print(f"Book Name: {book_data[0]}, Book ID: {book_data[1]}")

# Function to save student data to a file
def save_student_data(student_data):
    with open("students.txt", "w") as file:
        for student in student_data:
            file.write(student + "\n")

# Function to load student data from a file
def load_student_data():
    student_data = []
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as file:
            for line in file:
                student_data.append(line.strip())
    return student_data

# Function to borrow a book
def borrow_book(student_data):
    student_roll = input("Enter student roll number: ")
    book_id = input("Enter book ID to borrow: ")
    return_date = (datetime.date.today() + datetime.timedelta(days=10)).strftime("%Y-%m-%d")
    borrowed_info = f"{student_roll},{book_id},{return_date}"
    with open("borrows.txt", "a") as file:
        file.write(borrowed_info + "\n")
    print("Book borrowed successfully!")

# Function to receive a book
def receive_book():
    book_id = input("Enter book ID to receive: ")
    student_roll = input("Enter student roll number: ")
    borrows = []
    found = False

    with open("borrows.txt", "r") as file:
        for line in file:
            borrow_data = line.strip().split(',')
            if borrow_data[0] == student_roll and borrow_data[1] == book_id:
                found = True
            else:
                borrows.append(line)

    if found:
        with open("borrows.txt", "w") as file:
            for line in borrows:
                file.write(line)
        print("Book received successfully!")
    else:
        print("Book not found in the borrowed list.")

# Function to display all borrowed books
def display_borrowed_books():
    with open("borrows.txt", "r") as file:
        print("List of Borrowed Books:")
        for line in file:
            borrow_data = line.strip().split(',')
            return_date = datetime.datetime.strptime(borrow_data[2], "%Y-%m-%d").date()
            today = datetime.date.today()
            if today > return_date:
                late_days = (today - return_date).days
                print(f"Book ID: {borrow_data[1]} (Late by {late_days} days)")
            else:
                print(f"Book ID: {borrow_data[1]} (Due on {return_date})")

# Main menu
while True:
    print("\nLibrary Management System Menu:")
    print("1. Add a Book")
    print("2. Update a Book")
    print("3. Delete a Book")
    print("4. Display All Books")
    print("5. Borrow a Book")
    print("6. Receive a Book")
    print("7. Display Borrowed Books")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        display_books()
    elif choice == "5":
        student_data = load_student_data()
        borrow_book(student_data)
    elif choice == "6":
        receive_book()
    elif choice == "7":
        display_borrowed_books()
    elif choice == "8":
        break
    else:
        print("Invalid choice. Please try again.")

print("Thank you for using the Library Management System!")

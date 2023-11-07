# Library-Management-System

This Python program is a simple Library Management System (LMS) that allows users to manage and keep track of books, students, and book borrowings. It provides various functionalities such as adding books, updating book information, deleting books, displaying all books, borrowing books, receiving books, and displaying borrowed books. Below, we'll provide a detailed step-by-step description of the program and guide you on how to upload it to GitHub.

## Program Structure:

The program consists of the following key components:

1. Importing Required Modules:
   - The program starts by importing two modules: `os` for file and directory operations and `datetime` for working with dates and times.

2. Functions:
   - The program defines several functions that handle different aspects of library management:

   - `get_student_info()`: This function prompts the user to enter a student's name and roll number and returns this information as a string.

   - `get_book_info()`: This function prompts the user to enter a book's name and ID and returns this information as a string.

   - `add_book()`: This function allows the user to add a book's information to a file named "books.txt."

   - `update_book()`: This function allows the user to update the information of a specific book by specifying its ID.

   - `delete_book()`: This function allows the user to delete a book by specifying its ID.

   - `display_books()`: This function displays a list of all books stored in the "books.txt" file.

   - `save_student_data(student_data)`: This function saves student data to a file named "students.txt."

   - `load_student_data()`: This function loads student data from the "students.txt" file.

   - `borrow_book(student_data)`: This function allows a student to borrow a book and records the borrowing details in a file named "borrows.txt."

   - `receive_book()`: This function allows a student to return a borrowed book.

   - `display_borrowed_books()`: This function displays a list of all borrowed books and indicates if they are overdue.

3. Main Menu:
   - The program's main functionality is accessible through a menu system. The menu options include adding, updating, deleting, and displaying books, as well as borrowing, returning, and displaying borrowed books. The program runs in a loop, continuously displaying the menu and waiting for user input.

4. User Interaction:
   - The user interacts with the program by entering a numeric choice corresponding to the desired action in the menu.

5. Exit:
   - The program provides an option to exit the menu loop and gracefully terminates when the user chooses to do so.

## Suggested Program Name:
A better name for this program could be "LibrarySys" or "Librarian." These names better reflect the program's functionality and purpose.

## Uploading to GitHub:

To upload this program to GitHub, you can follow these steps:

1. **Create a GitHub Account:**
   If you don't already have one, create a GitHub account at https://github.com/.

2. **Create a New Repository:**
   - Click on the "New" button in the upper right corner of your GitHub dashboard.
   - Choose a name for your repository.
   - You can add a description to explain the purpose of your repository, similar to the program description provided above.

3. **Initialize a Git Repository Locally:**
   - If you haven't already, install Git on your local machine.
   - Open a terminal or command prompt and navigate to the directory where your program is stored.

   ```shell
   cd /path/to/your/program
   ```

   - Initialize a Git repository in this directory.

   ```shell
   git init
   ```

4. **Link Your Local Repository to GitHub:**
   - On your GitHub repository page, you'll see the option to set up a remote repository URL. Copy the URL.

5. **Add and Commit Your Code:**
   - Use the following Git commands to add and commit your code.

   ```shell
   git add .
   git commit -m "Initial commit"
   ```

6. **Set the Remote Origin:**
   - Use the remote URL you copied in step 4 to set the remote origin.

   ```shell
   git remote add origin < https://hari7261.github.io/Library-Management-System/>
   ```

7. **Push Your Code to GitHub:**
   - Push your code to GitHub to upload it.

   ```shell
   git push -u origin master
   ```

8. **GitHub Repository:**
   - Your code is now uploaded to your GitHub repository.

Your program is now hosted on GitHub, and others can access and contribute to it. You can also make updates and improvements to your code by pushing changes to your GitHub repository.

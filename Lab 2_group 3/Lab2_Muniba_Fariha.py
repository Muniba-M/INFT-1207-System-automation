
import csv

# Function to add a book to the reading list
def add_book(title, author, year):
    if not title.strip():
        print("Error: Book title can not be empty. ")
        return
    if not author.strip():
        print("Error: Book author can not be empty. ")
        return

    with open('books.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, year])
        return "Book added successfully!"

# Function to list all books
def list_books():
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}\n')


# Function to search for a book by title
def search_book(title):
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == title.lower():
                print(f'Found: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
                return
        print('Book not found')


# Function to delete a book
def delete_books(title):
    books = []
    deleted = False

    with open('books.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] != title:
                books.append(row)
            else:
                deleted = True
    if deleted:
        with open('books.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(books)
        print(f"Book '{title}' has been deleted.")
    else:
        print(f"Book '{title}' not found.")


# Function to update a book
def update_books(old_title, new_title, new_author, new_year):
    books = []
    updated = False

    with open('books.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == old_title:
                books.append([new_title, new_author, new_year])
                updated = True
            else:
                books.append(row)
    if updated:
        with open('books.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(books)
        print(f"Book '{old_title}' has been updated to '{new_title}'.")
    else:
        print(f"Book '{old_title}' not found.")


# Menu loop
def menu():
    while True:
        print("\n1. Add Book\n2. List Books\n3. Search Book\n4. Delete Book\n5. Update Book\n6. Quit")
        choice = input("Select an option: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")
            add_book(title, author, year)
        elif choice == '2':
            list_books()
        elif choice == '3':
            title = input("Enter book title to search: ")
            search_book(title)
        elif choice == '4':
            title = input("Enter a book title to delete: ")
            delete_books(title)
        elif choice == '5':
            old_title = input("Enter the book title you want to update: ")
            new_title = input("Enter a new book title: ")
            new_author = input("Enter a new book author: ")
            new_year = input("Enter a new book year: ")
            update_books(old_title, new_title, new_author, new_year)
        elif choice == '6':
            user= input("Do you want to exit the program? ")
            if user== "yes":
                break
        else:
            print("Invalid choice. Try again.")


# Run the program
if __name__ == "__main__":
    menu()
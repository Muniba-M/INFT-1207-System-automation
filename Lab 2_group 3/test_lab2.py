import unittest
import csv
from Lab2_Muniba_Fariha import add_book, search_book, list_books, delete_books, update_books

class TestReadingList(unittest.TestCase):

    def book_exists(self, title):
        """Checks if a book exists in books.csv."""
        with open("books.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            return any(len(row) > 0 and row[0] == title for row in reader)

    # Test adding a book with valid inputs
    def test_add_book_valid(self):
        result = add_book("The Kite Runner", "Khalid Hussaini", "2003")
        print(result)
        self.assertEqual(result, "Book added successfully!")
        self.assertTrue(self.book_exists("The Kite Runner"))

    # Test adding a book with an empty title
    def test_add_book_empty_title(self):
        add_book("", "Charles Perrault", "1697")
        self.assertFalse(self.book_exists(""))

    # Test adding a book with an empty author
    def test_add_book_empty_author(self):
        add_book("Beautiful Ugly", "", "2025")
        self.assertFalse(self.book_exists("Beautiful Ugly"))

    # Test listing books (Manually check console output)
    def test_list_books(self):
        add_book("Fourth Wing", "Rebecca Yarros", "2023")
        add_book("The Big Empty", "Robert Crais", "2023")
        list_books()  # This will print to console; manual validation required

    # Test searching for an existing book
    def test_search_book_existing(self):
        add_book("Dark Matter", "Blake Crouch", "2016")
        search_book("Dark Matter")  # Manually check console for correct output

    # Test searching for a non-existing book
    def test_search_book_not_found(self):
        search_book("Sleeping Bird")  # Manually check console for "Book not found"

    # Test deleting a book that exists
    def test_delete_book_existing(self):
        add_book("Treasure Island", "Robert Louis", "1883")
        delete_books("Treasure Island")
        self.assertFalse(self.book_exists("Treasure Island"))

    # Test deleting a book that does not exist
    def test_delete_book_not_found(self):
        delete_books("White House")  # Manually check console for "Book not found"

    # Test updating a book that exists
    def test_update_book_existing(self):
        add_book("To Kill a Mockingbird", "Harper Lee", "1960")
        update_books("To Kill a Mockingbird", "1984", "George Orwell", "1949")
        self.assertFalse(self.book_exists("To Kill a Mockingbird"))
        self.assertTrue(self.book_exists("1984"))

    # Test updating a book that does not exist
    def test_update_book_not_found(self):
        update_books("Bye Bye Sweetheart", "Brave New World", "Aldous Huxley", "1932")
        self.assertFalse(self.book_exists("Brave New World"))  # Should not have been added


if __name__ == '__main__':
    unittest.main()
import unittest
from main_lib import Book, PrintedBook, EBook, User, Library, Librarian


class TestBook(unittest.TestCase):

    def test_book_basic(self):
        b = Book("Title", "Author", 2000)
        self.assertEqual(b.get_title(), "Title")
        self.assertEqual(b.get_author(), "Author")
        self.assertEqual(b.get_year(), 2000)
        self.assertTrue(b.is_available())

    def test_mark_as_taken_and_returned(self):
        b = Book("T", "A", 2020)
        self.assertTrue(b.mark_as_taken())
        self.assertFalse(b.is_available())
        self.assertTrue(b.mark_as_returned())
        self.assertTrue(b.is_available())


class TestPrintedBook(unittest.TestCase):

    def test_repair(self):
        pb = PrintedBook("T", "A", 2020, 100, "плохая")
        self.assertEqual(pb.repair(), "New condition хорошая")
        self.assertEqual(pb.repair(), "New condition новая")
        self.assertEqual(pb.repair(), "Condition новая the best")

        pb2 = PrintedBook("T2", "B", 1999, 300, "wrong")
        self.assertEqual(pb2.repair(), "not correct condition")


class TestEBook(unittest.TestCase):

    def test_download(self):
        eb = EBook("E", "Author", 2010, 5, "pdf")
        self.assertEqual(eb.download(), "Книга E загружается")


class TestUser(unittest.TestCase):

    def test_borrow_and_return(self):
        user = User("Ivan")
        b = Book("T", "A", 2001)

        self.assertEqual(user.borrow(b), "Add this book")
        self.assertIn(b, user.get_borrowed_books())

        # книга "условно" занята, но метод книги доступность не меняет
        # проверяем только поведение пользователя
        self.assertEqual(user.return_book(b), "Delete successfully")
        self.assertNotIn(b, user.get_borrowed_books())

        self.assertEqual(user.return_book(b), "This book is not on the list")


class TestLibrary(unittest.TestCase):

    def test_add_and_find_book(self):
        lib = Library()
        b = Book("T", "A", 2001)
        lib.add_book(b)

        self.assertEqual(lib.find_book("T"), b)
        self.assertEqual(lib.find_book("NO"), "Нет такой книги")

    def test_add_user_and_lend_return(self):
        lib = Library()
        b = Book("T", "A", 2001)
        u = User("Ivan")

        lib.add_book(b)
        lib.add_user(u)

        self.assertEqual(lib.lend_book("T", "Ivan"), "Successfull")
        self.assertIn(b, u.get_borrowed_books())

        self.assertEqual(lib.return_book("T", "Ivan"), "Successfull")
        self.assertNotIn(b, u.get_borrowed_books())

    def test_show_available(self):
        lib = Library()
        b1 = Book("A", "AA", 1999)
        b2 = Book("B", "BB", 2000)

        lib.add_book(b1)
        lib.add_book(b2)

        b1.mark_as_taken()

        av = lib.show_available_books()
        self.assertNotIn(b1, av)
        self.assertIn(b2, av)


class TestLibrarian(unittest.TestCase):

    def test_librarian_functions(self):
        lib = Library()
        libn = Librarian("Admin")
        b = Book("T", "A", 2001)
        u = User("Ivan")

        self.assertEqual(libn.add_book(lib, b), "Successfull")
        self.assertEqual(libn.register_user(lib, u), "Successfull")
        self.assertEqual(libn.remove_book(lib, "T"), "Successfull")


if __name__ == "__main__":
    unittest.main()

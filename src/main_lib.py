class Book:
    def __init__(self, title: str, author: str, year: int):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__available = True

    def __str__(self):
        return "class book"


    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_year(self):
        return self.__year
    
    def is_available(self):
        return self.__available
    

    def mark_as_taken(self):
        try:
            self.__available = False
        except:
            return False
        finally:
            return True
        
    def mark_as_returned(self):
        try:
            self.__available = True
        except:
            return False
        finally:
            return True



class PrintedBook(Book):
    
    def __init__(self, title, author, year, pages: int, condition: str):
        super().__init__(title, author, year)
        self.pages = pages
        self.condition = condition
        self.__cond = ["плохая", "хорошая", "новая"]

    def repair(self):
        if self.condition in self.__cond:
            if self.condition == self.__cond[-1]:
                return f"Condition {self.condition} the best"
            idx = self.__cond.index(self.condition)
            self.condition = self.__cond[idx + 1]
            return f"New condition {self.condition}"
        return "not correct condition"
        

class EBook(Book):
    def __init__(self, title, author, year, file_size: int, format: str):
        super().__init__(title, author, year)
        self.file_size = file_size
        self.format = format

    
    def download(self):
        return f"Книга {self.get_title()} загружается"
    


class User:

    def __init__(self, name: str):
        self.name = name
        self.__borrowed_books = []

    def borrow(self, book: Book):
        if book.is_available():
            self.__borrowed_books.append(book)
            return "Add this book"
        return "This book is not available"
    
    def return_book(self, book: Book):
        if book in self.__borrowed_books:
            self.__borrowed_books.remove(book)
            return "Delete successfully"
        return "This book is not on the list"
    
    def show_books(self):
        return self.__borrowed_books
    
    def get_borrowed_books(self):
        return self.__borrowed_books.copy()

class Library:
    def __init__(self):
        self.__books = []
        self.__users = []

    def add_book(self, book: Book):
        self.__books.append(book)
        return "Successfull"
    
    def add_user(self, user: User):
        self.__users.append(user)
        return "Successfull"
    
    def remove_book(self, title: str):
        for book in self.__books:
            if title == book.get_title():
                self.__books.remove(book)
                break
        return "Нет такой книги"
    
    def find_book(self, title):
        for book in self.__books:
            if title == book.get_title():
                return book
        return "Нет такой книги"
    
    def show_all_books(self):
        return self.__books
    
    def show_available_books(self):
        av_books = []
        for book in self.__books:
            if book.is_available():
                av_books.append(book)
        return av_books
    
    def lend_book(self, title, user_name):
        userr: User
        bookk: Book
        for user in self.__users:
            if user_name == user.name:
                userr = user
                break
        
        for book in self.__books:
            if title == book.get_title():
                bookk = book
                break

        userr.borrow(bookk)
        return "Successfull"

    def return_book(self, title, user_name):
        userr: User
        bookk: Book
        for user in self.__users:
            if user_name == user.name:
                userr = user
                break
        
        for book in self.__books:
            if title == book.get_title():
                bookk = book
                break

        userr.return_book(bookk)
        return "Successfull"



    


class Librarian(User):
    def __init__(self, name):
        super().__init__(name)
    
    def add_book(self, library: Library, book: Book):
        library.add_book(book)
        return "Successfull"
    
    def remove_book(self, library: Library, title: str):
        library.remove_book(title)
        return "Successfull"
    
    def register_user(self, library: Library, user: User):
        library.add_user(user)
        return "Successfull"
    



# b = Book("dsc","dcdsc",23, True)   
# a = User("DDD")
# print(a.get_borrowed_books())

# print(a.get_borrowed_books())
# dost = Book("Dost", "DDD", 2000,True)

# print(dost.get_title())
# print(dost.is_available())
# print(dost.mark_as_taken())
# print(dost.is_available())

lib = Library()

# --- создаём книги ---
b1 = PrintedBook("Война и мир", "Толстой", 1869, 1225, "хорошая")
b2 = EBook("Мастер и Маргарита", "Булгаков", 1966, 5, "epub")
b3 = PrintedBook("Преступление и наказание", "Достоевский", 1866, 480, "плохая")

# --- создаём пользователей ---
user1 = User("Анна")
librarian = Librarian("Мария")

# --- библиотекарь добавляет книги ---
librarian.add_book(lib, b1)
librarian.add_book(lib, b2)
librarian.add_book(lib, b3)

# --- библиотекарь регистрирует пользователя ---
librarian.register_user(lib, user1)

# --- пользователь берёт книгу ---
lib.lend_book("Война и мир", "Анна")

# --- пользователь смотрит свои книги ---
user1.show_books()

# --- возвращает книгу ---
lib.return_book("Война и мир", "Анна")

# --- электронная книга ---
b2.download()

# --- ремонт книги ---
b3.repair()
print(b3)
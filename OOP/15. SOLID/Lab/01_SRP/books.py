class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.page = 0
        self.location = location

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def get_books_by_author(self, author):
        books = [book for book in self.books if book.author == author]

        if not books:
            return None

        return books


    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            raise Exception('Book not found.')
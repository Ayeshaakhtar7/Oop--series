# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.


class Book:
    total_books = 0

    def __init__(self, title, author):
        self.name = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        
    @classmethod
    def get_total_books(cls):
        return cls.total_books


book1 = Book("Namal", "Nimrah Ahmad")
print(f"\nTitle: {book1.name}\nAuthor: {book1.author}")
print(f"Total books so far: {Book.get_total_books()}")

book2 = Book("The Alchemist", "Paulo Coelho")
print(f"\nTitle: {book2.name}\nAuthor: {book2.author}")
print(f"Total books so far: {Book.get_total_books()}")


from LibraryHashTable import LibraryHashTable
from Book import Book

# Ejemplo de uso
library_system = LibraryHashTable(10)

book1 = Book("1984", "George Orwell", "Ciencia ficción")
library_system.insert_book(book1)
book2 = Book("Fahrenheit 451", "Ray Bradbury", "Ciencia ficción")
library_system.insert_book(book2)
book3 = Book("Orgullo y prejuicio", "Jane Austen", "Clásico")
library_system.insert_book(book3)
book4 = Book("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico")
library_system.insert_book(book4)
book5 = Book("Crónica de una muerte anunciada", "Gabriel García Márquez", "Drama")
library_system.insert_book(book5)

# for avl in library_system.table:
#     for book in avl.in_order():
#         print(book.name)

# library_system.delete_book(book2)
# for avl in library_system.table:
#     for book in avl.in_order():
#         print(book.name)

print(book1.state, book1.num_borrowed_books)
library_system.update_state(book1, "borrowed")
print(book1.state, book1.num_borrowed_books)
library_system.update_state(book2, "borrowed")
library_system.update_state(book3, "borrowed")
library_system.update_state(book4, "borrowed")

# for book in library_system.search_by_category("Ciencia ficción"):
#     print(book.name, book.category)

# for book in library_system.search_by_category("Clásico"):
#     print(book.name, book.category)

# for book in library_system.search_by_category("Realismo mágico"):
#     print(book.name, book.category)

# for book in library_system.search_by_author("Gabriel García Márquez"):
#     print(book.name, book.author)

# most_borrowed_category, borrows = library_system.get_most_borrowed_category()
# print(most_borrowed_category, borrows)

# least_borrowed_categories = library_system.get_least_borrowed_category()
# for category in least_borrowed_categories:
#     print(category[0], category[1])

# library_system.show_books_categories()

# for book in library_system.search_borrowed_books():
#     print(book.name, book.author)

book1.num_borrowed_books = 3
library_system.show_popular_books_by_category()
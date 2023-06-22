from LibraryHashTable import LibraryHashTable
from Book import Book

"""
Inicialización de objetos
"""
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

library_system.update_state(book1, "borrowed")
library_system.update_state(book2, "borrowed")
library_system.update_state(book3, "borrowed")

book1.num_borrowed_books = 5
book2.num_borrowed_books = 3
book3.num_borrowed_books = 2

"""
Mostrar todos los libros
"""
# for avl in library_system.table:
#     for book in avl.in_order():
#         print(book.name)

"""
Eliminar un libro
"""
# library_system.delete_book(book2)
# for avl in library_system.table:
#     for book in avl.in_order():
#         print(book.name)

"""
Mostrar los libros de una categoría en específico
"""
# for book in library_system.search_by_category("Ciencia ficción"):
#     print(f"Book: {book.name} - Category: {book.category} - Author: {book.author}")

# for book in library_system.search_by_category("Clásico"):
#     print(f"Book: {book.name} - Category: {book.category} - Author: {book.author}")

# for book in library_system.search_by_category("Realismo mágico"):
#     print(f"Book: {book.name} - Category: {book.category} - Author: {book.author}")

"""
Mostrar los libros de un autor en específico
"""
# for book in library_system.search_by_author("Gabriel García Márquez"):
#     print(f"Book: {book.name} - Category: {book.category} - Author: {book.author}")

"""
Detectar el libro más prestado
"""
# most_borrowed_book = library_system.get_most_borrowed_book()
# print(f"Book: {most_borrowed_book.name} - Category: {most_borrowed_book.category} - Number of Borrows: {most_borrowed_book.num_borrowed_books}")

"""
Detectar la categoría más prestada
"""
# most_borrowed_category, borrows = library_system.get_most_borrowed_category()
# print(f"Category: {most_borrowed_category} - Number of Borrows: {borrows}")

"""
Detectar las categorías menos prestadas
"""
# least_borrowed_categories = library_system.get_least_borrowed_categories()
# for category in least_borrowed_categories:
#     print(f"Category: {category[0]} - Number of Borrows: {category[1]}")


"""Funciones específicas"""


"""
Mostrar el número de libros de cada categoría
"""
# library_system.show_num_books_categories()

"""
Buscar libros prestados
"""
# for book in library_system.search_borrowed_books():
#     print(f"Book: {book.name} - Category: {book.category} - Author: {book.author} - State: {book.state}")

"""
Buscar libros disponibles
"""
# for book in library_system.search_available_books():
#     print(f"Book: {book.name} - Category: {book.category} - Author: {book.author} - State: {book.state}")

"""
Mostrar libros prestados de una categoría en específico
"""
# library_system.show_borrowed_books_by_category("Ciencia ficción")
# library_system.show_borrowed_books_by_category("Clásico")
# library_system.show_borrowed_books_by_category("Realismo mágico")
# library_system.show_borrowed_books_by_category("Drama")

"""
Mostrar libros disponibles de una categoría en específico
"""
# library_system.show_available_books_by_category("Ciencia ficción")
# library_system.show_available_books_by_category("Clásico")
# library_system.show_available_books_by_category("Realismo mágico")
# library_system.show_available_books_by_category("Drama")

"""
Mostrar libros populares de cada categoría
"""
# library_system.show_popular_books_ordered_by_category()
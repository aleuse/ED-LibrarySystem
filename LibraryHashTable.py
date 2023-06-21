from TreeAVL import TreeAVL
from collections import defaultdict

class LibraryHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [TreeAVL() for _ in range(size)]
        self.category_count = defaultdict(int)

    def hash_func(self, key):
        hash_value = 5381
        for char in key:
            hash_value = (hash_value * 33) ^ ord(char)
        return hash_value % self.size

    def insert_book(self, book):
        index = self.hash_func(book.category)
        tree = self.table[index]
        tree.insert(tree.root, book)
        self.category_count[book.category] += 1

    def delete_book(self, book):
        index = self.hash_func(book.category)
        tree = self.table[index]
        books = tree.in_order()
        for _book in books:
            if _book.name == book.name:
                tree.delete(tree.root, _book)
                self.category_count[_book.category] -= 1
                break

    def update_state(self, book, state):
        index = self.hash_func(book.category)
        tree = self.table[index]
        books = tree.in_order()
        for _book in books:
            if _book.name == book.name:
                _book.state = state
                if state == "borrowed":
                    _book.num_borrowed_books += 1
                break

    def search_by_category(self, category):
        books_in_category = []
        index = self.hash_func(category)
        tree = self.table[index]
        for book in tree.in_order():
            if book.category == category:
                books_in_category.append(book)
        
        return books_in_category
        
    def search_by_author(self, author):
        books_of_author = []
        for tree in self.table:
            books = tree.in_order()
            for book in books:
                if book.author == author:
                    books_of_author.append(book)
        return books_of_author

    def get_most_borrowed_book(self):
        most_borrowed_book = None
        for tree in self.table:
            books = tree.in_order()
            for book in books:
                if not most_borrowed_book or book.num_borrowed_books > most_borrowed_book.num_borrowed_books:
                    most_borrowed_book = book
        return most_borrowed_book

    def get_most_borrowed_category(self):
        most_borrowed_category = None
        max_borrows = 0
        for category in self.category_count.keys():
            borrows = 0
            index = self.hash_func(category)
            tree = self.table[index]
            for book in tree.in_order():
                if book.category == category:
                    borrows += book.num_borrowed_books
            if borrows > max_borrows:
                most_borrowed_category = category
                max_borrows = borrows
                
        return most_borrowed_category, max_borrows

    def get_least_borrowed_categories(self):
        least_borrowed_categories = []
        least_borrows = float("inf")
        for category in self.category_count.keys():
            borrows = 0
            index = self.hash_func(category)
            tree = self.table[index]
            for book in tree.in_order():
                if book.category == category:
                    borrows += book.num_borrowed_books
            if borrows < least_borrows:
                least_borrowed_categories = [[category, borrows]]
                least_borrows = borrows
            elif borrows == least_borrows:
                least_borrowed_categories.append([category, borrows])
        return least_borrowed_categories

    def show_books_categories(self):
        categories = sorted(self.category_count.keys(), key = lambda x: self.category_count[x], reverse = True)
        for category in categories:
            num_books = self.category_count[category]
            print(f"Category: {category} - Number of Books: {num_books}")

    def search_borrowed_books(self):
        borrowed_books = []
        for tree in self.table:
            books = tree.in_order()
            for book in books:
                if book.state == "borrowed":
                    borrowed_books.append(book)
        return borrowed_books
    
    def search_available_books(self):
        available_books = []
        for tree in self.table:
            books = tree.in_order()
            for book in books:
                if book.state == "available":
                    available_books.append(book)
        return available_books
    
    def show_borrowed_books_by_category(self, category):
        borrowed_books = []
        index = self.hash_func(category)
        tree = self.table[index]
        for book in tree.in_order():
            if book.category == category:
                if book.state == "borrowed":
                    borrowed_books.append(book)        
        print(f"Category: {category}")
        for book in borrowed_books:
            print(f"Book: {book.name}")
        print()
        
    
    def show_available_books_by_category(self, category):
        available_books = []
        index = self.hash_func(category)
        tree = self.table[index]
        for book in tree.in_order():
            if book.category == category:
                if book.state == "available":
                    available_books.append(book)        
        print(f"Category: {category}")
        for book in available_books:
            print(f"Book: {book.name}")
        print()

    def show_popular_books_ordered_by_category(self):
        popular_books = defaultdict(list)
        for tree in self.table:
            books = tree.in_order()
            for book in books:
                popular_books[book.category].append((book.name, book.num_borrowed_books))

        for category, books in popular_books.items():
            books.sort(key = lambda x: x[1], reverse = True)
            print(f"Category: {category}")
            for book, borrows in books:
                print(f"Book: {book} - Number of Borrows: {borrows}")
            print()
            

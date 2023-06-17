class Book:
    def __init__(self, name, author, category):
        self.name = name
        self.author = author
        self.category = category
        self.state = "available"
        self.num_borrowed_books = 0
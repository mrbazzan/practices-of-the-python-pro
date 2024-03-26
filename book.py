
import warnings

###########
# INITIAL #
###########

class Book:
    def __init__(self, data):
        self.author_data = data['author']

    @property
    def author_for_display(self):
        return f"{self.author_data['first_name']} {self.author_data['last_name']}"

    @property
    def author_for_citation(self):
        return f"{self.author_data['last_name']}, {self.author_data['first_name'][0]}"

book_data = {
    'title': 'Ahmad',
    'subtitle': 'The zeal of prophet',
    'author': {
        'first_name': 'Bazzan',
        'last_name': 'Don',
    }
}
book = Book(book_data)

print(book.author_for_display)
print(book.author_for_citation)

###########
# BECOMES #
###########

class Author:
    def __init__(self, author_data):
        self.first_name = author_data['first_name']
        self.last_name = author_data['last_name']

    @property
    def for_display(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def for_citation(self):
        return f"{self.last_name}, {self.first_name[0]}"

class NewBook:
    def __init__(self, data):
        self.author_data = data['author']
        self.author = Author(self.author_data)

    @property
    def author_for_display(self):
        warnings.warn("Use book.author.for_display instead", DeprecationWarning)
        return self.author.for_display

    @property
    def author_for_citation(self):
        warnings.warn("Do not use this anymore!", DeprecationWarning)
        return self.author.for_citation

newbook = NewBook(book_data)
print(newbook.author_for_display)
print(newbook.author_for_citation)



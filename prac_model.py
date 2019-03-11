

#create book class with atleast two properties and one method

class Book:
    def __init__(self, name, pages, authors, publisher):
        self.name = name
        self.pages = pages
        self.authors = [authors]
        self.publisher = publisher

    def addAuthor(self, name):
        self.authors.append(name)
        
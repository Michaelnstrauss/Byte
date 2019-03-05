

#create two instances of the book class and compare their properties

import model

b1 = model.Book('Coding', 200, 'Martin', 'Wiley')
book_1_name = b1.name
book_1_pages = b1.pages
book_1_authors = b1.authors
book_1_publisher = b1.publisher

b2 = model.Book('Byte', 150, 'Bob', 'Moore')
book_2_name = b2.name
book_2_pages = b2.pages
book_2_authors = b2.authors
book_2_publisher = b2.publisher

add_author_1 = b1.addAuthor('Wayne simon')
print(add_author_1)

print('book name:        ', book_1_name, '       | ',book_2_name)
print('---------------------------------------------')
print('book pages:        ', b1.pages, '         | ', b2.pages)
print('---------------------------------------------')
print('book authors:       ', b1.authors, '     | ', b2.authors)
print('---------------------------------------------')
print('book publisher:     ', b1.publisher, '     | ', b2.publisher)

'''def organize_book(*arg):
    for info in arg:
        print(info)

print(organize_book(book_2_name,book_2_pages,book_2_authors,book_2_publisher))'''



import os
from app.orm import ORM
from app.books import Book
from app.words import Word

DIR = os.path.dirname(__file__)
DBFILENAME = 'bookstore.db'
DBPATH = os.path.join(DIR, DBFILENAME)

def seed(dbpath=DBPATH):
    ORM.dbpath = dbpath

    wizard_of_oz = Book(title='The Wizard of OZ', text_content='yellow brick road', author='L. Frank Baum')
    wizard_of_oz.save()


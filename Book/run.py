#! /usr/bin/env python3
from app.books import Book
from app.words import Word
import os
from app.orm import ORM

DIR = os.path.dirname(__file__)
DBNAME = 'bookstore.db'
DBPATH = os.path.join(DIR, 'data', DBNAME)

ORM.dbpath = DBPATH
#bk = Book(title="text")
#bk.load_text()
bkm = Word(word_count='word count')
bkm.makeword(word)
bkm.

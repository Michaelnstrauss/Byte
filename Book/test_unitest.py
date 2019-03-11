import sqlite3
import os
import unittest
from app.orm import ORM
from app.books import Book
from app.words import Word
from data.seed import seed
from data.schema import schema

DIR = os.path.dirname(__file__)
DBFILENAME = 'data/bookstore.db'
DBPATH = os.path.join(DIR, DBFILENAME)
TXTFILENAME = 'mobydick.1.txt'
TXTPATH = os.path.join(DIR, TXTFILENAME)

""" setting ORM.dbpath changes the db for all classes inheriting from it """
ORM.dbpath = DBPATH


class TestAccount(unittest.TestCase):
    def setUp(self):
        """ the setup method must be called setup """
        schema(DBPATH)
        seed(DBPATH)

    def tearDown(self):
        """ the tear down method must be called tearDown """
        os.remove(DBPATH)

    def test_save_and_pk_load(self):
        title_name = Book(title="Rufus")
        title_name.save()
        self.assertIsInstance(title_name.pk, int, 'save set pk')

        pk = title_name.pk
        same_title_name = Book.one_from_pk(pk)

        self.assertIsInstance(same_title_name, Book, 'one_from_pk loads an Account object')
        
        self.assertEqual(same_title_name.title, 'Rufus', 'save creates database row')
        same_title_name.save()

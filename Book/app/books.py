import sqlite3
from app.orm import ORM
from app.words import Word
import os

DIR = os.path.dirname(__file__)
DBFILENAME = 'data/bookstore.db'
DBPATH = os.path.join(DIR, DBFILENAME)
TXTFILENAME = 'mobydick.1.txt'
TXTPATH = os.path.join(DIR, TXTFILENAME)

class Book(ORM):
    tablename = 'books'
    fields = ['title', 'text_content', 'author']

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.title = kwargs.get('title')
        self.text_content = kwargs.get('text_content')
        self.author = kwargs.get('author')

    @classmethod
    def from_title(cls,title):
        """ return Book object for a given title in the database """
        return cls.select_one_where('WHERE title = ?', (title,))


    def load_text(self, dbpath='bookstore.db'):
        """ load a text file's content into the book's text content """
        with open(TXTPATH,'r') as txt_file:
            lines = txt_file.readlines()
            text_word = ''
            for line in lines:
                splitted_lines = line.split()
                for word in splitted_lines:
                    char = '!$/\'%*+=?\'\-.,*#[]()1234567890;:'
                    word = word.strip(char)
                    text_word += " " + word
            self.title = input('Input new title: ')
            self.author = input('Author name: ')
            self.text_content = text_word
            self.save()

    

       
        # view = View()
        # words = Words.select_many_where('WHERE books_pk = ?')
        # for word in words:
        #     view.words(self, word)

#if __name__ == '__main__':
#    load_word_count()

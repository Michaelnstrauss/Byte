import sqlite3
from app.orm import ORM
import os
from collections import Counter
import re

DIR = os.path.dirname(__file__)
DBFILENAME = 'data/bookstore.db'
DBPATH = os.path.join(DIR, DBFILENAME)
TXTFILENAME = 'mobydick.1.txt'
TXTPATH = os.path.join(DIR, TXTFILENAME)

class Word(ORM):
    tablename = 'words'
    fields = ['word','books_pk', 'word_count']

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.word = kwargs.get('word')
        self.books_pk = kwargs.get('books')
        self.word_count = kwargs.get('word_count')

    # def load_word_count(self, dbpath='bookstore.db'):
    #     with open(TXTPATH,'r') as txt_file:
    #         lines = txt_file.readlines()
    #         text_word = ''
    #         word_count_total = {}
    #         for line in lines:
    #             for word in line.split():
    #                 char = '!$/\'%*+=?\'\-.,*#[]()1234567890;:'
    #                 word = word.strip(char)

    #                 word_count_total[word] = 
    #                 print(word_count_total)


    
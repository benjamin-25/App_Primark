import sqlite3
from sqlite3 import Error

def connection():

    try:
        db = sqlite3.connect('db_primark.db')
        return db

    except Error:
        print(Error)


def close_db():
    
    con = connection()
    con.close()

from ntpath import join
from os import getcwd
import os
import sqlite3
from sqlite3 import Error



def connection():

    try:
        db  = sqlite3.connect('mydatabase.db')
        return db

    except Error:
        print(Error)

db=connection()

def getProductF(db):
    cursor=db.cursor()
    query="SELECT NombreProducto FROM Productos WHERE Categoria='F' "
    return cursor.execute(query).fetchall()

LPf=getProductF(db)

# print(getcwd())

def close_db():
    
    con = connection()
    con.close()

close_db()
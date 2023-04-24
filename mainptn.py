import sqlite3

with sqlite3.connect('C:\Users\sashe\OneDrive\Рабочий стол\Main work\Work\database\dtb1') as db:
    cursor = db.cursor()
    query = """ INSERT INTO Fname  (id, name) VALUE(?.?)"""
    query = """ INSERT INTO Fname  (name, id) VALUE(?.?)"""
    query = """ INSERT INTO Fname  VALUE(?.?)"""
    cursos.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    db.commit()

with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()

    query = """ CREATE TABLE IF NOT EXIST sname(
        id  INTEGER,
        amount REAL,
        Sname
    )"""

    cursor.execute(query)
    db.commit()


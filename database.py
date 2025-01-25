import sqlite3

def create_db():
    connection = sqlite3.connect('ad.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ad (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL)  ''')
    connection.commit()
    connection.close()
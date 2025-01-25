import sqlite3

def create_db():
    connection = sqlite3.connect('ad.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ad (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL) ''')
    connection.commit()
    connection.close()

def create_ad(title, content):
    connection = sqlite3.connect('ad.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO ad (title, content) VALUES (?,?)', (title, content))
    connection.commit()
    connection.close()

def read_ad():
    connection = sqlite3.connect('ad.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM ad')
    ads = cursor.fetchall()
    connection.close()
    return ads

def update_ad(id, title, content):
    connection = sqlite3.connect('ad.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE ad SET title=?, content=? WHERE id=?', (title, content, id))
    connection.commit()
    connection.close()

def delete_ad(id):
    connection = sqlite3.connect('ad.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM ad WHERE id=?', (id))
    connection.commit()
    connection.close()

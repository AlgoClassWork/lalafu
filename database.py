import sqlite3

DB_NAME = "ads.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_ads():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content FROM ads")
    ads = cursor.fetchall()
    conn.close()
    return ads

def create_ad(title, content):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ads (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()

def update_ad(ad_id, title, content):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE ads SET title = ?, content = ? WHERE id = ?", (title, content, ad_id))
    conn.commit()
    conn.close()

def delete_ad(ad_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ads WHERE id = ?", (ad_id,))
    conn.commit()
    conn.close()

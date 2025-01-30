import sqlite3

PATH = "./backend/server/database.db"

def db_init():
    with sqlite3.connect(PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS stories(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                story TEXT
            )
        ''')
        conn.commit()

def db_connection():
    conn = sqlite3.connect(PATH)
    conn.row_factory = sqlite3.Row
    return conn
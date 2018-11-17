import sqlite3

def connect():
    conn = sqlite3.connect("songs.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS song (id INTEGER PRIMARY KEY, title TEXT, artist TEXT, album TEXT, year INTEGER)")
    conn.commit()
    conn.close()

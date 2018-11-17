import sqlite3

def connect():
    conn = sqlite3.connect("songs.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS song (id INTEGER PRIMARY KEY, title TEXT, artist TEXT, album TEXT, year INTEGER)")
    conn.commit()
    conn.close()

def insert(title, artist, album, year):
    conn=sqlite3.connect("songs.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO song VALUES (NULL, ?, ?, ?, ?)", (title, artist, album, year))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("songs.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM song")
    rows = cur.fetchall()
    conn.close()
    return rows

connect()
insert("Gettin' Jiggy with it", "Will Smith", "Jiggin' with Jiggy", 2000)
delete(1)
print(view())

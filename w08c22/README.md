#w08c22

Applications must be interfaced with. Often this interface is with other systems, but also, it involved interacing with a "human". The methods of deploying an application are varied. If we look at the evolution of the human computer interaction, we find an increasing exanding arena of possibilities. This week we look at one of HCI these methods, Desktop GUI programming in Python.


To develop GUI's in Python we need to import and use specialized packages. There are a number of common packages used by Python GUI programmers. Programming GUI's for cross platform use requires a framework. These frameworks are typically independent of the language, but languages have bindings through which to create GUI's based on these frameworks. The most common of these frameworks include [Gtk](http://www.gtk.org/) (GNU LGPL license), [Qt](https://www.qt.io/) (commercial license), [Tk](http://wiki.tcl.tk/477) (very open licensing from University of California), and [wxWidgets](https://www.wxwidgets.org/) (A modified Library General Public License that let's you commercialize any derived products).

The most popular are Tkinter (it's part of the python distribution, so is the most common) which binds to and uses Tk. We will use Tkinter for this portion of the course because Tkinker if part of the standard Python library (but if you wish to get into serious Python GUI programming, you may want to look at PyQT/Qt Creator -- or other frameworks/GUI layout editors).

Note on GUI builders - there doesn't seem to be a defacto standard for Python Tkinker (you can look at PAGE, Pygubu). You're welcome to google and explore the various options.  We will only build  simple interfaces without the need to employ a GUI builder. The objective is to simply familiarize you with the Tkinker framework, and if you choose to build a GUI for your final project, you have a foundation from which to understand how to build a GUI in python.

## Aside: creating an exe from Python.
If we wish to create a Python application that we can distribute to users, it would be quite useful to not require the user to have Python installed. ...


# Tkinker

## History of Tkinker....

# Our sample application: Song database
Let's learn about Tkinker by building an application. If you want to learn more about Tkinker, you can access the latest API documentation here... (insert link to offical Tkinker documentation.... also list any books)

Song
Album
Artist
Genre

## Sketch the Interface

First we need to sketch out the interface, create a Wireframe
![Interface Mockup](wireframe.png)

In Tkinker we can create applications using Pack or Grid. We will be using Grid, which allows up to specify our layout using cell referencing. To help guide our development we now overlay a grid on our sketch...

![Interface Mockup](wireframe_grid.png)

## Build the Front-End

When building applications we often think of them in "tiers". In our GUI application we have two tiers, the "front-end" and the "back-end".  In this section we focus on building the front-end.


### Step 1

Let's get the titles in place.

```python
"""Program that stores song information: Song, Album, Artist, and Genre.

User can:
    View all songs
    Search for a song
    Add a song
    Update a song
    Delete a song
    Exit the application

NOTE: See wireframe.png for sketch of interface.

"""
from tkinter import *

window=Tk() # TK method that creates a windows objective

l1=Label(window, text="Song")
l1.grid(row=0,column=0)

l2=Label(window, text="Arist")
l2.grid(row=0,column=2)

l3=Label(window, text="Album")
l3.grid(row=1,column=0)

l3=Label(window, text="Year")
l3.grid(row=1,column=2)

window.mainloop()
```
<center><sub>[^click here for code^](songDB_01.py)</sub></center>
<br>
<br>

### Step 2

Let's get the input text fields in place

```python
# Display text entry fields
song_text=StringVar()
e1=Entry(window,textvariable=song_text)
e1.grid(row=0,column=1)

artist_text=StringVar()
e2=Entry(window,textvariable=artist_text)
e2.grid(row=0,column=3)

album_text=StringVar()
e3=Entry(window,textvariable=album_text)
e3.grid(row=1,column=1)

year_text=StringVar()
e4=Entry(window,textvariable=year_text)
e4.grid(row=1,column=3)
```
<center><sub>[^click here for code^](songDB_02.py)</sub></center>
<br>
<br>

### Step 3

Let's create a listbox and attach a scroll bar

```python
# display listbox and attached a Scrollbar
list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan = 6, columnspan= 2 ) # we want to span across multiple rows and columns

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)
```
<center><sub>[^click here for code^](songDB_03.py)</sub></center>
<br>
<br>

### Step 4
Display Buttons

```python
b1=Button(window, text="View All songs", width=12)
b1.grid(row=2, column=3)
b2=Button(window, text="Search ", width=12)
b2.grid(row=3, column=3)
b3=Button(window, text="Add Song", width=12)
b3.grid(row=4, column=3)
b4=Button(window, text="Update Song", width=12)
b4.grid(row=5, column=3)
b5=Button(window, text="Delete Song", width=12)
b5.grid(row=6, column=3)
b6=Button(window, text="Exit", width=12)
b6.grid(row=7, column=3)
```
<center><sub>[^click here for code^](songDB_04.py)</sub></center>
<br>
<br>

## Build the back-end

Let's now start thinking of our application as a multi-tiered application, with a "front-end" and a "back-end". We first rename our songDB_04.py file to frontend_01.py and add an import backend statement.

```python
import backend_01 as backend
```
<center><sub>[^click here for code^](frontend_01.py)</sub></center>
<br>
<br>

And now create our backend_01.py to being the coding of our backend. In this first version, we just want to create our database and table if they do not already exist.

```python
import sqlite3

def connect():
    conn = sqlite3.connect("songs.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS song (id INTEGER PRIMARY KEY, title TEXT, artist TEXT, album TEXT, year INTEGER)")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("This is a module and is not designed to be run as main script.")
else:
    connect()
```
<center><sub>[^click here for code^](backend_01.py)</sub></center>
<br>
<br>


Now, let's add an insert and view function. We'll eventually attach these functions to our front end, but for now we will only test them within the backend module.

```python
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
print(view())
```
<center><sub>[^click here for code^](backend_02.py)</sub></center>
<br>
<br>

When we run this this multiple times from the command line, we see that it is adding our records to the database and incrementing the ID by one each time.

```
$ python backend_01.py
This is not meant to be called directly
$ python backend_02.py
[(1, "Gettin' Jiggy with it", 'Will Smith', "Jiggin' with Jiggy", 2000)]
$ python backend_02.py
[(1, "Gettin' Jiggy with it", 'Will Smith', "Jiggin' with Jiggy", 2000), (2, "Gettin' Jiggy with it", 'Will Smith', "Jiggin' wi
th Jiggy", 2000)]
```

Now, let's add all the remaining functions (that is, search, delete and update) that will be needed by our front end to our backend.py file

```python
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

def search(title="", artist="", album="", year=""):
    conn=sqlite3.connect("songs.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM song WHERE title=? OR artist=? OR album=? OR year=?", (title, artist, album, year))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("songs.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM song WHERE id=?", (id,)) # don't forget the comma or python will not interptret this as a tuple
    conn.commit()
    conn.close()

def update(id, title, artist, album, year):
    conn = sqlite3.connect("songs.db")
    cur = conn.cursor()
    cur.execute("UPDATE song SET title=?, artist=?, album=?, year=? WHERE id=?", (title, artist, album, year, id)) # don't forget the comma or python will not interptret this as a tuple
    conn.commit()
    conn.close()
```
<center><sub>[^click here for code^](backend_03.py)</sub></center>
<br>
<br>

## Integrate the front and back end.

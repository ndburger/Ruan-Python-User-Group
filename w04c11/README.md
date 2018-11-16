
# w04c11



## Python module loading process

A few things to mention about modules in Python.

### Importing modules

When a module is imported, it is run. If a module is imported more than once, it will not run the second time.

Once a module runs the first time, the interpreter will store a bytecode compiles version of the module in the ```__pycache__``` folder. In this folder you'll find files with the extension .pyc. These are compiled (into bytecode, not machine code) versions of the modules.


### Using ```__name__``` in modules

When the Python interpreter reads a source file, it attempts to executes all of the code found in it. Before this process starts though, the interpreter will define a few special variables; one of the variables is ```__name__```. If the source file being loaded is the first file (the python code that we call to start the whole programming running) then this variable ```__name__``` will be set to the value ```__main```. Often though, Python loads source files that are treated as modules, that is, they are not the starting script, but are called by the starting script (or scripts that are called by the starting script, etc.). In these cases the ```__name``` variable is set to the name of the module (filename without the .py extension).

If we call a script directly:

```
$ python helloworld.py
```

The ```__name__``` will be set to ```__main```.

But, if helloworld.py imports helloworld_module.py, then ```__name__``` within the module will be set to ```helloworld_module```.

I've provided sample code to illustrate

First, we create a module called aboutmain.py
```python
"""Demo __name__ and it's values."""

def f():
    print(__name__)
    return None

print(__name__)
f()
```

Secondly we create another module that imports aboutmain and calls the f() function defined in aboutmain.

```python
"""Demo use of __name__ in modules."""

import aboutmain

aboutmain.f()

```

When we call aboutmain.py, here is the Output

```python
$ python aboutmain.py
__main__
__main__
```

But, when we call import_aboutmain.py, here is output:

```python
$ python import_aboutmain.py
aboutmain
aboutmain
aboutmain
```

Now, think about this output. Not only does it demonstrate that ```__name__``` changes based on if the module is called directly or imported, but also, notice how we get three (not two) prints of the value of ```__name__```. This is because mainmodule automatically runs when imported, and then again, we call the f() function in mainmodule. This results in printing the ```__name__``` value (which is aboutmain) three times.


### detecting if the module has been called directly

A common piece of code that you'll find in modules is as follows:

```python
if __name__ == "__main__":
    print("You're calling me as if I was a program, but alas, I'm just a lowly module.")
```


## File IO discussion continued:

### JSON

> JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. It is based on a subset of the JavaScript Programming Language, Standard ECMA-262 3rd Edition - December 1999. JSON is a text format that is completely language independent but uses conventions that are familiar to programmers of the C-family of languages, including C, C++, C#, Java, JavaScript, Perl, Python, and many others. These properties make JSON an ideal data-interchange language. (taken from www.json.org)

For more detail on the format of a JSON file, see www.json.org.

In Python, we can use a module "json" to serialize and store our Python objects in a json format file. We can also deserialize and bring these objects back into memory. Json thus serves as a convenient method of storing and sharing persistent data.

For example, let's create a json string (this could simply be a string stored in memory, which is a serialized version of the data structures we are interested in).

```python
import json

somedata = [{'fname': 'Alfred', 'occupation': 'Butler', 'a': (2, 4), 'b': 3.0}]
print('DATA:', repr(somedata))

data_string = json.dumps(somedata)
print('JSON:', data_string)
```
<center><sub>[^click here for code^](json1.py)</sub></center>
<br>
<br>

We can also easily store this Json encoded string to a file.

```python
import json
somedata = [{'fname': 'Alfred', 'occupation': 'Butler', 'a': (2, 4), 'b': 3.0}]
with open('data01.json','w') as outfile:
  json.dump(data.outfile)

```
<center><sub>[^click here for code^](json2.py)</sub></center>
<br>
<br>


```python
import json

somedata = [{'fname': 'Alfred', 'occupation': 'Butler', 'a': (2, 4),
            'b': 3.0, 'c': {'x': 12, 'y': 100}}]

# translate this data structur into a json string
data_string = json.dumps(somedata)

# display the contents of the json encoded (serialized) string representation of our somedata data structure.
print('ENCODED:', data_string)

# now, let's reverse the process, deencoding (or deserialize) the data.
decoded = json.loads(data_string)

# and print the result
print('DECODED:', decoded)

# now, let's compare the results of the preencoded data, and the end result of the unencoded (deserialized data)
print('ORIGINAL:', type(somedata[0]['fname']))
print('DECODED :', type(decoded[0]['fname']))
print('ORIGINAL:', type(somedata[0]['occupation']))
print('DECODED :', type(decoded[0]['occupation']))
print('ORIGINAL:', type(somedata[0]['a']))
print('DECODED :', type(decoded[0]['a']))
print('ORIGINAL:', type(somedata[0]['b']))
print('DECODED :', type(decoded[0]['b']))
print('ORIGINAL:', type(somedata[0]['c']))
print('DECODED :', type(decoded[0]['c']))

# notice how tuple became a list!
```
<center><sub>[^click here for code^](json3.py)</sub></center>
<br>
<br>

As we see from the above code, tuples become lists.


Here is an example of updating what is stored in a JSON file:  we load, edit, and the store the stored objects - thus simply rewriting the old file.

```python
import json
somedata = {'fname': 'Alfred', 'occupation': 'Butler', 'a': (2, 4),
            'b': 3.0, 'c': {'x': 12, 'y': 100}}
print(somedata)

f = open('data.json', 'w')
json.dump(somedata, f)
f.close()

f = open('data.json', 'r')
somedata = json.load(f)
f.close()
print(somedata)

somedata['fname'] = 'Al'
f = open('data.json', 'w')
json.dump(somedata, f)
f.close()

f = open('data.json', 'r')
somedata = json.load(f)
f.close()
print(somedata)
```
<center><sub>[^click here for code^](json3.py)</sub></center>
<br>
<br>


__NOTE__: Notice that dictionary data types are unordered. If you print them, the order may not display in the same order in which the items were created, also, the order could change each time it is printed.

As interesting as JSON is, it's probably not the best approach to storing, and editing, data with any frequency. In such cases, we may want to look at SQLite instead.

### SQLLite

>SQLite is a high-reliability, embedded, zero-configuration, public-domain, SQL database engine. SQLite is the most used database engine in the world. [more info](https://www.sqlite.org/about.html)

SQLite is not a complete multiuser database system, but it's a lightweight, serverless, and supports much of the SQL language. It's a great tool for your programs to store and retrieve local data using SQL.

How SQLite achieves this with such a simple approach is quite impressive.

* to understand more about locking, contention, journalling etc. see https://www.sqlite.org/lockingv3.html
* if you run into problems (or want to avoid doing so) when accessing an SQLite database (either concurrently, or not) see https://www.sqlite.org/howtocorrupt.html

Though SQLite can easily handle many processes or thread accessing the database at the same time, care must be taken when multiple updates are occurring. Only one process can update changes to the database at any moment in time. Most updates only briefly lock the database, and will work under such conditions, but clearly any large scale deployment with concurrent usage will require a more robust database such as MySQL, PostgreSQL, Oracle, SQLserver, etc.

But, with that said, the are many useful applications for SQLite, and often, requiring a large database (Oracle et. al) can be the exception rather than the rule.


Let's create a simple database with one table, and three columns

```python
import sqlite3

sqlite_file = 'dbsample.sqlite'    # name of the sqlite database file

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# we can simply execute SQL using string literals as follows...
c.execute("CREATE players IF NOT EXISTS players (ID 'INTEGER' PRIMARY KEY, FName 'TEXT', LName 'TEXT')")
conn.commit()
conn.close()
```
<center><sub>[^click here for code^](dbcreate.py)</sub></center>
<br>
<br>


But, things get a little more interesting when we want to programatically (dynamically) create  SQL statements.

```python
import sqlite3

sqlite_file = 'dbsample.sqlite'
table_name = 'players'  # name of the table access

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.format(tn=table_name, v1=10, v2='"Bob"', v3='"Gainey"'))
c.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.format(tn=table_name, v1=11, v2='"Bobby"', v3='"Orr"'))
c.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.format(tn=table_name, v1=12, v2='"Sidney"', v3='"Crosby"'))
c.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.format(tn=table_name, v1=13, v2='"Guy"', v3='"Lafleur"'))

conn.commit()
conn.close()
```
<center><sub>[^click here for code^](dbinsert.py)</sub></center>
<br>
<br>


Finally, we want to extract data from the database:

```python
import sqlite3


sqlite_file = 'dbsample.sqlite'    # name of the sqlite database file
table_name = 'players'   # name of the table to be queried
id_column = 'ID'
column_2 = 'FName'
column_3 = 'LName'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('SELECT * FROM {tn}'.format(tn=table_name))
all_rows = c.fetchall()
print('1):', all_rows)

c.execute('SELECT * FROM {tn} WHERE {cn}=10'.format(tn=table_name, cn=id_column))
all_rows = c.fetchall()
print('2):', all_rows)

conn.close()
```
<center><sub>[^click here for code^](dbquery.py)</sub></center>
<br>
<br>


The above code illustrated how we can create SQLcode for execution, and analyze the results.

Some other SQL patterns include:

```
# Add a columns to players
ALTER TABLE players ADD COLUMN points INTEGER

# Insert a new row into players
INSERT INTO players VALUES (99, "Wayne", "Gretzky")

# Insert if it can...
INSERT OR IGNORE INTO players VALUES (10,"Bob","Gainey")

# Update existing row
UPDATE players SET ID=3 WHERE ID=10
```

Here is an overview of the datatypes supports by SQLite
```
    INTEGER: A signed integer up to 8 bytes depending on the magnitude of the value.
    REAL: An 8-byte floating point value.
    TEXT: A text string, typically UTF-8 encoded (depending on the database encoding).
    BLOB: A blob of data (binary large object) for storing binary data.
    NULL: A NULL value, represents missing data or an empty cell.
```

__NOTE__: A handy tool for exploring SQLlite DB's can be found here http://sqlitebrowser.org/

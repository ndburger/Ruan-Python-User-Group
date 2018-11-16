# w04c12




## SQLite Redux: The Horror, the Horror.

When we execute a SQL command, we get back a cursor object. We can use this object to read rows one by one, in "chunks", or all at once.

### Using the cursor object (Query handling)

Here we use the fetchall() command:

```python
import sqlite3


sqlite_file = 'dbsample.sqlite'    # name of the sqlite database file
table_name = 'person'   # name of the table to be queried

conn = sqlite3.connect(sqlite_file)
cur = conn.cursor()

cur.execute('SELECT * FROM {tn}'.format(tn=table_name))
all_rows = cur.fetchall()
print('1):', all_rows)

conn.close()

```
<center><sub>[^click here for code^](slight1.py)</sub></center>
<br>
<br>



Here, we fetchone(), but then a fetchall() after

```python
import sqlite3

sqlite_file = 'dbsample.sqlite'    # name of the sqlite database file
table_name = 'person'   # name of the table to be queried

conn = sqlite3.connect(sqlite_file)
cur = conn.cursor()

cur.execute('SELECT * FROM {tn}'.format(tn=table_name))
one_row = cur.fetchone()
print('1a):', one_row)
all_rows = cur.fetchall()
print('1b):', all_rows)
conn.close()

```
<center><sub>[^click here for code^](slight2.py)</sub></center>
<br>
<br>



Here, we fetch fetchmany(), but not all, and then fetchone() until none left.

```python
import sqlite3

sqlite_file = 'dbsample.sqlite'    # name of the sqlite database file
table_name = 'person'   # name of the table to be queried

conn = sqlite3.connect(sqlite_file)
cur = conn.cursor()

cur.execute('SELECT * FROM {tn}'.format(tn=table_name))
many_rows = cur.fetchmany(2)
print('1a):', many_rows)

all_rows = cur.fetchall()
print('1b):', all_rows)
conn.close()

```
<center><sub>[^click here for code^](slight3.py)</sub></center>
<br>
<br>



Alter, we can iterate through the rows, and elements of the row, as follows:

```python
import sqlite3

sqlite_file = 'dbsample.sqlite'    # name of the sqlite database file
table_name = 'person'   # name of the table to be queried

conn = sqlite3.connect(sqlite_file)
cur = conn.cursor()

cur.execute('SELECT * FROM {tn}'.format(tn=table_name))

for row in cur:
    for elem in row:
        print(elem)

conn.close()

```
<center><sub>[^click here for code^](slight4.py)</sub></center>
<br>
<br>

### Transactions

You may read about transactions, SQLite supports transactions. Transactions allow for you to group a number of insertions almost as one transaction. This can improve speed any many cases, but is most useful when you wish to rollback a transaction. With the SQLite DBI (database interface) SQLite3 attempts to automate such transactions, and will automatically set up transaction begin and end. We're not getting too deep into any work that would require us to subvert this, but it is something to remember if you're finding some abnormalities on failed insertion and rollbacks. If you wish to do a number of transactions, and if one fails rollback all of these transactions, you'll need to set your connection object to isolation_level=None (see below)

__NOTE__: In the following code, the last insert conflicts with a record already in the database. This is a rather contrived example, but illustrates how if a set of DML statements has one bad/unexecutable statement, you can rollback the entire transaction.


```python
import sqlite3

sqlite_file = 'dbsample.sqlite'
table_name = 'person'   # name of the table to be queried

conn = sqlite3.connect(sqlite_file)
conn.isolation_level = None

try:
    cur = conn.cursor()
    cur.execute("begin")
    cur.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.\
        format(tn=table_name, v1=15, v2='"Tim"', v3='"Horton"'))
    cur.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.\
        format(tn=table_name, v1=16, v2='"Wendel"', v3='"Clark"'))
    cur.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.\
        format(tn=table_name, v1=17, v2='"Ty"', v3='"Domi"'))
    cur.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.\
        format(tn=table_name, v1=11, v2='"Bobby"', v3='"Orr"'))
    cur.exectute("commit")
except:
    cur.execute("rollback")
```
<center><sub>[^click here for code^](slight5.py)</sub></center>
<br>
<br>

### Date and Time Handling in SQLite

Date and Time Handling in SQLite. You can test these commands using DB Browser for SQLIte (and more generally, use DB Browser for SQLite to build and test your queries and database before translating it into Python sqlite3 calls)

(note: The following sql is taken from the sqlite.org official documentation)

(note2: as mentioned in last lecture, if you work allot with SQLite, download and install http://sqlitebrowser.org/)


```SQL
--Compute the current date.
    SELECT date('now');

--Compute the last day of the current month.
    SELECT date('now','start of month','+1 month','-1 day');

--Compute the date and time given a unix timestamp 1092941466.
    SELECT datetime(1092941466, 'unixepoch');

--Compute the date and time given a unix timestamp 1092941466, and compensate for your local timezone.
    SELECT datetime(1092941466, 'unixepoch', 'localtime');

--Compute the current unix timestamp.
    SELECT strftime('%s','now');

--Compute the number of days since the signing of the US Declaration of Independence.
    SELECT julianday('now') - julianday('1776-07-04');

--Compute the number of seconds since a particular moment in 2004:
    SELECT strftime('%s','now') - strftime('%s','2004-01-01 02:34:56');

--Compute the date of the first Tuesday in October for the current year.
    SELECT date('now','start of year','+9 months','weekday 2');

--Compute the time since the unix epoch in seconds (like strftime('%s','now') except includes fractional part):
    SELECT (julianday('now') - 2440587.5)*86400.0;
```
<center><sub>[^click here for code^](datetime.sql)</sub></center>
<br>
<br>


For more information on Date Time handling in SQLite, see https://www.sqlite.org/lang_datefunc.html


For more on SQLite, I'd recommend https://www.sqlite.org/docs.html or a the more tutorial oriented site here http://www.tutorialspoint.com/sqlite/sqlite_primary_key.htm


## Control Flow

We've already seen some control flow operations in Python. Let's spend a bit more time with this topic.

### If statements

```python

import random

number = random.randint(1,100)

guess = int(input("I'm thinking of a number between 1 and 100. What is it? : "))

if guess == number:
    print('The odds of getting this in the first guess are 1/100.')
    print('Congratulations, you guessed it.')
elif guess < number:
    print('No, it is a little higher than that')
else:
    print('No, it is a little lower than that')

print('Done')

```
<center><sub>[^click here for code^](cf1.py)</sub></center>
<br>
<br>


Like any other computer language, the meeting a condition involves a boolean calculation. The result from a boolean expression is always either true or false.
```python

if True:
  print(True)
elif:
  print(False)
```
<center><sub>[^click here for code^](cf2.py)</sub></center>
<br>
<br>

There is no switch statement in Python. You can use an if..elif..else statement to do the same thing.


### Branching with dictionaries

In some situations, you can use a dictionary for branching:

```python
passwords = {'Tim': 'sdfasdf', 'Bob': 'dfafsdc', 'Sue': 'wnkrewd'}
uname = input('Please enter your username : ')
username, password = uname, passwords.get(uname, 'unkown')
print(username,password)
```
<center><sub>[^click here for code^](cf3.py)</sub></center>
<br>
<br>


```python
dict1 = { 'a': lambda: print("Hello A"), 'b': lambda: print("Hello B") }
dict1[input("Input 'a' or 'b': ")]()
```
<center><sub>[^click here for code^](cf4.py)</sub></center>
<br>
<br>


```python
dict = { 'f1': lambda x,y: x**2+y**2, 'f2': lambda x,y: x+y**3 }
print(dict[input("Which function [f1 or f2]? : ")](10,12))
```
<center><sub>[^click here for code^](cf5.py)</sub></center>
<br>
<br>


### Loops

```python
for letter in 'MIS407':
  print('Current Letter :', letter)

langs = ['Python', 'Java',  'C', 'R']
for lang in langs:        # Second Example
   print('Current language :', lang)
```
<center><sub>[^click here for code^](cf6.py)</sub></center>
<br>
<br>


Here we create an index, and iterate through the list using the index:
```python
langs = ['Python', 'Java',  'C', 'R']
for i in range(len(langs))
   print('Current language :', lang[i])
```
<center><sub>[^click here for code^](cf7.py)</sub></center>
<br>
<br>

Iterating through a 2 dimensional array (Python style): __NOTE__:We'll later be using Pandas and Numpy for handling of vectors, matrices, and dataframes. But, to illustrate for loops...

```python
x, y = 4, 4
twodra = [[x for x in range(x)] for y in range(y)]
for i in range(len(twodra)):
    for j in range(len(twodra[i])):
        print(twodra[i][j])
```
<center><sub>[^click here for code^](cf8.py)</sub></center>
<br>
<br>

__NOTE__: The above code demonstrates a use of "list comprehensions". Python is not only object oriented, but also functionally oriented as well. Though functional programming has been around for some time,  functional programming languages are becoming quite popular. Much like OOP was 25 years ago, functional programming is "all the rage" now. see: https://www.smashingmagazine.com/2014/07/dont-be-scared-of-functional-programming/. We'll be covering functional programming more in the coming weeks.


### While Loops

Finite loop:

```python
count = 0
while (count < 9):
   print('The count is:', count)
   count += 1
```
<center><sub>[^click here for code^](whl1.py)</sub></center>
<br>
<br>

Infinite loop with terminating condition:

```python
num = 1
while (int(num) != 0):
   num = input("Enter a number (0 to stop)  :")
   print("You entered: ", num)
```
<center><sub>[^click here for code^](whl2.py))</sub></center>
<br>
<br>

__NOTE__ Obviously, use infinite loops with care.


### Break, continue and pass statements


Break: Terminates current loop and resumes.

Break example
```python
for letter in "MIS407":
    if letter == '4':
        break
    print(letter)
```
<center><sub>[^click here for code^](break1.py)</sub></center>
<br>
<br>


The continue statement returns control to the beginning of a while loop.

Continue example
```python
while num > 0:
  num = (int)input("Input a whole number less than 100: ")
  if num > 99:
    continue
  print("Num = ", num)  
```

Pass comment is basically a blank, do nothing statement, that is used where syntax dictates that a statement must exist, but you have no reason to include a statement.

Pass example
```python
for letter in "MIS407":
  if letter == '4':
    pass
    print("This is passed")
  print("Current letter", letter)

```
<center><sub>[^click here for code^](pass.py)</sub></center>
<br>
<br>

Here is an example (from your IA02):

```python
import sys

if len(sys.argv) > 101:
    print("Sorry, the limit is 100 words")
else:
    vowels = ('a', 'e', 'i', 'o', 'u', 'y', 'A', "E", "I", "O", "U", "Y")
    for i in range(1, len(sys.argv)):
        if sys.argv[i][0] in vowels:
            print(sys.argv[i][:len(sys.argv[i])] + "way ", end="")
        else:
            wrd = ""
            for j in range(0, len(sys.argv[i])):
                if sys.argv[i][j] not in vowels:
                    wrd = wrd + sys.argv[i][j]
                else:
                    out = sys.argv[i][j:] + wrd.lower() + "ay "
                    if sys.argv[i][0].isupper():
                        print(out.title(), end="")
                    else:
                        print(out, end="")
                    break
```

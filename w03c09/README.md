# W03c09: Python Data Types

__TOC W03c09__:

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [W03c09: Python Data Types](#w03c09-python-data-types)
	- [The Standard Type Hierarchy](#the-standard-type-hierarchy)
		- [Ellipsis type](#ellipsis-type)
		- [Sequences](#sequences)
			- [Immutable Sequences](#immutable-sequences)
			- [Mutable Sequences](#mutable-sequences)
		- [Tuples, Lists and Dictionaries](#tuples-lists-and-dictionaries)
			- [Tuples](#tuples)
			- [Lists](#lists)
			- [Dictionaries](#dictionaries)
			- [Casting a tuple](#casting-a-tuple)
	- [Collections](#collections)
	- [Operators](#operators)
		- [The 'in' Python Operator](#the-in-python-operator)
		- [Other operators in Python](#other-operators-in-python)

<!-- /TOC -->
## The Standard Type Hierarchy

Python has a standard Hierarchy of types. For our discussion on variables, in this lecture we are most interested in three main types: None, Ellipses, and Sequences (others include sets, mappings, callable, module, class instances, I/O objects, internal types).

(Note: this section is adapted from https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy)

### Ellipsis type

This is the parent type (superclass) of the numerical types, of which there are three major subtypes - integral, real, and complex.

* __Integral__
  * Integers (in)
  * Booleans (bool)
* __Real__
  * float
* __Complex__
  * complex

### Sequences
Sequences represent finite ordered sets that are indexed by non-negative numbers. The built-in function len() returns the number of items of a sequence. When the length of a sequence is n, the index set contains the numbers 0, 1, ..., n-1. Item i of sequence a is selected by __a[i]__.

Sequences also support slicing: __a[i:j]__ selects all items with index k such that i <= k < j. When used as an expression, a slice is a sequence of the same type. This implies that the index set is renumbered so that it starts at 0.

Some sequences also support “extended slicing” with a third “step” parameter: __a[i:j:k]__ selects all items between i and j in steps of k.

```
>>> x = (1,2,3,4,5,6,7,8,9,10)
>>> x[1]
2
>>> x[0]
1
>>> x[1:5]
(2, 3, 4, 5)
>>> x[1:10:2]
(2, 4, 6, 8, 10)
>>>
```

Sequences are distinguished according to their mutability:

__There are two major classes of sequences, those the are mutable, and those that are not (immutable).__

#### Immutable Sequences

Once set, these variables cannot change (but you can cast them to a mutable, make a change, and cast them back to an immutable)

Python "mutable" types:

* Strings - A string is a sequence of values that represent Unicode code points. All the code points in the range U+0000 - U+10FFFF can be represented in a string. Python doesn’t have a char type; instead, every code point in the string is represented as a string object with length 1. The built-in function ord() converts a code point from its string form to an integer in the range 0 - 10FFFF; chr() converts an integer in the range 0 - 10FFFF to the corresponding length 1 string object. str.encode() can be used to convert a str to bytes using the given text encoding, and bytes.decode() can be used to achieve the opposite.
* __Tuples__ - The items of a tuple are arbitrary Python objects. Tuples of two or more items are formed by comma-separated lists of expressions. A tuple of one item (a ‘singleton’) can be formed by affixing a comma to an expression (an expression by itself does not create a tuple, since parentheses must be usable for grouping of expressions). An empty tuple can be formed by an empty pair of parentheses.
* __Bytes__ - A bytes object is an immutable array. The items are 8-bit bytes, represented by integers in the range 0 <= x < 256. Bytes literals (like b'abc') and the built-in function bytes() can be used to construct bytes objects. Also, bytes objects can be decoded to strings via the decode() method.

#### Mutable Sequences
* __Lists__ - The items of a list are arbitrary Python objects. Lists are formed by placing a comma-separated list of expressions in square brackets. (Note that there are no special cases needed to form lists of length 0 or 1.)
* __Byte Arrays__ - A bytearray object is a mutable array. They are created by the built-in bytearray() constructor. Aside from being mutable (and hence unhashable), byte arrays otherwise provide the same interface and functionality as immutable bytes objects.

### Tuples, Lists and Dictionaries

We've already discussed some of the basic python types. Let's look at a few of the more advanced datatypes: tuples, lists and dictionaries.

#### Tuples

Tuples are a convenient way to store and access information in Python. They are like an array of objects, where not all the objects need to be the same type.

Here is an example of a tuple of objects of the same type and how we reference the values found within a tuple (HINT: All sequence types behave the same wrt to indexing).

```python
>>> atuple = (1000,1001,1002,1003)
>>> atuple[0]
1000
>>> atuple[1]
1001
>>> len(atuple)
4
>>> atuple[4] # NOTE: This will create an error!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> atuple[3]
1003
```

Here is an example of a tuple of dissimilar objects (3 strings and an integer)

```python
>>> btuple = ("Prof.", "Tim", "Smith", 2039)
>>> len(btuple)
4
>>> btuple[0]
'Prof.'
>>> btuple[1]
'Tim'
>>> btuple[2]
'Smith'
>>> btuple[3]
2039
>>>
```

Tuples can also contain other tuples.

```python
>>> ctuple = (("Tim","Smith"),(123,"xyx street"),(23,32,45,54))
>>> ctuple[0]
('Tim', 'Smith')
>>> ctuple[0][0]
'Tim'
>>> ctuple[0][1]
'Smith'
>>> ctuple[2][1]
32
>>> ctuple[2][3]
54
```

#### Lists

Lists are tuples that are mutable (that can be changed), while tuples are immutable (that cannot change once they have been established).

First, let's look what happens when we attempt to change one of the values of a tuple

```python
>>> atuple=(1000,1001,1002,1003)
>>> atuple
(1000, 1001, 1002, 1003)
>>> atuple[0]
1000
>>> atuple[0]=999
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Now, let's create a list containing the same sequence of numbers. Look what happens when we attempt to change the number.
```python
>>> alist=[1000,1001,1002,1003]
>>> alist[0]
1000
>>> alist[0]=999
>>> alist
[999, 1001, 1002, 1003]
```

In the case of a tuple, we received an error when attempting to change one of the values. In the case of the list, we did not.

>Sidebar: You may ask, "why use tuples?". I offer three key reasons: 1) You want to protect the data within the data structure from being updated, 2) Accessing data using tuples is much faster than accessing data in lists (uses less processing) 3) taking advantage of the handling of immutable objects in modules and classes (more later)

#### Dictionaries

Dictionaries allow you to name elements of a tuple or list. As we saw in the last tuple example above (ctuple), this could be a valuable addition to our programming toolset.

Let's look at a dictionary version of the "ctuple" example:
```python
>>> adict = {'name':("Tim","Smith"),'address':(123,"xyx street"), 'data':(23,32,45,54)}
>>> adict['name']
('Tim', 'Smith')
>>> adict['name'][0]
'Tim'
>>> adict['address'][1]
'xyx street'
>>> len(adict['data'])
4
>>> adict['data'][len(adict['data'])-1]
54
```

Dictionaries are particular good at finding data:

```
>>> pets = {'dog':'Fluffy', 'cat':'Whiskers', 'rabbit':'Fang'}
>>> pets
{'rabbit': 'Fang', 'dog': 'Fluffy', 'cat': 'Whiskers'}
>>> pets = dict(dog='Fluffy', cat='Whiskers', rabbit='Fang')
>>> pets
{'rabbit': 'Fang', 'dog': 'Fluffy', 'cat': 'Whiskers'}
>>> if 'rabbit' in pets:
...  print(pets['rabbit'])
...
Fang
```

NOTE: The lookup value in a dictionary must be unique

```
>>> pets = {'dog':'Fluffy', 'cat':'Whiskers', 'rabbit':'Fang', 'dog':'Killer'}
>>> pets
{'cat': 'Whiskers', 'rabbit': 'Fang', 'dog': 'Killer'}
```

#### Casting a tuple

Often we find ourselfs wishing to change a tuple we've already created. One way to accomplish this is to "cast" to tuple to a list value, and then recast it back to the tuple.

```python
>>> ctuple = (1000,1001,1002,1003)
>>> ctuple[0]=999 # because tuples data is protected, we will generate an error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> clist=list(ctuple) # cast to a list
>>> clist[0]
1000
>>> clist
[1000, 1001, 1002, 1003]
>>> clist[0]=999
>>> clist
[999, 1001, 1002, 1003]
>>> ctuple=tuple(clist) # cast back to a tuple
>>> ctuple
(999, 1001, 1002, 1003)
>>>
```

## Collections

Collections are a rather new data type (introduced in later 2 version of Python). These "advanced" data types include Chainmap, Counter, deque (Double ended Queue), defaultdict, namedtuple, OrderedDict, UserDict, UserList, Userstring. These can be thought of as more specific extensions of the Tuple, List, and Dictionary types covered above. For certain things we might do with a one of these other data types, Collections will be much quicker to code and will run much faster (for instance, see Counter objects)

I'd encourage you to familiarize yourself with these: so that you can think, "hmm, what I'm doing with this tuple might be more efficiently handled using a Counter object" or other similar thoughts)

See: https://docs.python.org/3/library/collections.html


## Operators

### The 'in' Python Operator

One interesting example of using tuples is to utilize the "in" operator in Python

```python
>>> btuple  # we defined this in the above tuple examples
('Prof.', 'Tim', 'Smith', 2039)
>>> 'Tim' in btuple
True
>>> 'tim' in btuple
False
>>> 2039 in btuple
True
>>>
```

And, as you'd expect, you can also do this with lists (only the code will run slower)

```python
>>> blist  # we defined this in the above tuple examples
('Prof.', 'Tim', 'Smith', 2039)
>>> 'Tim' in blist
True
>>> 'tim' in blist
False
>>> 2039 in blist
True
>>>
```

You can also use the "not in" form as well:

```python
>>> btuple  # we defined this in the above tuple examples
('Prof.', 'Tim', 'Smith', 2039)
>>> 'Tim' not in btuple
False
>>> 'tim' not in btuple
True
>>> 2039 not in btuple
False
>>>
```

### Other operators in Python

'in' and 'not in' are two of the many operators you can find in Python. You should be familiar with many of these from your Java classes. Review this [link](http://www.tutorialspoint.com/python/python_basic_operators.htm) for a description of the Python operators.

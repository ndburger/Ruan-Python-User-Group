# W02c06: Basic Python Syntax


1. [Two Modes of Programming](#two-modes-of-programming)
    * Interactive
    * Scripting
2. [Getting Help](#getting-help)
    * dir(), type() and help()
3. [Indentation and Blocking](#indentation-and-blocking)
    * Python suites
4. [Python variable naming rules (Identifiers)](#python-variable-naming-rules)
5. [Multi-Line Statements](#multi-line-statements)
6. [Quotation in Python](#quotation-in-python)
7. [Comments (and Docstrings)](#commenting)
8. [Printing to screen](#printing-to-screen)
9. [Python's range() function](#range-function)
10. [Getting command line Input](#getting-command-line-Input)
    * Args
    * Input
11. [Exception Handling](#exception-handling)

## Two Modes of Programming

As we discussed in last class, there are two general modes, or approaches to programming in Python. The first involves entering code directly, line-by-line, into the interpreter. This can be a quick and convenient way to test out ideas. The second way is by creating a script. In this second approach, you use a text editor to create a text file that contains your python code (see last lecture for more detail on invoking the Python interpreter. NOTE: Remember, if running Python from the Bash command line in Windows, you may need to start it using winpty)


## Getting Help

There are three handy functions in Python that you should be in the habit of using. The first is dir(), the second type(), and the third is help().

We discussed dir() in the previous class. This function will return a list of names in the namespace given. If no input is given, then it will list all the names (variable identifiers) currently in the current namespace. If we give it a function, class, of class object it will return with the namespace content of the object given.

Here are some examples:
```
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>>
```

```
>>> dir(requests)
['ConnectTimeout', 'ConnectionError', 'DependencyWarning', 'FileModeWarning', 'HTTPError', 'NullHandler', 'PreparedRequest', 'ReadTimeout', 'Request', 'RequestException
', 'Response', 'Session', 'Timeout', 'TooManyRedirects', 'URLRequired', '__author__', '__build__', '__builtins__', '__cached__', '__copyright__', '__doc__', '__file__',
 '__license__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__title__', '__version__', 'adapters', 'api', 'auth', 'certs', 'codes', 'compat', 'coo
kies', 'delete', 'exceptions', 'get', 'head', 'hooks', 'logging', 'models', 'options', 'packages', 'patch', 'post', 'put', 'request', 'session', 'sessions', 'status_cod
es', 'structures', 'utils', 'warnings']
>>>
```

Now, help provides some information on the object of interest. Taking a look at your previous dir() examples, let's look at the options identifier found in the requests package:

```
>>> dir(requests.options)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__
', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__',
'__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```

If we want to know the type of an identifier.
```
>>> x = 9
>>> y = 8.8
>>> type(x)
<class 'int'>
>>> type(y)
<class 'float'>
>>> type(requests.options.__sizeof__)
<class 'builtin_function_or_method'>
```

Finally, we can use help() to extract the docstring for the given function, and obtain some indication/documentation on how to use it.

NOTE: We'll discuss docstring's later when we review functions, for now, know that the programmer should include these to describe what the function does.

```
>>> help(requests.options.__sizeof__)
Help on built-in function __sizeof__:

__sizeof__(...) method of builtins.function instance
    __sizeof__() -> int
    size of object in memory, in bytes
```

## Indentation and Blocking

As we mentioned in class 4, in Python whitespaces often matter. Indentation, though a stylistic element in many languages, indicates code blocks in Python -- much the same as curly brackets do in Java

## Python variable naming rules

* Variables names must start with a letter or an underscore, such as: `_underscore. underscore_`
* The remainder of your variable name may consist of letters, numbers and underscores. password1. n00b. ...
* Names are case sensitive. case_sensitive, CASE_SENSITIVE, and Case_Sensitive are each a different variable.

## Multi-Line Statements

In Python, we do not need to add a semicolon at the end of statements. As we write a new line, the terminal is implied.

```Python
a = 1
b = 2
c = 3
```

The only time we need to end our statements with a semicolon are when we need to write multiple statements per line
```Python
a=1; b=2; c=3
```

We can also have instances where a statement can space multiple lines. There are two general situations where this occurs: 1) implicit line continuation, and 2) explicit line continuation.

### Explicit line continuation

We use the backslash to signal that our statement continues to the next line

```Python
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
```

### Implicit line continuation

Often though, there are an implied continuation of the statement on the next line. This occurs within blocks indicates by () [] and  {}.
```Python
a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)
names = ['Jill',
          'Brenda',
          'Julie']
```

## Quotation in Python

In Python we can use single, double, or triple quotes to indicate string literals. Single and double quotes operate much the same as in Java and other languages. Triple quotes (either single or double) represent a multi-line block of text.

```Python
name1 = 'Vickie' # correct
name2 = "Sally' # ERROR
name3 = "Anne" # correct

saying1 = "It's a beautiful day in my neighborhood" # correct
saying1 = 'It's a beautiful day in my neighborhood"' # ERROR

long_text1 = ```To be or not to be-that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And, by opposing, end them. To die, to sleep-
No more-and by a sleep to say we end``` # ERROR

>>>long_text2 = """To be or not to be-that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And, by opposing, end them. To die, to sleep-
No more-and by a sleep to say we end""" # CORRECT
```
## Commenting

Python only has a single line comment. It is designated using the # symbol.

```
# this is a comment
print("say something") # this is another comment
# This
# is
# a
# multi-line comment
```

## Printing to screen

There is no distinction between println and print. In Python the print statement behaves like Java's println() function.

```Python
print("Hello")
print("These strings all print on their own line")
```

We can, however, create the equivalent of Java's print() function:
```Python
print("Hello", end="")
```

## String formatters

Python has advanced string formatter functionality.


The old way of formatting string literals (still works in Python, but the .format() approach is now preferred and more feature rich)
```
>>> x = '%s %s' % ('one', 'two')
>>> x
'one two'
```

The new .format() way of forming string literals is now preferred
```
>>> x = '{} {}'.format('one', 'two')
>>> x
'one two'
>>>
>>> x = '{first} {last}'.format(last='Jones', first='Bob')
>>> x
'Bob Jones'
>>>
```

See more examples here  https://pyformat.info/

## Range function

NOTE: THis section is adapted from http://pythoncentral.io/pythons-range-function-explained/

Pythons range()function generates a list, or sequence, of numbers. It's most often used to find the range for a for loop.

The range() function has two sets of parameters, as follows:

* range(stop)
  * stop: Number of integers (whole numbers) to generate, starting from zero. eg. range(3) == [0, 1, 2].
* range([start], stop[, step])
  * start: Starting number of the sequence.
  * stop: Generate numbers up to, but not including this number.
  * step: Difference between each number in the sequence.

Rules:
* All parameters must be integers.
* All parameters can be positive or negative.
* range() (and Python in general) is 0-index based, meaning list indexes start at 0, not 1. eg. The syntax to access the first element of a list is mylist[0]. Therefore the last integer generated by range() is up to, but not including, stop. For example range(0, 5) generates integers from 0 up to, but not including, 5.

```
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
>>> for i in range(10, 12):
...     print(i)
...
10
11
>>> for i in range(3, 15, 3):
...     print(i)
...
3
6
9
12
>>> for i in range(0, -6, -2):
...     print(i)
...
0
-2
-4
```
## Getting Input

### Command line Input
Command line input is a way to get user input, or provide a programmatic interface for other programs to interact with yours.

Create a program with the following code
```Python
import sys
print(sys.argv)
```

And then run it from the command line as follows:
```Python
$ python myprog.py first second third
['myprog.py', 'first', 'second', 'third']
```

Now, I can access these arguments as follows
```Python
import sys
print(sys.argv)
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
```

And, now when I run the program again
```
$ python myprog.py first second third
['myprog.py', 'first', 'second', 'third']
myprog.py
first
second
third
```

Let me further this by showing you what happens when to attempt to read more arguments that were given by the user.

```Python
import sys
print(sys.argv)
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(sys.argv[4])
```

When we save and run this new script, we get the following:
```Python
import sys
print(sys.argv)
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(sys.argv[4])
```

And, now when we run the program, we get an error:
```Python
$ python myprog.py first second third
['myprog.py', 'first', 'second', 'third']
myprog.py
first
second
third
Traceback (most recent call last):
  File "myprog.py", line 7, in <module>
    print(sys.argv[4])
IndexError: list index out of range
```

You should always protect your programs from users not using your system correctly. In this case, we need to add better logic surrounding how many arguments we will read.

```Python
import sys
for i in range(0, len(sys.argv)):
    print(sys.argv[i])
```

#### NOTE:

Refer back to the help section in the document. You can use the command type(sys.argv) to find that this is a list. You can access the elements of a list with the [] notation. List indices start at 0. Therefore, if you have a list X of length three, there are three items accessible via X[0], X[1], X[2]. Trying to access X[3] would be a mistake, as it would be off the end of the list, and generate an error.


### Console Input
This is accomplished using the input command:

```Python
name = input('Enter your name: ')
print('Hello', name )
```

To enter numbers, you need to convert these (or cast)
```Python
x = int(input("Enter a number: "))
y = int(input("Enter a second number: "))
print('The sum of ', x, ' and ', y, ' is ', x+y, '.', sep='')
```

## Exception Handling

```Python
try:
# Division by zero raises an exception
    10 / 0
except ZeroDivisionError:
    print("Tried to divide by zero!")
else:
    # Exception didn't occur, we're good.
    pass
finally:
    # This is executed after the code block is run
    # and all exceptions have been handled, even
    # if a new exception is raised while handling.
    print("We've now handled that!")
```

See https://docs.python.org/3/tutorial/errors.html for more information on exception handling.

# w05c13 - Functions in Python

A function is a block of reusable code performs a task. Functions provide better modularity for your application and a high degree of code reusing.

The advantages of using functions are:
  1. Reducing duplication of code
  2. Decomposing complex problems into simpler pieces (but don't go overboard)
  3. Improving readability of the code (see second item comment about going overboard)

As we have seen already, Python gives us many built-in functions:
* See the extensive list of functions available in Python 3.5.2 [here](https://docs.python.org/3/library/functions.html).

> In computer science, a programming language is said to have first-class functions if it treats functions as first-class citizens. Specifically, this means the language supports passing functions as arguments to other functions, returning them as the values from other functions, and assigning them to variables or storing them in data structures.[1] Some programming language theorists require support for anonymous functions (function literals) as well.[2] In languages with first-class functions, the names of functions do not have any special status; they are treated like ordinary variables with a function type.[3] The term was coined by Christopher Strachey in the context of "functions as first-class citizens" in the mid-1960s.[4] (taken from [here](https://en.wikipedia.org/wiki/First-class_function))

Based on their first class status, as we have seen previously, functions can be assigned to variables, stored in collections and passed as arguments. The results in providing Python with new/additional flexibility over many other languages, and allows us to utilize concepts such as closures, decorators, and other modern language constructs.

## Defining functions

As we have seen already, a function is created with the def keyword. Unlike languages like Java, or C/C++, the indication of a block of code belonging to a function is through indentation.

```python
def function():
    pass
```

__NOTE__: We covered the pass statement before, but as a reminder, it is a statement that does nothing. It's used as a placeholder where syntactically it is necessary to have a statement.

The def keyword is followed by the function name with parentheses followed by a colon.

The function is later "called" when needed. The statements inside a function are not executed until the function is called.

To call a function, we specify the function name along with parentheses/round brackets.

```python
"""Fun01.py demonstration of functions."""


def display_curr_docstring():
    return(__doc__)


def display_curr_module_filename():
    return(__file__)


def display_curr_module_name():
    return(__name__)

s1 = display_curr_docstring()
s2 = display_curr_module_filename()
s3 = display_curr_module_name()

print(s1, s2, s3, dir(), sep="\n")
```
<center><sub>[^click here for code^](fun01.py)</sub></center>
<br>
<br>

### Functions and a revisit of Modules

As we have discussed previously, all python code exists within a module. Non-trivial Python programs are a collection of modules calling modules, with the first module being called ```__main__```.

We can call any python script by simply importing. For instance, if we have a module called mymodule.py that contains the following code:

```python
"""This is the docstring associated with mymodule.


If I call help(mymodule) the docstring found at the beginning of the file is
displayed. Convention is to include a brief description of the module in the
docstring.

This module contains two variables (var1 and var2), one function (fun1), and
one line of code (a print statement) that will be run as soon as the module
is first imported.
"""

var1 = 10
var2 = "Some string"


def fun1():
    """This is a docstring that describes fun1()."""
    return("Hello from fun1")

print("This print statement is not in a function, therefore, is run when the module is first imported.")

```
<center><sub>[^click here for code^](mymodule.py)</sub></center>
<br>
<br>

We can load this module into the current running module by importing it.

```python
"""Function and module demonstration."""

import mymodule

print(mymodule.var1, mymodule.var2, mymodule.fun1(), sep="\n")
print(help(mymodule))
print(help(mymodule.fun1))
```
<center><sub>[^click here for code^](fun02.py)</sub></center>
<br>
<br>


If we run fun02.py, we get the following output:

```
python fun02.py
This print statement is not in a function, therefore, is run when the module is first imported.
10
Some string
Hello from fun1
Help on module mymodule:

NAME
    mymodule - This is the docstring associated with mymodule.

DESCRIPTION

    If I call help(mymodule) the docstring found at the beginning of the file is
    displayed. Convention is to include a brief description of the module in the
    docstring.

    This module contains two variables (var1 and var2), one function (fun1), and
    one line of code (a print statement) that will be run as soon as the module
    is first imported.

FUNCTIONS
    fun1()
        This is a docstring that describes fun1().

DATA
    var1 = 10
    var2 = 'Some string'

FILE
    c:\users\timsmith\dropbox\___iastate\mis407\_f16_mis407_repos\class-notes-and-admin\classes\w05c13\mymodule.py


None
Help on function fun1 in module mymodule:

fun1()
    This is a docstring that describes fun1().
```

## Function definition and calling

Calling a function before it is defined will cause an error:

```python
f2()  # will generate error

def f2():
    print "f2()"
```
<center><sub>[^click here for code^](fun03.py)</sub></center>
<br>
<br>

We only call a function after it has been defined.

A we have seen before, function names are object names, and can be reassigned or passed around like any other variable.

## Again, functions are objects

Since functions are objects, as we'd expect from an object, there will be exposed methods.

```python
"""This is another function demonstration, fun04."""


def f():
    """This function simply prints a message. """
    print("This is MIS407.")

print(isinstance(f, object))  # is this an instance of an object

print(id(f))  # like we've seen before, name of objects are simply ID/pointers

print(f.__doc__)  # print the docstring for the function
print(f.__name__)  # print the name of the function
```
<center><sub>[^click here for code^](fun04.py)</sub></center>
<br>
<br>

When we run this script, we get the following output:

```
$ python fun04.py
True
2219357497272
This function simply prints a message.
f
```

Objects can be stored in collections and passed to functions.


```python
"""This is the fun05.py docstring."""


def f():
    print("Hello from f()")

def g():
    print("Hello from g()")

def h():
    print("Hello from h()")


a = (f, g, h)

for i in a:
    i
    i()
```
<center><sub>[^click here for code^](fun05.py)</sub></center>
<br>
<br>

When we run this script, we get the following output:

```
python fun05.py
<function f at 0x0000026E5F28E840>
Hello from f()
<function g at 0x0000026E5F28E8C8>
Hello from g()
<function h at 0x0000026E5F28E950>
Hello from h()
```

Here is an example of creating a switch like statement using a dictionary:

```python
from sys import argv

def a():
    return("Alpha")
def b():
    return("Beta")
def c():
    return("Gamma")
def d():
    return("Delta")
def unkown():
    return("ERROR")

switcher = { 'A': a, 'a': a, 'B': b, 'b': b, 'C': c, 'c': c, 'D': d, 'd': d}

s = ''
for i in range(1, len(argv)):
    s = s + switcher.get(argv[i], unkown)() + ","
    if i == len(argv)-1:
        s = s[:-1]
print(s)
```
<center><sub>[^click here for code^](fun06.py)</sub></center>
<br>
<br>

__NOTE__: "live in-class only view" of an example using dictionary as a switch

### Closures, revisit

__NOTE__: "live in-class only view" of an example IA03 solution


### Multiple values

We can sent and receive more than one value to and from a function. The objects after the return keyword are separated by commas.

```python
x = [1, 2, 3, 4, 5]

def var_summary(x):
    maxx = max(x)
    minx = min(x)
    n = len(x)
    sum_x = sum(x)
    avg = sum_x / n
    deviations = [(a - avg)**2 for a in x]
    variation = sum(deviations)/n
    std_deviation = variation ** .5
    return({'max': maxx, 'min': minx, 'n': n, 'sum': sum_x,
            'avg': avg, 'variance': variation, 'stdev': std_deviation})


def zscore(avg, stdev, x):
    return((x-avg)/stdev)

summary = var_summary(x)
print(summary)
print("zscore x1 = ", zscore(summary['avg'], summary['stdev'], x[0]))
print("zscore x2 = ", zscore(summary['avg'], summary['stdev'], x[1]))
print("zscore x3 = ", zscore(summary['avg'], summary['stdev'], x[2]))
print("zscore x4 = ", zscore(summary['avg'], summary['stdev'], x[3]))
print("zscore x5 = ", zscore(summary['avg'], summary['stdev'], x[4]))
```
<center><sub>[^click here for code^](fun07.py)</sub></center>
<br>
<br>

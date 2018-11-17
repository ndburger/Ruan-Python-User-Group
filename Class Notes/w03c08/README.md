# W03c08: Data Types

__TOC W03c08__:


<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [W03c08: Data Types](#w03c08-data-types)
	- [Objects, values and types](#objects-values-and-types)
	- [Naming and Assigning Variables](#naming-and-assigning-variables)
		- [Names without an object](#names-without-an-object)
		- [Garbage collection](#garbage-collection)
	- [Nested Functions](#nested-functions)
		- [Closures](#closures)
	- [Namespace & Scoping: Redux](#namespace-scoping-redux)
		- [Modules, Scoping and namespaces](#modules-scoping-and-namespaces)
			- [Scoping examples](#scoping-examples)
			- [Python's Global Statement](#pythons-global-statement)
			- [Global and nonlocal](#global-and-nonlocal)
		- [Scoping and Namespaces](#scoping-and-namespaces)

<!-- /TOC -->
## Objects, values and types

Objects are Python’s abstract representation for data. All data in a Python program are represented by objects or by relations between objects. Objects apply structure to data through typing of the data.

Every object has an identity, a type, and associated data (value(s)).

## Naming and Assigning Variables

Generally, in Python there is no "variable declaration" or "variable initialization", rather, there is "assignment", which is a process we simply call "naming".

Let's create a name called var:

```python
>>> var = 5
>>> var
5
```

>__SIDEBAR__: Multiple assignment
* In Python, we can assign multiple variables at a time:

```python
>>> x, y = 10, 20
>>> x
10
>>> y
20
>>> x, y
(10, 20)
>>> x, y = y, x
>>> x, y
(20, 10)
>>>
```

The process of "naming", therefore, provides us with a means to refer to a specific object. The "name" allows us to access things such as an attribute of the object or method offered to us by the object through the objects interface; but keep in mind that the name is not the object itself.

Names' don't have associated types, but rather their associated objects do. Under this approach, the rules of Python allow us to simply apply a new name to a variable (object) or to reuse a name for a new variable (object).

```python
>>> Var = 6
>>> Var
6
>>> Var = 3.14
>>> Var
3.14
>>> Var = "I love Py"
>>> Var
'I love Pi'
>>>
```

An object’s identity never changes once it has been created; you may think of it as the object’s address in memory. But the naming of the object is not the object itself, it is simply a mapping between a name and the objects ID.

> __Sidebar__: We'll cover operators in more detail later, but now is a good time to introduce the ‘is‘ operator. The 'is' operator compares the identity of two objects; the id() function returns an integer representing its identity. The 'in' operator provides us a convenient means to ask "does ID(obj1) == id(obj2)?"

```python
>>> x = 10
>>> y = "Hello"
>>> id(x)
1353406880
>>> id(y)
24841440
>>> x = 20
>>> y = "Goodbye"
>>> id(x)
1353407040
>>> id(y)
24840672
>>> x is y
False
>>> x = y
>>> x
'Goodbye'
>>> y
'Goodbye'
>>> id(x)
24840672
>>> id(y)
24840672
>>> x is y
True
>>>
```

### Names without an object

Technically, a name exists because of an associated object. There are times though that we may wish to signify that a name doesn't have a value (in other words, no associated object). In such cases we can use a special object class called None.

```
>>> x=10
>>> x
10
>>> x = None
>>> x  # notice how 'nothing' shows?
>>> print(x)
None
>>> x = 10
>>> print(x)
10
>>>
```

### Garbage collection

Once a variable "looses it's name" (becomes unreferenced) it's cleaned up in the background by Python's garbage collection process, and once this occurs the variable ceases to exist. The specific details surrounding how the Python interpreter handles garbage collection can vary across different implementation of Python (FYI we're using CPython), but on the "surface", all implementations should all behave the same as far as the programmer is concerned.

There are times though that we may wish to represent something as an unnamed variable. It is conventional to do this using the underscore character:

```python
for _ in range(5)
  pass
```

>NOTE: We discussed range in the last class (and I provided more notes on this post-class). Since we often use the form rang(0,x), Python assumes a 0 start when we enter range(x) - so  range(x) is the same as range(0,x) .

To further illustrate that a name can be assigned to any Python object, let's look at how we can also associate an existing name with a function object (yes, functions are object too).

```python
>>> def f():
...  print("Hello from function f!")
...
>>> x = 10
>>> x
10
>>> x = 3.14
>>> x
3.14
>>> x = f
>>> x
<function f at 0x0000022F162E9048>
>>> x()
Hello from function f!
```

## Nested Functions

Python's flexibility in naming and scope management creates many interesting opportunities for more advanced structures. As a "teaser", look at the following code. Since names are simply associations with an object (and in Python a function is simply an object) we can create a function within a function (aka "nested function", and return this function to the caller.

```python
def f():
    def g():
        return("Hello from g")
    return(g)
myfun = f()
yourfun = f()
print(myfun(), '\n', yourfun(), sep='')
```

### Closures

The last example is interesting, but frankly, a little boring. Each function we create does exactly the same thing. Where this feature of Python become much more powerful with nested functions is when we "program" the creation of different functions based on run time conditions. For example, the following code generates a function based on the parameters you give it. Think about it as "meta programming", that is, you're using Python to generate code for you based on the logic you provide.

```python
def f(x):
    def g():
        print(x)
    return(g)

fnc = f(2)
fnc()
fnc = f(100)
fnc()
```
The output of which is:
```
$ python function_generator1.py
2
100
```

Now, here's where some of the really interesting opportunities of this concept come to fruition. In this case, we can create a function that generates power functions of any degree that we'd like:

```python
def f(x):
    def g(y):
        return(y**x)
    return(g)
sqr = f(2)
print(sqr(3))
sqrt = f(1/2)
print(sqrt(9))
cube = f(3)
print(cube(3))
cubert = f(1/3)
print(cubert(27))
```

This produces the following output.

```
$ python nested_functions3.py
9
3.0
27
3.0
```
> __SIDEBAR__: The last two examples illustrate a specific type of nested function called a "closure". We will cover this concept (and the related concept of decorators) next week when we discuss functions in greater detail

## Namespace & Scoping: Redux

We've already took a preliminary look at namespaces in w02c04. Let's dig a little deeper into this important concept.

Namespaces are the space in which names are stored. As we create new names, these names are added to our namespace. Any non-trivial program will have multiple namespaces. Python "scoping" rules help us implicitly organize namespaces. Namespaces are simply dictionaries of name object pairs; and a namespace is either in, or out of, scope. Scope is the current active namespace. Scoping is the process of managing and switching between these namespace contexts. Generally, namespaces can be accessed even when they are not in scope. This is accomplish being providing the name of the namespace as a qualifier, such as with modules.

### Modules, Scoping and namespaces

We covered off the basic structure of a package and modules in w02c04 (please refer to the example from this class)

As we discussed, all Python files are modules. Any non-trivial Python program will start with a call to one module, but will most likely include other modules which in turn may call other modules.

We import a module using the import statement.

```
import somemodule # this "imports" somemodule.py code (located in the current directory) to be used within the current modules namespace.

dir(somemodule) # using the dir() function we can query the lost of names available in the imported modules global namespace.

somemodule.somefunction() # we can call functions found within the module using this format.

```

We can also import as

```
import somemodule as sm # this "imports" somemodule.py code (located in the current directory) to be used within the current modules namespace and renames the module sm.

dir(sm) # using the dir() function we can query the lost of names available in the imported modules global namespace.

sm.somefunction() # we can call functions found within the module using this format.

```

We can also import functions from the module into our current namespace


```
from somemodule import somefunction1, somefunction2

somefunction1()
somefunction2()
# Notice that since we have imported the functions into our current namespace (using the from/import command combination) we don't need to include the module name,

```
__NOTE:__ For more information on modules, please review  https://docs.python.org/3/tutorial/modules.html

#### Scoping examples

```python
def outer_function():
    a = 20
    def inner_function():
        a = 30
        print('a =',a)

    inner_function()
    print('a =',a)
a = 10
outer_function()
print('a =',a)
```

The output from this snippet of code is:
```
a = 30
a = 20
a = 10
```

#### Python's Global Statement

"The global statement is a declaration which holds for the entire current code block. It means that the listed identifiers are to be interpreted as globals. It would be impossible to assign to a global variable without global, although free variables may refer to globals without being declared global."" (taken from https://docs.python.org/3/reference/simple_stmts.html)

Now let's look at this example.

```python
def outer_function():
    global a
    a = 20
    def inner_function():
        global a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)
a = 10
outer_function()
print('a =', a)
```

Can you guess the output from the above code? Here is what it is?

output is...
```
$ python scoping2.py
a = 30
a = 30
a = 30
```


Note: The following will produce and error. The inner_function nonlocal call will attempt to alter the outer function name "a", but this outer fucntion doesn't really have the name a, rather it too is attempting to alter it's enclosing namespace (the global environment). Nonelocal's do not chain well, in this case the first nonlocal reference will generate an error.

```python
def outer_function():
    nonlocal a
    a = 20
    def inner_function():
        nonlocal a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)
a = 10
outer_function()
print('a =', a)
```

As we can see from the code below, we can eliminate this error if the outer_function namepace has an actual "a" name (id).
```python
def outer_function():
    nonlocal a
    a = 20
    def inner_function():
        nonlocal a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)
a = 10
outer_function()
print('a =', a)
```

#### Global and nonlocal

EX1: Error: Nested namespaces are, by default, hidden from global namespaces

```python
def f():
    somestr = "locally defined"  # Defined only in local context, or "namespace"
    print(somestr)
f()
print(somestr) # Error: Asking for a variable in the current namespace (global) that isn't here
```

Running this above code will produce an error:

```python
>>> print(somestr)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'somestr' is not defined

```
Ex2: The global command allows nested namespaces to access and manipulate values in global namespaces

```python
def f():
    global somestr
    somestr = "locally defined"  # Defined only in local context, or "namespace"
    print(somestr)
f()
print(somestr) # No error: Asking for a variable in the current namespace (global) that IS here
```

The ex2 code will run without error.

```python
>>> print(somestr)
locally defined
```

### Scoping and Namespaces

Namespaces are simply dictionaries of name object pairs. The define the association between these names and objects within a given scope. As we have seen (w02c06) we can query the contents of a names space using the dir() function.

```python
def f ():
    a = 10
    print("## Namespace inside our function:")
    print(dir())
    print("## And the value of a inside our function? a=",a)

print("## Calling function...")
f()
print("## ...we're back from the function call.")
a = 20
print("## Namespace inside our program (aka: the global namespace):")
print(dir())
print("## And, finally, what is the value of a? a=",a)
```

Namespaces, in the example above, can be thought of as nested. The namespace within our function f is 'nested' within the global namespace of our program.

There are often times when we need to explicitly reference a global name... a name that existing in the encapsulating namespace (the namespace within which the current namespace is generated). We saw the use of this in class w02c05.

Some simple examples (using Python command line interface) to illustrate:

```python
>>> def f():
...  a = 10
...  print(a)
...
>>> a = 12
>>> f()
10
```

Nothing unusual about this last one, look at this one. Note that since our function f() doesn't return a value, print() will display None for the return value from the function, but the function will also print a value 10 as part of it's execution.

```python
>>> def f():
...  a = 10
...  print(a)
...
>>> a = 12
>>> print(f())
10
None
```

Here, we notice how the print function will call any functions first before it begins to print:
```python
>>> def f():
...  a = 20
...  print(a)
...
>>> a = 12
>>> print(a + f())
20
12 None
```

Now, we use the global command to specify within the function that the local a name used is really part of the global environment in which the function is called:
```python
>>> def f():
...  global a
...  a = 20
...  print(a)
...
>>> a = 12
>>> print(a, f())
20
12 None
```

Finally, to show how the global command works, we find that our a = 12 has been overwritten by the function f() assignmnet. This is because a is declared global within this function, and thus, any use of the variable will be essentially altering the same variable held within the global environment from which the function is called.

```python
>>> def f():
...  global a
...  a = 20
...  print(a)
...
>>> a = 12
>>> f()
20
>>> print(a)
20
>>>
```


>Sidebar: As we mentioned, namespaces are implemented in Python using the dictionary data type. This is one of the example of Python's more complex built-in datatypes which we cover in a section below.

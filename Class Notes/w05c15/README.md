# w05c14: More on functions

Agenda
* Review of IA0A5 (and IA04 stats)
* Continue our discussion of Functions and related concepts in Python
  * Passing arguments
     * Mutable and immutable
     * Shallow and deep copy
  * Recursion
  * overloading
  * List comprehensions
  * Function decorators

## Passing arguments

All parameters (arguments) passed to functions in Python are passed by reference. This results in any changes made to a parameter within a function, also reflect back in the namespace in the calling function.

```python
def theChanger (blist) :
    blist.append(2)
    blist.append(1)
    return

alist = [1,2,3]
theChanger(alist)
print(alist)
```

Now, what do you think will be the output from the following?

```python
def theChanger (blist) :
    blist = [3,2,1]
    return

alist = [1, 2, 3]
theChanger(alist)
print(alist)
```

Notice, in this case, our "change" to blist did not affect alist. Why is this? Well, we need to understand a bit more about mutable and immutable variables in Python. Lists are a mutable object, therefore that list object itself can be changed. But, we must also remember, changing the list is different than creating a new one. In the first example, we utilized a method of list to append data. List being a mutable, allows for this. But, in our second example, a "new" list object is created. The Parameter passing is by reference, so if we create a new object we are not changing the object that the parameter was referring too, rather we made the local name blist point to a new object. Our alist variable continues to point to the origin object, which is unchanged.

(note: the following discussion on Mutable Default Arguments was taking from http://docs.python-guide.org/en/latest/writing/gotchas/)

## Mutable Default Arguments

Seemingly the most common surprise new Python programmers encounter is Python’s treatment of mutable default arguments in function definitions.

...What You Wrote

```python
def append_to(element, to=[]):
    to.append(element)
    return to
```

What You Might Have Expected to Happen

```python
my_list = append_to(12)
print my_list

my_other_list = append_to(42)
print my_other_list
```

A new list is created each time the function is called if a argument isn’t provided, so that the output is:
```
[12]
[42]
```
What Does Happen
```
[12]
[12, 42]
```
__A new list is created once when the function is defined, and the same list is used in each successive call.__

__Python’s default arguments are evaluated once when the function is defined, not each time the function is called__ (like it is in say, Ruby). This means that if you use a mutable default argument and mutate it, you will and have mutated that object for all future calls to the function as well.
What You Should Do Instead

Create a new object each time the function is called, by using a default arg to signal that no argument was provided (None is often a good choice).

```python
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to
```
When the Gotcha Isn’t a Gotcha

Sometimes you can specifically “exploit” (read: use as intended) this behavior to maintain state between calls of a function. This is often done when writing a caching function.


## Mutable and immutable - and revisit of the Python approach to naming variables

In languages such as C/C++, you have two general ways in which arguments are treated -- pass by value (where the value is copied to the local scope of the function) and pass by reference (where the value is not a value, but rather a pointer to a value... thus, any changes made within the function using this pointer will be reflected in the value to which it points to)

Python uses a __pass by object__ mechanism; where such objects are either mutable, or non-mutable. Those objects that are non-mutable (i.e. integers, strings, tuples) will be passed by value, while mutable objects (such as lists) will be passed by reference.

![Mutables in Python](images/mutables.png)

### Side effects

#### No side effects...

```python
>>> def func1(list):
...     print list
...     list = [47,11]
...     print list
...
>>> fib = [0,1,1,2,3,5,8]
>>> func1(fib)
[0, 1, 1, 2, 3, 5, 8]
[47, 11]
>>> print fib
[0, 1, 1, 2, 3, 5, 8]
>>>
```
Though we may have "passed by reference", or statement list=[47,11] has created a new list object - an object that is local to the functions namespace, and thus no change to the list in the calling namespace is made.


#### Has side-effects...

```python
>>> def func2(list):
...     print list
...     list += [47,11]
...     print list
...
>>> fib = [0,1,1,2,3,5,8]
>>> func2(fib)
[0, 1, 1, 2, 3, 5, 8]
[0, 1, 1, 2, 3, 5, 8, 47, 11]
>>> print fib
[0, 1, 1, 2, 3, 5, 8, 47, 11]
>>>
```
In this second case, we haven't created a new list within the function. Using the statement list += [47,11] we have altered the existing list, and thus not "triggered" the creation of a new list.

#### Avoiding side-effects

```python
>>> def func2(list):
...     print list
...     list += [47,11]
...     print list
...
>>> fib = [0,1,1,2,3,5,8]
>>> func2(fib[:])
[0, 1, 1, 2, 3, 5, 8]
[0, 1, 1, 2, 3, 5, 8, 47, 11]
>>> print fib
[0, 1, 1, 2, 3, 5, 8]
>>>
```
In the example above, by using the form fib[:], we have passed a reference to a copy (new) list - thus, protecting the existing list in the calling namespace.

> NOTE: Great resource on this is here [http://www.python-course.eu/passing_arguments.php](http://www.python-course.eu/passing_arguments.php). The above two examples were taken from this site.

> NOTE: Review the following webpage for a review (and different look) at the concepts we've covered when discussing names and namespaces in past lectures - http://www.python-course.eu/python3_deep_copy.php

### Arbitrary number of parameters

In C/C++ we have the varargs feature, in Python we use an asterisk based notation.

The * notation simply allows for a list of arguments to be passed, literally... the variable number of arguments provided will be turned into a list.

```python
>>> def f(*x):
...  print(x)
...
>>> f(12, 123.4, "Hello", "MIS407")
(12, 123.4, 'Hello', 'MIS407')
```

```python
>>> def f(*x):
...  print(x[0])
...
>>> f(12, 123.4, "Hello", "MIS407")
12
```

```python
>>> def f(*x):
...  for i in range(len(x)):
...   print(x[i])
...
>>> f(12, 123.4, "Hello", "MIS407")
12
123.4
Hello
MIS407
```

Also, what is rather unique about Python, is we can use this asterisk notation in reverse:

```python
>>> def f(x, y, z):
...  print(x, y, z)
...
>>> l = (10, "Hello", 12.3)
>>> f(*l)
10 Hello 12.3
```

Finally,  using the ** we also have the means of sending an arbitrary number of keyword parameters (note: like the * argument acts like a list, the ** acts like a dictionary):

```python
>>> def f(**x):
...  print(x)
...
>>> f(a=10, b="Hello", c=12.3)
{'b': 'Hello', 'a': 10, 'c': 12.3}
```

### Overloading??

You can't have two methods with the same name in Python, and in Python you don't need to anyways.

Python does not support overloading (but discuss alternatives that are "Pythonic"), but since it's dynamically types and supports optional arguments, we can do the same thing using the following approach:

```python
>>> def f(x, y=None):
...  if y==None:
...    print("do some x function stuff")
...  else:
...    print("do some x y function stuff")
...
>>> f(10)
do some x function stuff
>>> f(10, 12)
do some x y function stuff
```

## list comprehensions

From math, you're probably familiar with set notation (where some variable is in some set, and the set is defined as subset of the reals, or the whole numbers, etc.)

List comprehensions are a powerful means of taking this idea and bringing it to your programming. It is an example of what is found in "functional" programming languages.

```python
s1 = [x for x in range(10)]
s2 = [x**2 for x in range(10)]
s3 = [x for x in range(10) if x % 2 == 0]
print(s1)
print(s2)
print(s3)
```

The output of which will be...

```
$ python fun03.py
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
[0, 2, 4, 6, 8]
```

NOTE: For more examples on how we can use list comprehensions, take a look at the  demo code showing the standardization of universities.csv measures (see IA03 repo).

### List generators

In very simple terms... list generators create results similar to list comprehensions, but do so on as needed basis. If you know you want to look at data from a list (that you generate) multiple times or ways, you should use a list comprehension. A list comprehension creates the entire list, and stores in memory - thus allowing for rapid access and analysis of the set of data in the list.

I'll not cover generators in class. Please see here for more information (https://wiki.python.org/moin/Generators)

## Function decorators

Function decorators are simply wrappers around existing functions. This wrapping adds the functionality of the function in some way.

Let's say we have a function that prints text to the command line. We have no reason to change this function, it works fine, but we'd like it to output to a webpage.

```python
def print_x(x):
    return(x**2)

def html_decorate(func):
    def wrapper(x):
        return("<html><header></header><body><p>{0}</p></body></html>".format(func(x)))
    return wrapper

print_x_html = html_decorate(print_x)
print(print_x_html(10))
```
(see [fun04.py](fun04.py))


## Functional Programming

I'll not cover the complete "paradigm" of functional programming, but I encourage you to read the following. Companies analyzing large data sets will most like be using, or be interested in employing functional programming into their skillset. It's especially relevant to "big data" and technologies such as hadoop.


http://www.python-course.eu/python3_lambda.php

https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming

http://www.ibm.com/developerworks/library/l-prog/

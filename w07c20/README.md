# w07c19 OOP (there it is)

Python has been an object oriented language since it's inception. As we have discussed in past classes, everything in Python is an object. You've therefore, in a sense, already been OOP'ing in Python.

> Python’s class mechanism adds classes with a minimum of new syntax and semantics. It is a mixture of the class mechanisms found in C++ and Modula-3. Python classes provide all the standard features of Object Oriented Programming: the class inheritance mechanism allows multiple base classes, a derived class can override any methods of its base class or classes, and a method can call the method of a base class with the same name. Objects can contain arbitrary amounts and kinds of data. As is true for modules, classes partake of the dynamic nature of Python: they are created at runtime, and can be modified further after creation. (from [Python documentation](https://docs.python.org/2/tutorial/classes.html))

## Defining a class

A class is a data structure that consists of both variables (attributes) and functions (methods).

Like any data structure, it must be defined before using.

In Python, the class statement creates a new class definition. One we have defined a class, we can create instances of it. These instances are objects (objects are instances of classes).

```python
class ClassName:
   """Optional class documentation string"""
   <statement 1>
   ...
   <statement-N>
```

* This class has a documentation string, which can be accessed via ClassName.__doc__.

* The definition would then include a block (indicated by indentation, as is all blocks in Python) containing all class statements that define things such as class members, data attributes and methods.

For example, let's look a simple "Employee" class

```python
class Employee:
    """Common base class for all employees"""
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)
```

* The first method `__init__()` is a special method, which is called class constructor or initialization method that Python calls when you create a new instance of this class.

* You declare other class methods like normal functions with the exception that the first argument to each method is self. Python adds the self argument to the list for you; you do not need to include it when you call the methods.

* The self.name and self.salary statements initialize variables that belong to any instances of this class (object)

> NOTE: The use of "self". What's with the self parameter to the class methods? Each method we define in a class provides instructions for working with some abstract object - look at is as a template. To instantiate the template, we need some where to reference the specific instance of the object that is created through the instantiation process. This "self" parameter provides us the name through which we can access this specific instance.... what's this about instantiation? We'll now discuss this more...

## Instantiating a class

Instantiating a class is the process of creating an object from the class definition. To create instances of a class, you call the class using class name and pass in whatever arguments are required by the classes `__init__` method.

```python
# This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
emp1.displayEmployee()
# This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp2.displayEmployee()
```

When this code is executed, we get the following output:
```
Name :  Zara , Salary:  2000
Name :  Manni , Salary:  5000
```

# Classes can also have their own variables

Let's modify our employee class.

```python
class Employee:
    """Common base class for all employees"""
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)
```

* Note that we have added a new variable called empCount. EmpCount exists outside any method defintions, and is therefore a variable of the class.
* Class variables are shared by any instances of the class.

We can see how this works as follows:

```python
# This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
emp1.displayCount()
emp1.displayEmployee()
# This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp2.displayCount()
emp2.displayEmployee()
```

When this code is executed, we get the following output:
```
Total Employee 1
Name :  Zara , Salary:  2000
Total Employee 2
Name :  Manni , Salary:  5000
```

### Accessing an Objects Attributes

An instance of a class is called an object. All the methods and variables inside this object are refered to at attributed of the object.

You access the object's attributes using the dot operator with object.

```python
print(emp1.name)
print(emp1.salary)
```

Class variable belong to all instances of the class (all the objects we create from it). We can access a class variable through using the class name.

```python
print("Total Employee %d" % Employee.empCount)
```

## Built-in Class Attributes

Much modules, classes also contain a number of built-in attributes that can be accessed using the dot operator.

    * `__dict__`: Dictionary containing the class's namespace.
    * `__doc__`: Class documentation string or none, if undefined.
    * `__name__`: Class name.
    * `__module__`: Module name in which the class is defined. This attribute is `__main__` in interactive mode.
    * `__bases__`: A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.

```
Employee.__doc__: Common base class for all employees
Employee.__name__: Employee
Employee.__module__: __main__
Employee.__bases__: (<class 'object'>,)
Employee.__dict__: {'__module__': '__main__', '__init__': <function Employee.__init__ at 0x01105660>, 'empCount': 2, 'newvar': 10, '__doc__': 'Common base class for all employees', '__dict__
': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, 'displayCount': <function Employee.displayCount at 0x015E7078>, 'displayEmplo
yee': <function Employee.displayEmployee at 0x015E7030>}

```

### Object ref count and garbage collection

```python
a = 40      # Create object, ref count = 1
b = a       # Increase ref. count by one

del a       # Decrease ref. count to 1
b = 100     # Decrease ref. count to 0 (and now flagged for garbage collection)
```

```python
import sys
print(sys.getrefcount(123))
a = 123
print(sys.getrefcount(123))
b = 123
print(sys.getrefcount(123))
c = 123
print(sys.getrefcount(123))
del(a)
print(sys.getrefcount(123))
c = 10
print(sys.getrefcount(123))
```

The output from this is:
```
$ python refcount.py
16
17
18
19
18
17
```

NOTE: The starting value if the number of references that exist for the object "123" that the Python is managing.  This will vary. Our naming of 123 (naming it a, b, c etc.) increases the reference count to the object 123. As we reassign names (for instance c = 10), or delete a name (i.e. del(a)) the reference count to the object 123 decreases.

## `__init__` method

As we have seen, the `__init__` method is a constructor that is called when we instantiate and object. Unlike many other languages, in Python it's typical to try to avoid introducing a new attribute outside of the __init__ method, otherwise you've given the caller an object that isn't fully initialized. This is more of a tendency, or default you should follow, not a hard rule. Obviously, there are legitimate exceptions, but it's a good principle to keep in mind.

## `__del__` method

Like a constructor, we can also have a destructor. As we have seen, in Python the constructor method is always called  `__init__`. In Python, the destructor method is always called `__del__`.

Defining a `__del__` method is not necessary, but can be useful in situations where we wish to execute some tasks just before the object is destroyed. One example might be the close a database connection that was opened by the constructor (`__init__`) function.

```python
class Employee:
    """Common base class for all employees"""
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)

    def __del__(self):
        print("Destroyed")
```

## Editing an object or class dynamically

Unlike many other languages, in Python you can add, delete, or modify attributes of class or objects during runtime.

```python
emp1.age = 7  # Add an 'age' attribute to the object emp1.
emp2.age = 8  # Modify 'age' attribute to the object emp1.
Employee.newvar = 10 # Add "newvar" class variable to Employee class

print(emp1.age, emp2.age, Employee.newvar)
```

the resulting output is...

```
7 8 10
```

We can even delete variables within classes and objects during runtime:

```python
del emp2.age  # Delete 'age' attribute from the object emp1.

print(emp1.age)
print(emp2.age)
print(Employee.newvar)
```

Output of which is as follows:

```
7
Traceback (most recent call last):
  File "emp_class.py", line 35, in <module>
    print(emp2.age)
AttributeError: 'Employee' object has no attribute 'age'
```

You can also query and manipulate objects at runtime using the following built-in Python functions:

* The getattr(obj, name[, default]) : to access the attribute of object.
* The hasattr(obj,name) : to check if an attribute exists or not.
* The setattr(obj,name,value) : to set an attribute. If attribute does not exist, then it would be created.
* The delattr(obj, name) : to delete an attribute.


```Python
print("hasattr : ", hasattr(emp1, 'age'))    # Returns true if 'age' attribute exists
print("getattr : ", getattr(emp1, 'age'))    # Returns value of 'age' attribute
print("setattr : ", setattr(emp1, 'age', 8)) # Set attribute 'age' at 8
print("delattr : ",delattr(emp1, 'age'))    # Delete attribute 'age'
```

Outputs the following:
```
hasattr :  True
getattr :  7
setattr :  None
delattr :  None
```

## Instance attributes

A function defined in a  class is referred to as a method. Methods have access to all the data within the instance of the object. The instance of the object is referenced through "self". Because such methods require a "self" reference, then an instance must be created in order for these attributes to be used. These are referred to as "instance methods", that is, methods that are specific to the instance of the object.

We can also create static methods. These are methods that do not require a reference to "self".

```python
class Employee:
    """Common base class for all employees"""
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)

    def diplayHelp():  ## note, there isn't a reference to self. This method is therefore a class method, or static method.
        print("This object contains employee information for XYZ corp.")

    def __del__(self):
        print("Destroyed")
```

```python
@staticmethod
def diplayHelp():  ## note, there isn't a reference to self. This method is therefore a class method, or static method.
    print("This object contains employee information for XYZ corp.")

```

### Class method

One final form of method in Python OOP is the Class Method. It is like an instance method, but instead of receiving a the "self" instance reference as the first parameter, it receives a reference to the class. With class method, the class reference is implicitly passed as the first argument.

```python
@classmethod
def are_there_employees(emp):
  return emp.empcount > 0
```

## Inheritance

Let's say we have an system for keeping track of inventory. In our inventory, we have washers, dryers, and refrigerators.

Our accounting system will want to record each inventory item. We can do this by creating a washer class, a dryer class, and a refrigerator class. In each class we could define a method called "getPrice" and another called "getCost". Also in each object, we might have specific methods and attributes for each class. The washer might have attributes to indicate that it's upright washer, or sideload. A dryer might have BTU's. A refrigerator might was a boolean representing water dispensor. Etc.

When thinking about modeling such a system, balance our thoughts between thinking about what is different (unique) about each class of inventory item, and what is the same. Inheritance allows us to model both of these ideas.

In "polymorphism" all objects share a common attribute. For instance, all road vehicles have wheels. All mammals have legs, etc. In this thinking, we may want to take advantage of the fact that every class of inventory item has a cost. We can create a function, therefore, that accepts any inventory and prints out the cost - no matter what the class.

```python

class inventoryItem:
    itemCount = 0

    def __init__(self, sku, cost, category):
        self.sku = sku
        self.cost = cost
        self.cat = category
        inventoryItem.itemCount += 1

    def getCost(self):
        print("Our cost is ", self.cost)

    def getPrice(self):
        print("Our price is ", self.cost * 1.5)

class washer(inventoryItem):
    def __init__(self, sku, cost, frontLoad):
        inventoryItem.__init__(self, sku, cost, "Washer")
        self.fl = frontLoad
    def printType(self):
        if frontLoad:
            print("Frontload")
        else:
            print("Sideload")


class dryer(inventoryItem):
    def __init__(self, sku, cost, btus):
        inventoryItem.__init__(self, sku, cost, "Washer")
        self.btus = btus
    def printBtus(self):
        print(self.btus)


def printCost(inItem): # "polymorphism" example, that is, all inventoryItems have a cost
    print(inItem.getCost())

w = washer(123, 600, True)
d = washer(123, 500, 1200)

printCost(w)
printCost(d)
```



#### Appendix
__NOTE__: Some of the material above is derived the [official Python 3.5.2 documentation on classes](https://docs.python.org/3/tutorial/classes.html) and from http://www.tutorialspoint.com/python/python_classes_objects.htm (which also seems to be closely derived from the official documentation)

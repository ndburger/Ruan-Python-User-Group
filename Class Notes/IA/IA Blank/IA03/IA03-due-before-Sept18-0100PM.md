
# IA03: Model Generators using Closures
* __Due September 18, by 1 PM __
* __Submit this assignment via git to your individual private repo (MIS407-cid00xx) under  directory IA03.__


In this exercise you will create a module called __predictive_models__.

* When called directly from a python command line, __predictive_models.py__ should return the message "Sorry, not for human consumption."

* The module and any functions within this module will include descriptive docstrings that inform users as to the usage of the module and functions.

* Inside this module, you will create 2, and not more than two, functions (this count does not  include any nested functions).  The first function will be called __lm__, and the second will be called __lm_p__.

* This __predictive_models__ module must not import any other modules or packages.

__NOTE__: To accomplish this task you will use the concept of closures. As we saw last week, closures are self contained chunks of code that have store references to any constants or variables from the original scope in which they were created. This is referred to as "closing" over those variables, and hence the name "closure".

As we saw previously, an illustrative example of a closure is as follows:

```Python
## see nested_functions3.py in this lecture repo
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

## lm() and lm_p()

The details for each of the two functions you'll create are as follows:

__lm__ returns a function defines linear model identified by two parameters, intercept and slope.

The following code illustrates how this function will be used (and should behave)

```Python
# Use lm to create a linear model with a slope of 2, and an intercept of 10 and
# name the returned function lm1
lm1 = pm.lm(i=10, m=2)
print(lm1(1))  # prints the result of 10 + 2(1)
print(lm1(0))  # prints the result from 10 + 2(0)
print(lm1(-1.1))  # prints the result from1 0 + 2(-1.1)
```

For further illustration, the following example creates another linear model names lm2.

```Python
# Use lm to create a linear model with a slope of -2.2, and an intercept of
# 1001.23 and name the returned function lm2
lm2 = pm.lm(i=1001.23, m=-2.2)
print(lm2(1))  # print the result of 1001.23 + 1*(-2.2)
print(lm2(0))  # print the result of 1001.23 + 0*(-2.2)
print(lm2(-3.9))  # print the result of 1001.23 + (-3.9)*(-2.2)
```

The other function, __lm_p__,  returns a function defined as a power transformation of the predictive variable of a lm model.

The following code illustrates:

```Python
lm1 = pm.lm(i=10, m=2)
# create an exp tranform of predictor for lm
pm1 = pm.lm_p(l=lm1, p=2)
# use our new model to generate various output
print(pm1(2))  # 10+2(2**2)
print(pm1(10))  # 10+2(10**2)
print(pm1(127))  # 10+2(127**2)

# create an exp tranform of lm to the power of 3.5
pm2 = pm.lm_p(l=lm1, p=3.5)
# use our new model to generate various output
print(pm2(2))  # 10+2(2**3.5)
print(pm2(10))  # 10+2(10**3.5)
print(pm2(127))  # 10+2(127**3.5)
```

__NOTE:__ lm_p is of the form f(g(x)), where f(x) = i + m(x), and g(x) = x ** p

## IA03_tester.py
I have provided a test script called IA03_tester.py that you can use to test your module. Your module should produce the results as shown in the comments at the end of the IA03_test.py script.

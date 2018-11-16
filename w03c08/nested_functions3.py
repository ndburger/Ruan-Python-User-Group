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

# The above nested function is a "closure". We'll discuss more about this later
# but, here's something to start to explore...
print("### Let's look into sqr...")
print(sqr.__closure__)  # tuple of closured vars, in this case just one
type(sqr.__closure__[0])  # cell type https://docs.python.org/2/c-api/cell.html
print(sqr.__closure__[0].cell_contents)  # print value of the cell var

print("### Let's look into sqrt...")
print(sqrt.__closure__)
type(sqrt.__closure__[0])
print(sqrt.__closure__[0].cell_contents)

print("### Let's look into cube...")
print(cube.__closure__)
type(cube.__closure__[0])
print(cube.__closure__[0].cell_contents)

print("### Let's look into cubert...")
print(cubert.__closure__)
type(cubert.__closure__[0])
print(cubert.__closure__[0].cell_contents)

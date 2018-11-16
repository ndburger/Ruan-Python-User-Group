def f(x):
    def g():
        print(x)
    return(g)

fnc = f(2)
fnc()
fnc = f(100)
fnc()

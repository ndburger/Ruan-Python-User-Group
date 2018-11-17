"""Demo __name__ and it's values."""


# If this aboutmain.py file is called first, then __name__ will equal __main__
# If this aboutmain.py file is called from another module (that imports this
# module) then the __name__ will be set to aboutmain (the name of this file)
def f():
    print(__name__)
    return None

print(__name__)
f()

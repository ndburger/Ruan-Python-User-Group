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

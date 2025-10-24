"""
Dynamic typing means that you don’t have to declare the type of a variable when you create it
"""

x = 10         # x is an integer
print(type(x)) # <class 'int'>

x = "Hello"    # now x is a string
print(type(x)) # <class 'str'>

x = 3.14       # now x is a float
print(type(x)) # <class 'float'>

"""
Python doesn’t care that x changed from an integer → string → float.
It updates the variable type automatically each time."""
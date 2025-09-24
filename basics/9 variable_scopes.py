'''variable scope => where variables can be accessed from
LEGB
    •	L: Local
    •	E: Enclosing
    •	G: Global
    •	B: Built-in

'''
#!================================================================
#local scope => variables defined within a function and can only be accessed in that function
def local_scope():
    local_variable = 'can only be accessed in this function'
    print(local_variable)

local_scope()

#!================================================================
#global scope =>variables can be accessed from throughout the module and by any function within the module
#use global keyword within a function to modify a global variable
global_variable = 'can only be accessed by any function within the module'

def global_scope():
    print(f'global scope means: {global_variable}')

global_scope()

#eg2
age = 20  

# def my_function():
#     global agenot advisible. use return statements
#     age 30  # Modifies the global variable age
#     print(age)# 30

# my_function()
# print(age)# 30

def my_function():
    return age + 1

age = my_function()
print(f'new age is {age}') # output: 21

#only use global keyword when setiing contstants that are not going to change eg
PI = 3.141
URL = 'www.youtube.com'
INSTAGRAM_HANDLE = 'k1bet_'

#!================================================================
#built-in scope => name that are predefined in py eg len, str, print
print(len([1, 2, 3]))  # Uses the built-in len function

import builtins 
# print(dir(builtins)) #gives list of all built-in names

#!================================================================
#Enclosing scope => refers to variables in nested functions
#outer function => #?enclosing scope
#TODO inner function can see and access variables in enclosing function

def outer_function():
    message = 'greetings from outer/enclosing function'

    def inner_function():
        print(message)

    inner_function()

outer_function() #output => Hello from the outer/enclosing function

#TODO modifying enclosing scope variable
#You cannot directly modify a variable in the enclosing scope from the inner function unless you use the nonlocal keyword.
#? without nonlocal keyword
def outer():
    note = 'this is the outer function'
    
    def inner():
        note = 'this is the inner function'
        print('inner: ', note)

    inner()
    print('outer: ', note)

outer()

#? with nonlocal keyword
def enclosing_function():
    message = 'hello'
    
    def nested_function():
        nonlocal message
        message = 'hello changes to hi'
        print(f'inner: {message}')
    
    nested_function()
    print(f'outer: {message}')

enclosing_function()


#?use of enclosing scope
def multiplier(factor):
    def multiply_by(value):
        return value * factor  # Accesses `factor` from the enclosing scope
    return multiply_by

double = multiplier(2)
print(double(5))  # Output: 10

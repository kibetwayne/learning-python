'''
Blocks of reusable codes that perform specific tasks
Local Scope: Variables created inside a function exist only within that function.
Global Scope: Variables created outside all functions are accessible from anywhere in the code.
'''

#👉👉A blank function == it wont do anything
def hello_func(parameters):
    pass

#👉👉Simple function
def greet():
    print("Hello, welcome!")
    
greet()  # Output: Hello, welcome!
#!================================================================

#👉👉Parameters and Arguments
'''
parameters (placeholders within the function)
Arguments (actual values passed in when the function is called).
'''

def greet_with_name(name):
    print(f"Hello, {name}")

greet_with_name("Alice")  # Output: Hello, Alice
greet_with_name("Bob")    # Output: Hello, Bob

#👉👉positional arguments == Values are matched based on their position. The order is important.
def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

greet("Alice", 25)  # Output: Hello, Alice. You are 25 years old.

#👉👉keyword arguments == Values are matched to parameter names directly, making order unimportant and allowing selective use of parameters.

def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

greet(age=25, name="Alice")  # Output: Hello, Alice. You are 25 years old.


#👉👉Return Statement == they allow a function to send back a result to the caller.
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print(result)  # Output: 15

#👉👉Default parameters

def default_name(name="Guest"):
    print(f"Hello, {name}")

default_name()  # Output: Hello, Guest
default_name("Alice")  # Output: Hello, Alice
#!================================================================

#👉👉Args & Kwargs
'''
args == For a variable number of positional arguments.
kwargs == For a variable number of keyword arguments.
'''
#?args
def concatenate(*words):
    return '-'.join(words)
print(concatenate('hello', 'world', '!')) # Output: Hello-world-!

#?kwargs
def greet_with_details(**details):
    print(f"Hello, {details['name']}. Your age is {details['age']}.")

greet_with_details(name="Alice", age=25)  # Output: Hello, Alice. Your age is 25.

def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Alice", age=25, job="Developer")

#!================================================================

#👉👉local & global scope
#?local scope == here you cant print salutations as it is inside the greet function
def greet():
    salutations = "Hello, welcome!"
    print(salutations)
greet()  

#?global scope == you are able to access message as it is in the global scope
message = "Hello, welcome!"
def greet():
    print(message)
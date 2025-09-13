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
#👉👉Function calling another function
def print_many(n, thing):
    for _ in range(n):
        print(thing)

def print_twice(x):
    print_many(2, x)

print_twice("Hello")

#!================================================================
#👉👉Function returning values
def double(x):
    return x * 2

number = 5
twice = double(number)
print(number)
print(twice)

'''Once a return statement is executed, the function will stop, and the rest of the code is ignored. This means that any code immediately after a return in the same block is unreachable: '''
def example():
    return "This will be printed"
    return "This will NOT be printed"
    
example()

def foo():
    for letter in 'abc':
        for number in range(3):
            print(f"{letter} {number}")
            if letter == 'b':
                return letter

foo()   # **Output: a 0, a 1, a 2, b 0. As before, return stops the whole function, including all loops.

def foo():
    for letter in 'abc':
        for number in range(3):
            print(f"{letter} {number}")
            if letter == 'b':
                break

foo()   # **Output: a 0, a 1, a 2, b 0, c 0, c 1, c 2. Here break only stops the inner loop.
#!================================================================
#👉👉testing functions
def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def double(x):
    return x * 2

assert_equal(double(2), 4)
assert_equal(double(5), 10)

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

#?kwargs keyword arguments
def greet_with_details(name, age):
    print(f"Hello, {name}. Your age is {age}.")
    
greet_with_details(age=25, name="Alice")  # Output: Hello, Alice. Your age is 25.
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
    
#!================================================================
#prime number checker
def is_prime_number(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print('Its a prime number')
    else:
        print('Its not a prime number')
        
n = int(input('Check this number: '))
is_prime_number(number = n)

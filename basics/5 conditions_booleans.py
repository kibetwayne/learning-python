'''
•	Used to execute specific blocks of code based on whether certain conditions are T or F
•	A Boolean is a data type that can only be T or F
•   Use conditional operators
'''
#👉👉BOOLEAN
is_raining = True
has_umbrella = False

#👉👉CONDITIONAL OPERATORS eg
age1 = 20
print(age1 > 18)     # Output: True
print(age1== 18)    # Output: False

#👉👉CONDITIONAL STATEMENTS
'''
•	if: Executes if the condition is T.
•	elif: Adds additional conditions to check if the previous ones were F.
•	else: Executes if none of the above conditions are T.
'''
age3 = 17
if age3 >= 18:
    print('adult')
elif age3 >= 13:
    print('teenager')
else:
    print('child')
    
#👉👉LOGICAL OPERATORS
'''
They combine multiple conditions into a single expression.
•	and: Returns True if both conditions are True.  AND GATE
•	or: Returns True if at least one condition is True. OR GATE
•	not: Returns True if the condition is False, and vice versa. NOT GATE
'''
age2 = 20
has_id = False

# Check if age is above 18 and has an ID
if age2 > 18 and has_id:
    print('is a citizen and has id')
else:
    print('underage')

# Check if age is above 21 or has an ID
if age2 > 21 or has_id:
    print('citizen')
else:
    print('has id')

# Check if user has an id
if not has_id:
    print('apply for an id')   
else:
    print('has id')

#👉👉OBJECT IDENTITY 'IS'
'''
Object identity refers to the uniqueness of an object. It can be thought of as its "address" in memory, which remains constant for the lifetime of the object. You can use Python's built-in id() function to get the identity of an object.
•	Identity (IS) checks if two variables reference the exact same object in memory.
•	Equality (==) checks if two objects have the same value (i.e., content).
'''
a = [1, 2, 3]
b = a  
print(id(a))
print(id(b))      # Both a and b now point to the same object(have same id)

print(a is b)     # True, both refer to the same list
print(a == b)     # True, same content

# Create a new, separate list with the same content
c = [1, 2, 3]
print(a is c)     #  False,  a and c are different objects
print(a == c)     #  True,  same content

'''
Python optimizes memory usage by reusing objects for some immutable values.
'''
x = 10
y = 10
print(x is y)    # True, because small integers are often reused by Python

x = 1000
y = 1000
print(x is y)    # False, large integers are not necessarily reused

#👉👉TRUTHY AND FALSY VALUES
'''
Falsy Values
•	False
•	None
•	0 (zero)
•	"" (empty string)
•	[] (empty list)
•	{} (empty dictionary
'''#everything else returns true
name = ""
if name:
    print("Name exists.")
else:
    print("Name is empty.")


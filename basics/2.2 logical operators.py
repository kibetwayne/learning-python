#📑📑COMPARISON OPERATORS
num_1 = 3
num_2 = 4
print(num_1 == num_2) #False
print(num_1 != num_2) #True
print(num_1 > num_2)  #False
print(num_1 < num_2)  #True
print(num_1 >= num_2) #False
print(num_1 <= num_2) #True



def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
	    print(f"Error! {repr(actual)} != {repr(expected)}")
   

#📑📑AND returns true if all the variables evaluate to true
price = 1
print(price > 50 and price < 200) #returns true if price is between 50 and 200

#📑📑OR returns true if atleast one of the variables evaluate to true
print(price > 50 or price < 200) #true


def is_friend(name):
    return name == 'Alice' or 'Bob'
    #? return name == "Alice" or "Bob" Python iterpretres this as (name == "Alice") or ("Bob") which evaluates to "Bob" when name == "Alice" is False

assert_equal(is_friend("Alice"), True)
assert_equal(is_friend("Bob"), True)
assert_equal(is_friend("Charlie"), False)

#📑📑NOT  It negates the expression to which it is applied
legal_age = True
print(f'Is of legal age: {not legal_age}')
not True or True #returns True. NOT has higher priority than OR & AND. 

#📑📑COMPARISON CHAINING
age = 20
print(18 <= age <= 30)   # True

score = 120
print(score < 0 or score > 100)   # True (outside valid percentage range)

x = 5
print(5 == x == 5)     # True
print(5 == x == 6)     # False

x1 = 5
print(5 != x1 != 10)    # True (x is not 5 AND x is not 10)
print(5 != x1 != 6)     # True (x != 5 and x != 6)
print(5 != x1 != 4)     # False (since x = 5, fails first check)

x2 = 7
print(10 > x2 > 5)      # True  (10 > 7 and 7 > 5)
print(10 > x2 > 8)      # False (10 > 7 true, but 7 > 8 false)

x3 = 10
print(10 >= x3 >= 5)    # True  (10 >= 10 and 10 >= 5)
print(10 >= x3 >= 11)   # False

x4 = 10
print(5 <= x4 <= 10)    # True  (5 <= 10 and 10 <= 10)
print(11 <= x4 <= 20)   # False

x5 = 7
print(5 < x5 != 10)     # True  (5 < 7 and 7 != 10)
print(5 < x5 == 7 < 10) # True  (5 < 7 and 7 == 7 and 7 < 10)

#📑📑Combining AND and OR
True or False and False #True
''' it's equivalent to [True or (False and False)] This is because and has a higher priority than or
Be extra careful when combining operators. Either add parentheses to be safe or break up your expression into smaller parts and assign each part to a variable'''
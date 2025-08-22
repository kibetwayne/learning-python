#📑STRINGS
#!strings are immutabe. python doesnt change the original value of a string. You simply can't change the original string - you can only create new variables and asing the changes to it.

#👉string methods
print(help(str))#list all mehods on string and what they do

message = 'hello world'
print(dir(message)) #gives a list of all available methods
print(message)
print(message[0:4])#range

#👉methods
# 1. Changing Case
text = "hello world"
print(text.upper())      # "HELLO WORLD"
print(text.lower())      # "hello world"
print(text.capitalize()) # "Hello world"
print(text.title())      # "Hello World"

# 2. Whitespace Management
text_with_spaces = "  hello  "
print(text_with_spaces.strip())   # "hello"
print(text_with_spaces.lstrip())  # "hello  "
print(text_with_spaces.rstrip())  # "  hello"

# 3. Finding and Replacing
print(text.find("world"))         # 6
print(text.replace("world", "Python"))  # "hello Python"

# 4. Checking String Content
print(text.startswith("he"))  # True
print('hello' in text)        # True
print(text.endswith("ld"))    # True
print("123".isdigit())        # True
print("hello123".isdigit())   # False
print("hello".isalpha())      # True
print("hello123".isalnum())   # True

# 5. Splitting and Joining
print(text.split())              # ['hello', 'world']
print("-".join(["hello", "world"]))  # "hello-world"

# 6. Other Useful Methods
print(text.count("o"))      # 2
print(text.index("world"))  # 6
print("42".zfill(5))         # "00042"

#7. joining multiple strings
greetings = 'hello'
name = 'wayne'
message = f'{greetings}, {name.upper()}. welcome'
print(message)

#8. finding a word in a string
sentence = "The quick brown fox jumps over the lazy dog"
print('fox' in sentence)  # True
print('cat' in sentence)  # False

#9. count
print(sentence.count('o'))  # Count occurrences of 'o'

#10. index
print(sentence.index('fox'))  # Find index of 'fox'. Each caracter has an index

#11. length
print(len(sentence))  # how many characters are in the string

#!================================================================
#?string slicing

#1. Basic Slicing:
text = "python"
print(text[1:4])  # Output: "yth"

#2. Omitting start or stop:
print(text[:4])   # Output: "pyth" (start is 0 by default)
print(text[2:])   # Output: "thon" (stops at the end of the string)

#3. Using step:
print(text[::2])  # Output: "pto" (every second character)
print(text[1::2]) # Output: "yhn" (starts at index 1, every second character)

#4. Reversing a Sequence:
print(text[::-1])  # Output: "nohtyp" (reverses the string)

#5. Negative Indices:
print(text[-4:-1])  # Output: "tho" (slices from index -4 to -1, exclusive)

#!================================================================
#?inputs 

car = input('what car do you prefer') #output is always a string
print(f'your favorite car is {car}')

#!================================================================
#?conversion

#1. string to int
birth_year = input('what year were you born?')
age = 2023 - int(birth_year)
print(f'you are {age} years old')

#2. int to string
age = 25
age_str = str(age)
print(f'you are {age_str} years old')

#3. string to float
weight = input('what is your weight?')
weight_float = float(weight)
print(f'your weight is {weight_float}kg')

#4. float to string
weight_float = 75.5
weight_str = str(weight_float)
print(f'your weight is {weight_str}kg')

#5. string to boolean
is_student = input('are you a student?')
is_student_bool = bool(is_student)
print(f'you are a student: {is_student_bool}')
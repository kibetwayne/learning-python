#📑STRINGS
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

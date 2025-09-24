name = "Bob"

is_friend = name == "Alice" or \
            name == "Bob"
print(is_friend)

is_friend = (name == "Alice" or
             name == "Bob")
print(is_friend)

is_friend = [name == "Alice",
             name == "Bob"]
print(is_friend)

print(name == "Alice" or
      name == "Bob")
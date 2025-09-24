''' data structure that stores key-value pairs
    allows  fast retrieval of values based on unique keys(immutable keys)
    used for mapping relationships between data.
    Mutable, Unordered,
    we use keys to access values and not the other way round. keys must be unique(no duplicates) and immutable
    '''
    
student = {'name': 'wayne', 'age': '20', 'course': ['compsci', 'math'], 'city': 'Nairobi'}
print(student['name'])      #to access the value under the key 'name'
print(student.get('team'))  #easier way to access a value as it returns none instead of an error when the  key doest exist
print(student.get('team', 'Not found')) #specify a default value to be shown when a key is not found


#👉👉adding and updating items
student['age'] = 25             # Update the value for 'age'
student['country'] = 'KENYA'    # Add a new key-value pair
print(student)

##👉👉removing items
updated =student.pop('age')         # Removes the 'age' key and its value 
print(updated)
del student['city']        # Deletes the 'city' key and its value

print(student)
student.clear()            # Removes all items from the dictionary

#👉👉Items method
'''When you print student2.items(), it outputs a list-like view of tuples, where each tuple consists of a key and its associated value from the dictionary.'''
student2 = {'name': 'john', 'age': '30', 'course': ['eng', 'lit'], 'city': 'mombasa'}

for key, value in student2.items():
    print(f'{key}: {value}')

#👉👉 iterating over keys
quantities = {'apple': 1, 'cat': 10}
for key in quantities:
    print(key)

def print_words(french, german):
    for key, value in french.items():
        print(f'English: {key}\nFrench: {value}\nGerman: {german[key]}\n---')

print_words(
    {'apple': 'pomme', 'box': 'boite'},
    {'apple': 'apfel', 'box': 'kasten'},
)


#!======================================================================
#?eg1
def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def total_cost(cart, prices):
    result = 0
    for item in cart:
        price = prices[item]
        result += price
    return result

assert_equal(
    total_cost(
        ['apple', 'box', 'cat'],
        {'apple': 2, 'box': 5, 'cat': 100, 'dog': 100},
    ),
    107,
)

#?eg2
def substitute(string, d):
    result = ""
    for letter in string:
        result += d[letter]
    return result

plaintext = 'helloworld'
encrypted = 'qpeefifmez'
letters = {'h': 'q', 'e': 'p', 'l': 'e', 'o': 'f', 'w': 'i', 'r': 'm', 'd': 'z'}
reverse = {'q': 'h', 'p': 'e', 'e': 'l', 'f': 'o', 'i': 'w', 'm': 'r', 'z': 'd'}
assert_equal(substitute(plaintext, letters), encrypted)
assert_equal(substitute(encrypted, reverse), plaintext)


def make_english_to_german(english_to_french, french_to_german):
    english_to_german = {}
    for word, value in english_to_french.items():
        english_to_german[word] = french_to_german[value]
    return(english_to_german)

assert_equal(
    make_english_to_german(
        {'apple': 'pomme', 'box': 'boite'},
        {'pomme': 'apfel', 'boite': 'kasten'},
    ),
    {'apple': 'apfel', 'box': 'kasten'},
)

def swap_keys_values(d):
    new = {}
    for key, word in d.items():
        new[word] = key
    return(new)
        

assert_equal(
    swap_keys_values({'apple': 'pomme', 'box': 'boite'}),
    {'pomme': 'apple', 'boite': 'box'},
)

def swap_keys_values(d):  #**adding duplicate items
    new_dict = {}
    for key, value in d.items():
        if value in new_dict:
            # if already exists, append the key
            new_dict[value].append(key)
        else:
            # otherwise create a list
            new_dict[value] = [key]
    return new_dict


print(swap_keys_values({'apple': 'pomme', 'avocado': 'avocat', 'lawyer': 'avocat'}))
print(swap_keys_values({'apple': 'pomme', 'lawyer': 'avocat', 'avocado': 'avocat'}))

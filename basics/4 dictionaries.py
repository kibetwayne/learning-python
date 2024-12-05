''' data structure that stores key-value pairs
    allows  fast retrieval of values based on unique keys(immutable keys)
    used for mapping relationships between data.
    Mutable, Unordered, '''
    
student = {'name': 'wayne', 'age': '20', 'course': ['compsci', 'math'], 'city': 'Nairobi'}
print(student['name'])      #to access the value under the key 'name'
print(student.get('team'))  #easier way to access a value as it returns none instead of an error when the  key doest exist
print(student.get('team', 'Not found')) #specify a default value to be shown when a key is not found


#👉👉adding and updating items
student['age'] = 25             #Update the value for 'age'
student['country'] = 'KENYA'    #Add a new key-value pair
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
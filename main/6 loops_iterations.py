'''
are used to execute a block of code multiple times. Useful when working with repetitive tasks or performing operations over a range of values.
1.	for loop: iterates over a sequence or a range of numbers.
2.	while loop: Repeats a block of code if a specified condition is True.
'''
#👉👉FOR LOOP used to iterate over each item in a collection
#? (syntax: for item in sequence)

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

#for loop in range == often used to loop a specific number of times
#? (syntax: for item in range(staring value, end)
for i in range(1,6):#prints starting with 1 upto 5
    print(i)
    
for i in range(5):#prints from 0 to 4
    print(i)

#👉👉FOR LOOP with a dictionary
student = {'name': 'alice', 'age': 20, 'grade': 'A'}
for key, value in student.items():
    print(key, ':', value)
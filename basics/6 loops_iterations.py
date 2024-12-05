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

#👉👉WHILE loop
#? (syntax: while condition:)

count = 5
while count > 0:
    print(count)
    count -= 1

#👉👉BREAK AND CONTINUE STATEMENTS
'''
Break == exits loops immediately
Continue == skips the rest of the current iteration and moves to the next iteration
'''
for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        print('three')
        continue
    print(i)

#👉👉NESTED LOOPS == loops within loops
num = [1,2,3,4,5,6,7,8]
for i in num:
    for word in ['odd', 'even']:
        print (i, word)

'''
are used to execute a block of code multiple times. Useful when working with repetitive tasks or performing operations over a range of values.
1.	for loop: iterates over a sequence or a range of numbers.
2.	while loop: Repeats a block of code if a specified condition is True.
'''
#👉👉FOR LOOP used to iterate over each item in a collection
#? (syntax: for item in sequence)  for <variable> in <collection>: <code to repeat>

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

#for loop in range == often used to loop a specific number of times
#? (syntax: for item in range(staring value, end, step value)
for i in range(1,6):#prints starting with 1 upto 5
    print(i)
    
for i in range(5):#prints from 0 to 4
    print(i)
    
for i in range(1, 10, 2):#prints odd numbers from 1 to 9
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
Break == exits loops immediately if condition is met.
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

#!===================================================================
#?Iterating over a list and modifying it
'''Never modify something while you iterate over it. Keep mutation and looping separate. 
Do this instead:
        1. Build up a new list from scratch.  
        2. Modify a copy.
        3. Iterate over a copy and modify the original.
'''


# * numbers = [10, 7, 8, 3, 12, 15]
# * for number in numbers:
# *     if number <= 10:
# *         numbers.remove(number)
# * print(numbers)

''' As it runs, it clearly skips even looking at 7 or 3 and doesn't remove them. The index variable i runs through the usual values 0, 1, 2, ... as it's supposed to, but as the list changes those are no longer the positions we want. For example in the first iteration i is 0 and number is 10, which gets removed. This shifts the rest of the numbers left one position, so now 7 is in position 0. But then in the next iteration i is 1, and numbers[i] is 8. 7 got skipped.'''

# Use a copy of the original collection if you need to modify it.
numbers = [10, 7, 8, 3, 12, 15]
for number in numbers.copy():
    if number <= 10:
        numbers.remove(number)
print(numbers)  

#Similarly, you could loop over the original and modify a copy:
numbers = [10, 7, 8, 3, 12, 15]
big_numbers = numbers.copy()

for number in numbers:
    if number <= 10:
        big_numbers.remove(number)
print(big_numbers)

#Or you could build up a new list from scratch.

numbers = [10, 7, 8, 3, 12, 15]
big_numbers2 = []

for number in numbers:
    if number > 10:
        big_numbers2.append(number)
print(big_numbers2)


#!===================================================================
#multiplication table
for cur in range(1, 13):
    for num in range(1, 13):
        answer = cur*num
        print(f'{cur} x {num} = {answer}')
    print('---')
    
# vs table
players = ["Alice", "Bob", "Charlie"]

for player in players:
    for _ in players:
        if player != _:
            print(f'{player} vs {_}')
            
# possible combination of characters
letters = "ABCD"

for char1 in letters:
    for char2 in letters:
        for char3 in letters:
            for char4 in letters:
                print(char1 +char2 +char3 +char4)
                
# upside down triangle
size = 5
use = size
num = 1
plus = '+'

for _ in range(size):
    if num <= size:
        print(plus * use)
        num += 1
        use -= 1    
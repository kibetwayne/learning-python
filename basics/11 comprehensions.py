''' comprehension is a readable way to create a sequence by applying an expression to each item in an iterable
'''
#?list comprehension
#syntax => [expression for item in iterable if condition ]

nums = [1,2,3,4,5,6,7,8,9,10]
# my_list1 = []
# for n in nums:   #old syntax => code isn't clean
#     my_list1.append(n)
# print(f'my_list1: {my_list1}')

my_list2 = [n for n in nums] #better version
print(f'my_list2: {my_list2}')

squares = [x*x for x in range(5)]
print(squares)

evens = [x for x in range(10) if x % 2 ==0]
print(evens)

# letter_list1 =[]
# for letter in 'a,b,c,d':
#     for num in range(4):
#         letter_list1.append((letter, num))
# print(f'letter_list1: {letter_list1}')

letter_list2 = [(l,n)for l in 'abcd' for n in range(4)]
print(f'letter_list2: {letter_list2}')

#!================================================================
#?dictionary comprehension
#syntax => {key_expression: value_expression for item in iterable if condition}

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
squared_dict = {n: n*n for n in numbers if n % 2 == 0} 
print(f'squared_dict: {squared_dict}')

#transforming a list into a dictionary
name = ['bruce', 'clark', 'peter', 'wade', 'tony', 'steve']
second_name = ['wayne', 'kent', 'parker', 'wilson', 'stark', 'rogers']

# my_dict = {}
# for name,second_name in zip(name,second_name):
#     my_dict[name] = second_name
# print(f'my_dict: {my_dict}')

combined_name = {k: v for k, v in zip (name, second_name)}
print(combined_name)

words = ["apple", "banana", "cherry"]
word_length_dict = {word: len(word) for word in words}
print(word_length_dict)

original = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {v: k for k, v in original.items()}
print(reversed_dict)

#nested dictionary comprehension
multiplication_table ={n: {i: n*i for i in range(1,5)} for n in range (1,5)}
print(multiplication_table)

#!================================================================
#?set comprehension
#syntax => {expression for item in iterable if condition}
#Set comprehensions automatically remove duplicate values

number = [1, 2, 3, 4, 5]
squares = {n**2 for n in number}
print(squares)

#!================================================================
#?generator expressions

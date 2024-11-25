''' comprehension is a readable way to create a sequence by applying an expression to each item in an iterable
'''
#?list comprehension
#syntax => [expression for item in iterable if condition ]
nums = [1,2,3,4,5,6,7,8,9,10]
my_list1 = []
for n in nums:   #old syntax => code isnt clean
    my_list1.append(n)
print(f'my_list1: {my_list1}')

my_list2 = [n for n in nums] #better version
print(f'my_list2: {my_list2}')

squares = [x**2 for x in range(5)]
print(squares)

evens = [x for x in range(10) if x % 2 ==0]
print(evens)
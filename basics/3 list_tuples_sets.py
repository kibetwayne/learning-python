#📑📑LIST[]
empty_list = []            #how to create empty lists
empty_list = list()

'''A list is an ordered, mutable collection of items. Allow duplicate items and can contain elements of different data types.
'''

my_list = [1, 2, 3, 4, 5]
my_list2 = [1, 2, 3, 4, 5]
courses = ['geo', 'hist', 'phy', 'pop']

#👉👉methods
print(my_list[0])           # Output: 1
my_list.remove(1)           # Removes the first occurrence of 1
my_list.insert(3, 'new')    # Adds to a specific location
my_list[2] = 'changed'      # Modifies the element at index 2
my_list.extend(courses)     # Adds second list to 1st list
my_list.append(6)           # Adds 6 to the end of the list
print(len(my_list))         # Output: 8 (length of the list)
print(my_list)

copied_list = my_list.copy()  # Creates a shallow copy of the list
print(copied_list)             

my_list2.sort()             #largest to smallest
my_list2.reverse()
print(my_list2)

courses2 = sorted(courses)  #doesnt make changes to original
print(courses.index('hist'))#find the index of a value

print(courses.pop(1))       #removes the value at index 1 and returns it    
print(courses)

print(my_list.index(2))      #rerurns the first occurence of the value in a list
print(my_list.count(2))       #count how many times a value appears in the list


nums = [2, 9, 1, 8, 5, 64]   #?syntax value in some_list
print(7 in nums)     #in: A comparison operator that checks if a value is in a list 

sum([5, 3, 4])             #sum: A function that returns the sum of a list

[1, 2, 3, 2, 7, 2, 5].count(2) #count: counts the occurrences of a value in a list

#📑📑difference between IS and == in lists
# IS checks if two variables point to the same object in memory. lets say you have a set of twins, they are two different people(lists) but they look the same. when you append 4 to list1, list2 will not change because they are two different objects in memory.
# == checks if the values of two variables are equal

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 is list2)  # Output: False (different objects in memory)
print(list1 == list2)  # Output: True (same values)
print(list1 is list3)  # Output: True  there is only one list, and the two variables list1 and list3 both refer to that same list

#!================================================================
#📑📑TUPLES()
empty_tuple = ()           #how to create empty tuple
empty_tuple = tuple()

'''
are like lists only difference is they are immutable
methods in lists that are used to mutate original list arent available in tuples'''
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])         # Output: 1
# my_tuple[1] = 10         # Error: Tuples are immutable

#!================================================================
#📑📑SETS{}
empty_set = {}            #this isnt right as it creates an empty dictionary
empty_list = set()        #how to create empty lists

'''
A set is an unordered, mutable collection of unique items. Sets do not allow duplicates and do not maintain any specific order of elements.
The order of elements is not preserved, and they are accessed by value, not by index.
'''
my_set = {1, 2, 3, 4, 5}
cs_courses = {'math', 'phy', 'business', 'calculus'}
art_courses = {'math', 'art', 'business', 'desing'}

print(my_set)              # Output: {1, 2, 3, 4, 5}
my_set.add(6)              # Adds 6 to the set
my_set.add(3)              # No effect, as 3 is already in the set
print(my_set)              # Output: {1, 2, 3, 4, 5, 6}

print(cs_courses.intersection(art_courses)) #used to check which elements are share across multiple sets
print(cs_courses.difference(art_courses)) #used to check which elements are the 1st set but not in second
print(cs_courses.union(art_courses)) #join elements in all the sets
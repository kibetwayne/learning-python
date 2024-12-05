#📑📑LIST[]
empty_list = []            #how to create empty lists
empty_list = list()

'''A list is an ordered, mutable collection of items. Allow duplicate items and can contain elements of different data types.
'''

my_list = [1, 2, 3, 4, 5]
my_list2 = [1, 2, 3, 4, 5]
courses = ['geo', 'hist', 'phy']

#👉👉methods
print(my_list[0])           # Output: 1
my_list.append(6)           # Adds 6 to the end of the list
my_list.insert(4, 'new')    # Adds to a specific location
my_list.remove(1)
my_list[2] = 'changed'      # Modifies the element at index 2
my_list.extend(courses)     #add second list to 1st list
print(my_list)              # Output: [1, 2, 'changed', 4, 5, 6]

my_list2.sort()             #largest to smallest
my_list2.reverse()
print(my_list2)

courses2 = sorted(courses)  #doesnt make changes to original
print(courses.index('hist'))#find the index of a value

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
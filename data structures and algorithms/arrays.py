'''
arrays can only store data of he same type

typecode == c-type == python-type == size-in-bytes
b  -  signed char    -  int                -    1
B  -  unsighed char  -  int                -    1
u  -  Py_UNICODE     -  Unicode character  -    2
h  -  signed short   -  int                -    2
H  -  unsigned short -  int                -    2
i  -  signed int     -  int                -    2
l  -  unsigned int   -  int                -    2
l  -  signed long    -  int                -    2
L  -  unsigned long  -  int                -    4
f  -  float          -  float              -    4
d  -  double         -  float              -    8
'''
#!================================================================
# ====== ===== Types of arrays ===== ===== 
#?lists
# lists act as arrays => no additional libraries required
vals =  [1, 2, 3, 4]
vals.append(5)
vals.reverse() 
print(vals)

#?array module(static typed arrays)
# *requires defining the type of element when creating the array using typecode
from array import *

arr = array('i', [1, 2, 3, 4, 5, 6, 7])
arr2 = array('i', [20, 30, 40, 50])

'''basic array operations'''
arr.append(8)                       #add new element to the end of an array
arr[1] = 10                         #modify an element in an array
arr.extend(arr2)                    #used to add 1 array to the end of another array
arr.insert(2, 11)                   #used to insert an element(11) at a specific index(2)
arr.remove(3)                       #used to remove an element by its value
print(f'removing last element {arr.pop()}')#used to remove the last element and returns it
print(f'removing element by index {arr.pop(7)}')#used to remove an element by its index and returns it
print(f'array length {len(arr)}')   #array length
print(arr)

'''array concatenation'''
arr3 = arr + arr2
print(arr3)


#?NumPy Array
'''efficient for multidimensional numeric computing'''
import numpy as np

# Create a 1D array
np_array = np.array([1, 2, 3, 4])

# Perform operations
print(np_array * 2)  # Output: [2 4 6 8]

# Create a 2D array (matrix)
matrix = np.array([[1, 2], [3, 4]])
print(matrix)

'''array slicing'''
a=np.array(['first', 'second', 'third', 'last'])
print(a[0:2])
print(a[::-1])

#?panda series
'''Pandas is a data analysis library, and its Series object functions like an array but with additional metadata
'''
import pandas as pd

# Create a Series
series = pd.Series([10, 20, 30])
print(series)

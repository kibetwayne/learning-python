'''
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
# *requires defining the type of element when creating the array 
from array import *

arr = array('i', [1, 2, 3, 4])
arr.append(5)
arr[1] = 10
print(arr)

#?NumPy Array
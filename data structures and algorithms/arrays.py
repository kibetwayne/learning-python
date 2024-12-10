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


vals =  [1, 2, 3, 4]
vals.reverse() # reverse
print(vals)
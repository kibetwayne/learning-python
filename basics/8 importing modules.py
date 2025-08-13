#Import the Entire Module
import math #?print(math.sqrt(16))
#Import Specific Functions or Variables
from math import sqrt #?print(sqrt(16))
#Import with an Alias
import math as m #?print(m.sqrt(16))
#Import All with
from math import *  #?print(sqrt(16))  

#!================================================================

#Creating and Importing a Custom Module
import my_modules as mm
print(mm.greet('wayne'))

subjects = ['hist', 'math', 'phy', 'eng']
index =mm.find_index(subjects, 'hist')
print(index)

#!================================================================

import random
random_subject = random.choice(subjects)
print(random_subject)



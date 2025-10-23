#*args Example
def add(*number):
    print(number[0]) #prints 1 as it is the first element of the tuple
    total = sum(number)
    return total

result = add(1, 2, 3, 4, 5)
print(result)  # Output: 15

def calculate(n, **kwargs):
    print(kwargs)  # prints the dictionary of the kwargs {'add': 3, 'multiply': 5}
    
    n += kwargs['add'] # adds 3 to n
    n *= kwargs['multiply'] # multiplies n by 5
    print(n) # prints 25
    
    
calculate(2, add=3, multiply=5)  
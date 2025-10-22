#*args Example
def add(*number):
    print(number[0]) #prints 1 as it is the first element of the tuple
    total = sum(number)
    return total

result = add(1, 2, 3, 4, 5)
print(result)  # Output: 15
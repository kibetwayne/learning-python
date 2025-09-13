import math


#📑📑ARITHMETIC OPERATORS
print(3 + 2)   # Addition
print(3 - 2)   # Subtraction
print(3 * 2)   # Multiplication
print(3 / 2)   # Division
print(3 // 2)  # Floor Division discarding any remainder resulting in 1
print(3 ** 2)  #exponation
print(3 % 2)   #modulus (remainder)

#📑📑   ARGUMENTED ASSINGMENT OPERATOR
x = 10
x += 5
x2 = 10
x2 -= 5
x3 = 10
x3 *= 5
x4 = 10
x4 /= 5

print(f'x= {x}')
print(f'x2= {x2}')
print(f'x3= {x3}')
print(f'x4= {x4}')

#👉incrementing values
num = 1
num += 1
print(num)

example_1 = '100'
example_2 = '200'
print(int(example_1) + int(example_2)) #turn string to integer

##decimal places
number = 3.14159
print(round(number, 3))
print(f'{number:.2f}')

#📑📑INPUT
first = float(input('enter first number '))
second = float(input('enter second number '))

sum = first + second
print('sum is '+sum) #wont work because you are trying to add a string to a float
print(f'the sum is {sum}')

#📑📑methods
#1. max
print(max(1, 2, 3, 4, 5))  # Output: 5 (maximum value)
#2. min           
print(min(1, 2, 3, 4, 5))  # Output: 1 (minimum value)
#3. abs
print(abs(-10))  # Output: 10 (absolute value)
#4. round
print(round(3.14159, 2))  # Output: 3.14
print(round(3.14159)) # Output: 3 (rounds to the nearest integer)
#5. pow
print(pow(2, 3))  # Output: 8 (2 raised to the power of 3)
#6. sort
print(sorted([5, 2, 9, 1]))  # Output: [1, 2, 5, 9] (sorted list)
#7. sum
print(sum([1, 2, 3, 4, 5]))  # Output: 15 (sum of the list)
#8. divmod
print(divmod(10, 3))  # Output: (3, 1) (quotient and remainder)
#9. math.floor()
print(math.floor(3.7))  # Output: 3 (rounds down to the nearest integer)
#10. math.ceil()
print(math.ceil(3.2))  # Output: 4 (rounds up to the nearest integer)
#11. math.trunc()
print(math.trunc(3.9))  # Output: 3 (removes the decimal part)
#12. int()
print(int(3.9))  # Output: 3 (converts float to integer by truncating)

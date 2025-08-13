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

print(abs(-2.7)) 
print(round(3.14159)) # Output: 3 (rounds to the nearest integer)
print(round(3.75, 2)) # Output: 3.14 (rounds to 2 decimal places)

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
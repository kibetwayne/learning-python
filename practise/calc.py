

#add
def add(n1, n2):
    return n1 + n2

#asubtract
def subtract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

num1 = int(input('whats your first number: '))
num2 = int(input('whats your second number: '))

for sign in operations:
    print(sign) 
    
symbol = input('pick an operation symbol: ')

operation = operations[sign]
answer = operation(num1, num2)

print(answer)
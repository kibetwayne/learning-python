

num1 = input('enter the first number: ')
num2 = input('enter the second number: ')
operation = input('enter the operation sign: ')
result = 0

def calculations(num1, num2, operation):
    if operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation in ['^', '**']: #same as operation == ** or operation == ^
        result = num1 ** num2
    else:
       print ('Invalid operation')
    
if num1.isnumeric() and num2.isnumeric:
    calculations(num1, num2, operation)
    print('Result:', result)
else:
    print( 'please enter a number')
    
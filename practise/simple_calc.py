num1 = input('enter the first number: ')
num2 = input('enter the second number: ')
operation = input('enter the operation sign: ')

def calculations(num1, num2, operation):
    if operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2 if num2 != 0 else print('trying to divide by 0')
    elif operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation in ['^', '**']: #same as operation == ** or operation == ^
        return num1 ** num2
    else:
        print ('Invalid operation')

try:
    num1 = float(num1)
    num2 = float(num2)
    result = calculations(num1, num2, operation)
    
    if result != 'Invalid operation':
        print('Result:', result)
    else:
        print(result)
except ValueError:
    print('Please enter valid numbers.')
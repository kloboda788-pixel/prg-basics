###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = float(input('Enter first number: '))
number2 = float(input('Enter second number: '))
operator = input('Enter operator (+, -, *, /): ')
operator_ok = True
if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    if number2 == 0:
        print('Division by zero is not allowed')
        operator_ok = False
    else:
        result = number1 / number2
else:
    operator_ok = False
    print('Invalid operator')

# print result
if operator_ok:
    print(f'{number1} {operator} {number2} = {result}')
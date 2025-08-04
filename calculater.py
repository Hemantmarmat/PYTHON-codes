def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return 'Error: Division by zero'
        return num1 / num2
    elif operator == '**':
        return num1 ** num2
    else:
        return 'Error: Invalid operator'

number1 = float(input('Enter first number: '))
op = input('Enter operator (+,-,*,/,**): ')
number2 = float(input('Enter second number: '))

print(number1, op, number2)
result = calculate(number1, number2, op)
print('=', result)

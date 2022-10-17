# Better calculator

# get input from the user

num1 = float(input('Enter first number: '))
operator = input('Enter operator: ')
num2 = float(input('Enter third number: '))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '/':
    print(num1 / num2)
elif operator == '*':
    print(num1 * num2)
else:
    print("Invalid operator")
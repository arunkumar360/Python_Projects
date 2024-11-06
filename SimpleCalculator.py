num1 = float(input("Enter 1st Number:"))
operator = input("Enter operator(+,-,*,/):")
num2 = float(input("Enter 2nd Number:"))

if operator == '+':
    result = num1 + num2
    print(round(result,2))

elif operator == '-':
    result = num1 - num2
    print(round(result,2))

elif operator == '/':
    result = num1 / num2
    print(round(result,2))

elif operator == '*':
    result = num1 * num2
    print(round(result,2))

else:
    print(f'{operator} is invalid operator!')


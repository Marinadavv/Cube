# задание 2
num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
operator = input('Введите операцию (+, -, *, /, //, **): ')
if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if num2 == 0:
        print('На ноль делить нельзя!')
    else:
        print(num1 / num2)
elif operator == '//':
    if num2 == 0:
        print('На ноль делить нельзя!')
    else:
        print(num1 // num2)
elif operator == '**':
        print(num1 ** num2)

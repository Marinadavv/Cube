# задание 2
a = int(input('Введите первое число'))
b = int(input('Введите второе число'))
c = int(input('Введите третье число'))
print(max(a, b, c))
print(a + b + c - max(a, b, c)- min(a, b, c))
print(min(a, b, c))
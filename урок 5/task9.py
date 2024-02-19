# задание 6
a = float(input('Введите коэффициент а'))
b = float(input('Введите коэффициент b'))
c = float(input('Введите коэффициент c'))
d = (b ** 2) - 4 * a * c
import math
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
elif d == 0:
    print(-b / (2 * a))
else:
    print('Корней нет')
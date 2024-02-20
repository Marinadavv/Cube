# задание 2
num = int(input('Введите число:'))
a = 1
sum = 0
for i in range(1, num + 1):
    a *= i
    sum += a
print(sum)
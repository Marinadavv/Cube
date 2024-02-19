# задание 3
num = int(input('Введите трехзначное число'))
a1 = num // 100
a2 = num % 10
a3 = (num // 10) % 10
symm = (a1 + a2 + a3) - min(a1, a2, a3) - max(a1, a2, a3)
num_min = min(a1, a2, a3)
num_max = max(a1, a2, a3)
if (num_max - num_min) == symm:
    print('прикольное')
else:
    print('не прикольное')
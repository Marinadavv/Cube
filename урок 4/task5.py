# задание 5
a = int(input())
if (a % 7 == 0 or a % 17 == 0) and (a >= 1000 and a <= 9999):
    print('Красивое')
else:
    print('Страшное')
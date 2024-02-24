number = int(input("Введите число: "))
n = -1 
while number > 0:
    i = number % 10
    if i % 2 == 0 and i > n:
        n = i
    number = number // 10
if n != -1:
    print (n)
else:
    print('0')
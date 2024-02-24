n = int(input("Введите количество карт: "))
sum1 = n * (n + 1) // 2
sum2 = sum(int(input("Введите номер карты: ")) 
           for _ in range(n - 1))
n1 = sum1 - sum2
print(n1)
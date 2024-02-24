n = int(input("Введите натуральное число n: "))
total = 1
for i in range(1, n + 1):
    total *= i
print(total)
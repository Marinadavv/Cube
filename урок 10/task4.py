s = int(input("Введите число n: "))
list = [[i for i in range(1, s + 1)] for _ in range(s)]
for i in list:
    print(i)

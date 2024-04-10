# творческое задание сортировка пустыми вставками
number = [4, 2, 1, 3, 5]
n = len(number)
for i in range(1, n):
    for j in range(i, 0, -1):
        if number[j] < number[j-1]:
            number[j], number[j-1] = number[j-1], number[j]
        else:
            break
print(number)
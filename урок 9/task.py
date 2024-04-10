# творческое задание сортировка выбором
numbers = [4, 2, 1, 3, 5]
n = len(numbers)
for i in range(n - 1):
    min = numbers[i]
    min1 = i
    for j in range(i+1, n):
        if min > numbers[j]:
            min = numbers[j]
            min1 = j
    if min1 != i:
        a = numbers[i]
        numbers[i] = numbers[min1]
        numbers[min1] = a
print(numbers)
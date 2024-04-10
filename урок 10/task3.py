list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total = 0
for row in list1:
    for number in row:
        total += number
count = 0
for row in list1:
    count += len(row)
result = total / count
print(result)

numbers = []
while True:
    numbers1 = input()
    if numbers1 == 'СТОП':
        break
    numbers.append(int(numbers1))
top3max = sorted(numbers, reverse=True)[:3]
print(*top3max, sep=',')
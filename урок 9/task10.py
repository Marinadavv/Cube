s = input()
numbers = s.split()
total = 0
for num in numbers:
    if int(num) > 50:
        total += 1
print(total)

s = input()
numbers = [int(i) for i in s.split()]
numbers1 = []
for i in numbers:
    if i % 2 == 0:
        numbers3 = i ** 2      
        if numbers3 % 10 != 4:          
            numbers1.append(numbers3)
print(*numbers1)

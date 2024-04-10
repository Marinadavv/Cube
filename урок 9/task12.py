s = input()
numbers = s.split()
min1 = numbers.index(min(numbers))
max1 = numbers.index(max(numbers))
numbers[min1], numbers[max1] = numbers[max1], numbers[min1]
print(*numbers)
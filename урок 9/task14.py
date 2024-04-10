s = input()
numbers = [int(i) for i in s.split()]
s1 = numbers.copy()
s1.sort()
s2 = numbers.copy()
s2.sort(reverse=True)
print("по возрастанию:", s1)
print("по убыванию:", s2)
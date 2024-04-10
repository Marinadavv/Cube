n = int(input())
strings = []
for _ in range(n):
    s = input()
    if s in strings:
        continue
    strings.append(s)
print('вывод:')
for s in strings:
    print(s)

n = int(input())
strings = []
for _ in range(n):
    s = input()
    strings.append(s)
string1 = input()
print("вывод:")
for s in strings:
    if string1 in s:
        print(s)

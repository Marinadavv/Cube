s = int(input())
strings = []
for i in range(s):
    string = input()
    strings.append(string)
s1 = int(input())
result = [word[s1 - 1] for word in strings if len(word) >= s1]
print(*result)

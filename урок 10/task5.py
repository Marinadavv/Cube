s = input().split()
lst = [[s[0]]]
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        lst[-1].append(s[i])
    else:
        lst.append([s[i]])
print(lst)

s = 'abcdefghijklmnopqrstuvwxyz'
s1 = []
for i in range(1, 27):
    x = s[i-1] * i
    s1.append(x)
print(s1)
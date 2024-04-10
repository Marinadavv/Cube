s = input()
words = s.split()
s1 = min(words, key=len)
s2 = max(words, key=len)
min1 = words.index(min(words))
max1 = words.index(max(words))
words[min1], words[max1] = s2, s1
print(*words)
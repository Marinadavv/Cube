# задание 4
a = input('Введите первое имя')
b = input('Введите второе имя')
c = input('Введите третье имя')
len_a = len(a)
len_b = len(b)
len_c = len(c)
if min(len_a,len_b,len_c) == len_a:
    print(a)
elif min(len_a,len_b,len_c) == len_b:
    print(b)
elif min(len_a,len_b,len_c) == len_c:
    print(c)
if max(len_a,len_b,len_c) == len_a:
    print(a)
elif max(len_a,len_b,len_c) == len_b:
    print(b)
elif max(len_a,len_b,len_c) == len_c:
    print(c)
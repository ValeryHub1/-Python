a1 = int(input("Введите число без пробела: "))
a2 = []
if 1 <= a1 <= 1000000:
    a2.append(a1)

a = list(map(int, input("Введите строку чисел с пробелами: ").split())) 
i = len(a) - 1 
while i > 0: 
    if a[i] <= i <= 1000000: 
        a.insert(i + 1) 
    i -= 1 
a = a[-1:] + a[:-1]

print(a, a2)

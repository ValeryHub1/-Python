a = int(input("Введите количество чисел: "))
for i in range(a):
    a1 = str(input("Введите строку чисел с пробелами: "))
    b = a1.split(' ')

c = set(b)

print(len(c))
n = int(input("Введите количество элементов: "))
b = []
for i in range(n):
    a = int(input("Введите значение элемента: "))
    if 1 <= a <= 1000000:
        b.append(a)
b.reverse()
print(b)


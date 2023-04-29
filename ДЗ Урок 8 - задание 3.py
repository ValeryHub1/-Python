m = int(input("Введите сколько лодка выдерживает кг одна лодка: "))
n = int(input("Введите количество рыбаков: "))
a = []
b = []
for i in range(n):
    a.append(int(input("Вес рыбока: ")))
 
for x in range(len(a)):
    if a[x] + min(a) <= m:
        b += [[a[x], min(a)]]
        a[x] += m
        a[a.index(min(a))] += m
    else:
        if a[x] > m:
            continue
        else:
            b += [[a[x]]]
print(len(b))

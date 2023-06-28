a = set()

for i in input("Введите строку чисел через пробел: ").split():
    if i not in a:
        a.add(i)
        print("No")
    else:
        print("YES")

from math import factorial
a = int(input("Введите число: "))
print(factorial(a))

def factorial(a):
    if a == 0:
        return 1
    return factorial(a - 1) * a

b = int(input("Введите число, факториал которого нужно вычислить: "))

for i in range(b, 0, -1):
    print(factorial(i))
n = int(input("Введите сколько будет чисел: "))
cnt = 0
for i in range(1, n+1):
    a = int(input("Введите число: "))
    n -= 1

    if a == 0 :
        cnt += 1
print("=", cnt)


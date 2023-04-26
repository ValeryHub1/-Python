mini = int(input("Минимальная сумма инвестиций: "))
mikl = int(input("Сумма у Майкала: "))
ivan = int(input("Сумма у Ивана: "))

if (mikl >= mini) and (ivan >= mini):
    print(2)

elif (mikl >= mini) and (ivan <= mini):
    print("Mike")

elif (mikl <= mini) and (ivan >= mini):
    print("Ivan")

elif (mikl <= mini) and (ivan <= mini) and ((mikl + ivan) >= mini):
    print(1)

elif (mikl <= mini) and (ivan <= mini):
    print(0)
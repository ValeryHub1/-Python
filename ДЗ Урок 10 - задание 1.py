pets = {}
pets2 = {}

while (True):
    a = input("Введите имя питомца  (клавиша enter - выход): ")
    if a == "":
        break
    else:
        b = input("Введите вид питомца: ")
        c = int(input("Введите возраст: "))
        d = ""
    if c % 10 == 1 and c != 11 and c % 100 != 11:
        d = 'год'
    elif 1 < c % 10 <= 4 and c != 12 and c != 13 and c != 14:
        d = 'года'
    else:
        d = 'лет'
    e = input('Имя владельца: ')
    pets[a] = pets2
pets2 = {'Вид питомца:': b, 'Возраст питомца:': c, 'Имя владельца:': e}

for i in pets.keys():
    print("Это", pets2['Вид питомца:'], "по кличке", i,". Возраст питомца:", pets2['Возраст питомца:'], d, "Имя владельца:", pets2['Имя владельца:'])
print(pets)
print(pets2)
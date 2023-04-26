slovo = input("Введите слово: ")

e=slovo.count('e')
a=slovo.count('a')
i=slovo.count('i')
u=slovo.count('u')
o=slovo.count('o') 

schetglas=e+a+i+u+o

print("Всего гласных",schetglas)

print("Всего согласных",len(slovo)-schetglas)

if (e==0):
    print ("Гласной e в слове False")

else:
    print("e =",e)

if (u==0):
    print ("Гласной u в слове False")

else:
    print("u =",u)

if (o==0):
    print ("Гласной o в слове False")

else:
    print("o =",o)

if (a==0):
    print ("Гласной a в слове False")

else:
    print("a =",a)

if (i==0):
    print ("Гласной i в слове False")

else:
    print("i =",i)

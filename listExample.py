pierwszyElement = 4
lista = list()
l = list()

print("zawartość listy: ", lista)
print()
lista.append(pierwszyElement)
print("zawartość listy: ", lista)

lista.append(6)
lista.append(10)
print("nowa zawartość listy: ", lista)

ileElementow = len(lista)
print("Moja lista ma nastepujaca liczbe elementow", ileElementow)
print()

for elementListy in lista:
    print("jestem w srodku petli")
    print("element jest rowny: ", elementListy)

print("koniec programu")
input()
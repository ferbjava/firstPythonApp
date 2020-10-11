import random

print("Witaj w grze 'zgadywanka'!")
# print("Jaką Liczbę z zakresu 1-10 mam na myśli?")
gornyLimit = int(input("W jakim zakresie mam wygenerować liczbę do zgadnięcia? "))
wynikLosowania = random.randint(1, gornyLimit)
musiZgadywac = True

while musiZgadywac:
    typUzytkownika = int(input("Podaj liczbe: "))
    if wynikLosowania == typUzytkownika:
        musiZgadywac = False
        print("Brawo, zgadłeś!")
    else:
        print("Niestety, nie jest to prawidłowa odpowiedź :-( Spróbuj jeszcze raz!")

print("koniec gry!")
input()
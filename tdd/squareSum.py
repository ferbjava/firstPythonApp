###########################################################################################
# Twoim zadanie jest obliczenie sumu kwadratów dla liczb podanych w tablicy, na przyklad:
# [1, 2] -> 1**2 + 2**2 = 1 + 4 = 5
# [0, 3, 4, 5] -> 0**2 + 3**2 + 4**2 + 5**2 = 0 + 9 + 16 + 25 = 50
#
# Tablica to obiekt w pythonie do przechowywania wiekszej liczby danych
# indeks oznacza miejsce w tablicy, gdzie przychowywany jest konkretny element
#
#         indeks '0'   indeks '1'   indeks '2'  indeks '3'
#            ^            ^            ^
# tablica = [5,           6,           12,        2]
#
# dlatego:
# tablica[1] = 6
# tablica[3] = 2
# tablica[0] = 5
#
# Podpowiedz do zadania:
# jak widzisz w drugim przykladzie, 4 razy wykonujesz to samo dzialanie matematyczne
# dlatego w rozwiazaniu uzyj petli
#
############################################################################################


def suma_kwadratow(liczby):
    print("drukuje wszystkie elementy w tablicy: ", liczby)
    print("drukuje pierwszy element w tablicy (numerowanie od 0!): ", liczby[0])
    print("drukuje drugi element w tablicy: ", liczby[1])
    print("drukuje drugi element w tablicy podniesiony do kwadratu ", liczby[1]**2)
    return 0


assert suma_kwadratow([1, 2]) == 5
assert suma_kwadratow([0, 3, 4, 5]) == 50

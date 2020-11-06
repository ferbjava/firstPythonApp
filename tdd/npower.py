###############################################################################################
# Twoim zadanie jest obliczenie n-tej potegi elementu tablicy o indeksie n, na przyklad:
# index([1, 2,], 1) -> index[1] = 2 -> 2**1 = 2
#
# Tablica to obiekt w pythonie do przechowywania wiekszej liczby danych
# indeks oznacza miejsce w tablicy, gdzie przychowywany jest konkretny element
#
#         indeks '0'   indeks '1'   indeks '2'  indeks '3'
#            ^            ^            ^
# tablica = [10,           3,           4,        5]
#
# dlatego:
# tablica[0] = 10
# tablica[1] = 3
# tablica[1] = 4
# tablica[3] = 5
#
#
# Podpowiedz do zadania:
# operacja modulo - reszta z dzielenia  3 % 2 =1
# petla : for x in [4,5,6]:
#
############################################################################################

def index(array, n):
    return 0


assert index([1, 2, 3, 4], 2) == 9
assert index([1, 3, 10, 100], 3) == 1000000
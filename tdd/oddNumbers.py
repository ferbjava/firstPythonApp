###############################################################################################
# Twoim zadanie jest obliczenie ile liczb nieparzystych zawiera wejsciowa tablica, na przyklad:
# [1, 2] -> 1?nieparzysta:1 + 2?nieparzysta:0 = 1 + 0 = 1
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


def ile_nieparzystych(liczby):
    print("drukuje wszystkie elementy w tablicy: ", liczby)
    print("drukuje pierwszy element w tablicy (numerowanie od 0!): ", liczby[0])
    print("drukuje drugi element w tablicy: ", liczby[1])
    print("drukuje 1 jesli drugi element jest nieparzysty lub 0 w przeciwnym przypadku: ", liczby[1] % 2 )
    print("drukuje sume JEDYNEK i ZEROWEK :", liczby[0] % 2 + liczby[1] % 2)
    print("drukuje zawartosc tablicy : ")
    for x in [4,5,6,8,10]:
        print(x)

    return 1


assert ile_nieparzystych([10, 3, 4, 5]) == 2
#assert ile_nieparzystych([1, 2]) == 1
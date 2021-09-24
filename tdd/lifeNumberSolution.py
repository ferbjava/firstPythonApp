###############################################################################################
# Twoim zadanie jest obliczenie 'cyfry zycia', ktora jest wynikiem sumowania cyfr w twojej
# dacie urodzenia, do otrzymania pojedynczej cyfry. Date podajesz w nastepujacym formacie:
# "yyyy-mm-dd"
#
# dla daty: 14 marzec 1897 obliczenia wygladają następująco
# rok: 1 + 8 + 7 + 9 = 25; 2 + 5 = 7
# miesiąc (marzec): 0 + 3 = 3
# dzien: 1 + 4 = 5
# finalny wynik: 7 + 3 + 5 = 15; 1 + 5 = 6
#
#
# Podpowiedz do zadania:
# Zmienne tekstowe (Stringi) to tak naprawde tablice. Uzyj ich, oraz prostej nieskonczonej petli
# w celu obliczenia wyniku
# Zaponaj się z wbudowana metoda dla zmiennych tekstowych 'split'
#
############################################################################################


def life_path_number(dataUrodzenia):
    date = dataUrodzenia.split("-")
    yearSum = digits_sum(date[0])
    monthSum = digits_sum(date[1])
    daySum = digits_sum(date[2])
    return int(digits_sum(yearSum+monthSum+daySum))

def digits_sum(number):
    tempNumber = number
    while tempNumber > 9:
        sum = 0
        for digit in tempNumber:
            sum += int(digit)
        tempNumber = str(sum)
    return tempNumber

assert life_path_number("1955-10-28") == 4
assert life_path_number("1971-06-28") == 7
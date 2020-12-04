import re
import random

class TicTacToeGame:

    def __init__(self):
        self.zawodnik = ""
        self.komputer = ""
        self.ostatniRuch = "X"
        self.koniecGry = False
        self.pola = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def __wyswietlPowitanie(self):
        print("######################################")
        print("\nHej! chcesz zagrac w kolko i krzyzyk?\n")

    def __wyborZawodnika(self):
        print("Wybierz zawodnika:\n")
        while len(self.zawodnik) == 0:
            wybor = input("kolko - [O], czy krzyzyk [X]? ")
            if (wybor.upper() == "O" or wybor.upper() == "X"):
                self.zawodnik = wybor.upper()
                self.komputer = "X" if self.zawodnik == "O" else self.komputer == "O"
                print("Twoj wybor to:", self.zawodnik)
            else:
                print("Niedozwolony wybor! Sprobuj jeszcze raz")

    def __wyswietlPlansze(self):
        poleGry = "######################################"
        poleGry += "\n     A   B   C"
        poleGry += "\n "
        poleGry += "\n 1  " + self.pola[0][0] + "  | " + self.pola[0][1] + " | " + self.pola[0][2] + " "
        poleGry += "\n    ___|___|___"
        poleGry += "\n 2   " + self.pola[1][0] + " | " + self.pola[1][1] + " | " + self.pola[1][2] + " "
        poleGry += "\n    ___|___|___"
        poleGry += "\n 3   " + self.pola[2][0] + " | " + self.pola[2][1] + " | " + self.pola[2][2] + " "
        poleGry += "\n       |   |   "
        poleGry += "\n"
        poleGry += "\n######################################"
        print(poleGry)

    def graj(self):
        self.__wyswietlPowitanie()
        self.__wyborZawodnika()
        self.__wyswietlPlansze()
        while not self.koniecGry:
            if (self.ostatniRuch != self.zawodnik):
                self.grajRuchZawodnika()
                self.ostatniRuch = self.zawodnik
            else:
                self.grajRuchKomputera()
                self.ostatniRuch = self.komputer

    def grajRuchZawodnika(self):
        czyRuchPoprawny = False
        print("\nTwoj ruch!\n")
        while not czyRuchPoprawny:
            ruch = input()
            czyRuchWPlanszy = self.sprawdzCzyWPlanszy(ruch)
            if not czyRuchWPlanszy:
                print("Ruch poza plansza! Sprobuj jeszcze raz")
                continue
            ruch = self.przeliczWspolrzedne(ruch)
            czyRuchNaWolnePole = self.sprawdzCzyWolnePole(ruch)
            if not czyRuchNaWolnePole:
                print("Pole już zajete! Sprobuj jeszcze raz")
                continue
            czyRuchPoprawny = czyRuchWPlanszy and czyRuchNaWolnePole
        self.pola[int(ruch[0])][int(ruch[1])] = self.zawodnik
        self.__wyswietlPlansze()
        self.sprawdzCzyWygrana()

    def grajRuchKomputera(self):
        czyRuchPoprawny = False
        ruchKomputera = ""
        while not czyRuchPoprawny:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            ruchKomputera = str(x) + str(y)
            czyRuchPoprawny = self.sprawdzCzyWolnePole(ruchKomputera)
        self.pola[int(ruchKomputera[0])][int(ruchKomputera[1])] = self.komputer
        self.__wyswietlPlansze()
        self.sprawdzCzyWygrana()

    def przeliczWspolrzedne(self, ruch):
        x = int(ruch[1]) - 1
        y = ord(ruch[0].upper()) - 65
        return str(x) + str(y)

    def sprawdzCzyWPlanszy(self, ruch):
        return False

    def sprawdzCzyWolnePole(self, ruch):
        return False

    def sprawdzCzyWygrana(self):
        return

if __name__ == "__main__":
    mojaGra = TicTacToeGame()
    mojaGra.graj()

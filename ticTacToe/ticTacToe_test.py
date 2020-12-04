import unittest
from ticTacToeGame import TicTacToeGame


class TicTacToeGameTest(unittest.TestCase):
    def setUp(self):
        self.gra = TicTacToeGame()


class TestGame(TicTacToeGameTest):
    def test_czy_w_planszy_01(self):
        ruch = "A1"
        self.assertTrue(self.gra.sprawdzCzyWPlanszy(ruch))

    def test_czy_w_planszy_02(self):
        ruch = "cx"
        self.assertFalse(self.gra.sprawdzCzyWPlanszy(ruch))

    def test_czy_w_wolne_pole_01(self):
        plansza = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        ruch = "A1"
        self.gra.pola = plansza
        ruch = self.gra.przeliczWspolrzedne(ruch)
        self.assertTrue(self.gra.sprawdzCzyWolnePole(ruch))

    def test_czy_w_wolne_pole_02(self):
        plansza = [["O", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        ruch = "A1"
        self.gra.pola = plansza
        ruch = self.gra.przeliczWspolrzedne(ruch)
        self.assertFalse(self.gra.sprawdzCzyWolnePole(ruch))

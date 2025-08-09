import unittest
from tablero import Tablero, PosOcupadaException

class TestTablero(unittest.TestCase):
    def test_poner_ficha_libre(self):
        tablero = Tablero()
        tablero.poner_ficha(0, 0, "X")
        self.assertEqual(tablero.contenedor[0][0], "X")

    def test_poner_ficha_ocupada(self):
        tablero = Tablero()
        tablero.poner_ficha(0, 0, "X")
        with self.assertRaises(PosOcupadaException):
            tablero.poner_ficha(0, 0, "O")

if __name__ == "__main__":
    unittest.main()

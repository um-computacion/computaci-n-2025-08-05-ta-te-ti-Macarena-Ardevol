import unittest
from tateti import Tateti

class TestTateti(unittest.TestCase):
    def test_ocupar_casilla_libre_cambia_turno(self):
        juego = Tateti()
        self.assertEqual(juego.turno, "X")
        exito = juego.ocupar_casilla(0, 0)
        self.assertTrue(exito)
        self.assertEqual(juego.tablero.contenedor[0][0], "X")
        self.assertEqual(juego.turno, "O")

    def test_ocupar_casilla_ocupada(self):
        juego = Tateti()
        juego.ocupar_casilla(0, 0)
        exito = juego.ocupar_casilla(0, 0)
        self.assertFalse(exito)

    def test_chequear_ganador_fila(self):
        juego = Tateti()
        juego.tablero.contenedor[0] = ["X", "X", "X"]
        self.assertTrue(juego.chequear_ganador(0, 1))

    def test_chequear_ganador_columna(self):
        juego = Tateti()
        for i in range(3):
            juego.tablero.contenedor[i][2] = "O"
        self.assertTrue(juego.chequear_ganador(1, 2))

    def test_chequear_ganador_diagonal(self):
        juego = Tateti()
        for i in range(3):
            juego.tablero.contenedor[i][i] = "X"
        self.assertTrue(juego.chequear_ganador(2, 2))

    def test_chequear_ganador_diagonal_secundaria(self):
        juego = Tateti()
        for i in range(3):
            juego.tablero.contenedor[i][2 - i] = "O"
        self.assertTrue(juego.chequear_ganador(1, 1))

    def test_tablero_lleno(self):
        juego = Tateti()
        juego.tablero.contenedor = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", ""]
        ]
        self.assertFalse(juego.tablero_lleno())
        juego.tablero.contenedor[2][2] = "X"
        self.assertTrue(juego.tablero_lleno())

if __name__ == "__main__":
    unittest.main()

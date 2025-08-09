import unittest
from jugador import Jugador

class TestJugador(unittest.TestCase):
    def test_crear_jugador(self):
        jugador = Jugador("Ana", "X")
        self.assertEqual(jugador.nombre, "Ana")
        self.assertEqual(jugador.ficha, "X")

if __name__ == "__main__":
    unittest.main()

from tablero import Tablero, PosOcupadaException

class Tateti:
    def __init__(self):
        self.turno = "X"  
        self.tablero = Tablero()

    def cambiar_turno(self):
        """Alterna entre jugador X y O."""
        self.turno = "O" if self.turno == "X" else "X"

    def ocupar_casilla(self, fila, col):
        """Intenta poner una ficha en la posición indicada."""
        try:
            self.tablero.poner_ficha(fila, col, self.turno)
            self.cambiar_turno()
        except PosOcupadaException as e:
            print(e)

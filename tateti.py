from tablero import Tablero, PosOcupadaException

class Tateti:
    def __init__(self):
        self.turno = "X"
        self.tablero = Tablero()
        self.ganador = None

    def cambiar_turno(self):
        self.turno = "O" if self.turno == "X" else "X"

    def ocupar_casilla(self, fila, col):
        try:
            self.tablero.poner_ficha(fila, col, self.turno)
            if self.chequear_ganador(fila, col):
                self.ganador = self.turno
            else:
                self.cambiar_turno()
        except PosOcupadaException as e:
            print(e)

    def chequear_ganador(self, fila, col):
        ficha = self.tablero.contenedor[fila][col]

        # Verificar fila
        if all(c == ficha for c in self.tablero.contenedor[fila]):
            return True

        # Verificar columna
        if all(self.tablero.contenedor[r][col] == ficha for r in range(3)):
            return True

        # Verificar diagonal principal
        if fila == col and all(self.tablero.contenedor[i][i] == ficha for i in range(3)):
            return True

        # Verificar diagonal secundaria
        if fila + col == 2 and all(self.tablero.contenedor[i][2 - i] == ficha for i in range(3)):
            return True

        return False

    def tablero_lleno(self):
        return all(all(c != "" for c in fila) for fila in self.tablero.contenedor)

    def juego_terminado(self):
        return self.ganador is not None or self.tablero_lleno()

class PosOcupadaException(Exception):
    """Se lanza cuando se intenta poner una ficha en una posición ocupada."""
    pass

class Tablero:
    def __init__(self):
        self.contenedor = [["" for _ in range(3)] for _ in range(3)]

    def poner_ficha(self, fila, col, ficha):
        """Coloca la ficha en la posición indicada si está libre."""
        if self.contenedor[fila][col] == "":
            self.contenedor[fila][col] = ficha
        else:
            raise PosOcupadaException("Esa posición ya está ocupada")

    def mostrar(self):
        """Muestra el tablero de forma simple."""
        for fila in self.contenedor:
            print(fila)

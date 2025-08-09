from tateti import Tateti
from jugador import Jugador

def main():
    print("Bienvenidos al juego de Tateti")

    nombre1 = input("Nombre del Jugador 1 (X): ")
    nombre2 = input("Nombre del Jugador 2 (O): ")

    jugador1 = Jugador(nombre1, "X")
    jugador2 = Jugador(nombre2, "O")

    juego = Tateti()

    while True:
        print("\nEstado del tablero:")
        juego.tablero.mostrar()
        print(f"Turno de: {juego.turno}")

        try:
            fila = int(input("Ingrese fila (0-2): "))
            col = int(input("Ingrese columna (0-2): "))
            juego.ocupar_casilla(fila, col)
        except ValueError:
            print("Por favor, ingrese un número válido.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

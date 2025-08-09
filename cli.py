from tateti import Tateti
from jugador import Jugador

def main():
    print("Bienvenidos al juego de Ta-Te-Ti")
    print("Para salir en cualquier momento, ingrese 'salir'.")
    print("Para reiniciar el juego, ingrese 'reiniciar'.\n")

    while True:
        nombre1 = input("Nombre del Jugador 1 (X): ")
        if nombre1.lower() == "salir":
            print("Gracias por jugar. ¡Hasta luego!")
            break
        if nombre1.lower() == "reiniciar":
            print("Reiniciando juego...")
            continue

        nombre2 = input("Nombre del Jugador 2 (O): ")
        if nombre2.lower() == "salir":
            print("Gracias por jugar. ¡Hasta luego!")
            break
        if nombre2.lower() == "reiniciar":
            print("Reiniciando juego...")
            continue

        jugador1 = Jugador(nombre1, "X")
        jugador2 = Jugador(nombre2, "O")

        juego = Tateti()

        while True:
            print("\nEstado del tablero:")
            juego.tablero.mostrar()
            print(f"Turno de: {juego.turno}")

            while True:
                entrada_fila = input("Ingrese fila (1-3): ").strip().lower()
                if entrada_fila == "salir":
                    print("Gracias por jugar. ¡Hasta luego!")
                    return
                if entrada_fila == "reiniciar":
                    print("Reiniciando juego...\n")
                    break

                entrada_col = input("Ingrese columna (1-3): ").strip().lower()
                if entrada_col == "salir":
                    print("Gracias por jugar. ¡Hasta luego!")
                    return
                if entrada_col == "reiniciar":
                    print("Reiniciando juego...\n")
                    break

                try:
                    fila = int(entrada_fila)
                    col = int(entrada_col)

                    if fila not in [1, 2, 3] or col not in [1, 2, 3]:
                        print("Por favor, ingrese números entre 1 y 3.")
                        continue

                    fila -= 1
                    col -= 1

                    if juego.ocupar_casilla(fila, col):
                        break
                except ValueError:
                    print("Por favor, ingrese un número válido.")

            else:
                continue

            if entrada_fila == "reiniciar" or entrada_col == "reiniciar":
                continue

            if juego.chequear_ganador(fila, col):
                juego.ganador = juego.tablero.contenedor[fila][col]
                print(f"\n¡Felicidades! Ganó el jugador {juego.ganador}")
                juego.tablero.mostrar()
                break

            if juego.tablero_lleno():
                print("\n¡Empate! No quedan más movimientos.")
                juego.tablero.mostrar()
                break

        while True:
            resp = input("\n¿Querés jugar otra vez? (s/n): ").strip().lower()
            if resp == "s":
                print("Reiniciando juego...\n")
                break
            elif resp == "n":
                print("Gracias por jugar. ¡Hasta luego!")
                return
            else:
                print("Por favor, ingrese 's' o 'n'.")

if __name__ == "__main__":
    main()

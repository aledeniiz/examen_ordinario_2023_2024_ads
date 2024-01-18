import time

def jugar_partida():
    tiempo_carlsen = 180  
    tiempo_nakamura = 180  
    tiempo_movimiento = 10 

    turno_actual = "Carlsen"

    while True:
        print(f"\nTiempo actual - Carlsen: {tiempo_carlsen} segundos | Nakamura: {tiempo_nakamura} segundos")
        print(f"Turno de {turno_actual}\n")

        if tiempo_carlsen <= 60 or tiempo_nakamura <= 60:
            tiempo_movimiento = 5

        jugador_movimiento = input("Ingrese el nombre del jugador para realizar un movimiento (Carlsen/Nakamura/Salir): ").capitalize()
        if jugador_movimiento == "Salir":
            print("La partida ha finalizado.")
            break
        elif jugador_movimiento == turno_actual:
            if turno_actual == "Carlsen":
                tiempo_carlsen -= tiempo_movimiento
            else:
                tiempo_nakamura -= tiempo_movimiento

            turno_actual = "Nakamura" if turno_actual == "Carlsen" else "Carlsen"
        else:
            print("Nombre de jugador incorrecto. Inténtalo de nuevo.")

        if tiempo_carlsen <= 0 or tiempo_nakamura <= 0:
            print(f"\n¡Tiempo agotado! La partida ha finalizado.")
            if tiempo_carlsen <= 0:
                print("¡Hikaru Nakamura ha ganado!")
            else:
                print("¡Magnus Carlsen ha ganado!")
            break

if __name__ == "__main__":
    jugar_partida()
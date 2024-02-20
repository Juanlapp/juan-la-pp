import random

def tirar_dado():
    return random.randint(1, 6)

def determinar_ganador(jugador1, jugador2):
    if jugador1 > jugador2:
        return "Álvaro"
    elif jugador2 > jugador1:
        return "Bárbara"
    else:
        return "Empate"

def main():
    print("¡Bienvenidos al juego de lanzamiento de dados!")
    input("Presiona Enter para lanzar los dados...")

    valor_alvaro = tirar_dado()
    valor_barbara = tirar_dado()

    print("Álvaro ha lanzado el dado y ha obtenido:", valor_alvaro)
    print("Bárbara ha lanzado el dado y ha obtenido:", valor_barbara)

    ganador = determinar_ganador(valor_alvaro, valor_barbara)
    if ganador == "Empate":
        print("¡Hubo un empate!")
    else:
        print("¡El ganador es:", ganador, "!")

if __name__ == "__main__":
    main()
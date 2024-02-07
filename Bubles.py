import random

def jugar_adivina_numero():
    numero_secreto = random.randint(1, 10)
    intentos = 0

    print("¡Bienvenido al juego Adivina el número!")
    print("Estoy pensando en un número entre 1 y 10. ¿Puedes adivinar cuál es?")

    while True:
        intento = int(input("Introduce tu suposición: "))
        intentos += 1

        if intento < numero_secreto:
            print("El número es más alto. ¡Intenta de nuevo!")
        elif intento > numero_secreto:
            print("El número es más bajo. ¡Intenta de nuevo!")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
            break

if __name__ == "__main__":
    jugar_adivina_numero()
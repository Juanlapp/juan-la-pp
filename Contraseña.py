def main():
    # Contraseña almacenada
    contraseña_correcta = "Juan la pp"

    # Bucle para solicitar la contraseña al usuario
    while True:
        contraseña_ingresada = input("Ingrese la contraseña: ")

        # Comprobar si la contraseña ingresada es correcta
        if contraseña_ingresada == contraseña_correcta:
            print("¡Contraseña correcta! Bienvenido al sistema. ")
            break
        else:
            print("Contraseña es incorrecta, Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
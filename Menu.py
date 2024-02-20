def ejercicio_1():
    print("Bienvenido al Ejercicio 1")
    # Aquí va el código del ejercicio 1

def ejercicio_2():
    print("Bienvenido al Ejercicio 2")
    # Aquí va el código del ejercicio 2

def ejercicio_3():
    print("Bienvenido al Ejercicio 3")
    # Aquí va el código del ejercicio 3

def mostrar_menu():
    print("Menú Principal:")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    main()
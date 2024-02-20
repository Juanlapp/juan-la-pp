def añadir_numero(lista):
    numero = int(input("Ingrese un número para añadir a la lista: "))
    lista.append(numero)
    print(f"Se añadió el número {numero} a la lista.")

def añadir_numero_posicion(lista):
    numero = int(input("Ingrese un número: "))
    posicion = int(input("Ingrese la posición donde desea añadir el número (empezando desde 1): "))
    if 1 <= posicion <= len(lista) + 1:
        lista.insert(posicion - 1, numero)
        print(f"Se añadió el número {numero} en la posición {posicion} de la lista.")
    else:
        print("Posición inválida.")

def longitud_lista(lista):
    print(f"La longitud de la lista es: {len(lista)}")

def eliminar_ultimo_numero(lista):
    if lista:
        ultimo_numero = lista.pop()
        print(f"Se eliminó el último número de la lista: {ultimo_numero}")
    else:
        print("La lista está vacía.")

def eliminar_numero(lista):
    posicion = int(input("Ingrese la posición del número que desea eliminar (empezando desde 1): "))
    if 1 <= posicion <= len(lista):
        numero_eliminado = lista.pop(posicion - 1)
        print(f"Se eliminó el número {numero_eliminado} de la lista.")
    else:
        print("Posición inválida.")

def contar_numeros(lista):
    numero = int(input("Ingrese un número para contar sus apariciones en la lista: "))
    apariciones = lista.count(numero)
    print(f"El número {numero} aparece {apariciones} veces en la lista.")

def posiciones_numero(lista):
    numero = int(input("Ingrese un número para encontrar sus posiciones en la lista: "))
    posiciones = [i + 1 for i, num in enumerate(lista) if num == numero]
    if posiciones:
        print(f"El número {numero} está en las posiciones: {', '.join(map(str, posiciones))}")
    else:
        print(f"El número {numero} no está en la lista.")

def mostrar_numeros(lista):
    print("Los números en la lista son:")
    for numero in lista:
        print(numero)

def main():
    lista = []
    while True:
        print("\nMenú:")
        print("1. Añadir número a la lista")
        print("2. Añadir número de la lista en una posición")
        print("3. Longitud de la lista")
        print("4. Eliminar el último número")
        print("5. Eliminar un número")
        print("6. Contar números")
        print("7. Posiciones de un número")
        print("8. Mostrar números")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            añadir_numero(lista)
        elif opcion == "2":
            añadir_numero_posicion(lista)
        elif opcion == "3":
            longitud_lista(lista)
        elif opcion == "4":
            eliminar_ultimo_numero(lista)
        elif opcion == "5":
            eliminar_numero(lista)
        elif opcion == "6":
            contar_numeros(lista)
        elif opcion == "7":
            posiciones_numero(lista)
        elif opcion == "8":
            mostrar_numeros(lista)
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
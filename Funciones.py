def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "No se puede dividir entre cero."

while True:
    print("\nMenú:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Seleccione una opción (1/2/3/4/5): ")

    if opcion == '5':
        print("¡Hasta luego!")
        break

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        print("El resultado de la suma es:", sumar(num1, num2))
    elif opcion == '2':
        print("El resultado de la resta es:", restar(num1, num2))
    elif opcion == '3':
        print("El resultado de la multiplicación es:", multiplicar(num1, num2))
    elif opcion == '4':
        print("El resultado de la división es:", dividir(num1, num2))
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
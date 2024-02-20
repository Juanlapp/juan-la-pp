def calcular_precio_entrada(edad):
    if edad < 4:
        precio = 0
    elif 4 <= edad <= 18:
        precio = 30000
    else:
        precio = 50000
    return precio

def main():
    try:
        edad = int(input("Ingrese la edad del cliente: "))
        if edad < 0:
            print("La edad no puede ser negativa.")
        else:
            precio_entrada = calcular_precio_entrada(edad)
            if precio_entrada == 0:
                print("El cliente puede entrar gratis.")
            else:
                print("El precio de la entrada es:", precio_entrada)
    except ValueError:
        print("Por favor, ingrese un número entero para la edad.")

if __name__ == "__main__":
    main()
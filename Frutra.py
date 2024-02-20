def calcular_precio(fruta, cantidad, precios):
    if fruta in precios:
        precio_unitario = precios[fruta]
        precio_total = precio_unitario * cantidad
        return precio_total
    else:
        return "Error: La fruta especificada no está en el diccionario de precios."

def main():
    precios_frutas = {
        "manzana": 2,
        "plátano": 1.5,
        "naranja": 3,
        "uva": 4,
        "pera": 2.5
    }

    while True:
        fruta = input("Ingrese el nombre de la fruta: ").lower()
        cantidad = int(input("Ingrese la cantidad vendida: "))

        precio = calcular_precio(fruta, cantidad, precios_frutas)
        print(f"Precio total: {precio}")

        continuar = input("¿Desea hacer otra consulta? (s/n): ")
        if continuar.lower() != "s":
            break

if __name__ == "__main__":
    main()
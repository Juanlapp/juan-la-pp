def mostrar_cesta(cesta):
    print("Lista de la compra:")
    total = 0
    for articulo, precio in cesta.items():
        print(f"{articulo}: ${precio}")
        total += precio
    print(f"Coste total: ${total}")

def main():
    cesta = {}
    while True:
        articulo = input("Ingrese el nombre del artículo (o 'fin' para terminar): ")
        if articulo.lower() == 'fin':
            break
        precio = float(input(f"Ingrese el precio de {articulo}: "))
        cesta[articulo] = precio

    mostrar_cesta(cesta)

if __name__ == "__main__":
    main()
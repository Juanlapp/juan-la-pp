def calcular_promedio_alturas(alturas):
    total = sum(alturas)
    promedio = total / len(alturas)
    return promedio

def main():
    alturas = []
    for i in range(3):
        altura = float(input(f"Ingrese la altura de la persona {i+1}: "))
        alturas.append(altura)

    promedio = calcular_promedio_alturas(alturas)
    print("El promedio de altura de las personas es:", promedio)

if __name__ == "__main__":
    main()
def obtener_notas_alumno():
    notas = []
    while True:
        nota_str = input("Introduce una nota (introduce un número negativo para terminar): ")
        nota = float(nota_str)
        if nota < 0:
            break
        notas.append(nota)
    return notas

def main():
    num_alumnos = int(input("Introduce el número de alumnos: "))
    alumnos = {}

    for _ in range(num_alumnos):
        nombre = input("Introduce el nombre del alumno: ")
        if nombre in alumnos:
            print("Error: El alumno ya existe.")
            continue
        notas = obtener_notas_alumno()
        alumnos[nombre] = notas

    print("\nLista de alumnos y sus notas medias:")
    for nombre, notas in alumnos.items():
        if notas:
            media = sum(notas) / len(notas)
            print(f"{nombre}: {media:.2f}")
        else:
            print(f"{nombre}: No hay notas registradas")

if __name__ == "__main__":
    main()
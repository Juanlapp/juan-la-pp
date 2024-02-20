def determinar_grupo(nombre, sexo):
    if (sexo == 'mujer' and nombre.lower() < 'm') or (sexo == 'hombre' and nombre.lower() > 'n'):
        return 'Grupo A'
    else:
        return 'Grupo B'

def main():
    nombre = input("Ingrese su nombre: ")
    sexo = input("Ingrese su sexo (mujer/hombre): ").lower()

    if sexo == 'mujer' or sexo == 'hombre':
        grupo = determinar_grupo(nombre[0], sexo)
        print("Usted pertenece al", grupo)
    else:
        print("Sexo no válido. Por favor, ingrese 'mujer' o 'hombre'.")

if __name__ == "__main__":
    main()
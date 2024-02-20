# Función para calcular el promedio de una lista de edades
def calcular_promedio(edades):
    if len(edades) == 0:
        return 0
    else:
        return sum(edades) / len(edades)

# Función para ingresar las edades de los estudiantes de un turno
def ingresar_edades(turno, cantidad_estudiantes):
    edades = []
    print(f"Ingrese las edades de los estudiantes del turno {turno}:")
    for i in range(cantidad_estudiantes):
        edad = int(input(f"Edad del estudiante {i+1}: "))
        edades.append(edad)
    return edades

# Ingresar las edades para cada turno
edades_manana = ingresar_edades("mañana", 6)
edades_tarde = ingresar_edades("tarde", 7)
edades_noche = ingresar_edades("noche", 12)

# Calcular promedio para cada turno
promedio_manana = calcular_promedio(edades_manana)
promedio_tarde = calcular_promedio(edades_tarde)
promedio_noche = calcular_promedio(edades_noche)

# Imprimir los promedios
print("Promedio de edades del turno mañana:", promedio_manana)
print("Promedio de edades del turno tarde:", promedio_tarde)
print("Promedio de edades del turno noche:", promedio_noche)

# Determinar el turno con el promedio mayor
if promedio_manana > promedio_tarde and promedio_manana > promedio_noche:
    print("El turno mañana tiene un promedio de edades mayor.")
elif promedio_tarde > promedio_manana and promedio_tarde > promedio_noche:
    print("El turno tarde tiene un promedio de edades mayor.")
else:
    print("El turno noche tiene un promedio de edades mayor.")
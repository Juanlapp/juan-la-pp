def main():
    total_empleados = int(input("Ingrese el número total de empleados: "))
    sueldos = []
    empleados_entre_rangos = 0

    for i in range(total_empleados):
        sueldo = float(input(f"Ingrese el sueldo del empleado {i+1}: "))
        sueldos.append(sueldo)
        if sueldo >= 1300000 and sueldo <= 10000000:
            empleados_entre_rangos += 1

    total_gasto = sum(sueldos)

    print(f"La cantidad de empleados que cobran entre 1.300.000 y 10.000.000 es: {empleados_entre_rangos}")
    print(f"El importe total que gasta la empresa en sueldos es: {total_gasto}")


if __name__ == "__main__":
    main()
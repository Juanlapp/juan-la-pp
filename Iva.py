def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    total = cantidad_sin_iva + (cantidad_sin_iva * porcentaje_iva / 100)
    return total

# Ejemplo de uso
cantidad_sin_iva = float(input("Ingrese la cantidad sin IVA: "))
porcentaje_iva = float(input("Ingrese el porcentaje de IVA (opcional, presione Enter para aplicar el 21% por defecto): ") or 21)

total_factura = calcular_total_factura(cantidad_sin_iva, porcentaje_iva)
print(f"El total de la factura es: {total_factura}")
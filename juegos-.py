edad = int(input("por favor ingresar su edad "))

if edad < 4:
    ingreso = 0
elif  edad < 18:

    ingreso = 5000
else:
    ingreso = 10000

print("el perecio de la entrada es ",ingreso)
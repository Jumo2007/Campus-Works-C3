total_ventas = 0
total_comisiones = 0

while True:
    cedula = int(input("Cédula (-1 para salir): "))
    if cedula == -1:
        break

    nombre = input("Nombre: ")
    tipo = int(input("Tipo (1-3): "))
    ventas = float(input("Ventas del mes: "))

    if tipo == 1:
        comision = ventas * 0.20
    elif tipo == 2:
        comision = ventas * 0.15
    elif tipo == 3:
        comision = ventas * 0.25

    total_ventas += ventas
    total_comisiones += comision

    print("Vendedor:", nombre)
    print("Comisión:", comision)
    print("----------------")

print("Total ventas:", total_ventas)
print("Total comisiones:", total_comisiones)

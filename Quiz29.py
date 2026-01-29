def menu():
    print("\n*** CAJERO AUTOMATICO ***")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

def leer_opcion():
    op = input("Opcion (1-4): ")
    while not op.isdigit() or int(op) < 1 or int(op) > 4:
        print("ERROR: opcion invalida")
        input("Presione cualquier tecla para continuar...")
        menu()
        op = input("Opcion (1-4): " )
    return int(op)

def Consultar_saldo(saldo):
    print("EL saldo actual es de : ", saldo )
    return saldo


def Depositar_saldo(saldo):
    monto = float(input("Ingrese el monto a cargar: " ) )
    if monto > 0:
        saldo += monto
        print("Saldo cargado correctamente,su saldo actual es de : ", saldo )
    else:
        print("Monto invalido, intentelo nuevamente . " ) 
    return saldo


def retirar_saldo(saldo):
    monto = int(input("Ingrese el monto a retirar: " ) )
    if monto > 0 and monto < saldo:
        saldo -= monto
        print("Cantidad retirada correctamente, su saldo actual es de: ", saldo)
    elif monto > saldo:
        print("No tienes suficiente saldo, por favor, ingresa una cantidad valida a retirar: " )
    else:
        print("Cantidad incorrecta, por favor, intèntenlo nuevamente " )
    return saldo


def main():
    saldo = 1000
    opcion = 0

    while opcion != 4:
        menu()
        opcion = leer_opcion()

        if opcion == 1:
            saldo = Consultar_saldo(saldo)
        elif opcion == 2:
            saldo = Depositar_saldo(saldo)
        elif opcion == 3:
            saldo = retirar_saldo(saldo)
        elif opcion == 4 :
            print("Gracias por usar nuestro Cajero. ADIOS")
        


main()



    
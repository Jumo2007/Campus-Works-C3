# ---------------- MENÚ ----------------
def menu():
    print("\n*** SISTEMA NEQUI ***")
    print("1. Cargar saldo")
    print("2. Pagar")
    print("3. Transferir dinero")
    print("4. Mostrar saldo")
    print("5. Salir")


# -------- LEER OPCIÓN VÁLIDA ----------
def leer_opcion():
    op = input("Opcion (1-5): ")
    while not op.isdigit() or int(op) < 1 or int(op) > 5:
        print("ERROR: opcion invalida")
        input("Presione cualquier tecla para continuar...")
        menu()
        op = input("Opcion (1-5): ")
    return int(op)


# -------- CARGAR SALDO ----------
def cargar_saldo(saldo):
    monto = float(input("Ingrese monto a cargar: "))
    if monto > 0:
        saldo += monto
        print("Saldo cargado correctamente.")
    else:
        print("Monto invalido.")
    return saldo


# -------- PAGAR ----------
def pagar(saldo):
    monto = float(input("Ingrese monto a pagar: "))
    if monto <= 0:
        print("Monto invalido.")
    elif monto > saldo:
        print("Fondos insuficientes.")
    else:
        saldo -= monto
        print("Pago realizado con exito.")
    return saldo


# -------- TRANSFERIR ----------
def transferir(saldo):
    celular = input("Ingrese numero de celular: ")
    monto = float(input("Ingrese monto a transferir: "))

    if len(celular) != 10:
        print("Numero de celular invalido.")
    elif monto <= 0:
        print("Monto invalido.")
    elif monto > saldo:
        print("Fondos insuficientes.")
    else:
        saldo -= monto
        print("Transferencia exitosa a", celular)

    return saldo


# -------- MOSTRAR SALDO ----------
def mostrar_saldo(saldo):
    print("Saldo actual:", saldo)


# ---------------- MAIN ----------------
def main():
    saldo = 0
    opcion = 0

    while opcion != 5:
        menu()
        opcion = leer_opcion()

        if opcion == 1:
            saldo = cargar_saldo(saldo)
        elif opcion == 2:
            saldo = pagar(saldo)
        elif opcion == 3:
            saldo = transferir(saldo)
        elif opcion == 4:
            mostrar_saldo(saldo)
        elif opcion == 5:
            print("Gracias por usar Nequi. ADIOS")


main()

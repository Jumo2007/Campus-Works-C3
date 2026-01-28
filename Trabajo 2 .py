def valor_programa(programa):
    if programa == 1:
        return 800000
    elif programa == 2:
        return 1000000
    elif programa == 3:
        return 1200000

def aplicar_beca(valor, beca):
    if beca == 1:
        return valor * 0.5
    elif beca == 2:
        return valor * 0.6
    else:
        return valor

# programa principal
nombre = input("Nombre del estudiante: ")
programa = int(input("Programa (1-3): "))
beca = int(input("Beca (1-3): "))

valor = valor_programa(programa)
total = aplicar_beca(valor, beca)

print("Estudiante:", nombre)
print("Valor a pagar:", total)


inventario = {
    "PO0001": {"nombre": "PORCHETE", "precio": 25000, "stock": 25},
    "PO0002": {"nombre": "MARTILLO", "precio": 30000, "stock": 10},
    "PO0003": {"nombre": "DESTORNILLADOR", "precio": 15000, "stock": 40}
}


def menu():
    print("\n*** INVENTARIO DE TIENDA ***")
    print("1. Agregar producto")
    print("2. Agregar lote de productos (stock)")
    print("3. Eliminar producto del inventario")
    print("4. Eliminar el producto más reciente")
    print("5. Mostrar inventario ordenado")
    print("6. Mostrar número total de productos")
    print("7. Salir")



def agregar_producto(inventario):
    codigo = input("Codigo del producto: ")
    nombre = input("Nombre del producto: ")
    precio = int(input("Precio: "))
    stock = int(input("Stock: "))

    inventario[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    print("Producto agregado correctamente.")



def agregar_lote(inventario):
    codigo = input("Codigo del producto: ")

    if codigo in inventario:
        cantidad = int(input("Cantidad a agregar al stock: "))
        inventario[codigo]["stock"] += cantidad
        print("Stock actualizado.")
    else:
        print("Producto no encontrado.")



def eliminar_producto(inventario):
    codigo = input("Codigo del producto a eliminar: ")

    if codigo in inventario:
        del inventario[codigo]
        print("Producto eliminado.")
    else:
        print("Producto no existe.")



def eliminar_reciente(inventario):
    if inventario:
        ultimo = list(inventario.keys())[-1]
        del inventario[ultimo]
        print("Producto más reciente eliminado.")
    else:
        print("Inventario vacío.")



def mostrar_inventario(inventario):
    print("\nINVENTARIO")
    print(f"{'CODIGO':<10} {'NOMBRE':<20} {'PRECIO':>10} {'STOCK':>8}")
    print("-" * 50)

    for codigo in sorted(inventario):
        p = inventario[codigo]
        print(f"{codigo:<10} {p['nombre']:<20} {p['precio']:>10} {p['stock']:>8}")



def total_productos(inventario):
    total = 0
    for p in inventario.values():
        total += p["stock"]
    print("Total de productos en stock:", total)



def main():
    opcion = 0

    while opcion != "7":
        menu()
        opcion = input("Elija una opcion (1-7): ")

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            agregar_lote(inventario)
        elif opcion == "3":
            eliminar_producto(inventario)
        elif opcion == "4":
            eliminar_reciente(inventario)
        elif opcion == "5":
            mostrar_inventario(inventario)
        elif opcion == "6":
            total_productos(inventario)
        elif opcion == "7":
            print("Saliendo del sistema...")
        else:
            print("Opcion invalida.")


main()

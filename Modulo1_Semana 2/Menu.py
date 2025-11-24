inventario = []
def Agregar(inventario):
        if(option == 1):
            try:
                nombre = input("Ingresa el nombre del producto: ")
                precio = float(input("Ingresa el precio del producto: "))
                cantidad = int(input("Ingresa la cantidad del producto: "))
            except ValueError:
                print("ERROR, VALOR INGRESADO NO VALIDO")
        producto = {
            "nombre" : nombre,
            "precio" : precio,
            "cantidad" : cantidad}
        inventario.append(producto)
def Mostrar(inventario):
        if not inventario:
            print("No hay productos en el inventario.")
            return
        print("\n--- Inventario actual ---")
        for i, producto in enumerate(inventario, 1):
            print(f"{i}. {producto['nombre']} | Precio: ${producto['precio']:.2f} | Cantidad: {producto['cantidad']}")
        print("--------------------------")
def Calcular(inventario):
    if not inventario:
        print("No hay productos en el inventario.")
        return
    total_valor = sum(p["precio"] * p["cantidad"] for p in inventario)
    total_productos = sum(p["cantidad"] for p in inventario)
    promedio_precio = total_valor / total_productos if total_productos > 0 else 0
    print("\n--- Estadísticas ---")
    print(f"Valor total del inventario: ${total_valor:.2f}")
    print(f"Cantidad total de productos: {total_productos}")
    print(f"Precio promedio por unidad: ${promedio_precio:.2f}")
    print("---------------------")

while True:
    try:
        option = int(input("""  
1. Agregar inventario  
2. Mostrar inventario  
3. Calcular estadísticas  
4. Salir del programa  
Elige una opción: """))
    except ValueError:
        print(" ERROR: Debes ingresar un número.")
        continue

    if option == 1:
        Agregar(inventario)
    elif option == 2:
        Mostrar(inventario)
    elif option == 3:
        Calcular(inventario)
    elif option == 4:
        print("👋 Saliendo del programa...")
        break
    else:
        print(" Opción no válida. Intenta de nuevo.")

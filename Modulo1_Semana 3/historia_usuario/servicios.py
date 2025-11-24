
"""
Módulo servicios.py
Contiene las funciones de manejo del inventario (CRUD) y estadísticas.
"""

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un producto al inventario.

    Parámetros:
        inventario (list): lista de productos.
        nombre (str): nombre del producto.
        precio (float): precio del producto.
        cantidad (int): cantidad en stock.

    Retorna:
        None
    """
    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})


def mostrar_inventario(inventario):
    """
    Muestra el inventario en formato legible.

    Parámetros:
        inventario (list)

    Retorna:
        None
    """
    if not inventario:
        print("Inventario vacío.")
        return

    print("\n=== INVENTARIO ===")
    for p in inventario:
        print(f"- {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")
    print()


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre.

    Parámetros:
        inventario (list)
        nombre (str)

    Retorna:
        dict o None
    """
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza el precio y/o cantidad de un producto existente.

    Parámetros:
        inventario (list)
        nombre (str)
        nuevo_precio (float or None)
        nueva_cantidad (int or None)

    Retorna:
        bool: True si se actualizó, False si no existe.
    """
    producto = buscar_producto(inventario, nombre)
    if not producto:
        return False

    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio

    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad

    return True


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario.

    Parámetros:
        inventario (list)
        nombre (str)

    Retorna:
        bool: True si se eliminó, False si no existe.
    """
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        return True
    return False


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario.

    Retorna dict con:
        unidades_totales
        valor_total
        producto_mas_caro (nombre, precio)
        producto_mayor_stock (nombre, cantidad)
    """
    if not inventario:
        return None

    subtotal = lambda p: p["precio"] * p["cantidad"]

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_mayor_stock": (producto_mayor_stock["nombre"], producto_mayor_stock["cantidad"])
    }


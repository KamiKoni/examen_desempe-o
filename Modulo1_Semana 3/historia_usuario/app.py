
"""
Archivo principal app.py
Menú principal de la aplicación.
"""

from colorama import Fore, Back, Style, init
init(autoreset=True)  # Inicializa colorama para que los colores se reseteen automáticamente
import csv
from servicios import (
    agregar_producto, mostrar_inventario, buscar_producto,
    actualizar_producto, eliminar_producto, calcular_estadisticas
)
from archivos import guardar_csv, cargar_csv
from Loading import load_bar

def pedir_float(msg):
    while True:
        try:
            valor = float(input(msg))
            if valor < 0:
                print("Debe ser un número no negativo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")


def pedir_int(msg):
    while True:
        try:
            valor = int(float(input(msg)))
            if valor < 0:
                print("Debe ser un número no negativo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")


def main():
    inventario = []

    while True:
        print("""
=== MENÚ PRINCIPAL ===
1. Agregar producto
2. Mostrar inventario
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Estadísticas
7. Guardar CSV
8. Cargar CSV
9. Salir
""")

        opcion = input("Seleccione opción (1-9): ")

        if opcion == "1":
            load_bar()
            nombre = input("Nombre: ")
            precio = pedir_float("Precio: ")
            cantidad = pedir_int("Cantidad: ")
            agregar_producto(inventario, nombre, precio, cantidad)
            load_bar()
            print("Producto agregado.\n")
        elif opcion == "2":
            load_bar()
            mostrar_inventario(inventario)
        elif opcion == "3":
            load_bar()
            nombre = input("Nombre a buscar: ")
            searched = buscar_producto(inventario, nombre)
            if searched:
                load_bar()
                print(f"Encontrado: {searched}")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            load_bar()
            nombre = input("Nombre del producto a actualizar: ")
            nuevo_precio = pedir_float("Nuevo precio: ")
            nueva_cantidad = pedir_int("Nueva cantidad: ")
            if actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad):
                load_bar()
                print("Producto actualizado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "5":
            load_bar()
            nombre = input("Nombre a eliminar: ")
            if eliminar_producto(inventario, nombre):
                load_bar()
                print("Producto eliminado.")
            else:
                print("No existe un producto con ese nombre.")

        elif opcion == "6":
            load_bar()
            estad = calcular_estadisticas(inventario)
            if not estad:
                print("Inventario vacío.")
            else:
                print("\n=== ESTADÍSTICAS ===")
                print(f"Unidades totales: {estad['unidades_totales']}")
                print(f"Valor total: {estad['valor_total']}")
                print(f"Producto más caro: {estad['producto_mas_caro']}")
                print(f"Producto con mayor stock: {estad['producto_mayor_stock']}\n")

        elif opcion == "7": 
            load_bar()
            ruta = input("Ruta para guardar CSV: ")
            print(guardar_csv(inventario, ruta))

        elif opcion == "8":
            load_bar()
            ruta = input("Ruta del CSV a cargar: ")
            inventario, resumen = cargar_csv(ruta, inventario)
            load_bar()
            print("\n=== RESUMEN DE CARGA ===")
            print(resumen)

        elif opcion == "9":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Debe ser 1–9.\n")


if __name__ == "__main__":
    main()











"""
Módulo archivos.py
Manejo de persistencia CSV.
"""

import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.

    Parámetros:
        inventario (list)
        ruta (str)
        incluir_header (bool)

    Retorna:
        str: mensaje final
    """
    if not inventario:
        return "Inventario vacío. No se pudo guardar."

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

    except PermissionError:
        return "Error: No se tienen permisos para escribir en el archivo."

    except Exception as e:
        return f"Error inesperado al guardar archivo: {str(e)}"

    return f"Inventario guardado en: {ruta}"


def cargar_csv(ruta, inventario):
    """
    Carga un CSV y lo integra con el inventario.

    Parámetros:
        ruta (str)
        inventario (list)

    Retorna:
        tuple: (inventario_actualizado, mensaje_resumen)
    """
    productos_cargados = []
    filas_invalidas = 0

    # Leer archivo
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            lector = csv.reader(f)
            filas = list(lector)

    except FileNotFoundError:
        return inventario, f"Error: Archivo '{ruta}' no encontrado."

    except UnicodeDecodeError:
        return inventario, "Error: Codificación inválida. El archivo debe ser UTF-8."

    except Exception as e:
        return inventario, f"Error inesperado: {str(e)}"

    if not filas:
        return inventario, "Error: El archivo está vacío."

    # Validar encabezado
    encabezado = [c.strip().lower() for c in filas[0]]
    if encabezado != ["nombre", "precio", "cantidad"]:
        return inventario, "Error: Encabezado inválido. Debe ser: nombre,precio,cantidad."

    # Procesar filas
    for fila in filas[1:]:
        if len(fila) != 3:
            filas_invalidas += 1
            continue

        nombre = fila[0].strip()

        try:
            precio = float(fila[1])
            cantidad = int(float(fila[2]))
            if precio < 0 or cantidad < 0:
                raise ValueError
        except ValueError:
            filas_invalidas += 1
            continue

        productos_cargados.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        })

    # Preguntar al usuario
    print("¿Sobrescribir inventario actual? (S/N)")
    op = input("> ").upper().strip()

    if op == "S":
        inventario = productos_cargados
        accion = "Inventario sobrescrito."

    else:
        accion = "Fusión aplicada."
        for prod in productos_cargados:
            existente = next((p for p in inventario if p["nombre"].lower() == prod["nombre"].lower()), None)
            if existente:
                existente["cantidad"] += prod["cantidad"]
                existente["precio"] = prod["precio"]
            else:
                inventario.append(prod)

    resumen = (
        f"Productos cargados: {len(productos_cargados)}\n"
        f"Filas inválidas omitidas: {filas_invalidas}\n"
        f"Acción: {accion}"
    )

    return inventario, resumen


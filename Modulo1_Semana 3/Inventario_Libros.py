from colorama import Fore, Back, Style, init
init(autoreset=True)  # Inicializa colorama para que los colores se reseteen automáticamente

# Inventario inicial de libros
inventory = [
    {"title": "it", "price": 10.0, "quantity": 100},
    {"title": "the diary of anne frank", "price": 15.0, "quantity": 50},
    {"title": "the portrait of markov", "price": 20.0, "quantity": 30},
    {"title": "pride and prejudice", "price": 25.0, "quantity": 10},
    {"title": "frankenstein", "price": 30.0, "quantity": 5}
]
Amount = 0  # Variable global para cantidad de libros a agregar

# Función para agregar libros
def agregar():
    book = []  # Lista temporal para almacenar el libro (no se agrega al inventario)
    try:
        Amount = int(input(Fore.BLUE + "¿Cuántos libros quieres agregar al sistema?: "))
    except ValueError:
        print(Fore.RED + "ERROR: Valor ingresado no válido.")
        return
    while Amount != 0:  # Bucle para agregar múltiples libros
        try:
            title = input("Cual es el titulo del libro?: ")
            price = float(input("Cual es el precio del libro?: "))
            quantity = int(input("Cual es la cantidad del libro en stock?: "))
        except ValueError:
            print(Fore.RED + ("ERROR, VALOR INGRESADO NO VALIDO"))
            return
        if(price <= 0 or quantity <= 0):  # Validación de números positivos
            print(Fore.RED+("ERROR, SOLO SE PERMITEN NUMEROS POSITIVOS"))
            continue
        else:
            print(Fore.GREEN+("Libro introducido, agregado al sistema exitosamente ✔"))
            Amount -= 1
            book = {"title": title, "price": price, "quantity": quantity}
            inventory.append(book)  #Agrega el libro introducido por el usuario al sistema.

# Función para consultar libros
def consultar():
    busqueda = input(Fore.BLUE+("Cual es el titulo del libro que buscas: "))
    for book in inventory:
        if book["title"].lower() == busqueda.lower():  # Ignora mayúsculas/minúsculas
            print(f"Titulo: {book['title']} | Precio: {book['price']} | Cantidad en stock: {book['quantity']}")
            return
    else:
        print(Fore.RED + ("El libro que ingresaste no esta actualmente en el inventario"))

# Función para actualizar el precio de un libro
def Actualizar():
    busqueda = input(Fore.BLUE+("Cual es el titulo del libro que actualizaras: "))
    encontrado = False
    for book in inventory:
        if book["title"].lower() == busqueda.lower():
            encontrado = True
            try:
                nuevo_precio = float(input(Fore.BLUE+(f"Ingresa el precio nuevo de {book['title']}: ")))
            except ValueError:
                print(Fore.RED + ("ERROR, VALOR INGRESADO NO VALIDO"))
                return
            if(nuevo_precio <= 0):
                print(Fore.RED+("ERROR, SOLO SE PERMITEN NUMEROS POSITIVOS"))
                return
            else:
                book["price"] = nuevo_precio
                print(Fore.GREEN+("Libro actualizado exitosamente ✔"))
    if not encontrado:  #Mensaje de error al no encontrar al libro.
        print(Fore.RED+("Libro no encontrado en el sistema (┬┬﹏┬┬)"))

# Función para eliminar libros por título
def eliminar():
    busqueda = input(Fore.BLUE+("Cual es el titulo del libro que eliminaras: "))
    encontrado = [book for book in inventory if book["title"].lower() == busqueda.lower()]
    if not encontrado:
        print(Fore.RED + "LIBRO NO ENCONTRADO EN EL SISTEMA")
        return
    while True:
        delete = input(Fore.BLUE + f"Se encontraron {len(encontrado)} libro(s) con el título '{busqueda}'. ¿Deseas eliminarlos todos? (Y/N): ").lower().strip()
        if delete == "y":
            for book in encontrado:
                inventory.remove(book)  # Elimina todos los libros encontrados
            print(Fore.GREEN + f"Se eliminaron {len(encontrado)} libro(s) correctamente.")
            break
        elif delete == "n":
            print(Fore.YELLOW + "No se eliminó ningún libro.")
            break
        else:
            print(Fore.RED + "INGRESA UN VALOR ENTRE Y/N")

# Función para calcular el valor total del inventario
def Calcular():
    total = sum(p["price"] * p["quantity"] for p in inventory)  # Multiplica precio por cantidad
    print(Fore.GREEN + f"El valor total del inventario es: {total:.2f}")

# Menú principal del programa
while True:
    try:
        option = int(input("""  
1. Agregar libros al inventario  
2. Consultar libros al inventario  
3. Actualizar precios del libro 
4. Eliminar libro del inventario
5. Calcular el valor total del inventario  
6. Salir del programa  
Elige una opción: """))
    except ValueError:
        print(Fore.RED + " ERROR: Debes ingresar un número.")
        continue

    if option == 1:
        agregar()
    elif option == 2:
        consultar()
    elif option == 3:
        Actualizar()
    elif option == 4:
        eliminar()
    elif option == 5:
        Calcular()
    elif option == 6:
        print("👋 Saliendo del programa...")
        break
    else:
        print(" Opción no válida. Intenta de nuevo.")











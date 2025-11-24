
import datetime
import heapq
from itertools import groupby


inventory = [
    {"title": "it", "price": 10.0, "author" : "stephen king", "category" : "horror", "quantity": 100},
    {"title": "the shining","author" : "stephen king","category" : "horror", "price": 15.0, "quantity": 50},
    {"title": "the portrait of dorian gray","author": "oscar wilde","category" : "gothic horror", "price": 20.0, "quantity": 30},
    {"title": "pride and prejudice","author" : "jane austen","category" : "romance", "price": 25.0, "quantity": 10},
    {"title": "frankenstein","author" : "mary shelley","category" : "gothic fiction", "price": 30.0, "quantity": 5}
]
sales_inventory = [ {"client" : "","selled product" : "","quantity" : 0,"date" : "","discount" : 0}
                       ]
Amount = 0  # global variable for the quantity of books to add

# Function to register books
def register():
    book = []  # temporal list that ultimately is added into the inventory
    try:
        Amount = int(input("¿Cuántos libros quieres agregar al sistema?: "))
    except ValueError:
        print("ERROR: Valor ingresado no válido.")
        return
    if not Amount:
        print(("ERROR, NO PUEDES DEJAR LOS CAMPOS VACIOS"))
        return
        
    while Amount != 0:  # loop to add multiple books
        title = input("Cual es el titulo del libro?: ")
        author = input("Cual es el autor del libro?")
        category = input("Cual es la categoria del libro?: ")

        try:
            price = float(input("Cual es el precio del libro?: "))
            quantity = int(input("Cual es la cantidad del libro en stock?: "))
        except ValueError:
            print("ERROR, VALOR INGRESADO NO VALIDO")
            return
        if(price <= 0 or quantity <= 0):  # positive numbers validation
            print(("ERROR, SOLO SE PERMITEN NUMEROS POSITIVOS"))
            continue
        if not title or not author or not category:
            print(("ERROR, NO PUEDES DEJAR LOS CAMPOS VACIOS"))
            return
        else:
            print("Libro introducido, agregado al sistema exitosamente ✔")
            Amount -= 1
            book = {"title": title,"author" : author, "price": price, "category" : category, "quantity": quantity}
            inventory.append(book)  #Adds the book, entered by the user onto the inventory.

# Function to consult books
def consult():
    search = input(("Cual es el titulo del libro que buscas: "))
    if not search:
        print(("ERROR, NO PUEDES DEJAR LOS CAMPOS VACIOS"))
        return
    for book in inventory:
        if book["title"].lower() == search.lower():  # Ignora mayúsculas/minúsculas
            print(f"Titulo: {book['title']} |Autor: {book["author"]}| Precio: {book['price']} | Categoria: {book['category']} |Cantidad en stock: {book['quantity']}")
            return
    else:
        print(("El libro que ingresaste no esta actualmente en el inventario"))

# Function to update the book's price
def update():
    search = input(("Cual es el titulo del libro que actualizaras: "))
    if not search:
        print(("ERROR, NO PUEDES DEJAR LOS CAMPOS VACIOS"))
        return
    found = False
    for book in inventory:
        if book["title"].lower() == search.lower():
            found = True
            try:
                new_price= float(input((f"Ingresa el precio nuevo de {book['title']}: ")))
            except ValueError:
                print(("ERROR, VALOR INGRESADO NO VALIDO"))
                return
            if(new_price<= 0):
                print(("ERROR, SOLO SE PERMITEN NUMEROS POSITIVOS"))
                return
            elif not new_price:
                print(("ERROR, NO PUEDES DEJAR LOS CAMPOS VACIOS"))
                return
            else:
                book["price"] = new_price
                print(("Libro actualizado exitosamente ✔"))
    if not found:  #error message for not finding the book
        print("Libro no encontrado en el sistema (┬┬﹏┬┬)")

# Function to remove book by title
def remove():
    search = input(("Cual es el titulo del libro que eliminaras: "))
    found = [book for book in inventory if book["title"].lower() == search.lower()]
    if not found:
        print("LIBRO NO ENCONTRADO EN EL SISTEMA")
        return
    if not search:
        print(("ERROR, NO PUEDES DEJAR LOS CAMPOS VACIOS"))
        return
    while True:
        delete = input(f"Se encontraron {len(found)} libro(s) con el título '{found}'. ¿Deseas eliminarlos todos? (Y/N): ").lower().strip()
        if delete == "y":
            for book in found:
                inventory.remove(book)  # Deletes every book that it finds.
            print(f"Se eliminaron {len(found)} libro(s) correctamente.")
            break
        elif delete == "n":
            print("No se eliminó ningún libro.")
            break
        else:
            print("INGRESA UN VALOR ENTRE Y/N")

def sales_CRUD():
    # Function to register books

    Amount = input("Cuantas ventas haras hoy: ")
    if not Amount:
        print( ("ERROR, NO PUEDES DEJAR LOS CAMPOS VACIOS"))
        return
    sale = []  # temporal list that ultimately is added into the inventory

    while Amount != 0:  # loop to add multiple books

        search = input(("Cual es el titulo del libro que venderas: "))
        for iteration in inventory:
            if iteration["title"].lower() == search.lower():  # Ignora mayúsculas/minúsculas
                continue
            else:
                print(("El libro que ingresaste no esta actualmente en el inventario"))
                return
        client = input("Cual es el nombre del cliente: ")
        try:
            quantity = int(input("Cual es la cantidad del producto vendido?: "))
            discount = float(input("Cual es el descuento aplicado a la compra: "))
        except ValueError:
            print(("ERROR, VALOR INGRESADO NO VALIDO"))
            return
        if(discount <= 0 or quantity <= 0):  # positive numbers validation
            print(("ERROR, SOLO SE PERMITEN NUMEROS POSITIVOS"))
            continue
        if(iteration["quantity"] <= 0):
            print("EL STOCK DEL PRODUCTO ESTA VACIO")
            break
        if not client or not quantity or not discount or not search:
            print(("ERROR, NO PUEDES DEJAR LOS CAMPOS VACIOS"))
            return
        else:
            print(("Venta introducida, agregada al sistema exitosamente✔"))
            Amount -= 1
            sale = {"client" : client,"selled product" : search, "author" : iteration["author"], "quantity" : quantity,"date" : datetime.date,"discount" : discount}
            iteration["quantity"] -= quantity
            inventory.append(sale)  # adds the book, entered by the user onto the inventory.


# Function to calculate the total value of the inventory
def Calculate():
    total = sum(p["price"] * p["quantity"] for p in inventory)  # Multiply price by quantity
    def majorThree():
        for iteracion in sales_inventory:
            quantity = int(iteracion("quantity"))
        major_three = heapq.nlargest(3, quantity)
        print(f"Los 3 números mayores son: {major_three}")
    def report():
        author_list = []
        for categoria, grupo in groupby(sales_inventory, key= sales_inventory["author"]):
            authord = authord.append(categoria)
            total_author = sum(authord["quantity"]*inventory["price"])
            author_list = {"author" : sales_inventory["author"], "total" : total_author}
            author_list.append(author_list)
            print(f"author : {author_list["author"]}, total : {author_list['total']}")

    def apply_discount():
        for keys, values in sales_inventory:
            net = sum((values["discount"]* total) - total)
            net = sum(net)
        return net
    majorThree()
    print(f"El valor total del inventario (ingreso bruto) es: {total:.2f}")
    print(f"El valor total del inventario (ingreso neto) es: {apply_discount():.2f}")


# main menu of the program.
while True:
    try:
        option = int(input("""  
1. Agregar libros al inventario  
2. Consultar libros al inventario  
3. Actualizar precios del libro 
4. Eliminar libro del inventario
5. Calcular el valor total del inventario
6. Inventario de ventas  
6. Salir del programa  
Elige una opción: """))
    except ValueError:
        print(" ERROR: Debes ingresar un número.")
        continue

    if option == 1:
        register()
    elif option == 2:
        consult()
    elif option == 3:
        update()
    elif option == 4:
        remove()
    elif option == 5:
        Calculate()
    elif option == 6:
        sales_CRUD()
    elif option == 7:
        print("👋 Saliendo del programa...")
        break
    else:
        print(" Opción no válida. Intenta de nuevo.")











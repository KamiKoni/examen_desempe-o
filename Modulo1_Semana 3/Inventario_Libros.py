from collections import defaultdict
from datetime import date
import heapq
from itertools import groupby


inventory = [
    {"title": "it", "author" : "stephen king", "category" : "horror","price": 10.0, "quantity": 100},
    {"title": "the shining","author" : "stephen king","category" : "horror", "price": 15.0, "quantity": 50},
    {"title": "the portrait of dorian gray","author": "oscar wilde","category" : "gothic horror", "price": 20.0, "quantity": 30},
    {"title": "pride and prejudice","author" : "jane austen","category" : "romance", "price": 25.0, "quantity": 10},
    {"title": "frankenstein","author" : "mary shelley","category" : "gothic fiction", "price": 30.0, "quantity": 5}
]
sales_inventory = [ {"client" : "Valentin","selled product" : "it", "author" : "stephen king", "quantity" : 10,"date" : date.today(),"discount" : 10}
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
    
def show():
        for book in inventory:
            print(f"Titulo: {book['title']} |Autor: {book["author"]}| Precio: {book['price']} | Categoria: {book['category']} |Cantidad en stock: {book['quantity']}")

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
    found = [book for book in inventory if book["title"].lower() == search.lower()] #search for the required book and verifies if it's on the inventory
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

def show_sales():
    for book in sales_inventory:
        print(f"cliente : {book["client"]}, producto vendido : {book["selled product"]}, author : {book["author"]}, quantity : {book["quantity"]},date : {date.today()}, discount : {book["discount"]}")

# Function to calculate the total value of the inventory

def sales_CRUD():
    # Function to register books

    sale = []  # temporal list that ultimately is added into the inventory
    
    def register_sales():
        while True:
            search = input(("Cual es el titulo del libro que venderas: "))
            for book in inventory:
                if book["title"].lower() == search.lower():  # Ignora mayúsculas/minúsculas
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
                    if(book["quantity"] <= 0):
                        print("EL STOCK DEL PRODUCTO ESTA VACIO")
                        break
                    if not client or not quantity or not discount or not search:
                        print(("ERROR, NO PUEDES DEJAR LOS CAMPOS VACIOS"))
                        return
                    else:
                        print(("Venta introducida, agregada al sistema exitosamente✔"))
                        sale = {"client" : client,"selled product" : search, "author" : book["author"], "quantity" : quantity,"date" : {date.today()},"discount" : discount}
                        book["quantity"] -= quantity
                        sales_inventory.append(sale)  # adds the book, entered by the user onto the inventory.
                        return
                else:
                        print(("El libro que ingresaste no esta actualmente en el inventario"))
                        return
    while True:
    # loop to add multiple books
            try:
                option = int(input("""
            Bienvenido al sistema de ventas:
                1. registrar ventas
                2. mostrar ventas
                3. salir del sistema
        """))
            except ValueError:
                print("ERROR VALOR INGRESADO NO VALIDO")
            if option == 1:
                register_sales()
                continue
            elif option == 2:
                show_sales()
            elif option == 3:
                print()
            else:
                print("ELIGE UN NUMERO ENTRE 1-3")
        
def Calculate():
    total = sum(p["price"] * p["quantity"] for p in inventory)  # Multiply price by quantity

    def majorThree(): #groups the three higher in quantity books
        count = {}
        for s in sales_inventory:
            name = s["client"]
            count[name] = count.get(name, 0) + s["quantity"]

        return sorted(count.items(), key=lambda x: x[1], reverse = False[:3])


    def group_by_author(): #Group by author
        grouped = {}
        for s in sales_inventory:
            author = s["author"]
            grouped[author] = grouped.get(author, 0) + s["quantity"]
            return grouped
    
    def apply_discount(): #Apply discount to the total value
        for values in sales_inventory:
            discount_amount = (values["discount"]/100) * total
            net = total - discount_amount
            return net
    
    print(majorThree())
    print(group_by_author())
    print(f"El valor total del inventario (ingreso bruto) es: {total:.2f}")
    print(f"El valor total del inventario (ingreso neto) es: {apply_discount()}")



# Main menu of the program.
while True:
    try:
        option = int(input("""  
1. Agregar libros al inventario  
2. Consultar libros al inventario
3. Mostrar inventario  
4. Actualizar precios del libro 
5. Eliminar libro del inventario
6. Calcular el valor total del inventario
7. Inventario de ventas
8. Mostrar inventario de ventas  
9. Salir del programa  
Elige una opción: """))
    except ValueError:
        print(" ERROR: Debes ingresar un número.")
        continue

    if option == 1:
        register()
    elif option == 2:
        consult()
    elif option == 3:
        show()
    elif option == 4:
        update()
    elif option == 5:
        remove()
    elif option == 6:
        Calculate()
    elif option == 7:
        sales_CRUD()
    elif(option == 8):
        show_sales()
    elif(option == 9):
        print("👋 Saliendo del programa...")
        break
    else:
        print(" Opción no válida. Intenta de nuevo.")











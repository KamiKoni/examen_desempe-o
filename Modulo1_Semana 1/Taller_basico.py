import random
continuar = True  
while continuar:
    print("="*100)
    print("Buenas tardes Usuario, Bienvenido al Sistema, elija un numero entre 1 y 31 para iniciar la funcion deseada ")
    print("="*100)
    print("""    
    1-Hola usuario: pide al usuario su nombre y edad. Luego imprime un mensaje: "Hola [nombre], tienes [edad] años."
    2-Suma de dos números.
    3-Área del triángulo.
    4-Conversor de grados Celsius a Fahrenheit.
    5-Tipo de dato: usar type() para mostrar el tipo de cada variable.
    6-Edad futura: pide la edad actual y muestra cuántos años tendrá el usuario dentro de 10 años.
    7-Mayor de edad.
    8-Número positivo, negativo o cero.
    9-Par o impar.
    10-Calculadora básica con +, -, *, /.
    11-Clasificador de notas (Excelente, Aprobado, Reprobado).
    12-Comparador de tres números: mayor y menor.
    13-Contar del 1 al 10.
    14-Sumatoria del 1 al n.
    15-Tabla de multiplicar.
    16-Contador regresivo con while.
    17-Adivina el número (usar random).
    18-Sumar hasta que el usuario escriba 0.
    19-Lista de frutas.
    20-Agregar y eliminar frutas.
    21-Buscar un elemento en la lista.
    22-Lista de números y promedio.
    23-Números pares: guardar solo los pares.
    24-Eliminar duplicados.
    25-Sistema de calificaciones.
    26-Carrito de compras.
    27-Cajero automático.
    28-Gestión de estudiantes (mini base de datos).
    29-Calculadora avanzada (usar funciones).
    30-Agenda de contactos (lista de diccionarios).
    31-Terminar el programa
          """)

    opcion = int(input("seleccione una opcion: "))

    if opcion == 1:
        nombre = input("Por Favor, ingresa tu nombre usuario => ")
        edad = int(input("Por favor, ingresa tu edad usuuario => "))
        print(f"Hola {nombre}, tienes {edad} años.")
    elif opcion == 2:
        print("La suma de 227 y 293 es => ", 227+ 293)
    elif opcion == 3 :
        print("Calcularemos el area de un triangulo")
        altura = float(int("Dime la altura de tu triangulo en metros =>"))
        base = float(int("Dime la base de tu triangulo en metros =>"))
        area = (base * altura) / 2
        print("La area de tu triangulo es =>", area)   
    elif opcion == 4 :
        celsius = float(input("Dime la temperatura en grados celsius que convertiras a fahrenheit => "))
        fahrenheit = (celsius * 9/5) + 32
        print("La temperatura a grados fahrenheit es => ", fahrenheit)
    elif opcion == 5 :
        texto = "bla"
        flotante = 1.5
        entero = 2
        booleano = True
        print(type(texto), type(booleano), type(flotante), type(entero))
    elif opcion == 6 :
        edad_actual = int(input("Dime tu edad actual => "))
        edad_futura = edad_actual + 10
        print("En 10 años tendras =>", edad_futura)
    elif(opcion == 7):
        edad = int(input("Dime tu edad actual => "))
        if(edad >= 18):
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")
    elif(opcion == 8):
        numero = int(input("INgresa tu numero =>"))
        if(numero <0):
            print("El numero es positivo")
        elif(numero > 0):
            print("El numero es negativo")
        else:
            print("Tu numero es cero")
    elif(opcion == 9):
        numero = int(input("Dime tu numero => "))
        if(numero % 2 == 0):
            print("tu numero es par")
        else:
            print("Tu numero es impar")
    elif(opcion == 10):
        # Definir funciones para cada operación
        def in_numero():
            global numero_1, numero
            numero = int(input("Dime tu primer numero => "))
            numero_1= int(input("Dime tu segundo numero => "))
        def sumar (a,b):
            print(f"La suma de {a} + {b} es {a+b}")
        def multiplicar (a,b):
            print(f"La multiplicacion de {a} * {b} es {a*b}")
        def division (a,b):
            if(b == 0):
                print("No se puede dividir por cero")
            else:
                print(f"La division de {a} / {b} es {a/b}")
        def resta (a,b):
            print(f"La resta de {a} +-{b} es {a-b}")
        # Mostrar opciones al usuario
        alt_opcion = int(input("""
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
                       """))
        # Solicita entrada al usuario, realiza el cálculo y muestra el resultado
        if(alt_opcion == 1):
            in_numero()
            sumar(numero, numero_1)
        elif(alt_opcion == 2):
            in_numero()
            resta(numero, numero_1)
        elif(alt_opcion == 3):
            in_numero()
            multiplicar(numero, numero_1)
        elif(alt_opcion == 4):
            in_numero()
            division(numero, numero_1)
    elif(opcion == 11):
        nota = int(input("Dime tu nota => "))
        if(nota >= 3):
            print("Has aprobado")
        elif (nota >= 4):
            print("Has sacado una nota excelente!")
        else:
            print("Has reprobado")
    elif(opcion == 12):
        num1 = 10
        num2 = 25
        num3 = 15

        # Encontrar el número mayor
        mayor = max(num1, num2, num3)
        print(f"El número mayor es: {mayor}")

        # Encontrar el número menor
        menor = min(num1, num2, num3)
        print(f"El número menor es: {menor}")
    elif(opcion == 13):
        for i in range (1,11):
            print(i)
    elif(opcion == 14):
        def suma_con_sum(n):
            return sum(range(1, n + 1))
        n = int(input("Dime el numero limite para tu sumatoria => "))
        resultado = suma_con_sum(n)
        print(f"La suma de 1 a {n} es: {resultado}")
    elif(opcion == 15):
        numero = int(input("Dime el numero del cual quieres ver su tabla de multiplicar => "))
        for i in range(1,11):
            i+1
            print(f"La multiplicacion de {numero} x {i} es {numero * i}")
    elif(opcion == 16):
        i = 10
        while (i > 0):
            print(i)
            i-= 1
    elif(opcion == 17):
        print("Adivina un numero aleatorio entre 1 al 30")
        numero = int(input("Escribe el numero => "))
        aleatorio = random(1,30)
        if(numero == aleatorio):
            print("Adivinaste!!")
        else:
            print("No adivinaste :(")
    elif(opcion == 18):

        total = 0

        while True:
            numero = float(input("Escribe un número (0 para terminar): "))
            if numero == 0:
                break
            total += numero

        print(f"La suma total es: {total}")
    elif(opcion == 19):
        global lista_frutas
        lista_frutas = ["Manzana", "Uva", "Naranja", "Melocoton", "Banano", "Piña"]
        print(lista_frutas)
    elif(opcion == 20):
        Ad_frut = input("agrega frutas a la lista de frutas => ") 
        lista_frutas.append(Ad_frut)
        rem_frut = input("Remover fruta de la lista de frutas => ")
        lista_frutas.remove(Ad_frut)
    elif(opcion == 21):
        ele = int(input=("NUmero del elemento que buscas en la lista => "))
        print(f"El elemento que buscaste es: {lista_frutas[ele]}")
    elif(opcion == 22):
        numeros = []
        while True:
            num = float(input("Escribe un número (0 para terminar): "))
            if num == 0:
                numeros.append(num)
                break
                
        if len(num) > 0:
            promedio = sum(num) / len(num)
            print(f"\nLista de números: {num}")
            print(f"Promedio: {promedio}")
        else:
            print("No ingresaste ningún número.")
    elif(opcion == 23):
        num = 0
        lista_num = []
        for num in range (1,31):
            num += 1
            if(num % 2 == 0):
                print(num)
                lista_num.append=(num)
    elif(opcion == 24):
        numeros = []
        while True:
            num = input("Escribe un número (o 0 para terminar): ")
            if num == "0":
                break
            numeros.append(int(num))

        # Eliminar duplicados usando 'set'
        sin_duplicados = list(set(numeros))

        print(f"\nLista original: {numeros}")
        print(f"Lista sin duplicados: {sin_duplicados}")
    elif(opcion == 25):
        # Solicitar la nota al usuario
        nota = float(input("Ingresa la nota (0-100): "))

        # Determinar la calificación
        if nota >= 90:
            calificacion = "A"
        elif nota >= 80:
            calificacion = "B"
        elif nota >= 70:
            calificacion = "C"
        elif nota >= 60:
            calificacion = "D"
        else:
            calificacion = "F"

        # Mostrar el resultado
        print(f"Tu calificación es: {calificacion}")
    elif(opcion== 26):
        Lista_Prod = []  
        def carrito():
             return int(input("""
1. Agregar Producto.
2. Remover Producto
3. Vaciar Carrito.
4. Ver Carrito.
5. Finalizar compra.
Elige una opción: """))
        def agregar():
            name = input("Dime el nombre del producto que agregaras a tu carrito => ")
            precio = float(input("Cual es el precio del producto que agregas al carrito => "))
            cantidad = int(input("Cual es la cantidad del producto que agregaras => "))
            producto = {"nombre" : name, "precio" : precio, "cantidad" : cantidad}
            Lista_Prod.append(producto)
        def remover():
            ver()
            if not Lista_Prod:
                return
            try:
                indice = int(input("Número del producto a eliminar: ")) - 1
                eliminado = Lista_Prod.pop(indice)
                print(f"❌ {eliminado['nombre']} eliminado del carrito.")
            except (IndexError, ValueError):
                print("⚠️ Opción inválida.")
        def ver():
            if not Lista_Prod:
                print("🛍️ El carrito está vacío.")
                return
            total = 0
            print("\n--- Contenido del carrito ---")
            for i, producto in enumerate(Lista_Prod, 1):
                subtotal = producto["precio"] * producto["cantidad"]
                total += subtotal
                print(f"{i}. {producto['nombre']} - ${producto['precio']:.2f} x {producto['cantidad']} = ${subtotal:.2f}")
            print(f"Total a pagar: ${total:.2f}")

        def vaciar():
            Lista_Prod.clear()
            print("Vaciado el carro exitosamente!")
        def Final ():
            ver()
            print("Gracias por tu compra!")
            Lista_Prod.clear()

        while True:
            opcion = carrito()
            if opcion == 1:
                agregar()
            elif opcion == 2:
                remover()
            elif opcion == 3:
                vaciar()
            elif opcion == 4:
                ver()
            elif opcion == 5:
                Final()
                break
            else:
                print("⚠️ Opción no válida. Intenta nuevamente.")
    elif(opcion == 27):
        print("---Bienvenido al cajero automático---")

        saldo = 1000
        while True:
            print(f'''
            Selecciona una opción:
            1. Ver saldo
            2. Retirar dinero
            3. Depositar dinero
            4. Salir del sistema''')

            op = input('Opción: \n')

            if op == 1:
                print(f'El saldo es: {saldo}')
            elif op == 2:
                monto_retirar = input("Ingrese el monto a retirar: ")
                saldo = saldo - monto_retirar
                print(f"El saldo es: {saldo}")
            elif op == 3:
                monto_depositar = input("Ingrese el monto a depositar: ")
                saldo = monto_depositar + saldo
                print(f"El saldo es: {saldo}")
            elif op == 4:
                print(f'''
                -----Saliendo del sistema-----
            ----Gracias por usar el cajero---''')
                break
    elif(opcion == 28):
   # Base de datos inicial de estudiantes
        Base_estu = {
            "Juan": {
                "Apellido": "Sanchez",
                "grades": {"Matematicas": 4.8, "Ciencias": 4.5}
            }
        }

        def agregar():
            nombre = input("Nombre del estudiante: ")
            apellido = input("Apellido del estudiante: ")
            matematicas = float(input("Nota en Matemáticas: "))
            ciencias = float(input("Nota en Ciencias: "))

            Base_estu[nombre] = {
                "Apellido": apellido,
                "grades": {"Matematicas": matematicas, "Ciencias": ciencias}
            }
            print(f"Estudiante {nombre} agregado correctamente.\n")


        def eliminar():
            if not Base_estu:
                print("La base de datos está vacía")
                return

            nombre = input("Nombre del estudiante a eliminar: ")

            if nombre in Base_estu:
                del Base_estu[nombre]
                print(f"Estudiante {nombre} eliminado correctamente.\n")
            else:
                print("Estudiante no encontrado.\n")


        def ver():
            if not Base_estu:
                print("La base de datos está vacía")
                return

            print("\nListado de estudiantes:")
            for i, (nombre, datos) in enumerate(Base_estu.items(), start=1):
                print(f"{i}. {nombre} {datos['Apellido']} - Notas: {datos['grades']}")
            print()


        def consultar():
            if not Base_estu:
                print("La base de datos está vacía")
                return

            busqueda = input("Dime el nombre del estudiante: ")
            if busqueda in Base_estu:
                print(f"\nEstudiante: {busqueda}")
                print(f"Apellido: {Base_estu[busqueda]['Apellido']}")
                print(f"Notas: {Base_estu[busqueda]['grades']}\n")
            else:
                print("Estudiante no encontrado.\n")


        def editar():
            nombre = input("Nombre del estudiante a editar: ")
            if nombre in Base_estu:
                nueva_mate = float(input("Nueva nota en Matemáticas: "))
                nueva_cien = float(input("Nueva nota en Ciencias: "))

                Base_estu[nombre]["grades"]["Matematicas"] = nueva_mate
                Base_estu[nombre]["grades"]["Ciencias"] = nueva_cien

                print(f"Notas actualizadas para {nombre}.\n")
            else:
                print("Estudiante no encontrado.\n")


        # Menú principal
        while True:
            print("""
        1. Agregar estudiante
        2. Eliminar estudiante
        3. Ver todos los estudiantes
        4. Consultar estudiante
        5. Editar estudiante
        6. Salir del sistema
        """)
            opcion_menu = input("Elige una opción: ")

            if opcion_menu == "1":
                agregar()
            elif opcion_menu == "2":
                eliminar()
            elif opcion_menu == "3":
                ver()
            elif opcion_menu == "4":
                consultar()
            elif opcion_menu == "5":
                editar()
            elif opcion_menu == "6":
                print("Saliendo del sistema de estudiantes...\n")
                break
            else:
                print("Opción no válida. Intenta de nuevo.\n")
    elif(opcion == 29):
             # Definir funciones para cada operación
        def in_numero():
            global numero_1, numero
            numero = int(input("Dime tu primer numero => "))
            numero_1= int(input("Dime tu segundo numero => "))
        def sumar (a,b):
            print(f"La suma de {a} + {b} es {a+b}")
        def multiplicar (a,b):
            print(f"La multiplicacion de {a} * {b} es {a*b}")
        def division (a,b):
            if(b == 0):
                print("No se puede dividir por cero")
            else:
                print(f"La division de {a} / {b} es {a/b}")
        def resta (a,b):
            print(f"La resta de {a} +-{b} es {a-b}")
        # Mostrar opciones al usuario
        alt_opcion = int(input("""
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
                       """))
        # Solicita entrada al usuario, realiza el cálculo y muestra el resultado
        if(alt_opcion == 1):
            in_numero()
            sumar(numero, numero_1)
        elif(alt_opcion == 2):
            in_numero()
            resta(numero, numero_1)
        elif(alt_opcion == 3):
            in_numero()
            multiplicar(numero, numero_1)
        elif(alt_opcion == 4):
            in_numero()
            division(numero, numero_1)
    elif(opcion == 30):
        # Diccionario base para guardar los contactos
        agenda = {}

        def agregar_contacto():
            nombre = input("Nombre del contacto: ")
            telefono = input("Número de teléfono: ")
            correo = input("Correo electrónico: ")

            agenda[nombre] = {
                "Teléfono": telefono,
                "Correo": correo
            }
            print(f"\n✅ Contacto '{nombre}' agregado correctamente.\n")


        def eliminar_contacto():
            if not agenda:
                print("\nLa agenda está vacía.\n")
                return

            nombre = input("Nombre del contacto a eliminar: ")
            if nombre in agenda:
                del agenda[nombre]
                print(f"\n🗑️ Contacto '{nombre}' eliminado correctamente.\n")
            else:
                print("\nContacto no encontrado.\n")


        def ver_contactos():
            if not agenda:
                print("\nLa agenda está vacía.\n")
                return

            print("\n📋 Lista de contactos:")
            for i, (nombre, datos) in enumerate(agenda.items(), start=1):
                print(f"{i}. {nombre} - Teléfono: {datos['Teléfono']}, Correo: {datos['Correo']}")
            print()


        def consultar_contacto():
            if not agenda:
                print("\nLa agenda está vacía.\n")
                return

            nombre = input("Nombre del contacto a consultar: ")
            if nombre in agenda:
                print(f"\n👤 Contacto: {nombre}")
                print(f"📞 Teléfono: {agenda[nombre]['Teléfono']}")
                print(f"📧 Correo: {agenda[nombre]['Correo']}\n")
            else:
                print("\nContacto no encontrado.\n")


        def editar_contacto():
            if not agenda:
                print("\nLa agenda está vacía.\n")
                return

            nombre = input("Nombre del contacto a editar: ")
            if nombre in agenda:
                nuevo_telefono = input("Nuevo número de teléfono: ")
                nuevo_correo = input("Nuevo correo electrónico: ")

                agenda[nombre]["Teléfono"] = nuevo_telefono
                agenda[nombre]["Correo"] = nuevo_correo

                print(f"\n✏️ Contacto '{nombre}' actualizado correctamente.\n")
            else:
                print("\nContacto no encontrado.\n")


        # Menú principal
        while True:
            print("""
        📞 AGENDA DE CONTACTOS

        1. Agregar contacto
        2. Eliminar contacto
        3. Ver todos los contactos
        4. Consultar contacto
        5. Editar contacto
        6. Salir
        """)

            opcion = input("Elige una opción: ")

            if opcion == "1":
                agregar_contacto()
            elif opcion == "2":
                eliminar_contacto()
            elif opcion == "3":
                ver_contactos()
            elif opcion == "4":
                consultar_contacto()
            elif opcion == "5":
                editar_contacto()
            elif opcion == "6":
                print("\n👋 Saliendo de la agenda...\n")
                break
            else:
                print("\n❌ Opción no válida. Intenta de nuevo.\n")
    elif(opcion == 31):
        break






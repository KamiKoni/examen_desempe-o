while True:
    with open(f"Modulo1_Semana 3/fruits.txt","w") as file:
        for i in range(1,6):
            num = input("Ingrese una fruta: ")
            file.write(f'{num}\n')
    palabra = input("Ingresa la fruta que deseas buscar: ")
    with open(f"Modulo1_Semana 3/fruits.txt","r") as file:
            i = file.readlines()
            print(len(i))
            for linea in i:
                if palabra in linea:
                    print(linea, end= "")
    veces = int(input("Cuantas tareas agregaras a la lista de tareas?: "))
    with open(f"Modulo1_Semana 3/lista_tareas.txt", "a") as f:
        for i in range(0, veces):
            tarea = input("Escribe la tarea que ingresaras a la lista de tareas: ")
            f.write(f"{tarea}\n ")
    with open(f"Modulo1_Semana 3/lista_tareas.txt", "r") as archivo:
        contenido = archivo.read()
        print(contenido)
    with open(f"Modulo1_Semana 3/pares.txt", "w") as f:
        for i in range (1,101):
            if(i % 2 == 0):
                f.write(f"{i}\n")
    break

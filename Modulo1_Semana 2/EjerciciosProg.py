#Ejercicio Fizz Buzz
for i in range (1, 101):
    if(i % 3 == 0 and i % 5 == 0):
        print("fizzbuzz")    
    if(i % 3 == 0):
        print("fizz")
    if(i % 5 == 0):
        print("buzz")    
    else:
        print(i)

#Clasificador de Numeros.
numeros = [1,-43,0,8,-2,-9,32,65,-34,0,-23,-12,42.1, 42.1, 32.1, 56.3,0]
num_positivos = list(filter(lambda  x : x > (0), numeros))
print(num_positivos)
num_negativos = list(filter(lambda  x : x < (0), numeros))
print(num_negativos)
num_cero = list(filter(lambda  x : x == (0), numeros))
print(num_cero)

#Contador de Vocales (Funciones)
Vocales = {"a": 3, "e": 1, "i": 0, "o": 2, "u": 0}
def conteo ():
    texto = input("Introduce un texto: ")
    for letra in texto.lower():
        if letra in Vocales:
            Vocales[letra] += 1
            print("Conteo de vocales:", Vocales)

#Lista de tareas
tareas = [
    {"titulo": "Comprar leche", "completada": False},
    {"titulo": "Estudiar Python", "completada": True},
    {"titulo": "Hacer ejercicio", "completada": False}
]
def agregar():
    titulo = input("Nombre de la tarea: ")
    completar =input("Estado de completacion (Y/N): ").lower().strip()
    verificacion = lambda x : x.lower() == "y"
    tarea = {"titulo": titulo, 'completada': completar}
    tareas.append(tarea)
def mostrar():
    for i, tarea in enumerate(tareas,1):
            estado = "✅" if tarea["completada"] == True else "❌"
            print(f"{i}. {tarea['titulo']} - {estado}")
def marcar():
    marca = int(input("Quieres marcar alguna tarea como completada, ingresa su indice para marcarla como completada: "))
    if (i in marca):
        tareas[i] = True
    else:
        print("Ingresa un valor valido: ")
try:
    opcion = int(input("""
        1. Agregar Tarea
        2. Mostrar tareas
        3. Marcar Tarea
    """))
except ValueError:
    print("Valor ingresado no valido")
if opcion == 1:
    agregar()
if opcion == 2:
    mostrar()
if opcion == 3:
    marcar()

#Maquina de bebidas (Condicionales, Loops)
Elementos = {
    'Agua' : 1,
    'Jugo' : 2,
    'Café' : 3
}
while True:
    print("""BIENVENIDOS A LA MAQUINA EXPENDEDORA 
            Elige tu bebida favorita por su indice:
          """)
    for i, Elemento in enumerate(Elementos,1):
        print(f"Indice: {i}, Bebida: {Elemento}")
    opcion = input("")







frutas = ['apple', 'pineapple', 'orange', 'grapefruit']
print(frutas[2])
frutas.sort()
print(frutas)
numeros = [3,1,2]
numeros.insert(99,2)
numeros.remove(2)
numeros.append(7)
print(numeros)
lista = [(2,'e',4,5,7), (45,87,23,1,'c'),1,2]
print(lista[0][1])
colores = ['red', 'blue', 'yellow']
print(colores)
colores[0]= 'rojo'
numeros = list(numeros)
numeros.append(4)
numeros = tuple(numeros)
numeros= list (numeros)
numeros.insert(0,'b')
numeros.insert(0,'a')
print(numeros)
print('count', numeros.count(2),"|", 'Index', numeros.index(2))
libro ={
    "titulo" : 'El gato negro',
    'Autor' : 'Edgar allan Poe',
    'Año' : 1843
}
campos = list(libro.keys())
for valor in libro.values():
    print(valor)
coche = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020
}

items = list(coche.items())
print(items[0])     # ('año', 2020)
print(items[0][1])  # 'año'
print(items[2][1])
for claves, valor in coche.items():
    print('clave:', {claves}, 'valor:', {valor})

config = {
    "tema": "claro",
    "tamaño_fuente": 14,
    'idioma': 'es'
}
config.get("tema")
config.get("idioma")

curso_python = {
    "nombre_curso": "Introducción a Python",
    "duracion_horas": 20,
    "estudiantes": ["Ana", "Luis", "Sofía"],
    "activo": True
}

print(list(curso_python.keys()))
print(list(curso_python.values()))

for clave, valor in curso_python.items():
    print(f"{clave}: {valor}")

nivel = curso_python.get("nivel", "principiante")
print("Nivel del curso:", nivel)


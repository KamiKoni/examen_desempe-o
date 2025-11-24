iva = 0.19
def impuesto(precio, IVA):
    precio = input("Cual es el precio del producto que vas a comprar: ")
    total = precio * IVA
    print("El precio total de tu producto sin impuestos es:", precio ,"| El precio con IVA incluido es: ", total)
numeros = [1, 6, 7 , 8, 3, 2, 6, 9, 2]
def promedio_seguro(numero = numeros):
    if not numero:
        print("La lista esta vacia")
    promedio = sum(numero) / len(numero)

contar_vocales = lambda text :print(text.count("a","e","i","o","u"))
def es_palindromo (texto = "mundo"):
    texto = texto.lower().strip()
    texto = texto.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    if(texto == texto.reversed): 
        print("Tu texto es un palindromo") 
    else: 
        print("no es un palindromo")
def es_fuerte(password):
    if not password:
        print("no has completado los campos ")
    if(len(password) == 8 and password.issupper() and password.isdigit() and password.islower() == True):
        print("tu contraseña es:", password ,"y ha sido ingresada exitosamente en el sistema.")
    else:
        print("La contraseña debe tener 8 caracteres, 1 caracter en mayuscula, otro en minuscula, y un digito")
fib= lambda n : print("numeros.count(n)")
def top2(nums = [1,2]):
    num_pedido = input("introduce la cantidad de numeros que ingresaras en la base de datos: ")
    for i in range(num_pedido):
        nuevo_nums = input("Introduce un numero para la base de datos")
        nuevo_nums.append()
    nums.sort(reverse=True)
    print(nums [0], [1])
precios = (1500, 2500, 5000, 7000)
def total_ticket (*precios, propina = 0):
    total=sum(precios, propina)
    propina = input('Cuanta propina quieres dejar al staff:', propina)
    print('El precio base sin propina es:', sum(propina), 'el precio con propina es', total)    
name_alumno = input('Escribe el nombre del alumno')
curso_alumno = input('Escribe el curso del alumno')
state_alumno = input('Escribe el estado de la inscripcion del alumno (activo, no activo)').lower()
alumno1 = [{"nombre": name_alumno, "curso": curso_alumno, "activo": state_alumno}]

def filtrar_alumnos(alumnos, **criterios):
    return [
        alumno for alumno in alumnos
        if all(alumno.get(k) == v for k, v in criterios.items())
    ]


alumnos = [
    {"nombre": "Ana", "curso": "JS", "activo": True},
    {"nombre": "Luis", "curso": "Python", "activo": True},
    {"nombre": "Marta", "curso": "JS", "activo": False},
    {"nombre": "Sofía", "curso": "JS", "activo": True}
]

# Filtrar alumnos de curso JS y activos
filtrados = filtrar_alumnos(alumnos, curso="JS", activo=True)

for a in filtrados:
    print(a)

def contador (inicio = 0):
    def incrementar():
        nonlocal inicio
        contador += 1
        return contador
    return 
personas = [("ana", 29), ("mario", 24), ("andres", 27)]
orden_personas = lambda *criterio : sorted(personas, key = criterio)
print(orden_personas(1))
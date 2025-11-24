#Solicitar datos al usuario.
nombre = input("Cual es el nombre del producto => ")

#Verificacion de la validez de los datos ingresados.
while True:
    precio = input("Cual es el precio del producto => ")
    cantidad = input("Cual es la cantidad del producto que compraste => ")
    try:
        #Conversion de los datos a variables numericas
        precio=float(precio)
        cantidad = int(cantidad)
        break
    except:
        print("Error, Por favor introduzca valores validos en el sistema")

#Operacion para obtener el resultado.
costo_total = round((precio * cantidad) ,2)
#Impresion de los datos recibidos del usuario y resultados obtenidos del sistema.
print(f"Producto : {nombre}| Precio : {precio}| Cantidad : {cantidad}| Costo Total = {costo_total}")

# Este programa funciona como una pequeña calculadora o caja registradora.
# Solicita al usuario el nombre del producto, su precio y la cantidad
# comprada. Luego verifica que el precio y la cantidad sean valores
# numéricos válidos, evitando errores de ingreso de datos.
# Una vez validados los datos, el programa calcula el costo total
# (precio × cantidad) y muestra en pantalla un resumen de la compra,
# incluyendo el nombre del producto, el precio unitario, la cantidad
# y el costo total.
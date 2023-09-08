cantidad = int(input("Ingrese la cantidad de datos que serán ingresados: "))
datos = []
mayor = -10
menor = 100000

for i in range(cantidad):
    dato = int(input("Ingrese el {} dato: ".format(i + 1)))
    datos.append(dato)
    if dato > mayor:
        mayor = dato
    elif dato < menor:
        menor = dato

rango = mayor - menor

print("Los números ingresados son:")
for i in range(cantidad):
    print("valor {} es: {}".format(i + 1, datos[i]))

print("Su rango es: {}".format(rango))
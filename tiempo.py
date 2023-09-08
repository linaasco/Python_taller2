suma = 0
veces = 0
while True:
    numero = int(input("Ingrese el " + str(veces + 1) + " viaje: "))
    veces += 1
    if numero == 0:
        break
    suma += numero

horas = suma // 60
minutos = suma % 60
print("Ha pasado " + str(horas) + " horas con " + str(minutos) + " minutos")

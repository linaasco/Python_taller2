positivos = 0
negativos = 0
while True:
    numero = int(input("Ingrese el numero: "))
    if numero == 0:
        break
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

for i in range(positivos):
    print("*")
print()

for i in range(negativos):
    print("*")
print()

print("Numeros positivos", positivos)
print("Numeros negativos", negativos)

import random
n = random.randint(0, 101)
numero = 0

while n != numero:
    numero = int(input("Intenta adivinar el número "))
    if numero > n:
        print("El número", numero, "es mayor al numero en busqueda")
    elif numero < n:
        print("El número", numero, "es menor al numero en busqueda")

print("Has acertado, el numero es", n)
import random
n = random.randint(0, 101)

Nmax = 100
Nmin = 1


while True:
    intento = n.randint(Nmin, Nmax)
    print("¿Es", intento, "tu número?")
    respuesta = input("Responde '=' si es correcto, '<' si tu número es menor, o '>' si es mayor: ")

    if respuesta == "=":
        print("Adivine el numero era :", intento)
        break
    elif respuesta == "<":
        Nmax = intento - 1
    elif respuesta == ">":
        Nmin = intento + 1
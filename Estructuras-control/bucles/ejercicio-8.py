# Adivina numero
# Decirle al usuario que adivino un numero entre 1 al 10, hasta que lo acierte

# Importar random
import random

numero_aleatorio = random.randint(1,10)
intento = None

while intento != numero_aleatorio:
    intento = int(input("Adivina el numero entre 1 y 10: "))
    if intento < numero_aleatorio:
        print("El numero es muy bajo, intenta de nuevo")
    elif intento > numero_aleatorio:
        print("El numero es muy alto, intenta nuevamente")
    else:
        print("Usted adivio el numero")
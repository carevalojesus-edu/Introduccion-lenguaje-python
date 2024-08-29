# Determinar el mayor de 3 numeros
# Usar if y elif para comparar los numeros
# Imprimir el mayor numero

numero1 = 53
numero2 = 112
numero3 = 45

if numero1 > numero2 and numero1 > numero3:
    print("El numero mayor es:", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("El numero mayor es:", numero2)
else:
    print("El numero mayor es:", numero3)
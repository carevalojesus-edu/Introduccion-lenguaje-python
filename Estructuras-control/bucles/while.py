# El bucle while repite un bloque de codigo mientras una condicion sea verdadera
# while condicion:
#   Bloque de codigo a ejecutar

i = 4

while i <= 5:
    print(i)
    i += 1

contador = 1
while contador <= 10:
    print("Contador:", contador)
    if contador == 5:
        break
    contador += 1 # contador = contador + 1


# Bucle while con "continue"
# Usar continue para saltarse el resto del codigo dentro del bucle para la iteracion actual y continuar con la siguiente iteraccion

contador = 0

while contador < 10:
    contador += 1 # contador = contador + 1
    if contador % 2 == 0:
        continue # salta esta parte
    print("Impares", contador)


#while True:
#    print("Hola mundo")


contador = 10

while contador > 0:
    print("Contador:", contador)
    contador -= 1 # contador = contador -1
print("¡Despegué!")
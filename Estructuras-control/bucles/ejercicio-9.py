# Validacion de datos ingresados por el usuario

numero = 0

while numero < 1 or numero > 10:
    numero = int(input("Ingresa un numero entre 1 y 10: "))
print("Ingresaste un numero valido", numero)
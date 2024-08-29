# Comprobar si año es bisiesto
# Es divisible por 4 y no es divisible por 100, amenos que tambien sea por 400

anio = 2024

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(anio, "Es un año bisiesto")
else:
    print(anio, "No es bisiesto")
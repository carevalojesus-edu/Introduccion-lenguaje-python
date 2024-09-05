# Funciones con Retorno Múltiple
# Las funciones que pueden devolver más de un valor

def operaciones(a,b):
    suma = a + b
    resta = a - b
    return suma, resta

resultado1, resultado2 = operaciones(10,5)
print(resultado1, resultado2)

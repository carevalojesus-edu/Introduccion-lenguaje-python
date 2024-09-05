# Posicionales: Se pasan en el orden en que la funcion los espera
# Nombrados: Se pasan en cualquier orden especificando el nombre del parametro

def resta(a,b):
    return a - b

print(resta(10,5)) # Posicionales
print(resta(b=10,a=5)) # Nombrados
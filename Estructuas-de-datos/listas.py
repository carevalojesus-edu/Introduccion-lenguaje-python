# Una lista en Python es una coleccion ordenada y mutable de elementos.
# Puede almacenar diferentes tipos de datos y una lista mismo

# Crear Lista

lista = [8,5,120,7,15,2]
frutas = ["pera","manzana","uva"]
abecedario = ["a","b","c","d","e","f","g"]
combinado = [12,"trece", True, [1,2,4], 12.4, -12, -23]


# Acceder a elemantos de la lista
print(lista[5])


# Modificar los elemetos de la lista
lista[0] = 6 # Modificando el valor del elemento
print(lista[0])

# Agregar mas elementos a la lista
# append() un elemento al final

combinado.append("Hola")

for elemento in combinado:
    print(elemento)


# Eliminar un elemento especifico
# remove()

combinado.remove("trece")

for elemento in combinado:
    print(elemento)


# Eliminar el ultimo elemento o la posicion de lista
# pop

combinado.pop(0)

for elemento in combinado:
    print(elemento)

lista.sort()

print(lista)
# Iterar elementos de un diccionario

personas = {"Ana": 28, "Luis": 34, "Carlos": 40}

for nombre, edad in personas.items():
    print(nombre,"tiene",edad,"años")
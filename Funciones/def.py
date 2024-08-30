# Una funcion es un bloque de codigo que realiza una tarea en especifico y que puede ser reutilizable en cualquier parte del codigo
# Una funcion puede dividir el codigo en parta mas pequeñas y manejables

# def nombre_de_la_funcion():

def saludar():
    print("Hola, bienvenidos al curso de Python")

saludar()
saludar()
saludar()

def saludar(nombre):
    print("Hola,",nombre,"bienvenido al curso de Python")


saludar("Christian")
saludar("Jorge")
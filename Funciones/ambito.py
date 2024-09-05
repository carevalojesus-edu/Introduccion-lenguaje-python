# Variables Locales: Definidas dentro de una función y solo accesibles en su interior 
# Variables Globales: Definidas fuera de todas las funciones y accesibles en todo el programa

sexo = "masculino" # Global

def saludar(nombre, anio_nacimiento):
    edad = 2024 - anio_nacimiento # Local
    print(edad, sexo)


print(edad) # Error ya que no se puede acceder a la variable local
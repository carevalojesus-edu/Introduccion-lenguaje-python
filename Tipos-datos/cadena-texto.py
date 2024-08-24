# Cadena de texto(string str) son una consecuencia de caracteres, se definen utilizando comillas simples o dobles
# Operaciones basicas: concatenaciones (+), repeticion (*) y acceder a los caracteres []

nombrePersona = "Christian "
saludo = "Hola programador"
despedida = 'Adios programadores'
texto_repetido = nombrePersona * 3

print(texto_repetido)
# mezclado = 'este es un ejemplo que no se puede realizar"

frase = saludo + " " + nombrePersona # Hola programador Christian
inicial = nombrePersona[0] # C
print(inicial)

# Metodo de cadena basicos
# tamaño len()
# mayuscula upper()
# minuscula lower()
# reemplazar replace() dos parametros

texto = "Python es divertido de aprender"
print(len(texto))
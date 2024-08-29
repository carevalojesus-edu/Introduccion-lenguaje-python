# Declarar una cadena de texto
# Obtener el largo de cadena len().
# Convertir la cadena a mayuscula y minuscula
# Reemplazar una palabra en la cadena con otra palabra
# Extraer un subconjunto de la cadena, usando la indexacion

# Declacion de la cadena de texto
cadena = "python para principiantes"

# Largo de la cadena
largo = len(cadena)
print("Largo de la cadena:", largo)

# Convertir a mayusculas (upper) y minusculas (lower)
mayuscula = cadena.upper()
minuscula = cadena.lower()
titulo = cadena.title()
capital = cadena.capitalize()
print("Mayuscula", mayuscula)
print("Minuscula", minuscula)
print("Tipo titulo", titulo)
print("Letra capita", capital)

# Reemplazar una palabra
nueva_cadena = cadena.replace("principiantes", "expertos")
print("Cadena modificada:", nueva_cadena)

# Subconjunto de la cadena
subcadena = cadena[8:14]
print("Subcadena", subcadena)

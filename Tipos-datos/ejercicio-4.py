# Declarar dos variables booleanas
# Utilizar los operadores logico (and, or, not) para combinar con otras variables
# Evaluar una expresion compleja y mostrar resultado

# Declara las variables booleanas
es_adulto = True
tiene_licencia = False

# Operadores logicos
resultado_and = es_adulto and tiene_licencia
resultado_or = es_adulto or tiene_licencia
resultado_not = not tiene_licencia

print("Resultado de AND", resultado_and)
print("Resultado de OR", resultado_or)
print("Resultado de NOT", resultado_not)

# Expresion compleja
es_condion_cumplida = (es_adulto and tiene_licencia) or (not es_adulto and not tiene_licencia)
print("Resultado de la expresion compleja:", es_condion_cumplida)

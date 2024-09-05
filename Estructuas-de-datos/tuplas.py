# Una Tupla es lista pero es inmutable (no se puede modificar despues de su creacion)

tupla = (12,-23,"Hola", False)

print(tupla[0])

# desempaquetar los elementos de Tuplas

a,b,c,d = tupla
print(a,b,c,d)

# Son mas eficientes en terminos de rendimiento y seguridad
# Utilizadas cuando no deseamos modificar los datos
# Crear una funcion para saludar a una persona segun el horario que se encuentre
# la funcion debe tener parametros por defecto

def saludar(nombre="Señor(a)", horario=7):
    if horario > 0 and horario < 12:
        print("Hola",nombre,"buenos dias")
    elif horario >= 12 and horario < 19:
        print("Hola",nombre,"buenas tardes")
    else:
        print("Hola",nombre,"buenas noches")

saludar()
saludar("Juanito",10)
saludar("Juanito",22)
saludar("Juanito",14)
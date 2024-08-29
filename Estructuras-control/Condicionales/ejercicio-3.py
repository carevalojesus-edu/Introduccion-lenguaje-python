# Calificacion Universitaria
# Determinar si un estudiante de acuerdo a su pps
# Gratuidad pps > 13
# Regular pps 11 - 13
# Amonestado pps < 11

pps_alumno = 32


if pps_alumno > 13 and pps_alumno < 20:
    print("Este alumno tiene gratuidad")
elif pps_alumno >= 11 and pps_alumno <= 13:
    print("Este alumno es regular")
elif pps_alumno < 11:
    print("Este alumno esta amonestado")
else:
    print("El pps del alumno es invalido")
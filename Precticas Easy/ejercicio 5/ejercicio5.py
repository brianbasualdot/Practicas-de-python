# Un alumno desea saber cual será su calificación final en la materia 
# de Algoritmos. Dicha calificación se compone de los siguientes 
# porcentajes:

# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.
# Este algoritmo lo realizamos en lenguaje python.

a = float(input("Ingresa la calificacion 1: "))
b = float(input("Ingresa la calificacion 2: "))
c = float(input("Ingresa la calificacion 3: "))

promedio = (a+b+c) / 3

examen = float(input("Ingresa el promedio del examen final: "))
trabajo = float(input("Ingresa la calificacion del tp final: "))

final = (promedio * .55) + (examen * .30) + (trabajo * .15)

print("EL promedio final de la materia es: ",round(final,1))
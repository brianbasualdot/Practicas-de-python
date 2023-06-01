# Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su promedio de tres 
# calificaciones es mayor o igual a 70; reprueba en caso contrario.

calificacion1 =float(input("Ingresqa la calificacion  1: "))
calificacion2 =float(input("Ingresqa la calificacion  2: "))
calificacion3 =float(input("Ingresqa la calificacion  3: "))

promedio = (calificacion1 + calificacion2 + calificacion3) / 3

if promedio >= 70:
    print("Aprobaste el curso con un pormedio de: ",round(promedio,1))
else:
    print("Reprobaste el curso con un pormedio de: ",round(promedio,1))
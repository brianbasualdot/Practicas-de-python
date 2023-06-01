# Un estudiante realiza cuatro examenes durante un semestre,
# los cuales tienen la misma ponderacion, calcular promedio #

a = float(input("Ingresa la calificacion 1: "))
b = float(input("Ingresa la calificacion 2: "))
c = float(input("Ingresa la calificacion 3: "))
d = float(input("Ingresa la calificacion 4: "))

promedio = (a|b|c|d)/4

print("El promedio de las calificaciones es: ",round(promedio,1))
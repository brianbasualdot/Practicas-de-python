# Obtener la edad promedio de un grupo de N alumnos

n = int(input("Ingresar el numero de alumnos: "))
x = 1
suma = 0
while x <= n:
    edad = int(input("Ingrese una edad: "))
    suma = suma + edad
    x += 1
    print("El promedio de edad es: ",suma / n)
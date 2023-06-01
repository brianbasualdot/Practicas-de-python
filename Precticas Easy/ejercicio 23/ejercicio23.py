# Se requiere un algoritmo para obtener la suma de diez cantidades

suma = 0
x = 1
while x <= 10:
    n = int(input("Ingresa un numero: "))
    suma = suma + n
    x += 1
    print("La suma de los 10 numeros es: ",suma)
# Escribir un programa que sume la serie 3 6 9 hasta 99

x = 3
suma = 0
while x <= 99:
    print(x)
    suma = suma + x
    x += 3
    print("La suma de los numeros es: ",suma)
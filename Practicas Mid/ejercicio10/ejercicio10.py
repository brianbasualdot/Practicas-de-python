# Leer 10 números enteros almacenarlos en un vector y determinar en qué posición 
#está el número cuya suma de dígitos sea la mayor

numeros = []
for i in range(0,10):
    n = int(input("Ingrese un numero: "))
    numeros.append(n)

    print(numeros)

for i in range(0,10):
    suma = 0
    while numeros[i] > 0:
        suma = suma + numeros[i] % 10
        numeros[i] = numeros[i] // 10

    if i == 0:
        mayor = suma
        z = i
    else:
        if suma > mayor:
            mayor = suma
            z = i

print(f"El numero con la suma de digitos mayor se encuentra en la posicion {z+1}")
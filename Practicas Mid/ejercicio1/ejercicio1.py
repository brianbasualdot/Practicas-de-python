# Sumar los números pares e impares de una lista

numeros = [1,2,3,4,5,6,7,8,9,10]
pares = 0
impares = 0

for x in numeros:
    if x % 2 == 0:
        pares = pares + x
    else:
        impares = impares + x
        
print("La suma de los numeros pares es: ",pares)
print("La suma de los numeros impares es: ",impares)
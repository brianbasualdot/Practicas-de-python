# Dada una cantidad en pesos, obtener 
# la equivalencia en dólares, asumiendo que la unidad cambiaría
# es un dato desconocido.

peso = float(input("Ingresa la cantidad de pesos: "))
dolar = float(input("Ingresa el precio del dolar: "))

conversion = peso / dolar

print(peso," pesos convertidos a dolares es: ",conversion)

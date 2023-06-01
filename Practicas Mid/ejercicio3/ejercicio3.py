# Crea un programa que muestre los números del 40 al 70 con un incremento de 5, al finalizar debe mostrar cuantos números ocurrieron entre ellos.

c = 0
for x in range(40,71,5):
    print(x)
    c = c + 1
print("La serie se compone de ",c," numeros")
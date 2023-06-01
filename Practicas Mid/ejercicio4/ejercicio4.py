# Programa que calcule el pago según los litros de gasolina, el programa deberá realizar el cálculo correspondiente, y preguntara de manera indefinida hasta que el usuario responda

x = 1
precio = float(input("Ingresa el precio del combustible: "))
total = 0
litros = 0
while x != 0:
    n = int(input("Ingrese los litros de combustible:"))
    total = total + (precio * n)
    litros = litros + n
    c = input("Quiere hacer la transaccion?(y o n): ")
    if c == "n" or c == "y":
        x = 0
        print("El total a pagar por ",litros," litros de combustible es: $",total)
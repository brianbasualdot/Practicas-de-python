# Leer 2 números si son iguales que los multiplique (condicional anidad)

a = int(input("Ingresa un numero: "))
b = int(input("Ingresa otro numero: "))

if a == b:
    print(a," x ",b," = ",a*b)
else:
    if a > b:
        print(a," - ",b," = ",a-b)
    else:
        print(a," + ",b," = ",a+b)
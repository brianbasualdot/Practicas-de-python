#  Calcular el factorial de un numero

n = int(input("Ingresa un numero: "))
if n >= 0:
    x = 1
    f = 1
    while x <= n:
        f = f * x
        x += 1
        print("El factorial de ",n," es: ",f)
else:
    print("No se puede calcular el factorial...")
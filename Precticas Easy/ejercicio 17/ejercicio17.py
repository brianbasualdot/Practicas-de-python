#  algoritmo de Condiciones anidadas 

n = int(input("Ingresar un numero: "))

if n == 0:
    print("El numero ",n," es neutro")
else:
    if n < 0:
        print("El numero ",n," es negrativo")
    else:
        print("El numero ",n," es positivo")
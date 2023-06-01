# Ingresar un carácter y determinar si es una vocal o consonante 

c = input("Ingresa una letra: ")
vocales = ["a","e","i","o","u","A","E","I","O","U"]
if c in vocales:
    print("Es una vocal")
else:
    print("Es una consonante!")
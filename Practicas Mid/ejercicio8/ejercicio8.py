# pedir un usuario y contraseña con 3 intentos

print("Tienes 3 intentos para ingresar los datos correctos")
contador = 1
while contador <= 3:
    usuario = input("Dime tu usuario: ")
    contraseña = input("Dime tu contraseña: ")
    if usuario == "Raul" and contraseña == "RaulMagic13":
        print("Felicitaciones, los datos con correctos!")
        contador = 4
    else:
        print("Los datos son incorrectos")
        if contador == 3:
            print("Comunicate con soporte por que has hecho tus 3 intentos")
            contador = contador + 1
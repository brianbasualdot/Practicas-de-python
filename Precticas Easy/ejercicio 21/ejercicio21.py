# Realizar un algoritmo que pida un usuario y una contraseña y determine si los datos son correctos.

usuario = input("Ingrese el usuario: ")

if usuario == "Roberto":
    contraseña = input("Ingrese la contraseña: ")
    if contraseña == "1234abc":
        print("Los datos son correctos!")
    else:
        print("La contrasña es incorrecta!")
else:
    print("El Usuario es incorrecto")
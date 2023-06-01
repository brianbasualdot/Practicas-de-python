# Crea un programa que pida al usuario su código de usuario (un número entero) y su contraseña numérica (otro número entero), y no le permita seguir hasta que introduzca como código 1024 y como contraseña 4567.

x = 1
while x != 0:
    codigo = int(input("Ingrese el codigo del usuario: "))
    constraseña = int(input("Ingrese la contraseña: "))
    if codigo == 1024 and constraseña == 4567:
        print("Los datos son correctos, wellcome!")
        x = 0
    else:
        print("Los datos son incorrectos")
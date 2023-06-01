# Un vendedor recibe un sueldo base de mas de un 10% extra por comision
# de sus ventas, el desea saber cuanto dinero obtendra por concepto de
# comision por las 3 ventas que realiza en el es y el total que recibirá
# en el mes tomando en cuenta su sueldo base y comisiones.

sueldo = float(input("Ingresar el sueldo: "))

a = float(input("Ingresar la venta 1: "))
b = float(input("Ingresar la venta 2: "))
c = float(input("Ingresar la venta 3: "))

comision = (a+b+c) * .10

print("La comision por la 3 ventas es: ",comision)
print("El sueldo del trabajador es: ",sueldo)
print("El sueldo total con la comision es: $ ",sueldo + comision)
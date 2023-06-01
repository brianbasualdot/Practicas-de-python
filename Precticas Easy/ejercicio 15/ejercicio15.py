# Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

compra = float(input("Ingresa la cantidad: "))

if compra > 1000:
    descuento = compra * .20
else:
    descuento = 0

print("La cantidad a pagar es: ",compra - descuento)
print("El descuento aplicado es: ",descuento)
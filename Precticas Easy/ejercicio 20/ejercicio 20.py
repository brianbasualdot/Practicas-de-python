 #Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas en una empresa,
# sabiendo que cuando las horas de trabajo exceden de 40, el resto se consideran horas extras y que estas se pagan al doble 
# de una hora normal cuando no exceden de 8; si las horas extras exceden de 8 se pagan las primeras 8 al doble de lo que se pagan las horas normales y el resto al triple.

horas = int(input("Ingresa las horas trabajadas: "))
pago = float(input("Ingresa el pago por horas: "))

triples = 0
dobles = 0
sueldo = 0

if horas > 48:
    triples = horas - 48
    dobles = 8
    sueldo = (40*pago) + (dobles*pago*2) + (triples*pago*3)
else:
    if horas > 40:
        dobles = horas - 40
        sueldo = (40*pago) + (dobles*pago*2)
    else:
        sueldo = horas * pago

print("El sueldo por las ",horas," horas es: $",sueldo)
print("Se pagó ",dobles," horas al doble, esto es: $",dobles*pago*2)
print("Se pagó ",triples," horas al doble, esto es: $",dobles*pago*3)
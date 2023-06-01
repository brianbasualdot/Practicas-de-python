# Se desea crear un algoritmo para un sistema de votación Supóngase en este caso que hay cuatro  candidatos, con identificadores 1, 2, 3, 4. Usted habrá de calcular mediante un programa,
# el número de votos correspondiente a cada candidato. El usuario ingresara los votos de manera desorganizada, 
#tal y como se obtuvieron en la elección. El conteo de votos se detiene si se ingresa el valor cero

a = b = c = d = 0
i = 1
while i != 0:
    i = int(input("Ingresa una opcion 1 , 2 , 3 , 4, 0: "))
    if i == 1:
        a +=1
    elif i == 2:
        b += 1
    elif i == 3:
        c += 1
    elif i == 4:
        d += 1

print(f"Votaciones del candidato 1: {a}")
print(f"Votaciones del candidato 2: {b}")
print(f"Votaciones del candidato 3: {c}")
print(f"Votaciones del candidato 4: {d}")
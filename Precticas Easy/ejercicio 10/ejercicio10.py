# La presión, el volumen y la temperatura de una masa 
# de aire se relacionan por la formula: masa = 
# (presión * volumen)/(0.37 * (temperatura + 460))

presion = float(input("Ingresa la presion: "))
volumen = float(input("Ingresa el volumen: "))
tempreatura = float(input("Ingresa la temperatura: "))

masa = (presion + volumen) / (0.37 * (tempreatura + 460))

print("El resultado de la masa de aire: ",masa)
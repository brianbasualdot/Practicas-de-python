# El 14 de febrero una persona desea comprarle un regalo al ser querido que más aprecia en ese momento, 
# su dilema radica en qué regalo puede hacerle, las alternativas que tiene son las siguientes:

# Regalo           Costo
# Tarjeta          $10.00 o menos
# Chocolates       $11.00 a $100.00
# Flores           $101.00 a $250.00
# Anillo           Más de $251.00

cantidad = float(input("Ingresa una cantidad: "))

if cantidad <= 10:
    print("Puedes regalar una tarjeta")
else:
    if cantidad <= 100:
        print("Puedes regalar chocolates")
    else:
        if cantidad <= 250:
            print("Puedes regalar flores")
        else:
            print("Puedes regalar un anillo")
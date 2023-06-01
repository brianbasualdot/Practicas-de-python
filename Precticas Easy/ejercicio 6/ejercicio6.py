# Un maestro desea saber que porcentaje de hombres y mujeres 
# hay en un grupo de estudiantes.

a = int(input("Ingresar el numero de mujeres: "))
b = int(input("Ingresar el numero de hombres: "))

total = a + b

print("El porcentaje de mujeres es: ",(a/total)*100,"%")
print("El porcentaje de hombres es: ",(b/total)*100,"%")
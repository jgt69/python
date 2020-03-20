'''
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.

'''
horas = int(input("¿Cuantas horas has trabajado?: "))
coste = int(input("¿Cual es el coste por hora?: "))
total = horas * coste

print("Por tu trabajo de " +str(horas) + " horas" + " a " + str(coste) + "€ por hora, vas a recibir " +
      str(total) + "€")

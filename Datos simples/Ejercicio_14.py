'''
Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca 
y el coste final total.

'''
barra = 3.49
descuento = 60
no_fresca = round(barra - barra * descuento/100,2)
num_no_fresca = int(input("Número de barras no del día: "))
coste = round(barra * num_no_fresca - no_fresca * num_no_fresca,2)
print("El precio de la barra normal es de " + str(barra) + "€" + " y de la que no es fresca es de " + str(no_fresca) 
      + "€ y el coste final es de " + str(coste) + "€ para " + str(num_no_fresca) + " barras no frescas")




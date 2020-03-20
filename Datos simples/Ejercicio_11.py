'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
y muestre por pantalla el capital obtenido en la inversión.
I = C * i * t (I --> Intereses C --> Capital inicial i --> tasa de interes t --> tiempo
I = C · (i / 100) · t   si t son años

'''
capital = input("Introduce el capital inicial: ")
tasa_interes = input("Introduce la tasa de interes: ")
tiempo = input("Introduce los años: ")

interes = round(int(capital) * int(tasa_interes)/100 * int(tiempo),2)

print("El capital que obtendrá en la inversión de " + str(capital) + "€ a un tipo de interes del " + str(tasa_interes) + "% a " + str(tiempo) + 
      " años es de " + str(interes) + "€")




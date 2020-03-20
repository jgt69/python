'''
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
Redondear cada cantidad a dos decimales.
I = C * i * t (I --> Intereses C --> Capital inicial i --> tasa de interes t --> tiempo
I = C · (i / 100) · t   si t son años

'''
capital = float(input("Introduce el saldo inicial: "))
tasa_interes = 4
tiempo = 1

while tiempo <= 3:
    interes = round(capital * tasa_interes/100 * tiempo,2)
    capital += interes
    print("El saldo del año " + str(tiempo) + " será de "  + str(capital) + "€")
    tiempo += 1




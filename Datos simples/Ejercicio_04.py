'''
Escribir un programa que pregunte el nombre del usuario en la consola
y un número entero e imprima por pantalla en líneas distintas el
nombre del usuario tantas veces como el número introducido.

'''


nombre = input("Introduce tu nombre: ")
repetir = int(input("Introduce un número de 0 a 10: "))
veces = repetir
while repetir != 0:
    print (str(repetir) + " " + nombre )
    repetir -= 1
print("Se ha repetido " + str(veces) + " veces")

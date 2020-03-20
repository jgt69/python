'''
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> 
y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto 
de la división entera respectivamente.

'''
num1 = input("Introduce el dividendo: ")
num2 = input("Introduce el divisor: ")
div = int(num1)//int(num2)
resto = int(num1) % int(num2)
print("El cociente de dividir " + str(num1) + " entre " + str(num2) + " es " + str(div) + " y el resto es " + str(resto))



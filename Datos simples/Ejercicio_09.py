'''
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla 
la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal 
calculado redondeado con dos decimales.

'''
peso = input("Introduce tu peso en kg k.ggg: ")
altura = input("Introduce tu altura en metros m.cc : ")
imc = round(float(peso)/float(altura)**2,2)
print("Tu índice de masa corporal es " + str(imc))


'''
Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido 
y calcule el peso total del paquete que será enviado.

'''
clown = 112
doll = 75

clown_num = int(input("Introduce el número de payasos enviados: "))
doll_num = int(input("Introduce lel número de muñecas enviadas: "))


peso = (clown * clown_num) + (doll * doll_num)

print("El peso total del paquete es " + str(peso) + "grs")




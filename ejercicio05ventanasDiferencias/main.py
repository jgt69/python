'''
Created on 17 mar. 2020

@author: JGT

***** JUEGO DE LAS DIFERENCIAS *****

'''
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from time import time

 
match = 0
end_game = False
marked = [0, 0, 0, 0, 0]

def click_raton(event):
    
    global match 
      
    #Coordenadas de cada click del raton
    x = event.x
    y = event.y
    
    print("x: " + str(x))
    print("y: " + str(y))
   
         
    if match < 5 or not end_game :       
        #  Coordenadas de las cinco zonas
        if x >= 460 and x <=  500 and y >= 170 and y <= 216:
            if marked[0] == 0:
                print("FELICIDADES " + user.upper() + " ADIVINASTE LA PRIMERA DIFERENCIA." + " \nTe quedan "  + str(4-match) + " diferencias por encontrar")
                mb.showinfo("Diferencia 1", "FELICIDADES "  + user.upper() + " ADIVINASTE LA PRIMERA DIFERENCIA" + " \nTe quedan "  + str(4-match) + " diferencias por encontrar" )
                marked [0] = 1
                match += 1
                if match == 5:
                    mb.showinfo(title = "THAT'S ALL FOLKS!!", message = "FELICIDADES, " + user.upper() + " HAS ACERTADO TODAS LAS DIFERENCIAS")     
                    end_game = True
                    
            else: 
                mb.showinfo(title = "***********", message = "Diferencia ya visitada")
                    
        elif x >= 570 and x <=  608 and y >= 54 and y <= 97 :
            if marked[1] == 0:
                print("FELICIDADES ADIVINASTE LA SEGUNDA DIFERENCIA")
                mb.showinfo("Diferencia 2", "MUY BIEN "  + user.upper() + " ADIVINASTE LA SEGUNDA DIFERENCIA." + " \nTe quedan " + str(4-match) + " diferencias por encontrar")
                marked [1] = 1
                match += 1
                if match == 5:
                    mb.showinfo(title = "THAT'S ALL FOLKS!!", message = "FELICIDADES, " + user.upper() + " HAS ACERTADO TODAS LAS DIFERENCIAS")     
                    end_game = True
                    
            else: 
                mb.showinfo(title = "***********", message = "Diferencia ya visitada")

        elif x >= 591 and x <=  620 and y >= 144 and y <= 171 :
            if marked[2] == 0:
                print("FELICIDADES ADIVINASTE LA TERCERA DIFERENCIA")
                mb.showinfo("Diferencia 3", "SIGUE ASÍ "  + user.upper() + " ADIVINASTE LA TERCERA DIFERENCIA." + " \nTe quedan " + str(4-match) + " diferencias por encontrar")
                marked [2] = 1
                match += 1
                if match == 5:
                    mb.showinfo(title = "THAT'S ALL FOLKS!!", message = "FELICIDADES, " + user.upper() + " HAS ACERTADO TODAS LAS DIFERENCIAS")     
                    end_game = True
                    
            else: 
                mb.showinfo(title = "***********", message = "Diferencia ya visitada")

        elif x >= 635 and x <=  670 and y >= 235 and y <= 270 :
            if marked[3] == 0:
                print("FELICIDADES ADIVINASTE LA CUARTA DIFERENCIA")
                mb.showinfo("Diferencia 4", "INCREIBLE "  + user.upper() + " ADIVINASTE LA CUARTA DIFERENCIA." + " \nTe quedan " + str(4-match) + " diferencias por encontrar")
                marked [3] = 1
                match += 1
                if match == 5:
                    mb.showinfo(title = "THAT'S ALL FOLKS!!", message = "FELICIDADES, " + user.upper() + " HAS ACERTADO TODAS LAS DIFERENCIAS")     
                    end_game = True
                    
            else: 
                mb.showinfo(title = "***********", message = "Diferencia ya visitada")
    
            
        elif x >= 764 and x <=  795 and y >= 121 and y <= 155 :
                if marked[4] == 0:
                    print("FELICIDADES ADIVINASTE LA QUINTA DIFERENCIA")
                    mb.showinfo("Diferencia 5", "ERES UN CRACK "  + user.upper() + " ADIVINASTE LA QUINTA DIFERENCIA." + " \nTe quedan " + str(4-match) + " diferencias por encontrar")
                    marked [4] = 1
                    match += 1
                    if match == 5:
                        mb.showinfo(title = "THAT'S ALL FOLKS!!", message = "FELICIDADES, " + user.upper() + " HAS ACERTADO TODAS LAS DIFERENCIAS")     
                        end_game = True

                else: 
                    mb.showinfo(title = "***********", message = "Diferencia ya visitada")

        else: #CLICK EN ÁREA SIN DIFERENCIA
            messagebox.showarning(title = "¡¡ AQUÍ NO !!", message = "En esta zona no hay nada :(")               
    else:
        mb.showinfo(title = "THAT'S ALL FOLKS!!", message = "FELICIDADES, " + user.upper() + " HAS ACERTADO TODAS LAS DIFERENCIAS")

#end click_raton()

def ventana_inicio():
    global user
    user = v.get()
    lista = []
    file = open("registro.txt","r+") #Con r+ además de abrir en modo lectura permite también añadir contenido al archivo
    for linea in file:
        new = linea.rstrip('\n')
        lista.append(new)
    if user in lista:
        print("El usuario "+ user + " ya está registrado")
        mb.showwarning("REGISTRO", "Hola " + user + " bienvenido de nuevo")
        ventana.deiconify()
        mb.showinfo("Inicio", "Pulsa 'Iniciar' y marca las diferencias en la imágen de la derecha. \nCuando termines, pulsa 'Parar")
    else:
        print("El usuario "+ user + " es nuevo")
        file.write(user + "\n")
        file.close()
        mb.showinfo("REGISTRO", "FELICIDADES " + user + ", TE HAS REGISTRADO CORRECTAMENTE")
        ventana.deiconify()
        mb.showinfo("Inicio", "Pulsa 'Iniciar' y marca las diferencias en la imágen de la derecha. \nCuando termines, pulsa 'Parar'")
#end ventana_inicio    
    
def cerrar_ventana():
    ventana.destroy()
#end cerrar_ventana()    
    
def iniciar():
    global inicio
    inicio = time()
#end iniciar()    
        
def parar():
    global tiempo
    fin = time()
    tiempo = round(fin - inicio,2)
    mb.showinfo("Tiempo en adivinar", user + " has tardado " + str(tiempo) + " segundos")
    marcador_final()
    cerrar_ventana()
#end parar    

def marcador_final():
    file = open("records.txt","a+")
    file.write(user + " " + str(tiempo) + "\n")
    file.close()
#end marcador_final()    

def mostrar_marcadores():
    lista = [] 
    file = open("records.txt","r") 
    for linea in file:
        lista.append(linea)
    marcas = "".join(map(str, lista))
    ventana.withdraw()
    ventana2 = tk.Toplevel()
    ventana2.geometry("180x250+580+300")
    ventana2.title("Marcadores")
    ventana2.configure(background = "LightSteelBlue")
    lbl = tk.Label(ventana2, text="MARCADORES", font=("Arial Bold", 14), fg="blue", bg = "LightSteelBlue")
    lbl.pack(padx=5,pady=5,ipadx=5,ipady=5,fill = tk.X)
    lbl2 = tk.Label(ventana2, text= marcas, font=("Arial Bold", 14), fg="blue", bg = "LightSteelBlue")
    lbl2.pack(padx=6,pady=6,ipadx=6,ipady=6,fill = tk.X)
    usuario()
#end mostrar_marcadores()
   
def usuario():
    ventana.withdraw()
    ventana3 = tk.Toplevel()
    ventana3.geometry("320x160+500+300")
    ventana3.title("ACCESO")
    ventana3.configure(background = "LightSteelBlue")
    lbl = tk.Label(ventana3, text="Ingresa tu usuario", font=("Arial Bold", 14), fg="blue", bg = "LightSteelBlue")
    global v
    v = StringVar()
    entrada = tk.Entry(ventana3, textvariable=v, font=("Arial Bold", 14),width=19, fg="green", bd=0,bg = "ivory")
    lbl.pack(padx=5,pady=5,ipadx=5,ipady=5,fill = tk.X) 
    entrada.pack(padx=6,pady=6,ipadx=6,ipady=6, fill = tk.X)
    btn = tk.Button(ventana3, text="Aceptar", font=("Arial Bold", 14), bg="blue", fg="white", command=ventana_inicio)
    btn.pack(side = tk.TOP) 
#end usuario()
       
ventana = tk.Tk()  

canvas = Canvas(ventana, width = 800, height= 320)
canvas.pack(expand = YES, fill = BOTH)

imagen = tk.PhotoImage(file ="image.png")

canvas.create_image(0,0, image = imagen, anchor = NW)

ventana.geometry("880x400+500+300")

ventana.title("JUEGO DE LAS DIFERENCIAS")

mostrar_marcadores() #Iniciamos la aplicación mostrando los maracadores guardados

#Se asignan eventos a los clicks

canvas.bind("<Button 1>", click_raton) # Funciona con ventana y canvas

tk.Button(ventana, text="Iniciar", font=("Arial Bold", 14), bg="blue", fg="white", command=iniciar).place(height=30, x=250, y=360)
tk.Button(ventana, text="Parar", font=("Arial Bold", 14), bg="orange", fg="white", command=parar).place(height=30, x=450, y=360)


ventana.mainloop()
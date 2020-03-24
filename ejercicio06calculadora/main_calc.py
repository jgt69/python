'''

Created on 21 mar. 2020

**** PYTHONIC CALCULATOR v.1.0 ****

'''
# -*- coding: utf-8 -*-

import tkinter as tk
from math import *
import time
import threading

#Create the main window
win = tk.Tk()

win.title("CALCULATOR v.1.0")
win.geometry("375x520+650+200")
win.resizable(0,0)
win.configure(bg = "#e3e3e3", relief = "groove", bd = 6, cursor="hand2")

in_txt = tk.StringVar()
operator=""

#Collect the input data when some button is clicked
def click(val):
    global operator
    operator += str(val)
    in_txt.set(operator)
    print(operator)
#end btnClick()

#Clean the screen and show 0
def clear():
    global operator
    operator = ("")
    in_txt.set("0")
#end clear()

#Eval the operations and show on the screen widget
def op():
    global operator
    try:
        opr=str(eval(operator))                  
    except:
        clear()
        opr = ("ERROR")
    in_txt.set(opr)
    operator = ("")
#end op()    

#Switch on the calculator
def on(color):
    screen.config(bg = color)         
    #Enable buttons
    btn_log.config(state="normal")
    btn_fact.config(state="normal")
    btn_inv.config(state="normal")
    btn_off.config(state="normal") 
    btn_npow.config(state="normal")
    btn_xpowy.config(state="normal")
    btn_sqr.config(state="normal")
    btn_0.config(state="normal")
    btn_1.config(state="normal")
    btn_2.config(state="normal")
    btn_3.config(state="normal")
    btn_4.config(state="normal")
    btn_5.config(state="normal")
    btn_6.config(state="normal")
    btn_7.config(state="normal")
    btn_8.config(state="normal")
    btn_9.config(state="normal")
    btn_plus.config(state="normal")
    btn_min.config(state="normal")
    btn_mul.config(state="normal")
    btn_div.config(state="normal")
    btn_c.config(state="normal")
    btn_parL.config(state="normal")
    btn_parR.config(state="normal")
    btn_mod.config(state="normal")
    btn_eq.config(state="normal")
    btn_dot.config(state="normal") 
    #Show the welcome message for a while when the calculator is on
    in_txt.set("Pythonic Calculator ")
    def msg(): 
        for i in range(1, 10):
            print(i)
            time.sleep(0.4)
 
        operator = ("")
        in_txt.set("0")  
 
    t = threading.Thread(target=msg) 
    t.start()
             
    return screen
#end on()                    

#Switch off the calculator        
def off(color):
    #Show the farewell message for a while when the calculator is off
    in_txt.set("Bye, bye..... ")
    def out(): 
        for i in range(1, 10):
            print(i)
            time.sleep(0.4)
 
        screen.config(bg = color)
        disable()                     
        operator=("")
        in_txt.set("") 
    t = threading.Thread(target=out) 
    t.start()
    
    return screen    
#end off()

#Disable all buttons except btn_on
def disable():
    #Disable buttons
    btn_log.config(state="disabled")
    btn_fact.config(state="disabled")
    btn_inv.config(state="disabled")
    btn_off.config(state="disabled") 
    btn_npow.config(state="disabled")
    btn_xpowy.config(state="disabled")
    btn_sqr.config(state="disabled")
    btn_0.config(state="disabled")
    btn_1.config(state="disabled")
    btn_2.config(state="disabled")
    btn_3.config(state="disabled")
    btn_4.config(state="disabled")
    btn_5.config(state="disabled")
    btn_6.config(state="disabled")
    btn_7.config(state="disabled")
    btn_8.config(state="disabled")
    btn_9.config(state="disabled")
    btn_plus.config(state="disabled")
    btn_min.config(state="disabled")
    btn_mul.config(state="disabled")
    btn_div.config(state="disabled")
    btn_c.config(state="disabled")
    btn_parL.config(state="disabled")
    btn_parR.config(state="disabled")
    btn_mod.config(state="disabled")
    btn_eq.config(state="disabled")
    btn_dot.config(state="disabled")
#end disable()    
    
#Calculator Screen

screen = tk.Label(win, textvariable= in_txt , padx = 5, anchor = "e", relief = "ridge", font=("Arial Bold", 24), bd = 8, 
                  fg="#636363", bg = "#404040")
screen.place(width = 320, height = 70, x=20, y=15)

#Buttons row1

btn_on = tk.Button(win, text = "On", font=("Arial Bold", 14), bg="green", bd = 4, 
                    fg="white", relief = "groove", command = lambda: on("#cdc9c9"))
btn_on.place(width = 60, height = 35, x = 25, y = 107)

btn_log = tk.Button(win, text = "log(x)", font=("Arial Bold", 16), bg="#d2b48c", bd = 4, 
                    fg="black", relief = "groove", command = lambda: click("log("))
btn_log.place(width = 70, height = 45, x = 105, y = 100)

btn_fact = tk.Button(win, text = " n! ", font=("Arial Bold", 16), bg="#d2b48c", bd = 4, 
                     fg="black", relief = "groove", command = lambda: click("factorial("))
btn_fact.place(width = 70, height = 45, x = 185, y = 100)

btn_inv = tk.Button(win, text = " 1/x ", font=("Arial Bold", 16), bg="#d2b48c", bd = 4, 
                    fg="black", relief = "groove", command = lambda: click("1/"))
btn_inv.place(width = 70, height = 45, x = 265, y = 100)

#Buttons row2

btn_off = tk.Button(win, text = "Off", font=("Arial Bold", 14), bg="red", bd = 4,
                     fg="white", relief = "groove", command = lambda: off("#404040"))
btn_off.place(width = 60, height = 35, x = 25, y = 162)

btn_npow = tk.Button(win, text = "n**2", font=("Arial Bold", 16), bg="#d2b48c", bd = 4,
                      fg="black", relief = "groove", command=lambda:click("**2"))
btn_npow.place(width = 70, height = 45, x = 105, y = 155)

btn_xpowy = tk.Button(win, text = "x**y", font=("Arial Bold", 16), bg="#d2b48c", bd = 4,
                      fg="black", relief = "groove", command=lambda:click("**"))
btn_xpowy.place(width = 70, height = 45, x = 185, y = 155)

btn_sqr = tk.Button(win, text = "√x", font=("Arial Bold", 16), bg="#d2b48c", bd = 4,
                     fg="black", relief = "groove", command=lambda:click("sqrt("))
btn_sqr.place(width = 70, height = 45, x = 265, y = 155)

#Buttons row3       

btn_7 = tk.Button(win, text = "7", font=("Arial Bold", 16), bg="#d15fee", bd = 4, 
                  fg="black", relief = "groove", command=lambda:click(7))
btn_7.place(width = 70, height = 45, x = 25, y = 210)

btn_8 = tk.Button(win, text = "8", font=("Arial Bold", 16), bg="#d15fee", bd = 4, 
                  fg="black", relief = "groove", command=lambda:click(8))
btn_8.place(width = 70, height = 45, x = 105, y = 210)

btn_9 = tk.Button(win, text = "9", font=("Arial Bold", 16), bg="#d15fee", bd = 4, 
                  fg="black", relief = "groove", command=lambda:click(9))
btn_9.place(width = 70, height = 45, x = 185, y = 210)

btn_plus = tk.Button(win, text = "+", font=("Arial Bold", 16), bg="#87ceff", bd = 4, 
                  fg="black", relief = "groove", command=lambda:click("+"))
btn_plus.place(width = 70, height = 45, x = 265, y = 210)

#Buttons row4

btn_4 = tk.Button(win, text = "4", font=("Arial Bold", 16), bg="#d15fee", bd = 4,
                   fg="black", relief = "groove", command=lambda:click(4))
btn_4.place(width = 70, height = 45, x = 25, y = 265)

btn_5 = tk.Button(win, text = "5", font=("Arial Bold", 16), bg="#d15fee", bd = 4,
                   fg="black", relief = "groove", command=lambda:click(5))
btn_5.place(width = 70, height = 45, x = 105, y = 265)

btn_6 = tk.Button(win, text = "6", font=("Arial Bold", 16), bg="#d15fee", bd = 4,
                   fg="black", relief = "groove", command=lambda:click(6))
btn_6.place(width = 70, height = 45, x = 185, y = 265)

btn_min = tk.Button(win, text = "-", font=("Arial Bold", 16), bg="#87ceff", bd = 4,
                   fg="black", relief = "groove", command=lambda:click("-"))
btn_min.place(width = 70, height = 45, x = 265, y = 265)

#Buttons row5

btn_1 = tk.Button(win, text = "1", font=("Arial Bold", 16), bg="#d15fee", bd = 4, 
                  fg="black", relief = "groove", command=lambda:click(1))
btn_1.place(width = 70, height = 45, x = 25, y = 320)

btn_2 = tk.Button(win, text = "2", font=("Arial Bold", 16), bg="#d15fee", bd = 4, 
                  fg="black", relief = "groove", command=lambda:click(2))
btn_2.place(width = 70, height = 45, x = 105, y = 320)

btn_3 = tk.Button(win, text = "3", font=("Arial Bold", 16), bg="#d15fee", bd = 4, 
                  fg="black", relief = "groove", command=lambda:click(3))
btn_3.place(width = 70, height = 45, x = 185, y = 320)

btn_mul = tk.Button(win, text = "x", font=("Arial Bold", 16), bg="#87ceff", bd = 4, pady = 5,
                  fg="black", relief = "groove", command=lambda:click("*"))
btn_mul.place(width = 70, height = 45, x = 265, y = 320)

#Buttons row6

btn_parL = tk.Button(win, text = "(", font=("Arial Bold", 16), bg="#b3ee3a", bd = 4, 
                    fg="black", relief = "groove", command = lambda: click("("))
btn_parL.place(width = 70, height = 45, x = 25, y = 375)

btn_0 = tk.Button(win, text = "0", font=("Arial Bold", 16), bg="#d15fee", bd = 4, 
                  fg="black", relief = "groove", command=lambda:click(0))
btn_0.place(width = 70, height = 45, x = 105, y = 375)

btn_parR = tk.Button(win, text = " ) ", font=("Arial Bold", 16), bg="#b3ee3a", bd = 4, 
                     fg="black", relief = "groove", command = lambda: click(")"))
btn_parR.place(width = 70, height = 45, x = 185, y = 375)

btn_div = tk.Button(win, text = u"\u00F7", font=("Arial Bold", 16), bg="#87ceff", bd = 4, 
                  fg="black", relief = "groove", command = lambda: click("/"))
btn_div.place(width = 70, height = 45, x = 265, y = 375)

#Buttons last row

btn_c = tk.Button(win, text = "C", font=("Arial Bold", 16), bg="#2f4f4f", bd = 4, 
                  fg="white", relief = "groove", command = clear)
btn_c.place(width = 70, height = 45, x = 25, y = 430)                  

btn_dot = tk.Button(win, text = ".", font=("Arial Bold", 20), bg="#b3ee3a", bd = 4, 
                    fg="black", relief = "groove", command=lambda:click("."))
btn_dot.place(width = 70, height = 45, x = 105, y = 430)

btn_eq = tk.Button(win, text = "=", font=("Arial Bold", 20), bg="#87ceff", bd = 4, 
                   fg="black", relief = "groove", command = op)
btn_eq.place(width = 70, height = 45, x = 185, y = 430)

btn_mod = tk.Button(win, text = "Mod", font=("Arial Bold", 16), bg="#87ceff", bd = 4, 
                    fg="black", relief = "groove", command=lambda:click("%"))
btn_mod.place(width = 70, height = 45, x = 265, y = 430)


disable()

win.mainloop()

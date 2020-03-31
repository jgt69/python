'''

Created on 24 mar. 2020

******* PyQt5 ejemplo 1  *****

'''
# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, uic
import sys

def boton_pulsado():
    
    win.etiqueta_ventana.setText("Gracias por pulsar el botón")
    
#En PyQt5 es obligatorio el siguiente objeto
app = QtWidgets.QApplication([])


#Interfaz creada a partir del diseño archivo .ui
win = uic.loadUi("ventana_ejemplo.ui") #specify the location of your .ui file

#de esta forma se va a ejecutar la funcion boton_pulsado cuando se pulse en el boton_pulsame
win.boton_pulsame.clicked.connect(boton_pulsado)

#muestra la ventana
win.show()

#la aplicacion no cierra hasta que no termine app
sys.exit(app.exec_())  
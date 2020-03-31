'''

Created on 24 mar. 2020

'''
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QDialog,QApplication

from dialogo_saludo import *
from tkinter import dialog

class DialogoSaludoAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.dialogo = Ui_Ventanasaludo()
        self.dialogo.setupUi(self)
        self.dialogo.btn_saludar.clicked.connect(self.mostrar_saludo)
        self.show()
        
    def mostrar_saludo(self):
        mensaje = self.dialogo.txt_nombre.text()
        self.dialogo.lbl_mensaje.setText("Hola " + mensaje)
        
        
#Creamos la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = DialogoSaludoAplicacion()
    dialogo.show()
    sys.exit(app.exec_())
    
    
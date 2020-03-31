'''

Created on 25 mar. 2020

**** Clase 

'''
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QDialog,QApplication
from DialogoClaseVuelo import *

class DialogoClaseVueloAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.dialogo = DialogoClaseVuelo()
        self.dialogo.setupUi(self)
        self.dialogo.rbn_primera_clase.toggled.connect(self.mostrar_informacion)
        self.dialogo.rbn_clase_negocio.toggled.connect(self.mostrar_informacion)
        self.dialogo.rbn_clase_economica.toggled.connect(self.mostrar_informacion)
        
        self.show()
        
    def mostrar_informacion(self):
        costo_vuelo = 0
        
        if self.dialogo.rbn_primera_clase.isChecked() == True:
            costo_vuelo = 190
            
        if self.dialogo.rbn_clase_negocio.isChecked() == True:
            costo_vuelo = 130
            
        if self.dialogo.rbn_clase_economica.isChecked() == True:
            costo_vuelo = 90
            
        self.dialogo.lbl_resultado_seleccion.setText('El coste del billete es de {}'.format(costo_vuelo))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = DialogoClaseVueloAplicacion()
    dialogo.show()
    
    sys.exit(app.exec_())
    
    
            
        
            
            
            
            
            
    
'''

Created on 26 mar. 2020

**** CONVERSOR MULTIDIVISA V1.0 *****

'''
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QDialog,QApplication
from ConversorDialog import ConversorDialog

class ConversorMonedas(QDialog):#Hereda de QDialog
    
    def __init__(self):
        
        #Invocamos el constructor de la clase padre
        super().__init__() 
        
        #Instanciamos un objeto de la clase ConversorDialog()
        self.ui = ConversorDialog()
        #Invocamos el método setupUi para cargar la interface del archivo ConversorDialog 
        self.ui.setupUi(self) 
        
        #Asociamos los eventos a los radiobuttons
        self.ui.rbn_usa.toggled.connect(self.convertir_divisa)
        self.ui.rbn_uk.toggled.connect(self.convertir_divisa)
        self.ui.rbn_jpn.toggled.connect(self.convertir_divisa)
        self.ui.rbn_china.toggled.connect(self.convertir_divisa)
        self.ui.rbn_rusia.toggled.connect(self.convertir_divisa)
        self.ui.rbn_brasil.toggled.connect(self.convertir_divisa)
        
        # Se muestra la interface con los componentes que hemos diseñado
        self.show() 
    #end __init__  
        
    def convertir_divisa(self):
        
        euros = self.ui.txt_cantidad.text()
        euros_float = float(euros.replace(",","."))
        
        # En cada selección de radiobutton se ejecuta el cálculo correspondiente que 
        # es visualizado en su label asignado
        
        if self.ui.rbn_usa.isChecked() == True:
            dolares = round(euros_float * 1.10,2)
            self.ui.lbl_dolar.setText(str(dolares).replace(".",",") + " dolares USA")
            
        if self.ui.rbn_uk.isChecked() == True:
            libras = round(euros_float * 0.91,2)
            self.ui.lbl_libra.setText(str(libras).replace(".",",") + " libras esterlinas")
            
        if self.ui.rbn_jpn.isChecked()  == True:
            yenes = round(euros_float * 120.74,2)
            self.ui.lbl_yen.setText(str(yenes).replace(".",",") + " yenes japoneses")
        
        if self.ui.rbn_china.isChecked() == True:
            yuanes = round(euros_float * 7.81,2)
            self.ui.lbl_yuan.setText(str(yuanes).replace(".",",") + " yuanes chinos")
            
        if self.ui.rbn_rusia.isChecked() == True:
            rublos = round(euros_float * 85.00,2)
            self.ui.lbl_rublo.setText(str(rublos).replace(".",",") + " rublos")
            
        if self.ui.rbn_brasil.isChecked() == True:
            reales = round(euros_float * 5.51,2)
            self.ui.lbl_real.setText(str(reales).replace(".",",") + " reales brasileños")
    #end convertir_divisas


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    dialogo = ConversorMonedas()
    dialogo.show()
    
    sys.exit(app.exec_())        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            
            
        

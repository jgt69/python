'''

Created on 26 mar. 2020

'''
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from CalculadoraDialog import CalculadoraDialog

class CalculadoraApplication(QDialog):
    
    def __init__(self):
        
        super().__init__()
               
        self.ui = CalculadoraDialog()
        self.ui.setupUi(self)
        
        self.ui.btn_sumar.clicked.connect(self.sumar)
        self.ui.btn_restar.clicked.connect(self.restar)
        self.ui.btn_multiplicar.clicked.connect(self.multiplicar)
        self.ui.btn_dividir.clicked.connect(self.dividir)
        
        self.show()
        
    def sumar(self):
        suma = 0
        num1 = 0
        num2 = 0
        
        if len(self.ui.txt_primer_numero.text()) > 0:
            num1 = int(self.ui.txt_primer_numero.text())
            
        if len(self.ui.txt_segundo_numero.text()) > 0:
            num2 = int(self.ui.txt_segundo_numero.text())
            
        suma = num1 + num2
        
        self.ui.txt_resultado.setText(str(suma))
        
    def restar(self): 
        resta = 0
        num1 = 0
        num2 = 0
        
        if len(self.ui.txt_primer_numero.text()) > 0:
            num1 = int(self.ui.txt_primer_numero.text())
            
        if len(self.ui.txt_segundo_numero.text()) > 0:
            num2 = int(self.ui.txt_segundo_numero.text())
            
        resta = num1 - num2
        
        self.ui.txt_resultado.setText(str(resta))
    
    def multiplicar(self):
        multiplica = 0
        num1 = 0
        num2 = 0
        
        if len(self.ui.txt_primer_numero.text()) > 0:
            num1 = int(self.ui.txt_primer_numero.text())
            
        if len(self.ui.txt_segundo_numero.text()) > 0:
            num2 = int(self.ui.txt_segundo_numero.text())
            
        multiplica = num1 * num2
        
        self.ui.txt_resultado.setText(str(multiplica))
    
    def dividir(self):
        division = 0
        num1 = 0
        num2 = 0
        
        if len(self.ui.txt_primer_numero.text()) > 0:
            num1 = int(self.ui.txt_primer_numero.text())
            
        if len(self.ui.txt_segundo_numero.text()) > 0:
            num2 = int(self.ui.txt_segundo_numero.text())
            
        division = num1 / num2
        
        self.ui.txt_resultado.setText(str(division))
                
                 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = CalculadoraApplication()
    dialogo.show()
    
    sys.exit(app.exec_())
'''

Created on 25 mar. 2020

'''
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication,QPushButton,QWidget
from DialogPizza import PizzaDialog

class PizzaDialogApplication(QDialog):
    def __init__(self):
        super().__init__()
        
        self.ui = PizzaDialog()
        self.ui.setupUi(self)
        
        self.ui.chk_queso.stateChanged.connect(self.calcular_precio_final)
        self.ui.chk_aceitunas.stateChanged.connect(self.calcular_precio_final)
        self.ui.chk_salsas.stateChanged.connect(self.calcular_precio_final)
        
        self.show()
        
    def calcular_precio_final(self):
        precio_base = 15
        
        if self.ui.chk_queso.isChecked() == True:
            precio_base += 1
            
        if self.ui.chk_aceitunas.isChecked() == True:
            precio_base += 1
            
        if self.ui.chk_salsas.isChecked() == True:
            precio_base += 2
            
        self.ui.precio_final.setText('El precio final es {}€'.format(precio_base))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = PizzaDialogApplication()
    dialogo.show()
        
    sys.exit(app.exec_())
        
        
        
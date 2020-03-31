'''

Created on 25 mar. 2020

'''
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from HeladeriaDialog import HeladeriaDialog

class HeladeriaDialogApplication(QDialog):
    
    def __init__(self):
        super().__init__()
        
        self.ui = HeladeriaDialog()
        self.ui.setupUi(self)
        
        self.ui.chk_chocolate.stateChanged.connect(self.calcular_total)
        self.ui.chk_vainilla.stateChanged.connect(self.calcular_total)
        self.ui.chk_fresa.stateChanged.connect(self.calcular_total)
        self.ui.chk_ron_pasas.stateChanged.connect(self.calcular_total)
        
        self.ui.chk_cafe.stateChanged.connect(self.calcular_total)
        self.ui.chk_agua.stateChanged.connect(self.calcular_total)
        self.ui.chk_refresco.stateChanged.connect(self.calcular_total)
        
        self.show()
        
    
    def calcular_total(self):
        
        total = 0.0
        
        if self.ui.chk_chocolate.isChecked()  == True:
            total += 3.0
            
        if self.ui.chk_vainilla.isChecked() == True:
            total += 2.0
            
        if self.ui.chk_fresa.isChecked() == True:
            total += 2.0
            
        if self.ui.chk_ron_pasas.isChecked() == True:
            total += 3.0
            
        if self.ui.chk_cafe.isChecked() == True:
            total += 2.0
            
        if self.ui.chk_agua.isChecked() == True:
            total += 1.0
            
        if self.ui.chk_refresco.isChecked() == True:
            total += 3.0
            
        self.ui.lbl_total.setText('El precio total de su pedido es {}'.format(total))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = HeladeriaDialogApplication()
    dialogo.show()
    
    sys.exit(app.exec_())
    
            
            
        
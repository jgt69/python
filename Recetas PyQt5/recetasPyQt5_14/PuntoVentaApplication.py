'''

Created on 27 mar. 2020

'''
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QDialog,QApplication
from PuntoVentaDialog import PuntoVentaDialog

class PuntoVentaApplication(QDialog):
    
    def __init__(self):
        
        super().__init__()
        
        self.ui = PuntoVentaDialog()
        self.ui.setupUi(self)
        
        self.ui.sbx_cantidad_mouse.editingFinished.connect(self.calcular_total)
        self.ui.sbx_cantidad_teclado.editingFinished.connect(self.calcular_total)
        
        self.show()
        
    def calcular_total(self):
        precio_mouse = int(self.ui.txt_valor_mouse.text())
        precio_teclado = int(self.ui.txt_valor_teclado.text())
        
        cantidad_mouse = int(self.ui.sbx_cantidad_mouse.value())
        cantidad_teclado = int(self.ui.sbx_cantidad_teclado.value())
        
        subtotal_mouse = precio_mouse * cantidad_mouse
        subtotal_teclado = precio_teclado * cantidad_teclado
        
        self.ui.txt_subtotal_mouse.setText(str(subtotal_mouse))
        self.ui.txt_subtotal_teclado.setText(str(subtotal_teclado))
        
        total = subtotal_mouse + subtotal_teclado
        
        self.ui.lbl_gran_total.setText(str(total) + "€")
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    dialogo = PuntoVentaApplication()
    dialogo.show()
    
    sys.exit(app.exec_())          
        
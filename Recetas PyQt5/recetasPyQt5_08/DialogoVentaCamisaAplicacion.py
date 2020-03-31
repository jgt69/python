'''

Created on 25 mar. 2020

'''
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QDialog,QApplication
from DialogoVentanaCamisa import DialogoVentaCamisa

class DialogoVentaCamisaAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        
        self.ui = DialogoVentaCamisa()
        self.ui.setupUi(self)
        
        self.ui.rbn_talla_xl.toggled.connect(self.mostar_informacion)
        self.ui.rbn_talla_l.toggled.connect(self.mostar_informacion)
        self.ui.rbn_talla_m.toggled.connect(self.mostar_informacion)
        self.ui.rbn_talla_s.toggled.connect(self.mostar_informacion)
        
        self.ui.rbn_pago_tarjeta.toggled.connect(self.mostar_informacion)
        self.ui.rbn_contado.toggled.connect(self.mostar_informacion)
        self.ui.rbn_cheque_regalo.toggled.connect(self.mostar_informacion)
        
        self.show()
    
    def mostar_informacion(self):
        
        talla_seleccionada =''
        metodo_pago = ''
        
        if self.ui.rbn_talla_xl.isChecked() == True:
            talla_seleccionada = 'XL'
            
        if self.ui.rbn_talla_l.isChecked() == True:
            talla_seleccionada = 'L'
            
        if self.ui.rbn_talla_m.isChecked() == True:
            talla_seleccionada = 'M'
            
        if self.ui.rbn_talla_s.isChecked() == True:
            talla_seleccionada = 'S'
            
        if self.ui.rbn_pago_tarjeta.isChecked() == True:
            metodo_pago = 'y pago con tarjeta'
            
        if self.ui.rbn_contado.isChecked() == True:
            metodo_pago = 'y pago al contado'
            
        if self.ui.rbn_cheque_regalo.isChecked() == True:
            metodo_pago = "y pago con cheque regalo"
            
        self.ui.lbl_selecciones.setText('La talla es la {} {}'
                    .format(talla_seleccionada,metodo_pago))
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = DialogoVentaCamisaAplicacion()
    dialogo.show()
    
    sys.exit(app.exec_())
    
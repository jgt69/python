'''

Created on 31 mar. 2020

'''
# -*- coding: utf-8 -*-

import sys
from DiagnosticosDialog import DiagnosticosDialog
from PyQt5.QtWidgets import QDialog, QApplication

class DiagnosticosAplication(QDialog):
    
    def __init__(self):
        
        super().__init__()
        
        self.ui = DiagnosticosDialog()
        self.ui.setupUi(self)
        
        self.ui.lst_diagnosticos.itemClicked.connect(self.seleccion)
        
        self.show()
        
    def seleccion(self):
        self.ui.lbl_resultado.setText("Ha seleccionado: {}".format(self.ui.lst_diagnosticos.currentItem().text()))
        
        
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    dialogo = DiagnosticosAplication()
    dialogo.show()

    sys.exit(app.exec_())
    
    
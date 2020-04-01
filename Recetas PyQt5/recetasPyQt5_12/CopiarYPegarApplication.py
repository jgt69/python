'''

Created on 25 mar. 2020

'''
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication,QWidget
from CopiarYPegarDialog import CopiarPegarDialog

class CopiarYPegarApplication(QDialog):
    
    def __init__(self):
        
        super().__init__()
        
        self.ui = CopiarPegarDialog()
        self.ui.setupUi(self)
        
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    dialogo = CopiarYPegarApplication()
    dialogo.show()
    
    sys.exit(app.exec_())


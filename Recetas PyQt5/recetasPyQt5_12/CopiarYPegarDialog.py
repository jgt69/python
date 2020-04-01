# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CopiarYPegarDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class CopiarPegarDialog(object):
    def setupUi(self, CopiarPegarDialog):
        CopiarPegarDialog.setObjectName("CopiarPegarDialog")
        CopiarPegarDialog.resize(360, 257)
        self.txt_origen = QtWidgets.QLineEdit(CopiarPegarDialog)
        self.txt_origen.setGeometry(QtCore.QRect(80, 30, 211, 20))
        self.txt_origen.setObjectName("txt_origen")
        self.btn_copiar = QtWidgets.QPushButton(CopiarPegarDialog)
        self.btn_copiar.setGeometry(QtCore.QRect(150, 80, 75, 23))
        self.btn_copiar.setObjectName("btn_copiar")
        self.btn_pegar = QtWidgets.QPushButton(CopiarPegarDialog)
        self.btn_pegar.setGeometry(QtCore.QRect(150, 130, 75, 23))
        self.btn_pegar.setObjectName("btn_pegar")
        self.txt_destino = QtWidgets.QLineEdit(CopiarPegarDialog)
        self.txt_destino.setGeometry(QtCore.QRect(80, 180, 211, 20))
        self.txt_destino.setObjectName("txt_destino")

        self.retranslateUi(CopiarPegarDialog)
        self.btn_pegar.clicked.connect(self.txt_destino.paste)
        self.btn_copiar.pressed.connect(self.txt_origen.selectAll)
        self.btn_copiar.released.connect(self.txt_origen.copy)
        QtCore.QMetaObject.connectSlotsByName(CopiarPegarDialog)

    def retranslateUi(self, CopiarPegarDialog):
        _translate = QtCore.QCoreApplication.translate
        CopiarPegarDialog.setWindowTitle(_translate("CopiarPegarDialog", "Copiar y Pegar"))
        self.btn_copiar.setText(_translate("CopiarPegarDialog", "Copiar"))
        self.btn_pegar.setText(_translate("CopiarPegarDialog", "Pegar"))

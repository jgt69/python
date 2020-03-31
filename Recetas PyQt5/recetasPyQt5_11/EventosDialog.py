# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EventosDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class EventosDialog(object):
    def setupUi(self, EventosDialog):
        EventosDialog.setObjectName("EventosDialog")
        EventosDialog.resize(344, 229)
        self.txt_texto = QtWidgets.QLineEdit(EventosDialog)
        self.txt_texto.setGeometry(QtCore.QRect(80, 30, 191, 20))
        self.txt_texto.setObjectName("txt_texto")
        self.btn_cambiar = QtWidgets.QPushButton(EventosDialog)
        self.btn_cambiar.setGeometry(QtCore.QRect(130, 100, 75, 23))
        self.btn_cambiar.setObjectName("btn_cambiar")

        self.retranslateUi(EventosDialog)
        self.btn_cambiar.clicked.connect(self.txt_texto.clear)
        QtCore.QMetaObject.connectSlotsByName(EventosDialog)

    def retranslateUi(self, EventosDialog):
        _translate = QtCore.QCoreApplication.translate
        EventosDialog.setWindowTitle(_translate("EventosDialog", "Señales y Slots"))
        self.btn_cambiar.setText(_translate("EventosDialog", "Borrar"))

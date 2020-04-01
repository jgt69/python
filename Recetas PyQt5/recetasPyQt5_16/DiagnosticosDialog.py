# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DiagnosticosDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class DiagnosticosDialog(object):
    def setupUi(self, DiagnosticosDialog):
        DiagnosticosDialog.setObjectName("DiagnosticosDialog")
        DiagnosticosDialog.resize(362, 291)
        self.lbl_seleccion_diagnostico = QtWidgets.QLabel(DiagnosticosDialog)
        self.lbl_seleccion_diagnostico.setGeometry(QtCore.QRect(50, 30, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_seleccion_diagnostico.setFont(font)
        self.lbl_seleccion_diagnostico.setObjectName("lbl_seleccion_diagnostico")
        self.lst_diagnosticos = QtWidgets.QListWidget(DiagnosticosDialog)
        self.lst_diagnosticos.setGeometry(QtCore.QRect(40, 60, 256, 171))
        self.lst_diagnosticos.setObjectName("lst_diagnosticos")
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos.addItem(item)
        self.lbl_resultado = QtWidgets.QLabel(DiagnosticosDialog)
        self.lbl_resultado.setGeometry(QtCore.QRect(25, 250, 300, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setItalic(True)
        self.lbl_resultado.setFont(font)
        self.lbl_resultado.setText("")
        self.lbl_resultado.setObjectName("lbl_resultado")

        self.retranslateUi(DiagnosticosDialog)
        QtCore.QMetaObject.connectSlotsByName(DiagnosticosDialog)

    def retranslateUi(self, DiagnosticosDialog):
        _translate = QtCore.QCoreApplication.translate
        DiagnosticosDialog.setWindowTitle(_translate("DiagnosticosDialog", "Diagnósticos"))
        self.lbl_seleccion_diagnostico.setText(_translate("DiagnosticosDialog", "Seleccione el diagnóstico"))
        __sortingEnabled = self.lst_diagnosticos.isSortingEnabled()
        self.lst_diagnosticos.setSortingEnabled(False)
        item = self.lst_diagnosticos.item(0)
        item.setText(_translate("DiagnosticosDialog", "Rayos X - 5€"))
        item = self.lst_diagnosticos.item(1)
        item.setText(_translate("DiagnosticosDialog", "Nivel de azucar - 3€"))
        item = self.lst_diagnosticos.item(2)
        item.setText(_translate("DiagnosticosDialog", "Prueba de hemoglobina - 7€"))
        item = self.lst_diagnosticos.item(3)
        item.setText(_translate("DiagnosticosDialog", "Análisis de orina - 8€"))
        item = self.lst_diagnosticos.item(4)
        item.setText(_translate("DiagnosticosDialog", "Análisis de PSA - 10€"))
        self.lst_diagnosticos.setSortingEnabled(__sortingEnabled)

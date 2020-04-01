# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NivelesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class NivelesDialog(object):
    def setupUi(self, NivelesDialog):
        NivelesDialog.setObjectName("NivelesDialog")
        NivelesDialog.resize(484, 362)
        self.lbl_nivel_azucar = QtWidgets.QLabel(NivelesDialog)
        self.lbl_nivel_azucar.setGeometry(QtCore.QRect(30, 20, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nivel_azucar.setFont(font)
        self.lbl_nivel_azucar.setObjectName("lbl_nivel_azucar")
        self.hsb_nivel_azucar = QtWidgets.QScrollBar(NivelesDialog)
        self.hsb_nivel_azucar.setGeometry(QtCore.QRect(180, 20, 261, 16))
        self.hsb_nivel_azucar.setOrientation(QtCore.Qt.Horizontal)
        self.hsb_nivel_azucar.setObjectName("hsb_nivel_azucar")
        self.lbl_presion_arterial = QtWidgets.QLabel(NivelesDialog)
        self.lbl_presion_arterial.setGeometry(QtCore.QRect(30, 60, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_presion_arterial.setFont(font)
        self.lbl_presion_arterial.setObjectName("lbl_presion_arterial")
        self.hsd_presion_arterial = QtWidgets.QSlider(NivelesDialog)
        self.hsd_presion_arterial.setGeometry(QtCore.QRect(180, 50, 251, 22))
        self.hsd_presion_arterial.setOrientation(QtCore.Qt.Horizontal)
        self.hsd_presion_arterial.setObjectName("hsd_presion_arterial")
        self.lbl_pulso = QtWidgets.QLabel(NivelesDialog)
        self.lbl_pulso.setGeometry(QtCore.QRect(30, 110, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_pulso.setFont(font)
        self.lbl_pulso.setObjectName("lbl_pulso")
        self.vsb_pulso = QtWidgets.QScrollBar(NivelesDialog)
        self.vsb_pulso.setGeometry(QtCore.QRect(180, 110, 16, 160))
        self.vsb_pulso.setOrientation(QtCore.Qt.Vertical)
        self.vsb_pulso.setObjectName("vsb_pulso")
        self.lbl_nivel_colesterol = QtWidgets.QLabel(NivelesDialog)
        self.lbl_nivel_colesterol.setGeometry(QtCore.QRect(260, 110, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nivel_colesterol.setFont(font)
        self.lbl_nivel_colesterol.setObjectName("lbl_nivel_colesterol")
        self.vsd_nivel_colesterol = QtWidgets.QSlider(NivelesDialog)
        self.vsd_nivel_colesterol.setGeometry(QtCore.QRect(420, 110, 22, 160))
        self.vsd_nivel_colesterol.setOrientation(QtCore.Qt.Vertical)
        self.vsd_nivel_colesterol.setObjectName("vsd_nivel_colesterol")
        self.txt_resultado = QtWidgets.QLineEdit(NivelesDialog)
        self.txt_resultado.setGeometry(QtCore.QRect(30, 310, 401, 20))
        self.txt_resultado.setReadOnly(True)
        self.txt_resultado.setObjectName("txt_resultado")

        self.retranslateUi(NivelesDialog)
        QtCore.QMetaObject.connectSlotsByName(NivelesDialog)

    def retranslateUi(self, NivelesDialog):
        _translate = QtCore.QCoreApplication.translate
        NivelesDialog.setWindowTitle(_translate("NivelesDialog", "Niveles"))
        self.lbl_nivel_azucar.setText(_translate("NivelesDialog", "Nivel de azucar"))
        self.lbl_presion_arterial.setText(_translate("NivelesDialog", "Presión arterial"))
        self.lbl_pulso.setText(_translate("NivelesDialog", "Pulso"))
        self.lbl_nivel_colesterol.setText(_translate("NivelesDialog", "Nivel colesterol"))

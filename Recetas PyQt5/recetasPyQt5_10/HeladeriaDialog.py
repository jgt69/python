# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HeladeriaDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class HeladeriaDialog(object):
    def setupUi(self, HeladeriaDialog):
        HeladeriaDialog.setObjectName("HeladeriaDialog")
        HeladeriaDialog.resize(493, 321)
        self.lbl_menu = QtWidgets.QLabel(HeladeriaDialog)
        self.lbl_menu.setGeometry(QtCore.QRect(230, 20, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_menu.setFont(font)
        self.lbl_menu.setObjectName("lbl_menu")
        self.lbl_seleccione_helado = QtWidgets.QLabel(HeladeriaDialog)
        self.lbl_seleccione_helado.setGeometry(QtCore.QRect(60, 70, 111, 16))
        self.lbl_seleccione_helado.setObjectName("lbl_seleccione_helado")
        self.lbl_seleccione_bebida = QtWidgets.QLabel(HeladeriaDialog)
        self.lbl_seleccione_bebida.setGeometry(QtCore.QRect(290, 70, 111, 16))
        self.lbl_seleccione_bebida.setObjectName("lbl_seleccione_bebida")
        self.gbx_helados = QtWidgets.QGroupBox(HeladeriaDialog)
        self.gbx_helados.setGeometry(QtCore.QRect(50, 100, 171, 141))
        self.gbx_helados.setCheckable(True)
        self.gbx_helados.setObjectName("gbx_helados")
        self.chk_chocolate = QtWidgets.QCheckBox(self.gbx_helados)
        self.chk_chocolate.setGeometry(QtCore.QRect(10, 20, 91, 17))
        self.chk_chocolate.setObjectName("chk_chocolate")
        self.chk_vainilla = QtWidgets.QCheckBox(self.gbx_helados)
        self.chk_vainilla.setGeometry(QtCore.QRect(10, 50, 70, 17))
        self.chk_vainilla.setObjectName("chk_vainilla")
        self.chk_fresa = QtWidgets.QCheckBox(self.gbx_helados)
        self.chk_fresa.setGeometry(QtCore.QRect(10, 80, 70, 17))
        self.chk_fresa.setObjectName("chk_fresa")
        self.chk_ron_pasas = QtWidgets.QCheckBox(self.gbx_helados)
        self.chk_ron_pasas.setGeometry(QtCore.QRect(10, 110, 111, 17))
        self.chk_ron_pasas.setObjectName("chk_ron_pasas")
        self.gbx_bebidas = QtWidgets.QGroupBox(HeladeriaDialog)
        self.gbx_bebidas.setGeometry(QtCore.QRect(290, 100, 141, 111))
        self.gbx_bebidas.setCheckable(True)
        self.gbx_bebidas.setChecked(True)
        self.gbx_bebidas.setObjectName("gbx_bebidas")
        self.chk_cafe = QtWidgets.QCheckBox(self.gbx_bebidas)
        self.chk_cafe.setGeometry(QtCore.QRect(10, 20, 70, 17))
        self.chk_cafe.setObjectName("chk_cafe")
        self.chk_agua = QtWidgets.QCheckBox(self.gbx_bebidas)
        self.chk_agua.setGeometry(QtCore.QRect(10, 50, 70, 17))
        self.chk_agua.setObjectName("chk_agua")
        self.chk_refresco = QtWidgets.QCheckBox(self.gbx_bebidas)
        self.chk_refresco.setGeometry(QtCore.QRect(10, 80, 91, 17))
        self.chk_refresco.setObjectName("chk_refresco")
        self.lbl_total = QtWidgets.QLabel(HeladeriaDialog)
        self.lbl_total.setGeometry(QtCore.QRect(60, 270, 371, 16))
        self.lbl_total.setText("")
        self.lbl_total.setObjectName("lbl_total")

        self.retranslateUi(HeladeriaDialog)
        QtCore.QMetaObject.connectSlotsByName(HeladeriaDialog)

    def retranslateUi(self, HeladeriaDialog):
        _translate = QtCore.QCoreApplication.translate
        HeladeriaDialog.setWindowTitle(_translate("HeladeriaDialog", "Heladería"))
        self.lbl_menu.setText(_translate("HeladeriaDialog", "MENÙ"))
        self.lbl_seleccione_helado.setText(_translate("HeladeriaDialog", "Seleccione su helado"))
        self.lbl_seleccione_bebida.setText(_translate("HeladeriaDialog", "Seleccione su bebida"))
        self.gbx_helados.setTitle(_translate("HeladeriaDialog", "Helados"))
        self.chk_chocolate.setText(_translate("HeladeriaDialog", "Chocolate 3€"))
        self.chk_vainilla.setText(_translate("HeladeriaDialog", "Vainilla 2€"))
        self.chk_fresa.setText(_translate("HeladeriaDialog", "Fresa 2€"))
        self.chk_ron_pasas.setText(_translate("HeladeriaDialog", "Ron con pasas 3€"))
        self.gbx_bebidas.setTitle(_translate("HeladeriaDialog", "Bebidas"))
        self.chk_cafe.setText(_translate("HeladeriaDialog", "Café 2€"))
        self.chk_agua.setText(_translate("HeladeriaDialog", "Agua 1€"))
        self.chk_refresco.setText(_translate("HeladeriaDialog", "Refresco 3€"))

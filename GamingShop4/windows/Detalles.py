# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Detalles.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Detalles(object):
    def setupUi(self, Detalles):
        Detalles.setObjectName("Detalles")
        Detalles.resize(500, 850)
        self.centralwidget = QtWidgets.QWidget(Detalles)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_logo_marca = QtWidgets.QLabel(self.centralwidget)
        self.lbl_logo_marca.setGeometry(QtCore.QRect(30, 40, 150, 150))
        self.lbl_logo_marca.setText("")
        self.lbl_logo_marca.setScaledContents(True)
        self.lbl_logo_marca.setObjectName("lbl_logo_marca")
        self.lbl_marca = QtWidgets.QLabel(self.centralwidget)
        self.lbl_marca.setGeometry(QtCore.QRect(210, 50, 231, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_marca.setFont(font)
        self.lbl_marca.setText("")
        self.lbl_marca.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_marca.setObjectName("lbl_marca")
        self.lbl_tipo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_tipo.setGeometry(QtCore.QRect(210, 130, 231, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lbl_tipo.setFont(font)
        self.lbl_tipo.setText("")
        self.lbl_tipo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_tipo.setObjectName("lbl_tipo")
        self.lbl_imagen = QtWidgets.QLabel(self.centralwidget)
        self.lbl_imagen.setGeometry(QtCore.QRect(80, 220, 320, 420))
        self.lbl_imagen.setText("")
        self.lbl_imagen.setScaledContents(True)
        self.lbl_imagen.setObjectName("lbl_imagen")
        self.lbl_modelo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_modelo.setGeometry(QtCore.QRect(40, 660, 410, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lbl_modelo.setFont(font)
        self.lbl_modelo.setText("")
        self.lbl_modelo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_modelo.setObjectName("lbl_modelo")
        self.lbl_precio = QtWidgets.QLabel(self.centralwidget)
        self.lbl_precio.setGeometry(QtCore.QRect(229, 710, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lbl_precio.setFont(font)
        self.lbl_precio.setText("")
        self.lbl_precio.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_precio.setIndent(4)
        self.lbl_precio.setObjectName("lbl_precio")
        self.btn_volver = QtWidgets.QPushButton(self.centralwidget)
        self.btn_volver.setGeometry(QtCore.QRect(200, 780, 80, 30))
        self.btn_volver.setObjectName("btn_volver")
        Detalles.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Detalles)
        self.statusbar.setObjectName("statusbar")
        Detalles.setStatusBar(self.statusbar)

        self.retranslateUi(Detalles)
        QtCore.QMetaObject.connectSlotsByName(Detalles)

    def retranslateUi(self, Detalles):
        _translate = QtCore.QCoreApplication.translate
        Detalles.setWindowTitle(_translate("Detalles", "MainWindow"))
        self.btn_volver.setToolTip(_translate("Detalles", "Volver a la tabla de productos"))
        self.btn_volver.setText(_translate("Detalles", "VOLVER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Detalles = QtWidgets.QMainWindow()
    ui = Ui_Detalles()
    ui.setupUi(Detalles)
    Detalles.show()
    sys.exit(app.exec_())

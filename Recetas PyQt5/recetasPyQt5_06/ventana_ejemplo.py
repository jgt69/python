# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_ejemplo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 298)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boton_pulsame = QtWidgets.QPushButton(self.centralwidget)
        self.boton_pulsame.setGeometry(QtCore.QRect(250, 120, 141, 41))
        self.boton_pulsame.setToolTip("")
        self.boton_pulsame.setToolTipDuration(2)
        self.boton_pulsame.setObjectName("boton_pulsame")
        self.etiqueta_ventana = QtWidgets.QLabel(self.centralwidget)
        self.etiqueta_ventana.setGeometry(QtCore.QRect(130, 70, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(False)
        self.etiqueta_ventana.setFont(font)
        self.etiqueta_ventana.setAlignment(QtCore.Qt.AlignCenter)
        self.etiqueta_ventana.setObjectName("etiqueta_ventana")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.menuArchivo.addAction(self.actionAbrir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQt5-Example"))
        self.boton_pulsame.setText(_translate("MainWindow", "PULSAME"))
        self.etiqueta_ventana.setText(_translate("MainWindow", "PULSA EN EL BOTÓN"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Listado_1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Listado1Main(object):
    def setupUi(self, Listado1Main):
        Listado1Main.setObjectName("Listado1Main")
        Listado1Main.setGeometry(50, 50, 750, 500)
        Listado1Main.setWindowIcon(QIcon('./icon/anonymous.png'))
        self.centralwidget = QtWidgets.QWidget(Listado1Main)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_listado1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_listado1.setGeometry(QtCore.QRect(230, 20, 260, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_listado1.setFont(font)
        self.lbl_listado1.setObjectName("lbl_listado1")
        self.txt_listado1 = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_listado1.setGeometry(QtCore.QRect(10, 80, 730, 360))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.txt_listado1.setFont(font)
        self.txt_listado1.setFrameShape(QtWidgets.QFrame.Box)
        self.txt_listado1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.txt_listado1.setLineWidth(3)
        self.txt_listado1.setMidLineWidth(1)
        self.txt_listado1.setReadOnly(True)
        self.txt_listado1.setObjectName("txt_listado1")
        Listado1Main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Listado1Main)
        self.statusbar.setObjectName("statusbar")
        Listado1Main.setStatusBar(self.statusbar)

        self.retranslateUi(Listado1Main)
        QtCore.QMetaObject.connectSlotsByName(Listado1Main)

    def retranslateUi(self, Listado1Main):
        _translate = QtCore.QCoreApplication.translate
        Listado1Main.setWindowTitle(_translate("Listado1Main", "Listado Text Edit"))
        self.lbl_listado1.setText(_translate("Listado1Main", "Listado Text Edit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Listado1Main = QtWidgets.QMainWindow()
    ui = Listado1Main()
    ui.setupUi(Listado1Main)
    Listado1Main.show()
    sys.exit(app.exec_())

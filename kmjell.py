# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kmjell.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Kmjell(object):
    def setupUi(self, Kmjell):
        Kmjell.setObjectName("Kmjell")
        Kmjell.resize(688, 550)
        self.profil_csoport = QtWidgets.QComboBox(Kmjell)
        self.profil_csoport.setGeometry(QtCore.QRect(20, 20, 381, 22))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.profil_csoport.setFont(font)
        self.profil_csoport.setObjectName("profil_csoport")
        self.szelvenyek_listaja = QtWidgets.QComboBox(Kmjell)
        self.szelvenyek_listaja.setGeometry(QtCore.QRect(20, 50, 381, 22))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.szelvenyek_listaja.setFont(font)
        self.szelvenyek_listaja.setObjectName("szelvenyek_listaja")
        self.profil_csoport_kivalaszto = QtWidgets.QPushButton(Kmjell)
        self.profil_csoport_kivalaszto.setGeometry(QtCore.QRect(420, 20, 120, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.profil_csoport_kivalaszto.setFont(font)
        self.profil_csoport_kivalaszto.setObjectName("profil_csoport_kivalaszto")
        self.kivalaszto = QtWidgets.QPushButton(Kmjell)
        self.kivalaszto.setGeometry(QtCore.QRect(420, 50, 120, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.kivalaszto.setFont(font)
        self.kivalaszto.setObjectName("kivalaszto")
        self.pngkep = QtWidgets.QPushButton(Kmjell)
        self.pngkep.setGeometry(QtCore.QRect(550, 20, 120, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.pngkep.setFont(font)
        self.pngkep.setObjectName("pngkep")
        self.kmjellemzok = QtWidgets.QPushButton(Kmjell)
        self.kmjellemzok.setGeometry(QtCore.QRect(550, 50, 120, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.kmjellemzok.setFont(font)
        self.kmjellemzok.setObjectName("kmjellemzok")
        self.pngrajz = QtWidgets.QGraphicsView(Kmjell)
        self.pngrajz.setGeometry(QtCore.QRect(20, 80, 661, 461))
        self.pngrajz.setObjectName("pngrajz")

        self.retranslateUi(Kmjell)
        QtCore.QMetaObject.connectSlotsByName(Kmjell)

    def retranslateUi(self, Kmjell):
        _translate = QtCore.QCoreApplication.translate
        Kmjell.setWindowTitle(_translate("Kmjell", "Profilok keresztmetszeti jellemzői"))
        self.profil_csoport_kivalaszto.setText(_translate("Kmjell", "Profil-csoport"))
        self.kivalaszto.setText(_translate("Kmjell", "Kiválaszt"))
        self.pngkep.setText(_translate("Kmjell", "PNG-kép"))
        self.kmjellemzok.setText(_translate("Kmjell", "Km. jellemzők"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Kmjell = QtWidgets.QDialog()
    ui = Ui_Kmjell()
    ui.setupUi(Kmjell)
    Kmjell.show()
    sys.exit(app.exec_())

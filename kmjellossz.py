# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kmjellossz.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Kmjellossz(object):
    def setupUi(self, Kmjellossz):
        Kmjellossz.setObjectName("Kmjellossz")
        Kmjellossz.resize(1200, 507)
        self.pngrajz = QtWidgets.QGraphicsView(Kmjellossz)
        self.pngrajz.setGeometry(QtCore.QRect(550, 10, 640, 480))
        self.pngrajz.setObjectName("pngrajz")
        self.label = QtWidgets.QLabel(Kmjellossz)
        self.label.setGeometry(QtCore.QRect(10, 10, 271, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.uj_osszetett = QtWidgets.QLineEdit(Kmjellossz)
        self.uj_osszetett.setGeometry(QtCore.QRect(10, 40, 381, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.uj_osszetett.setFont(font)
        self.uj_osszetett.setObjectName("uj_osszetett")
        self.Ujszelveny = QtWidgets.QPushButton(Kmjellossz)
        self.Ujszelveny.setGeometry(QtCore.QRect(430, 40, 101, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.Ujszelveny.setFont(font)
        self.Ujszelveny.setObjectName("Ujszelveny")
        self.label_2 = QtWidgets.QLabel(Kmjellossz)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 251, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.osszetett_szelvenyek = QtWidgets.QComboBox(Kmjellossz)
        self.osszetett_szelvenyek.setGeometry(QtCore.QRect(10, 100, 381, 22))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.osszetett_szelvenyek.setFont(font)
        self.osszetett_szelvenyek.setObjectName("osszetett_szelvenyek")
        self.Szelveny_kivalaszt = QtWidgets.QPushButton(Kmjellossz)
        self.Szelveny_kivalaszt.setGeometry(QtCore.QRect(430, 100, 101, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.Szelveny_kivalaszt.setFont(font)
        self.Szelveny_kivalaszt.setObjectName("Szelveny_kivalaszt")
        self.line = QtWidgets.QFrame(Kmjellossz)
        self.line.setGeometry(QtCore.QRect(10, 130, 521, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(Kmjellossz)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 281, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.alkotoelemek = QtWidgets.QTableWidget(Kmjellossz)
        self.alkotoelemek.setGeometry(QtCore.QRect(10, 180, 521, 121))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.alkotoelemek.setFont(font)
        self.alkotoelemek.setRowCount(0)
        self.alkotoelemek.setObjectName("alkotoelemek")
        self.alkotoelemek.setColumnCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.alkotoelemek.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.alkotoelemek.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.alkotoelemek.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.alkotoelemek.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.alkotoelemek.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.alkotoelemek.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.alkotoelemek.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.alkotoelemek.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.alkotoelemek.setHorizontalHeaderItem(8, item)
        self.label_4 = QtWidgets.QLabel(Kmjellossz)
        self.label_4.setGeometry(QtCore.QRect(10, 310, 211, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Kmjellossz)
        self.label_5.setGeometry(QtCore.QRect(16, 340, 61, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.szelvenyek_listaja = QtWidgets.QComboBox(Kmjellossz)
        self.szelvenyek_listaja.setGeometry(QtCore.QRect(90, 340, 431, 22))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.szelvenyek_listaja.setFont(font)
        self.szelvenyek_listaja.setObjectName("szelvenyek_listaja")
        self.label_6 = QtWidgets.QLabel(Kmjellossz)
        self.label_6.setGeometry(QtCore.QRect(16, 370, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.diffx = QtWidgets.QLineEdit(Kmjellossz)
        self.diffx.setGeometry(QtCore.QRect(92, 370, 101, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.diffx.setFont(font)
        self.diffx.setObjectName("diffx")
        self.label_7 = QtWidgets.QLabel(Kmjellossz)
        self.label_7.setGeometry(QtCore.QRect(246, 370, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.diffy = QtWidgets.QLineEdit(Kmjellossz)
        self.diffy.setGeometry(QtCore.QRect(320, 370, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.diffy.setFont(font)
        self.diffy.setObjectName("diffy")
        self.label_8 = QtWidgets.QLabel(Kmjellossz)
        self.label_8.setGeometry(QtCore.QRect(440, 370, 47, 14))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Kmjellossz)
        self.label_9.setGeometry(QtCore.QRect(200, 370, 47, 14))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Kmjellossz)
        self.label_10.setGeometry(QtCore.QRect(16, 400, 61, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.forgatas = QtWidgets.QSlider(Kmjellossz)
        self.forgatas.setGeometry(QtCore.QRect(90, 400, 211, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.forgatas.setFont(font)
        self.forgatas.setOrientation(QtCore.Qt.Horizontal)
        self.forgatas.setObjectName("forgatas")
        self.fok = QtWidgets.QLineEdit(Kmjellossz)
        self.fok.setGeometry(QtCore.QRect(320, 400, 113, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.fok.setFont(font)
        self.fok.setObjectName("fok")
        self.label_11 = QtWidgets.QLabel(Kmjellossz)
        self.label_11.setGeometry(QtCore.QRect(440, 400, 47, 14))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.Mirrorx = QtWidgets.QRadioButton(Kmjellossz)
        self.Mirrorx.setGeometry(QtCore.QRect(80, 430, 141, 18))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.Mirrorx.setFont(font)
        self.Mirrorx.setObjectName("Mirrorx")
        self.Mirrory = QtWidgets.QRadioButton(Kmjellossz)
        self.Mirrory.setGeometry(QtCore.QRect(80, 460, 141, 18))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.Mirrory.setFont(font)
        self.Mirrory.setObjectName("Mirrory")
        self.szelveny_hozzaad = QtWidgets.QPushButton(Kmjellossz)
        self.szelveny_hozzaad.setGeometry(QtCore.QRect(390, 460, 131, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.szelveny_hozzaad.setFont(font)
        self.szelveny_hozzaad.setObjectName("szelveny_hozzaad")
        self.Szelveny_modositas = QtWidgets.QPushButton(Kmjellossz)
        self.Szelveny_modositas.setGeometry(QtCore.QRect(430, 150, 101, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.Szelveny_modositas.setFont(font)
        self.Szelveny_modositas.setObjectName("Szelveny_modositas")

        self.retranslateUi(Kmjellossz)
        QtCore.QMetaObject.connectSlotsByName(Kmjellossz)

    def retranslateUi(self, Kmjellossz):
        _translate = QtCore.QCoreApplication.translate
        Kmjellossz.setWindowTitle(_translate("Kmjellossz", "Összetett szelvény konfigurátor"))
        self.label.setText(_translate("Kmjellossz", "Új összetett szelvény definiálás:"))
        self.Ujszelveny.setText(_translate("Kmjellossz", "Hozzáadás"))
        self.label_2.setText(_translate("Kmjellossz", "Meglévő összetett szelvény:"))
        self.Szelveny_kivalaszt.setText(_translate("Kmjellossz", "Kiválaszt"))
        self.label_3.setText(_translate("Kmjellossz", "Az összetett szelvény alkotóelemei:"))
        item = self.alkotoelemek.horizontalHeaderItem(0)
        item.setText(_translate("Kmjellossz", "ID"))
        item = self.alkotoelemek.horizontalHeaderItem(1)
        item.setText(_translate("Kmjellossz", "Szelvénynév"))
        item = self.alkotoelemek.horizontalHeaderItem(2)
        item.setText(_translate("Kmjellossz", "DiffX"))
        item = self.alkotoelemek.horizontalHeaderItem(3)
        item.setText(_translate("Kmjellossz", "DiffY"))
        item = self.alkotoelemek.horizontalHeaderItem(4)
        item.setText(_translate("Kmjellossz", "Forgatás"))
        item = self.alkotoelemek.horizontalHeaderItem(5)
        item.setText(_translate("Kmjellossz", "Tükr_X"))
        item = self.alkotoelemek.horizontalHeaderItem(6)
        item.setText(_translate("Kmjellossz", "Tükr_Y"))
        item = self.alkotoelemek.horizontalHeaderItem(7)
        item.setText(_translate("Kmjellossz", "Hiba"))
        item = self.alkotoelemek.horizontalHeaderItem(8)
        item.setText(_translate("Kmjellossz", "Törlés"))
        self.label_4.setText(_translate("Kmjellossz", "Szelvény-hozzárendelés:"))
        self.label_5.setText(_translate("Kmjellossz", "Neve:"))
        self.label_6.setText(_translate("Kmjellossz", "Eltolás X:"))
        self.label_7.setText(_translate("Kmjellossz", "Eltolás Y:"))
        self.label_8.setText(_translate("Kmjellossz", "mm"))
        self.label_9.setText(_translate("Kmjellossz", "mm"))
        self.label_10.setText(_translate("Kmjellossz", "Forgatás:"))
        self.label_11.setText(_translate("Kmjellossz", "fok"))
        self.Mirrorx.setText(_translate("Kmjellossz", "Tükrözés X"))
        self.Mirrory.setText(_translate("Kmjellossz", "Tükrözés Y"))
        self.szelveny_hozzaad.setText(_translate("Kmjellossz", "Hozzárendelés"))
        self.Szelveny_modositas.setText(_translate("Kmjellossz", "Módosít"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Kmjellossz = QtWidgets.QDialog()
    ui = Ui_Kmjellossz()
    ui.setupUi(Kmjellossz)
    Kmjellossz.show()
    sys.exit(app.exec_())

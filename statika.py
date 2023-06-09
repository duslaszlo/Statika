# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statika.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from drotvaz import Ui_Drotvaz
from kettamaszu import Ui_Kettamaszu
from kmjell import Ui_Kmjell
from kmjellossz import Ui_Kmjellossz
from kocka import Ui_Kocka
from projekt import Ui_Projekt
from racstervezo import Ui_Racstervezo
from tartok import Ui_Tartok

class Ui_MainWindow(object):
    def openDrotvaz(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Drotvaz()
        self.ui.setupUi(self.window)
        self.window.show()

    def openKettamaszu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Kettamaszu()
        self.ui.setupUi(self.window)
        self.window.show()

    def openKmjell(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Kmjell()
        self.ui.setupUi(self.window)
        self.window.show()

    def openKmjellossz(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Kmjellossz()
        self.ui.setupUi(self.window)
        self.window.show()

    def openKocka(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Kocka()
        self.ui.setupUi(self.window)
        self.window.show()

    def openProjekt(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Projekt()
        self.ui.setupUi(self.window)
        self.window.show()

    def openRacstervezo(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Racstervezo()
        self.ui.setupUi(self.window)
        self.window.show()

    def openTartok(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Tartok()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1066, 668)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Photo = QtWidgets.QLabel(self.centralwidget)
        self.Photo.setGeometry(QtCore.QRect(0, 0, 1071, 631))
        self.Photo.setText("")
        self.Photo.setPixmap(QtGui.QPixmap("./img/359839pu.jpg"))
        self.Photo.setObjectName("Photo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1066, 22))
        self.menubar.setObjectName("menubar")
        self.menuProjektek = QtWidgets.QMenu(self.menubar)
        self.menuProjektek.setObjectName("menuProjektek")
        self.menuHat_rozott_tart_k = QtWidgets.QMenu(self.menubar)
        self.menuHat_rozott_tart_k.setObjectName("menuHat_rozott_tart_k")
        self.menuR_csos_szerkezetek = QtWidgets.QMenu(self.menubar)
        self.menuR_csos_szerkezetek.setObjectName("menuR_csos_szerkezetek")
        self.menuKeresztmetszeti_jellemz_k = QtWidgets.QMenu(self.menubar)
        self.menuKeresztmetszeti_jellemz_k.setObjectName("menuKeresztmetszeti_jellemz_k")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionA_projekt_tart_i = QtWidgets.QAction(MainWindow)
        self.actionA_projekt_tart_i.setObjectName("actionA_projekt_tart_i")
        self.actionA_tart_k_er_i = QtWidgets.QAction(MainWindow)
        self.actionA_tart_k_er_i.setObjectName("actionA_tart_k_er_i")
        self.actionDr_tv_zak_megjelen_t_se = QtWidgets.QAction(MainWindow)
        self.actionDr_tv_zak_megjelen_t_se.setObjectName("actionDr_tv_zak_megjelen_t_se")
        self.actionR_csszerkezet_tervez = QtWidgets.QAction(MainWindow)
        self.actionR_csszerkezet_tervez.setObjectName("actionR_csszerkezet_tervez")
        self.actionKockav_z_tervez_s = QtWidgets.QAction(MainWindow)
        self.actionKockav_z_tervez_s.setObjectName("actionKockav_z_tervez_s")
        self.actionKeresztmetszeti_jellemz_k = QtWidgets.QAction(MainWindow)
        self.actionKeresztmetszeti_jellemz_k.setObjectName("actionKeresztmetszeti_jellemz_k")
        self.actionLemezek_defini_l_sa = QtWidgets.QAction(MainWindow)
        self.actionLemezek_defini_l_sa.setObjectName("actionLemezek_defini_l_sa")
        self.actionsszetett_szelv_nyek = QtWidgets.QAction(MainWindow)
        self.actionsszetett_szelv_nyek.setObjectName("actionsszetett_szelv_nyek")
        self.actionA_projekt_be_ll_t_sa = QtWidgets.QAction(MainWindow)
        self.actionA_projekt_be_ll_t_sa.setObjectName("actionA_projekt_be_ll_t_sa")
        self.actionKil_p_s = QtWidgets.QAction(MainWindow)
        self.actionKil_p_s.setObjectName("actionKil_p_s")
        self.menuProjektek.addAction("A projekt beállítása", lambda: self.openProjekt())
        self.menuHat_rozott_tart_k.addAction("A projekt tartói", lambda: self.openTartok())
        self.menuHat_rozott_tart_k.addAction("A tartók erői", lambda: self.openKettamaszu())
        self.menuR_csos_szerkezetek.addAction("Drótvázak megjelenítése", lambda: self.openDrotvaz())
        self.menuR_csos_szerkezetek.addAction("Rácsszerkezet tervező", lambda: self.openRacstervezo())
        self.menuR_csos_szerkezetek.addAction("Kockaváz tervezés", lambda: self.openKocka())
        self.menuKeresztmetszeti_jellemz_k.addAction("Keresztmetszeti jellemzők", lambda: self.openKmjell())
        self.menuKeresztmetszeti_jellemz_k.addAction(self.actionLemezek_defini_l_sa)
        self.menuKeresztmetszeti_jellemz_k.addAction("Összetett szelvények", lambda: self.openKmjellossz())
        self.menubar.addAction(self.menuProjektek.menuAction())
        self.menubar.addAction(self.menuHat_rozott_tart_k.menuAction())
        self.menubar.addAction(self.menuR_csos_szerkezetek.menuAction())
        self.menubar.addAction(self.menuKeresztmetszeti_jellemz_k.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Statikai számítások és keresztmetszeti jellemők"))
        self.menuProjektek.setTitle(_translate("MainWindow", "Projektek"))
        self.menuHat_rozott_tart_k.setTitle(_translate("MainWindow", "Határozott tartók"))
        self.menuR_csos_szerkezetek.setTitle(_translate("MainWindow", "Rácsos szerkezetek"))
        self.menuKeresztmetszeti_jellemz_k.setTitle(_translate("MainWindow", "Keresztmetszeti jellemzők"))
        self.actionA_projekt_tart_i.setText(_translate("MainWindow", "A projekt tartói"))
        self.actionA_projekt_tart_i.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionA_tart_k_er_i.setText(_translate("MainWindow", "A tartók erői"))
        self.actionA_tart_k_er_i.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionDr_tv_zak_megjelen_t_se.setText(_translate("MainWindow", "Drótvázak megjelenítése"))
        self.actionDr_tv_zak_megjelen_t_se.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionR_csszerkezet_tervez.setText(_translate("MainWindow", "Rácsszerkezet tervező"))
        self.actionR_csszerkezet_tervez.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionKockav_z_tervez_s.setText(_translate("MainWindow", "Kockaváz tervezés"))
        self.actionKockav_z_tervez_s.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionKeresztmetszeti_jellemz_k.setText(_translate("MainWindow", "Keresztmetszeti jellemzők"))
        self.actionKeresztmetszeti_jellemz_k.setShortcut(_translate("MainWindow", "Ctrl+K"))
        self.actionLemezek_defini_l_sa.setText(_translate("MainWindow", "Lemezek definiálása"))
        self.actionsszetett_szelv_nyek.setText(_translate("MainWindow", "Összetett szelvények"))
        self.actionsszetett_szelv_nyek.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionA_projekt_be_ll_t_sa.setText(_translate("MainWindow", "A projekt beállítása"))
        self.actionA_projekt_be_ll_t_sa.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionKil_p_s.setText(_translate("MainWindow", "Kilépés"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

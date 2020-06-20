# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pages\hoca_ekrani.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HocaEkraniMainWindow(object):
    def setupUi(self, HocaEkraniMainWindow):
        HocaEkraniMainWindow.setObjectName("HocaEkraniMainWindow")
        HocaEkraniMainWindow.resize(510, 554)
        self.centralwidget = QtWidgets.QWidget(HocaEkraniMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
                                 "background: #354152;\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit{\n"
                                 " border: 1px solid gray;\n"
                                 "    border-radius: 10px;\n"
                                 "    min-width: 6em;\n"
                                 "    font-size:20px;\n"
                                 "    padding-left:15px;\n"
                                 "    height:42px;\n"
                                 "    border-radius:15px;\n"
                                 "    border-color: #303030;\n"
                                 "    background: transparent;\n"
                                 "    color:white;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton{\n"
                                 "border-radius: 15px;\n"
                                 "    background-color: qlineargradient(spread:reflect, x1:1, y1:0.466409, x2:0.188, y2:0.482727, stop:0.823864 rgba(82, 185, 143, 255), stop:1 rgba(115, 185, 153, 255));\n"
                                 "padding: 8px 16px;\n"
                                 "color: white;\n"
                                 "font-size: 20px;\n"
                                 "}\n"
                                 "QPushButton#btn_login:pressed{\n"
                                 "color: black;\n"
                                 "background: #008bd1\n"
                                 "}\n"
                                 "QCommandLinkButton{\n"
                                 "font-size: 16px;\n"
                                 "background: #4c5d75;\n"
                                 "}\n"
                                 "QCommandLinkButton:pressed{\n"
                                 "    background-color: rgb(92, 186, 138);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QCheckBox{\n"
                                 "font-size:16px;;\n"
                                 "color:white;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QCheckBox::indicator{\n"
                                 "    height:15px;\n"
                                 "    width:15px;\n"
                                 "\n"
                                 "}\n"
                                 "QComboBox {\n"
                                 "    border: 1px solid gray;\n"
                                 "    border-radius: 10px;\n"
                                 "    min-width: 6em;\n"
                                 "    font-size:20px;\n"
                                 "    padding-left:15px;\n"
                                 "    height:42px;\n"
                                 "    border-radius:15px;\n"
                                 "    border-color: #303030;\n"
                                 "    background: transparent;\n"
                                 "    color:white;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox:on {\n"
                                 "    border-bottom-left-radius: 0px;\n"
                                 "    border-bottom-right-radius: 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox QAbstractItemView {\n"
                                 "    border-bottom-right-radius: 10px;\n"
                                 "    border-bottom-left-radius: 10px;\n"
                                 "    background: #354152;\n"
                                 "    border: 1px solid gray;\n"
                                 "    color:white;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::drop-down {\n"
                                 "    border-color: white;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "QLabel{\n"
                                 "    color:white;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.text_AdSoyad = QtWidgets.QLineEdit(self.frame)
        self.text_AdSoyad.setEnabled(False)
        self.text_AdSoyad.setGeometry(QtCore.QRect(250, 30, 251, 44))
        self.text_AdSoyad.setObjectName("text_AdSoyad")
        self.text_Bolum = QtWidgets.QLineEdit(self.frame)
        self.text_Bolum.setEnabled(False)
        self.text_Bolum.setGeometry(QtCore.QRect(250, 90, 241, 44))
        self.text_Bolum.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.text_Bolum.setObjectName("text_Bolum")
        self.cmb_Model = QtWidgets.QComboBox(self.frame)
        self.cmb_Model.setGeometry(QtCore.QRect(250, 160, 241, 44))
        self.cmb_Model.setObjectName("cmb_Model")
        self.cmb_Model.addItem("")
        self.cmb_Model.addItem("")
        self.cmb_Model.addItem("")
        self.cmb_Model.addItem("")
        self.cmb_Metrik = QtWidgets.QComboBox(self.frame)
        self.cmb_Metrik.setGeometry(QtCore.QRect(250, 230, 241, 44))
        self.cmb_Metrik.setObjectName("cmb_Metrik")
        self.cmb_Metrik.addItem("")
        self.cmb_Metrik.addItem("")
        self.cmb_Metrik.addItem("")
        self.cmb_Dersler = QtWidgets.QComboBox(self.frame)
        self.cmb_Dersler.setGeometry(QtCore.QRect(12, 326, 471, 44))
        self.cmb_Dersler.setObjectName("cmb_Dersler")
        self.cmb_Dersler.addItem("")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(20, 400, 281, 31))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.btn_login = QtWidgets.QPushButton(self.frame)
        self.btn_login.setGeometry(QtCore.QRect(110, 470, 257, 40))
        self.btn_login.setStyleSheet("")
        self.btn_login.setObjectName("btn_login")
        self.image_ogretmen = QtWidgets.QLabel(self.frame)
        self.image_ogretmen.setGeometry(QtCore.QRect(19, 34, 211, 231))
        self.image_ogretmen.setStyleSheet("")
        self.image_ogretmen.setObjectName("image_ogretmen")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        HocaEkraniMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HocaEkraniMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 26))
        self.menubar.setObjectName("menubar")
        self.menuEkle = QtWidgets.QMenu(self.menubar)
        self.menuEkle.setObjectName("menuEkle")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        self.menuExit_2 = QtWidgets.QMenu(self.menubar)
        self.menuExit_2.setObjectName("menuExit_2")
        HocaEkraniMainWindow.setMenuBar(self.menubar)
        self.action_DersEkle = QtWidgets.QAction(HocaEkraniMainWindow)
        self.action_DersEkle.setObjectName("action_DersEkle")
        self.action_OgrenciDuzenle = QtWidgets.QAction(HocaEkraniMainWindow)
        self.action_OgrenciDuzenle.setObjectName("action_OgrenciDuzenle")
        self.action_OgrenciEkle = QtWidgets.QAction(HocaEkraniMainWindow)
        self.action_OgrenciEkle.setObjectName("action_OgrenciEkle")
        self.action_DerseOgrenciEkle = QtWidgets.QAction(HocaEkraniMainWindow)
        self.action_DerseOgrenciEkle.setObjectName("action_DerseOgrenciEkle")
        self.action_OgretmenDuzenle = QtWidgets.QAction(HocaEkraniMainWindow)
        self.action_OgretmenDuzenle.setObjectName("action_OgretmenDuzenle")
        self.actionExit_2 = QtWidgets.QAction(HocaEkraniMainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionExit = QtWidgets.QAction(HocaEkraniMainWindow)
        self.actionExit.setObjectName("actionExit")
        self.action_SayfayiYenile = QtWidgets.QAction(HocaEkraniMainWindow)
        self.action_SayfayiYenile.setObjectName("action_SayfayiYenile")
        self.sinif_liste = QtWidgets.QAction(HocaEkraniMainWindow)
        self.sinif_liste.setObjectName("action_SinifListesi")
        self.menuEkle.addAction(self.action_DersEkle)
        self.menuEkle.addAction(self.action_OgrenciEkle)
        self.menuEkle.addAction(self.action_DerseOgrenciEkle)
        self.menuExit.addAction(self.action_OgrenciDuzenle)
        self.menuExit.addAction(self.action_OgretmenDuzenle)
        self.menuExit.addAction(self.action_SayfayiYenile)
        self.menuExit.addAction(self.sinif_liste)
        self.menuExit_2.addAction(self.actionExit)
        self.menubar.addAction(self.menuEkle.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        self.menubar.addAction(self.menuExit_2.menuAction())

        self.retranslateUi(HocaEkraniMainWindow)
        QtCore.QMetaObject.connectSlotsByName(HocaEkraniMainWindow)

    def retranslateUi(self, HocaEkraniMainWindow):
        _translate = QtCore.QCoreApplication.translate
        HocaEkraniMainWindow.setWindowTitle(_translate("HocaEkraniMainWindow", "MainWindow"))
        self.text_AdSoyad.setPlaceholderText(_translate("HocaEkraniMainWindow", "Adı ve Soyadı"))
        self.text_Bolum.setPlaceholderText(_translate("HocaEkraniMainWindow", "Bölüm"))
        self.cmb_Model.setItemText(0, _translate("HocaEkraniMainWindow", "VGG-Face"))
        self.cmb_Model.setItemText(1, _translate("HocaEkraniMainWindow", "Facenet"))
        self.cmb_Metrik.setItemText(0, _translate("HocaEkraniMainWindow", "cosine"))
        self.cmb_Metrik.setItemText(1, _translate("HocaEkraniMainWindow", "euclidean"))
        self.cmb_Metrik.setItemText(2, _translate("HocaEkraniMainWindow", "euclidean_l2"))
        self.cmb_Dersler.setItemText(0, _translate("HocaEkraniMainWindow", "Öğretmene Ait Ders Kaydı Bulunamadı"))
        self.checkBox.setText(_translate("HocaEkraniMainWindow", "Duygu - Yaş - Cinsiyet Analizi"))
        self.btn_login.setText(_translate("HocaEkraniMainWindow", "SINIFI VE MODELİ YÜKLE"))
        self.image_ogretmen.setText(_translate("HocaEkraniMainWindow", "TextLabel"))
        self.menuEkle.setTitle(_translate("HocaEkraniMainWindow", "Ekle"))
        self.menuExit.setTitle(_translate("HocaEkraniMainWindow", "Düzenle"))
        self.menuExit_2.setTitle(_translate("HocaEkraniMainWindow", "Exit"))
        self.action_DersEkle.setText(_translate("HocaEkraniMainWindow", "Ders Ekle"))
        self.action_OgrenciDuzenle.setText(_translate("HocaEkraniMainWindow", "Öğrenci Düzenle"))
        self.action_OgrenciEkle.setText(_translate("HocaEkraniMainWindow", "Öğrenci Ekle"))
        self.action_DerseOgrenciEkle.setText(_translate("HocaEkraniMainWindow", "Öğrenciyi Derse Ekle"))
        self.action_OgretmenDuzenle.setText(_translate("HocaEkraniMainWindow", "Öğretmen Düzenle"))
        self.actionExit_2.setText(_translate("HocaEkraniMainWindow", "Exit"))
        self.actionExit.setText(_translate("HocaEkraniMainWindow", "Exit"))
        self.action_SayfayiYenile.setText(_translate("HocaEkraniMainWindow", "Sayfayı Yenile"))
        self.sinif_liste.setText(_translate("HocaEkraniMainWindow", "Sınıf Listesi"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    HocaEkraniMainWindow = QtWidgets.QMainWindow()
    ui = Ui_HocaEkraniMainWindow()
    ui.setupUi(HocaEkraniMainWindow)
    HocaEkraniMainWindow.show()
    sys.exit(app.exec_())

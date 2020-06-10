# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pages\ders_ekle.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DersEkleForm(object):
    def setupUi(self, DersEkleForm):
        DersEkleForm.setObjectName("DersEkleForm")
        DersEkleForm.resize(478, 744)
        DersEkleForm.setFixedSize(478, 744)
        self.gridLayout = QtWidgets.QGridLayout(DersEkleForm)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(DersEkleForm)
        self.frame.setStyleSheet("QFrame{\n"
                                 "background: #354152;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel{\n"
                                 "    font-size:24px;\n"
                                 "    color:white;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit{\n"
                                 "border-radius:10px;\n"
                                 "padding-left: 15px;\n"
                                 "font-size:16px;\n"
                                 "\n"
                                 "}\n"
                                 "QPushButton{\n"
                                 "height:42px;\n"
                                 "border-radius: 15px;\n"
                                 "    background-color: qlineargradient(spread:reflect, x1:1, y1:0.466409, x2:0.188, y2:0.482727, stop:0.823864 rgba(82, 185, 143, 255), stop:1 rgba(115, 185, 153, 255));\n"
                                 "padding: 8px 16px;\n"
                                 "color: white;\n"
                                 "font-size: 20px;\n"
                                 "}\n"
                                 "QPushButton:pressed{\n"
                                 "color: black;\n"
                                 "background: #008bd1\n"
                                 "\n"
                                 "}\n"
                                 "QGroupBox{\n"
                                 "border:none;\n"
                                 "\n"
                                 "}\n"
                                 "QComboBox {\n"
                                 "    border: 1px solid gray;\n"
                                 "    border-radius: 10px;\n"
                                 "    min-width: 6em;\n"
                                 "    font-size:16px;\n"
                                 "    padding-left:15px;\n"
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
                                 "    background: white;\n"
                                 "    border: 1px solid gray;\n"
                                 "    box-shadow: transparent;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::drop-down {\n"
                                 "    border-color: transparent;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "QSpinBox{\n"
                                 "height:42px;\n"
                                 "}\n"
                                 "\n"
                                 "QSpinBox {\n"
                                 "    /*text-align: center;*/\n"
                                 "    padding-right: 15px;\n"
                                 "    border-width: 5px;\n"
                                 "    border-radius:10px;\n"
                                 "    padding-left:15px;\n"
                                 "    font-size:20px;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QSpinBox::up-button, QSpinBox::down-button {\n"
                                 "     subcontrol-origin: border;\n"
                                 "     padding-left: 10px;\n"
                                 "     padding-right: 40px;\n"
                                 "     width: 16px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
                                 "     /*height: 14px;*/\n"
                                 "     border-width: 1px;\n"
                                 "     border-radius: 5px;\n"
                                 "     background-color: #eeeeee;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "QSpinBox::up-button {\n"
                                 "    subcontrol-position: top right; /* position at the top right corner */\n"
                                 "    height:42px;\n"
                                 "}\n"
                                 "\n"
                                 "QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
                                 "    background-color: #bbbb;\n"
                                 "}\n"
                                 "\n"
                                 "QSpinBox::up-arrow:disabled, QSpinBox::down-arrow:disabled {\n"
                                 "    image: none;\n"
                                 "}\n"
                                 "QSpinBox::up-arrow, QSpinBox::down-arrow {\n"
                                 "     width: 20px;\n"
                                 "     height: 20px;\n"
                                 "     border: 1px;\n"
                                 "}\n"
                                 "QSpinBox::up-arrow {\n"
                                 "padding-left:20px;\n"
                                 "    image: url(:/resimler/icons/chevron-up.png);\n"
                                 "}\n"
                                 "\n"
                                 "QSpinBox::down-button {\n"
                                 "    subcontrol-position: bottom left; /* position at bottom right corner */\n"
                                 "    height:42px;\n"
                                 "}\n"
                                 "\n"
                                 "QSpinBox::down-arrow {\n"
                                 "image: url(:/resimler/icons/chevron-down.png);\n"
                                 "padding-left:20px;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 30, 341, 61))
        self.label_2.setStyleSheet("color: white;\n"
                                   "font: 44px \"Helvetica Neue\", sans-serif;\n"
                                   "margin: 0px 0px 16px;")
        self.label_2.setObjectName("label_2")
        self.spin_Kontenjan = QtWidgets.QSpinBox(self.frame)
        self.spin_Kontenjan.setGeometry(QtCore.QRect(180, 520, 224, 42))
        self.spin_Kontenjan.setObjectName("spin_Kontenjan")
        self.cmb_Program = QtWidgets.QComboBox(self.frame)
        self.cmb_Program.setGeometry(QtCore.QRect(180, 400, 224, 44))
        self.cmb_Program.setObjectName("cmb_Program")
        self.cmb_Program.addItem("")
        self.cmb_Program.addItem("")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(47, 460, 126, 44))
        self.label_7.setObjectName("label_7")
        self.text_DersAdi = QtWidgets.QLineEdit(self.frame)
        self.text_DersAdi.setGeometry(QtCore.QRect(180, 222, 224, 42))
        self.text_DersAdi.setObjectName("text_DersAdi")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(47, 104, 126, 44))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(47, 164, 126, 42))
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(47, 578, 126, 42))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(47, 280, 126, 44))
        self.label_10.setObjectName("label_10")
        self.cmb_Sinif = QtWidgets.QComboBox(self.frame)
        self.cmb_Sinif.setGeometry(QtCore.QRect(180, 460, 224, 44))
        self.cmb_Sinif.setObjectName("cmb_Sinif")
        self.cmb_Sinif.addItem("")
        self.cmb_Sinif.addItem("")
        self.cmb_Sinif.addItem("")
        self.cmb_Sinif.addItem("")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(47, 520, 126, 42))
        self.label_8.setObjectName("label_8")
        self.cmb_Sube = QtWidgets.QComboBox(self.frame)
        self.cmb_Sube.setGeometry(QtCore.QRect(180, 340, 224, 44))
        self.cmb_Sube.setStyleSheet("")
        self.cmb_Sube.setObjectName("cmb_Sube")
        self.cmb_Sube.addItem("")
        self.cmb_Sube.addItem("")
        self.cmb_Sube.addItem("")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(47, 400, 126, 44))
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(47, 340, 126, 44))
        self.label_4.setObjectName("label_4")
        self.text_GenelKod = QtWidgets.QLineEdit(self.frame)
        self.text_GenelKod.setEnabled(False)
        self.text_GenelKod.setGeometry(QtCore.QRect(180, 578, 224, 42))
        self.text_GenelKod.setObjectName("text_GenelKod")
        self.cmb_Bolum = QtWidgets.QComboBox(self.frame)
        self.cmb_Bolum.setGeometry(QtCore.QRect(180, 280, 224, 44))
        self.cmb_Bolum.setObjectName("cmb_Bolum")
        self.cmb_Bolum.addItem("")
        self.cmb_Bolum.addItem("")
        self.cmb_Bolum.addItem("")
        self.cmb_Bolum.addItem("")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(47, 222, 126, 42))
        self.label_5.setObjectName("label_5")
        self.btn_DersEkle = QtWidgets.QPushButton(self.frame)
        self.btn_DersEkle.setGeometry(QtCore.QRect(47, 636, 357, 58))
        self.btn_DersEkle.setStyleSheet("")
        self.btn_DersEkle.setObjectName("btn_DersEkle")
        self.text_DersKodu = QtWidgets.QLineEdit(self.frame)
        self.text_DersKodu.setGeometry(QtCore.QRect(180, 164, 224, 42))
        self.text_DersKodu.setObjectName("text_DersKodu")
        self.text_adiSoyadi = QtWidgets.QLineEdit(self.frame)
        self.text_adiSoyadi.setGeometry(QtCore.QRect(180, 110, 224, 42))
        self.text_adiSoyadi.setObjectName("text_adiSoyadi")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(DersEkleForm)
        QtCore.QMetaObject.connectSlotsByName(DersEkleForm)
        DersEkleForm.setTabOrder(self.text_DersKodu, self.text_DersAdi)
        DersEkleForm.setTabOrder(self.text_DersAdi, self.cmb_Bolum)
        DersEkleForm.setTabOrder(self.cmb_Bolum, self.cmb_Sube)
        DersEkleForm.setTabOrder(self.cmb_Sube, self.cmb_Program)
        DersEkleForm.setTabOrder(self.cmb_Program, self.cmb_Sinif)
        DersEkleForm.setTabOrder(self.cmb_Sinif, self.spin_Kontenjan)
        DersEkleForm.setTabOrder(self.spin_Kontenjan, self.text_GenelKod)
        DersEkleForm.setTabOrder(self.text_GenelKod, self.btn_DersEkle)
        DersEkleForm.setTabOrder(self.btn_DersEkle, self.text_adiSoyadi)

    def retranslateUi(self, DersEkleForm):
        _translate = QtCore.QCoreApplication.translate
        DersEkleForm.setWindowTitle(_translate("DersEkleForm", "Form"))
        self.label_2.setText(_translate("DersEkleForm", "DERS EKLE"))
        self.cmb_Program.setItemText(0, _translate("DersEkleForm", "Sabah"))
        self.cmb_Program.setItemText(1, _translate("DersEkleForm", "Akşam"))
        self.label_7.setText(_translate("DersEkleForm", "Sınıf"))
        self.text_DersAdi.setText(_translate("DersEkleForm", "algoritma"))
        self.text_DersAdi.setPlaceholderText(_translate("DersEkleForm", "Ders Adı"))
        self.label.setText(_translate("DersEkleForm", "Ders Hocası"))
        self.label_3.setText(_translate("DersEkleForm", "Ders Kodu"))
        self.label_9.setText(_translate("DersEkleForm", "Genel Kod"))
        self.label_10.setText(_translate("DersEkleForm", "Bölüm"))
        self.cmb_Sinif.setItemText(0, _translate("DersEkleForm", "1"))
        self.cmb_Sinif.setItemText(1, _translate("DersEkleForm", "2"))
        self.cmb_Sinif.setItemText(2, _translate("DersEkleForm", "3"))
        self.cmb_Sinif.setItemText(3, _translate("DersEkleForm", "4"))
        self.label_8.setText(_translate("DersEkleForm", "Kontenjan"))
        self.cmb_Sube.setItemText(0, _translate("DersEkleForm", "A"))
        self.cmb_Sube.setItemText(1, _translate("DersEkleForm", "B"))
        self.cmb_Sube.setItemText(2, _translate("DersEkleForm", "C"))
        self.label_6.setText(_translate("DersEkleForm", "Programı"))
        self.label_4.setText(_translate("DersEkleForm", "Şube"))
        self.text_GenelKod.setPlaceholderText(_translate("DersEkleForm", "Genel Kod"))
        self.cmb_Bolum.setItemText(0, _translate("DersEkleForm", "Yazılım Mühendisliği"))
        self.cmb_Bolum.setItemText(1, _translate("DersEkleForm", "Bilgisayar Mühendisliği"))
        self.cmb_Bolum.setItemText(2, _translate("DersEkleForm", "Makine Mühendisliği"))
        self.cmb_Bolum.setItemText(3, _translate("DersEkleForm", "Otomotiv Mühendisliği"))
        self.label_5.setText(_translate("DersEkleForm", "Ders Adı"))
        self.btn_DersEkle.setText(_translate("DersEkleForm", "DERS EKLE"))
        self.text_DersKodu.setText(_translate("DersEkleForm", "ymt213"))
        self.text_DersKodu.setPlaceholderText(_translate("DersEkleForm", "Ders Kodu"))
        self.text_adiSoyadi.setPlaceholderText(_translate("DersEkleForm", "Ders Hocası"))



from ui_pages.resoruces_rc import *
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    DersEkleForm = QtWidgets.QWidget()
    ui = Ui_DersEkleForm()
    ui.setupUi(DersEkleForm)
    DersEkleForm.show()
    sys.exit(app.exec_())

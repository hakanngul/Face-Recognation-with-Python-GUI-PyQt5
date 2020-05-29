# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pages\ogrenci_duzenle.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OgrenciDuzenleForm(object):
    def setupUi(self, OgrenciDuzenleForm):
        OgrenciDuzenleForm.setObjectName("OgrenciDuzenleForm")
        OgrenciDuzenleForm.resize(569, 622)
        self.gridLayout = QtWidgets.QGridLayout(OgrenciDuzenleForm)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(OgrenciDuzenleForm)
        self.frame.setStyleSheet("QFrame{\n"
"background: #354152;\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit{\n"
"height: 45px;\n"
"border-radius:15px;\n"
"padding-left: 18px;\n"
"font-size: 20px;\n"
"background:white;\n"
"}\n"
"QPushButton{\n"
"height:32px;\n"
"border-radius: 15px;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.466409, x2:0.188, y2:0.482727, stop:0.823864 rgba(82, 185, 143, 255), stop:1 rgba(115, 185, 153, 255));\n"
"padding: 8px 16px;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"QPushButton:pressed{\n"
"color: black;\n"
"background: #008bd1\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ogrenci_update = QtWidgets.QPushButton(self.frame)
        self.ogrenci_update.setGeometry(QtCore.QRect(30, 540, 521, 51))
        self.ogrenci_update.setObjectName("ogrenci_update")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(230, 20, 331, 521))
        self.frame_2.setStyleSheet("QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    min-width: 6em;\n"
"    font-size:16px;\n"
"    padding-left:15px;\n"
"    height:42px;\n"
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
"QFrame{\n"
"border:none;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cmb_Sinif = QtWidgets.QComboBox(self.frame_2)
        self.cmb_Sinif.setObjectName("cmb_Sinif")
        self.cmb_Sinif.addItem("")
        self.cmb_Sinif.addItem("")
        self.cmb_Sinif.addItem("")
        self.cmb_Sinif.addItem("")
        self.gridLayout_2.addWidget(self.cmb_Sinif, 4, 1, 1, 1)
        self.cmb_Bolum = QtWidgets.QComboBox(self.frame_2)
        self.cmb_Bolum.setObjectName("cmb_Bolum")
        self.cmb_Bolum.addItem("")
        self.cmb_Bolum.addItem("")
        self.cmb_Bolum.addItem("")
        self.cmb_Bolum.addItem("")
        self.gridLayout_2.addWidget(self.cmb_Bolum, 3, 1, 1, 1)
        self.cmb_Sube = QtWidgets.QComboBox(self.frame_2)
        self.cmb_Sube.setStyleSheet("")
        self.cmb_Sube.setObjectName("cmb_Sube")
        self.cmb_Sube.addItem("")
        self.cmb_Sube.addItem("")
        self.cmb_Sube.addItem("")
        self.gridLayout_2.addWidget(self.cmb_Sube, 5, 1, 1, 1)
        self.cmb_Program = QtWidgets.QComboBox(self.frame_2)
        self.cmb_Program.setObjectName("cmb_Program")
        self.cmb_Program.addItem("")
        self.cmb_Program.addItem("")
        self.gridLayout_2.addWidget(self.cmb_Program, 6, 1, 1, 1)
        self.txt_bolum = QtWidgets.QLineEdit(self.frame_2)
        self.txt_bolum.setEnabled(False)
        self.txt_bolum.setStyleSheet("font-size:12px;")
        self.txt_bolum.setObjectName("txt_bolum")
        self.gridLayout_2.addWidget(self.txt_bolum, 3, 0, 1, 1)
        self.ogrenci_soyadi = QtWidgets.QLineEdit(self.frame_2)
        self.ogrenci_soyadi.setObjectName("ogrenci_soyadi")
        self.gridLayout_2.addWidget(self.ogrenci_soyadi, 2, 0, 1, 2)
        self.ogrenci_adi = QtWidgets.QLineEdit(self.frame_2)
        self.ogrenci_adi.setObjectName("ogrenci_adi")
        self.gridLayout_2.addWidget(self.ogrenci_adi, 1, 0, 1, 2)
        self.ogrenci_okulNo = QtWidgets.QLineEdit(self.frame_2)
        self.ogrenci_okulNo.setEnabled(False)
        self.ogrenci_okulNo.setObjectName("ogrenci_okulNo")
        self.gridLayout_2.addWidget(self.ogrenci_okulNo, 0, 0, 1, 2)
        self.txt_sinif = QtWidgets.QLineEdit(self.frame_2)
        self.txt_sinif.setEnabled(False)
        self.txt_sinif.setObjectName("txt_sinif")
        self.gridLayout_2.addWidget(self.txt_sinif, 4, 0, 1, 1)
        self.txt_sube = QtWidgets.QLineEdit(self.frame_2)
        self.txt_sube.setEnabled(False)
        self.txt_sube.setObjectName("txt_sube")
        self.gridLayout_2.addWidget(self.txt_sube, 5, 0, 1, 1)
        self.txt_program = QtWidgets.QLineEdit(self.frame_2)
        self.txt_program.setEnabled(False)
        self.txt_program.setObjectName("txt_program")
        self.gridLayout_2.addWidget(self.txt_program, 6, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(20, 20, 201, 461))
        self.frame_3.setStyleSheet("QFrame{\n"
"border:none;\n"
"}\n"
"\n"
"QLabel{\n"
"    height:200px;\n"
"}\n"
"\n"
"QPushButton{\n"
"height:42px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.resimYukle = QtWidgets.QPushButton(self.frame_3)
        self.resimYukle.setGeometry(QtCore.QRect(0, 220, 201, 41))
        self.resimYukle.setObjectName("resimYukle")
        self.ogrenci_resim = QtWidgets.QLabel(self.frame_3)
        self.ogrenci_resim.setGeometry(QtCore.QRect(0, 10, 200, 190))
        self.ogrenci_resim.setStyleSheet("background: white;\n"
"")
        self.ogrenci_resim.setAlignment(QtCore.Qt.AlignCenter)
        self.ogrenci_resim.setObjectName("ogrenci_resim")
        self.ogrenci_aldigiDersler = QtWidgets.QListWidget(self.frame_3)
        self.ogrenci_aldigiDersler.setGeometry(QtCore.QRect(0, 280, 201, 171))
        self.ogrenci_aldigiDersler.setStyleSheet("background: white;")
        self.ogrenci_aldigiDersler.setObjectName("ogrenci_aldigiDersler")
        self.btn_dersCikart = QtWidgets.QPushButton(self.frame)
        self.btn_dersCikart.setGeometry(QtCore.QRect(20, 480, 201, 41))
        self.btn_dersCikart.setObjectName("btn_dersCikart")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(OgrenciDuzenleForm)
        QtCore.QMetaObject.connectSlotsByName(OgrenciDuzenleForm)

    def retranslateUi(self, OgrenciDuzenleForm):
        _translate = QtCore.QCoreApplication.translate
        OgrenciDuzenleForm.setWindowTitle(_translate("OgrenciDuzenleForm", "Form"))
        self.ogrenci_update.setText(_translate("OgrenciDuzenleForm", "Güncelle"))
        self.cmb_Sinif.setItemText(0, _translate("OgrenciDuzenleForm", "1"))
        self.cmb_Sinif.setItemText(1, _translate("OgrenciDuzenleForm", "2"))
        self.cmb_Sinif.setItemText(2, _translate("OgrenciDuzenleForm", "3"))
        self.cmb_Sinif.setItemText(3, _translate("OgrenciDuzenleForm", "4"))
        self.cmb_Bolum.setItemText(0, _translate("OgrenciDuzenleForm", "Yazılım Mühendisliği"))
        self.cmb_Bolum.setItemText(1, _translate("OgrenciDuzenleForm", "Bilgisayar Mühendisliği"))
        self.cmb_Bolum.setItemText(2, _translate("OgrenciDuzenleForm", "Makine Mühendisliği"))
        self.cmb_Bolum.setItemText(3, _translate("OgrenciDuzenleForm", "Otomotiv Mühendisliği"))
        self.cmb_Sube.setItemText(0, _translate("OgrenciDuzenleForm", "A"))
        self.cmb_Sube.setItemText(1, _translate("OgrenciDuzenleForm", "B"))
        self.cmb_Sube.setItemText(2, _translate("OgrenciDuzenleForm", "C"))
        self.cmb_Program.setItemText(0, _translate("OgrenciDuzenleForm", "Sabah"))
        self.cmb_Program.setItemText(1, _translate("OgrenciDuzenleForm", "Akşam"))
        self.txt_bolum.setPlaceholderText(_translate("OgrenciDuzenleForm", "Bölüm"))
        self.ogrenci_soyadi.setPlaceholderText(_translate("OgrenciDuzenleForm", "Soyadı"))
        self.ogrenci_adi.setPlaceholderText(_translate("OgrenciDuzenleForm", "Adı"))
        self.ogrenci_okulNo.setPlaceholderText(_translate("OgrenciDuzenleForm", "Okul No"))
        self.txt_sinif.setPlaceholderText(_translate("OgrenciDuzenleForm", "Sınıf"))
        self.txt_sube.setPlaceholderText(_translate("OgrenciDuzenleForm", "Şube"))
        self.txt_program.setPlaceholderText(_translate("OgrenciDuzenleForm", "Program"))
        self.resimYukle.setText(_translate("OgrenciDuzenleForm", "Yeni Resim Çek"))
        self.ogrenci_resim.setText(_translate("OgrenciDuzenleForm", "Resim"))
        self.btn_dersCikart.setText(_translate("OgrenciDuzenleForm", "Dersi Çıkart"))

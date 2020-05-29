# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pages\kayit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OgretmenKayitForm(object):
    def setupUi(self, OgretmenKayitForm):
        OgretmenKayitForm.setObjectName("OgretmenKayitForm")
        OgretmenKayitForm.setWindowModality(QtCore.Qt.NonModal)
        OgretmenKayitForm.resize(424, 750)
        OgretmenKayitForm.setMouseTracking(False)
        OgretmenKayitForm.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        OgretmenKayitForm.setWindowTitle("Form")
        OgretmenKayitForm.setToolTipDuration(0)
        OgretmenKayitForm.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(OgretmenKayitForm)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(OgretmenKayitForm)
        self.frame.setMouseTracking(True)
        self.frame.setFocusPolicy(QtCore.Qt.NoFocus)
        self.frame.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frame.setAcceptDrops(False)
        self.frame.setToolTipDuration(0)
        self.frame.setStyleSheet("QFrame{\n"
"\n"
"background: #354152;\n"
"\n"
"}\n"
"\n"
"QLineEdit{\n"
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
"\n"
"}\n"
"\n"
"\n"
"\n"
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
"QPushButton{\n"
"border-radius: 15px;\n"
"background-color: qlineargradient(spread:reflect, x1:1, y1:0.466409, x2:0.188, y2:0.482727, stop:0.823864 rgba(82, 185, 143, 255), stop:1 rgba(115, 185, 153, 255));\n"
"padding: 8px 16px;\n"
"color: white;\n"
"font-size: 20px;\n"
"height:42px;\n"
"}\n"
"QPushButton:pressed{\n"
"color: black;\n"
"background: #008bd1\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 260, 371, 481))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_signup = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_signup.setStyleSheet("")
        self.btn_signup.setObjectName("btn_signup")
        self.gridLayout_2.addWidget(self.btn_signup, 6, 0, 1, 2)
        self.txt_mail = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_mail.setStyleSheet("")
        self.txt_mail.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txt_mail.setObjectName("txt_mail")
        self.gridLayout_2.addWidget(self.txt_mail, 5, 0, 1, 2)
        self.txt_soyadi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_soyadi.setObjectName("txt_soyadi")
        self.gridLayout_2.addWidget(self.txt_soyadi, 0, 1, 1, 1)
        self.txt_sifre = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_sifre.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.txt_sifre.setObjectName("txt_sifre")
        self.gridLayout_2.addWidget(self.txt_sifre, 3, 0, 1, 2)
        self.txt_kullaniciAdi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_kullaniciAdi.setObjectName("txt_kullaniciAdi")
        self.gridLayout_2.addWidget(self.txt_kullaniciAdi, 2, 0, 1, 2)
        self.txt_adi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_adi.setStyleSheet("color: rgb(255, 255, 255);")
        self.txt_adi.setObjectName("txt_adi")
        self.gridLayout_2.addWidget(self.txt_adi, 0, 0, 1, 1)
        self.txt_sifreTekrar = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_sifreTekrar.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.txt_sifreTekrar.setObjectName("txt_sifreTekrar")
        self.gridLayout_2.addWidget(self.txt_sifreTekrar, 4, 0, 1, 2)
        self.cmb_bolum = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cmb_bolum.setObjectName("cmb_bolum")
        self.cmb_bolum.addItem("")
        self.cmb_bolum.addItem("")
        self.cmb_bolum.addItem("")
        self.cmb_bolum.addItem("")
        self.gridLayout_2.addWidget(self.cmb_bolum, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 30, 369, 142))
        self.label.setStyleSheet("image: url(:/resimler/icons/damla.png);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 369, 69))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("color: #7E8BA3;\n"
"font: 44px \"Helvetica Neue\", sans-serif;\n"
"margin: 0px 0px 16px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(OgretmenKayitForm)
        QtCore.QMetaObject.connectSlotsByName(OgretmenKayitForm)
        OgretmenKayitForm.setTabOrder(self.txt_adi, self.txt_soyadi)
        OgretmenKayitForm.setTabOrder(self.txt_soyadi, self.txt_kullaniciAdi)
        OgretmenKayitForm.setTabOrder(self.txt_kullaniciAdi, self.txt_sifre)
        OgretmenKayitForm.setTabOrder(self.txt_sifre, self.txt_sifreTekrar)
        OgretmenKayitForm.setTabOrder(self.txt_sifreTekrar, self.txt_mail)
        OgretmenKayitForm.setTabOrder(self.txt_mail, self.btn_signup)

    def retranslateUi(self, OgretmenKayitForm):
        _translate = QtCore.QCoreApplication.translate
        self.btn_signup.setText(_translate("OgretmenKayitForm", "KAYIT OL"))
        self.txt_mail.setText(_translate("OgretmenKayitForm", "eragoln@gmail.com"))
        self.txt_mail.setPlaceholderText(_translate("OgretmenKayitForm", "info@mailadress.com"))
        self.txt_soyadi.setText(_translate("OgretmenKayitForm", "GÜL"))
        self.txt_soyadi.setPlaceholderText(_translate("OgretmenKayitForm", "Soyadı"))
        self.txt_sifre.setText(_translate("OgretmenKayitForm", "123"))
        self.txt_sifre.setPlaceholderText(_translate("OgretmenKayitForm", "Şifre"))
        self.txt_kullaniciAdi.setText(_translate("OgretmenKayitForm", "hakn"))
        self.txt_kullaniciAdi.setPlaceholderText(_translate("OgretmenKayitForm", "Kullanıcı Adı"))
        self.txt_adi.setText(_translate("OgretmenKayitForm", "Hakan"))
        self.txt_adi.setPlaceholderText(_translate("OgretmenKayitForm", "Adı"))
        self.txt_sifreTekrar.setText(_translate("OgretmenKayitForm", "123"))
        self.txt_sifreTekrar.setPlaceholderText(_translate("OgretmenKayitForm", "Tekrar Şifre"))
        self.cmb_bolum.setItemText(0, _translate("OgretmenKayitForm", "Yazılım Mühendisliği"))
        self.cmb_bolum.setItemText(1, _translate("OgretmenKayitForm", "Bilgisayar Mühendisliği"))
        self.cmb_bolum.setItemText(2, _translate("OgretmenKayitForm", "Makine Mühendisliği"))
        self.cmb_bolum.setItemText(3, _translate("OgretmenKayitForm", "Otomotiv Mühendisliği"))
        self.label_2.setText(_translate("OgretmenKayitForm", "KAYIT OL"))



from ui_pages.resoruces_rc import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OgretmenKayitForm = QtWidgets.QWidget()
    ui = Ui_OgretmenKayitForm()
    ui.setupUi(OgretmenKayitForm)
    OgretmenKayitForm.show()
    sys.exit(app.exec_())

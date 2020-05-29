# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pages\sinif_yukleme_sayfasi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SinifYukleForm(object):
    def setupUi(self, SinifYukleForm):
        SinifYukleForm.setObjectName("SinifYukleForm")
        SinifYukleForm.resize(514, 501)
        self.gridLayout = QtWidgets.QGridLayout(SinifYukleForm)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(SinifYukleForm)
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
                                 "font-size:24px;\n"
                                 "color:white;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QCheckBox::indicator{\n"
                                 "    height:25px;\n"
                                 "    width:25px;\n"
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
                                 "\n"
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
        self.btn_login = QtWidgets.QPushButton(self.frame)
        self.btn_login.setGeometry(QtCore.QRect(20, 420, 461, 42))
        self.btn_login.setStyleSheet("")
        self.btn_login.setObjectName("btn_login")
        self.text_Bolum = QtWidgets.QLineEdit(self.frame)
        self.text_Bolum.setGeometry(QtCore.QRect(230, 90, 251, 42))
        self.text_Bolum.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.text_Bolum.setObjectName("text_Bolum")
        self.text_AdSoyad = QtWidgets.QLineEdit(self.frame)
        self.text_AdSoyad.setGeometry(QtCore.QRect(230, 30, 251, 42))
        self.text_AdSoyad.setObjectName("text_AdSoyad")
        self.image_ogretmen = QtWidgets.QTextEdit(self.frame)
        self.image_ogretmen.setGeometry(QtCore.QRect(20, 20, 191, 241))
        self.image_ogretmen.setObjectName("image_ogretmen")
        self.cmb_Dersler = QtWidgets.QComboBox(self.frame)
        self.cmb_Dersler.setGeometry(QtCore.QRect(20, 290, 461, 45))
        self.cmb_Dersler.setObjectName("cmb_Dersler")
        self.cmb_Model = QtWidgets.QComboBox(self.frame)
        self.cmb_Model.setGeometry(QtCore.QRect(230, 150, 251, 45))
        self.cmb_Model.setObjectName("cmb_Model")
        self.cmb_Model.addItem("")
        self.cmb_Model.addItem("")
        self.cmb_Model.addItem("")
        self.cmb_Model.addItem("")
        self.cmb_Metrik = QtWidgets.QComboBox(self.frame)
        self.cmb_Metrik.setGeometry(QtCore.QRect(230, 210, 251, 45))
        self.cmb_Metrik.setObjectName("cmb_Metrik")
        self.cmb_Metrik.addItem("")
        self.cmb_Metrik.addItem("")
        self.cmb_Metrik.addItem("")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(30, 350, 351, 61))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(SinifYukleForm)
        QtCore.QMetaObject.connectSlotsByName(SinifYukleForm)

    def retranslateUi(self, SinifYukleForm):
        _translate = QtCore.QCoreApplication.translate
        SinifYukleForm.setWindowTitle(_translate("SinifYukleForm", "Form"))
        self.btn_login.setText(_translate("SinifYukleForm", "SINIFI VE MODELİ YÜKLE"))
        self.text_Bolum.setPlaceholderText(_translate("SinifYukleForm", "Bölüm"))
        self.text_AdSoyad.setPlaceholderText(_translate("SinifYukleForm", "Adı ve Soyadı"))
        self.cmb_Model.setItemText(0, _translate("SinifYukleForm", "VGG-Face"))
        self.cmb_Model.setItemText(1, _translate("SinifYukleForm", "OpenFace"))
        self.cmb_Model.setItemText(2, _translate("SinifYukleForm", "Facenet"))
        self.cmb_Model.setItemText(3, _translate("SinifYukleForm", "DeepFace"))
        self.cmb_Metrik.setItemText(0, _translate("SinifYukleForm", "cosine"))
        self.cmb_Metrik.setItemText(1, _translate("SinifYukleForm", "euclidean"))
        self.cmb_Metrik.setItemText(2, _translate("SinifYukleForm", "euclidean_l2"))
        self.checkBox.setText(_translate("SinifYukleForm", "Duygu - Yaş - Cinsiyet Analizi"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SinifYukleForm = QtWidgets.QWidget()
    ui = Ui_SinifYukleForm()
    ui.setupUi(SinifYukleForm)
    SinifYukleForm.show()
    sys.exit(app.exec_())

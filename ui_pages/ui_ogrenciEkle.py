# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pages\ogrenciEkle.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OgrenciEkleWindow(object):
    def setupUi(self, OgrenciEkleWindow):
        OgrenciEkleWindow.setObjectName("OgrenciEkleWindow")
        OgrenciEkleWindow.resize(500, 800)
        OgrenciEkleWindow.setFixedSize(500,800)
        OgrenciEkleWindow.setStyleSheet("")
        self.ana_widget = QtWidgets.QWidget(OgrenciEkleWindow)
        self.ana_widget.setObjectName("ana_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.ana_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.ana_widget)
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
                                 "QGroupBox{\n"
                                 "border: none;\n"
                                 "\n"
                                 "\n"
                                 "}\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                 "color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setStyleSheet("QLineEdit{\n"
                                    "height:42px;\n"
                                    "}\n"
                                    "QComboBox{\n"
                                    "height:42px;\n"
                                    "}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.txt_Okulno = QtWidgets.QLineEdit(self.groupBox)
        self.txt_Okulno.setPlaceholderText("")
        self.txt_Okulno.setObjectName("txt_Okulno")
        self.gridLayout_2.addWidget(self.txt_Okulno, 0, 1, 1, 1)
        self.txt_Adi = QtWidgets.QLineEdit(self.groupBox)
        self.txt_Adi.setPlaceholderText("")
        self.txt_Adi.setObjectName("txt_Adi")
        self.gridLayout_2.addWidget(self.txt_Adi, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
        self.cmb_Bolum = QtWidgets.QComboBox(self.groupBox)
        self.cmb_Bolum.setObjectName("cmb_Bolum")
        self.cmb_Bolum.addItem("")
        self.cmb_Bolum.addItem("")
        self.cmb_Bolum.addItem("")
        self.cmb_Bolum.addItem("")
        self.gridLayout_2.addWidget(self.cmb_Bolum, 3, 1, 1, 1)
        self.txt_Soyadi = QtWidgets.QLineEdit(self.groupBox)
        self.txt_Soyadi.setPlaceholderText("")
        self.txt_Soyadi.setObjectName("txt_Soyadi")
        self.gridLayout_2.addWidget(self.txt_Soyadi, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)
        self.cmb_Sinif = QtWidgets.QComboBox(self.groupBox)
        self.cmb_Sinif.setObjectName("cmb_Sinif")
        self.cmb_Sinif.addItem("")
        self.cmb_Sinif.addItem("")
        self.cmb_Sinif.addItem("")
        self.cmb_Sinif.addItem("")
        self.gridLayout_2.addWidget(self.cmb_Sinif, 6, 1, 1, 1)
        self.cmb_Sube = QtWidgets.QComboBox(self.groupBox)
        self.cmb_Sube.setStyleSheet("")
        self.cmb_Sube.setObjectName("cmb_Sube")
        self.cmb_Sube.addItem("")
        self.cmb_Sube.addItem("")
        self.cmb_Sube.addItem("")
        self.gridLayout_2.addWidget(self.cmb_Sube, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.cmb_Program = QtWidgets.QComboBox(self.groupBox)
        self.cmb_Program.setObjectName("cmb_Program")
        self.cmb_Program.addItem("")
        self.cmb_Program.addItem("")
        self.gridLayout_2.addWidget(self.cmb_Program, 5, 1, 1, 1)
        self.btn_kayit = QtWidgets.QPushButton(self.groupBox)
        self.btn_kayit.setObjectName("btn_kayit")
        self.gridLayout_2.addWidget(self.btn_kayit, 7, 0, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        OgrenciEkleWindow.setCentralWidget(self.ana_widget)
        self.menubar = QtWidgets.QMenuBar(OgrenciEkleWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        OgrenciEkleWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(OgrenciEkleWindow)
        # self.statusbar.setObjectName("statusbar")
        # OgrenciEkleWindow.setStatusBar(self.statusbar)
        self.actionStart_Camera = QtWidgets.QAction(OgrenciEkleWindow)
        self.actionStart_Camera.setObjectName("actionStart_Camera")
        self.actionStop_Camera = QtWidgets.QAction(OgrenciEkleWindow)
        self.actionStop_Camera.setObjectName("actionStop_Camera")
        self.actionExit = QtWidgets.QAction(OgrenciEkleWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionStart_Camera)
        self.menuMenu.addAction(self.actionStop_Camera)
        self.menuExit.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(OgrenciEkleWindow)
        QtCore.QMetaObject.connectSlotsByName(OgrenciEkleWindow)
        OgrenciEkleWindow.setTabOrder(self.txt_Okulno, self.txt_Adi)
        OgrenciEkleWindow.setTabOrder(self.txt_Adi, self.txt_Soyadi)
        OgrenciEkleWindow.setTabOrder(self.txt_Soyadi, self.cmb_Bolum)
        OgrenciEkleWindow.setTabOrder(self.cmb_Bolum, self.cmb_Sube)
        OgrenciEkleWindow.setTabOrder(self.cmb_Sube, self.cmb_Program)
        OgrenciEkleWindow.setTabOrder(self.cmb_Program, self.cmb_Sinif)
        OgrenciEkleWindow.setTabOrder(self.cmb_Sinif, self.btn_kayit)

    def retranslateUi(self, OgrenciEkleWindow):
        _translate = QtCore.QCoreApplication.translate
        OgrenciEkleWindow.setWindowTitle(_translate("OgrenciEkleWindow", "MainWindow"))
        self.label.setText(_translate("OgrenciEkleWindow", "KAMERA EKRANI"))
        self.txt_Okulno.setText(_translate("OgrenciEkleWindow", "185542008"))
        self.txt_Adi.setText(_translate("OgrenciEkleWindow", "HAKAN"))
        self.label_5.setText(_translate("OgrenciEkleWindow", "Soyadı"))
        self.label_10.setText(_translate("OgrenciEkleWindow", "Bölüm"))
        self.cmb_Bolum.setItemText(0, _translate("OgrenciEkleWindow", "Yazılım Mühendisliği"))
        self.cmb_Bolum.setItemText(1, _translate("OgrenciEkleWindow", "Bilgisayar Mühendisliği"))
        self.cmb_Bolum.setItemText(2, _translate("OgrenciEkleWindow", "Makine Mühendisliği"))
        self.cmb_Bolum.setItemText(3, _translate("OgrenciEkleWindow", "Otomotiv Mühendisliği"))
        self.txt_Soyadi.setText(_translate("OgrenciEkleWindow", "GÜL"))
        self.label_2.setText(_translate("OgrenciEkleWindow", "Okul No"))
        self.label_7.setText(_translate("OgrenciEkleWindow", "Sınıf"))
        self.cmb_Sinif.setItemText(0, _translate("OgrenciEkleWindow", "1"))
        self.cmb_Sinif.setItemText(1, _translate("OgrenciEkleWindow", "2"))
        self.cmb_Sinif.setItemText(2, _translate("OgrenciEkleWindow", "3"))
        self.cmb_Sinif.setItemText(3, _translate("OgrenciEkleWindow", "4"))
        self.cmb_Sube.setItemText(0, _translate("OgrenciEkleWindow", "A"))
        self.cmb_Sube.setItemText(1, _translate("OgrenciEkleWindow", "B"))
        self.cmb_Sube.setItemText(2, _translate("OgrenciEkleWindow", "C"))
        self.label_3.setText(_translate("OgrenciEkleWindow", "Adı"))
        self.label_4.setText(_translate("OgrenciEkleWindow", "Şube"))
        self.label_6.setText(_translate("OgrenciEkleWindow", "Programı"))
        self.cmb_Program.setItemText(0, _translate("OgrenciEkleWindow", "Sabah"))
        self.cmb_Program.setItemText(1, _translate("OgrenciEkleWindow", "Akşam"))
        self.btn_kayit.setText(_translate("OgrenciEkleWindow", "Öğrenciyi Ekle"))
        self.menuMenu.setTitle(_translate("OgrenciEkleWindow", "Menu"))
        self.menuExit.setTitle(_translate("OgrenciEkleWindow", "Exit"))
        self.actionStart_Camera.setText(_translate("OgrenciEkleWindow", "Start Camera"))
        self.actionStop_Camera.setText(_translate("OgrenciEkleWindow", "Stop Camera"))
        self.actionExit.setText(_translate("OgrenciEkleWindow", "Exit"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    OgrenciEkleWindow = QtWidgets.QMainWindow()
    ui = Ui_OgrenciEkleWindow()
    ui.setupUi(OgrenciEkleWindow)
    OgrenciEkleWindow.show()
    sys.exit(app.exec_())

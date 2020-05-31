from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, QCoreApplication

from PyQt5.QtWidgets import QWidget, QMessageBox

import DataBaseManager
from ui_pages.ui_login import Ui_LoginForm
from OgretmenKayit import KayitWidget
from hoca_ekrani import HocaEkraniWidget
import DBCreate


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginForm()
        self.mainWindow = None
        self.initUI()

    def initUI(self):
        self.ui.setupUi(self)

        self.ui.text_kullaniciAdi.setText("hakn")
        self.ui.text_Sifre.setText("123456")
        self.initSlots()

    @pyqtSlot()
    def kayitWidget(self):
        self.register = KayitWidget()

    def initSlots(self):
        self.ui.btn_login.clicked.connect(self.login)
        self.ui.btn_kayit.clicked.connect(self.kayitWidget)

    @pyqtSlot()
    def login(self):
        data = (
            self.ui.text_kullaniciAdi.text().lower(),
            self.ui.text_Sifre.text().lower(),
        )
        kadi = self.ui.text_kullaniciAdi.text().lower()
        sifre = self.ui.text_Sifre.text().lower()
        if self.ui.text_kullaniciAdi.text().lower() == "" or self.ui.text_Sifre.text().lower() in " ":
            QMessageBox.warning(self, "Dikkat !!", "Lütfen Kullanıcı Adını Adresini  Giriniz")
        elif self.ui.text_Sifre.text().lower() == "" or self.ui.text_Sifre.text().lower() in " ":
            QMessageBox.warning(self, "Dikkat !!", "Lütfen Şifre Giriniz")
        else:
            result = DataBaseManager.Teacher.TeacherLogin(data)
            print(result)
            if result:
                QMessageBox.information(self, "Login", "Giriş Başarılı")
                self.hoca_ekrani = HocaEkraniWidget(kadi, sifre)
                self.destroy(destroyWindow=True)
            else:
                QMessageBox.warning(self, "Dikkat !!", "Kullanıcı Adı veya Şifre Yanlış")


if __name__ == '__main__':
    import sys

    DBCreate.DBCreate()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    loginWindow = LoginWindow()
    loginWindow.show()
    sys.exit(app.exec_())

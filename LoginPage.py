from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox
import DBCreate
import DataBaseManager
from OgretmenKayit import KayitWidget
from hoca_ekrani import HocaEkraniWidget
from ui_pages.ui_login import Ui_LoginForm


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginForm()
        self.ui.setupUi(self)
        self.initSlots()

    def initSlots(self):
        self.ui.btn_login.clicked.connect(self.login)
        self.ui.btn_kayit.clicked.connect(self.kayitWidget)

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

    def kayitWidget(self):
        self.register = KayitWidget()


if __name__ == '__main__':
    import sys

    DBCreate.DBCreate()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    loginWindow = LoginWindow()
    loginWindow.show()
    sys.exit(app.exec_())

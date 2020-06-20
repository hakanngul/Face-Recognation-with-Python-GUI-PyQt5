from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QWidget, QMessageBox
from ui_pages.ui_ogretmenKayit import Ui_OgretmenKayitForm
import DataBaseManager


class KayitWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_OgretmenKayitForm()
        self.Teacher = DataBaseManager.Teacher()
        self.initUI()
        self.show()

    def initUI(self):
        self.ui.setupUi(self)
        self.initSlots()

    def initSlots(self):
        self.ui.btn_signup.clicked.connect(self.register)

    def register(self):
        imagePath = "ogretmenler/"
        data = (self.ui.txt_adi.text().lower(),
                self.ui.txt_soyadi.text().lower(),
                self.ui.cmb_bolum.currentText().lower(),
                self.ui.txt_kullaniciAdi.text().lower(),
                self.ui.txt_sifre.text().lower(),
                self.ui.txt_mail.text().lower(),
                imagePath)
        if self.ui.txt_adi.text() == "" or self.ui.txt_adi.text() == " " \
                or self.ui.txt_soyadi.text() == "" or self.ui.txt_soyadi.text() == " " \
                or self.ui.txt_kullaniciAdi.text() == "" or self.ui.txt_kullaniciAdi.text() == " " \
                or self.ui.txt_sifre.text() == "" or self.ui.txt_sifre.text() == " " \
                or self.ui.txt_mail.text() == "" or self.ui.txt_mail.text() == " ":
            QMessageBox.warning(self, "Uyarı", "Lütfen Bilgileri Eksiksiz Doldurun")
        elif self.ui.txt_sifre.text() != self.ui.txt_sifreTekrar.text():
            QMessageBox.warning(self, "Uyarı", "Şifreler Uyuşmamaktadır.")
        elif len(self.ui.txt_sifre.text()) < 6:
            QMessageBox.warning(self, "Uyarı", "Şifre En az 6 Karakterden Oluşmalıdır.")
        elif self.ui.txt_sifre.text() != self.ui.txt_sifreTekrar.text():
            QMessageBox.warning(self, "Uyarı", "Lütfen Şifreyi Düzgün Doldurun")
        else:
            KullaniciAdiKontrol = self.KullaniciAdiKontrol(self.ui.txt_kullaniciAdi.text().lower())
            MailKontrol = self.MailKontrol(self.ui.txt_mail.text().lower())
            if KullaniciAdiKontrol and MailKontrol:
                result = self.Teacher.TeacherSignedUp(data)
                if result:
                    QMessageBox.information(self, "Başarılı", "Kayıt Başarılı")
                    self.destroy(destroyWindow=True)
                else:
                    QMessageBox.warning(self, "Dikkat !!", "Kayıt Başarısız")
            else:
                QMessageBox.critical(self, "Dikkat", "Kayıt Başarısız Oldu")

    def KullaniciAdiKontrol(self, KullaniciAdi):
        result = self.Teacher.getTeacherUserName()
        liste = []
        print(KullaniciAdi)
        if len(KullaniciAdi) < 5:
            QMessageBox.warning(self, "Uyarı", "Kullanıcı Adı En az 6 Karakter Olmalıdır")
            return False
        else:
            for i in range(len(result)):
                veri = ",".join(result[i])
                liste.append(veri)
            if KullaniciAdi in liste:
                QMessageBox.warning(self, "Uyarı", "Bu Kullanıcı Adı Kullanılmaktadır. Lütfen Başka Seçiniz")
                return False
            else:
                QMessageBox.information(self, "Bilgi", "Kullanıcı adı kontrol edildi")
                return True

    def MailKontrol(self, mail):
        from email_validator import validate_email, EmailNotValidError
        result = self.Teacher.getTeacherMail()
        liste = []
        print(mail)
        for i in range(len(result)):
            veri = ",".join(result[i])
            liste.append(veri)
        try:
            valid = validate_email(mail)
            c_email = str(valid.email)
            if c_email in liste:
                QMessageBox.warning(self, "Uyarı", "Bu Mail Kullanılmaktadır. Lütfen Başka Seçiniz")
                return False
            else:
                QMessageBox.information(self, "Bilgi", "Mail Adresi kontrol edildi")
                return True
        except EmailNotValidError as e:
            QMessageBox.warning(self, "Uyarı", f'Lütfen Mailinizi Düzgün Giriniz {str(e)}')


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    loginWindow = KayitWidget()
    loginWindow.show()
    sys.exit(app.exec_())

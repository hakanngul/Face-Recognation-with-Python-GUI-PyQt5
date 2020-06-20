import cv2
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

import DataBaseManager
from ui_pages.ui_ogretmenDuzenle import Ui_OgretmenDuzenleForm


class OgretmenDuzenleWidget(QWidget):
    def __init__(self, hoca_KullaniciAdi, sifre):
        super(OgretmenDuzenleWidget, self).__init__()
        self.ui = Ui_OgretmenDuzenleForm()
        self.ui.setupUi(self)
        self.Teacher = DataBaseManager.Teacher()
        self.hoca_kadi = hoca_KullaniciAdi
        self.hoca_sifre = sifre
        self.getTeacherInformations()
        self.ui.btn_update.clicked.connect(self.UpdateInformations)
        self.ui.btn_resimCek.clicked.connect(self.YeniResimCek)
        self.show()

    def getTeacherInformations(self):
        result = list(self.Teacher.getTeacherInformation((self.hoca_kadi, self.hoca_sifre)))[0]
        self.id = result[0]
        adi = result[1]
        soyadi = result[2]
        bolum = result[3]
        self.KullaniciAdi = result[4]
        self.sifre = result[5]
        email = result[6]
        if result[7] is not None:
            verdigiDersler = result[7].split(",")
        else:
            verdigiDersler = []
        self.imagePath = result[8]
        data = [self.id, adi, soyadi, self.KullaniciAdi, email, verdigiDersler, bolum]
        self.UI_Settings(data)
        print("deneme")
        # print("giriş")
        # try:
        #     result = list(self.Teacher.getTeacherInformation((self.hoca_kadi, self.hoca_sifre)))[0]
        #     self.id = result[0]
        #     adi = result[1]
        #     soyadi = result[2]
        #     bolum = result[3]
        #     self.KullaniciAdi = result[4]
        #     self.sifre = result[5]
        #     email = result[6]
        #     verdigiDersler = result[7].split(",")
        #     self.imagePath = result[8]
        #     data = [self.id, adi, soyadi, self.KullaniciAdi, email, verdigiDersler, bolum]
        #     self.UI_Settings(data)
        #     print("deneme")
        # except:
        #     QMessageBox.warning(self, "Uyarı", "Öğretmen Bulunamadı")

    def UI_Settings(self, data):
        self.ui.list_verilenDersler.clear()
        self.ui.txt_id.setText(str(data[0]).upper())
        self.ui.txt_adi.setText(data[1].upper())
        self.ui.txt_soyadi.setText(data[2].upper())
        self.ui.txt_kadi.setText(data[3])
        self.ui.txt_mail.setText(data[4])
        self.ui.list_verilenDersler.addItems(data[5])
        self.ui.txt_bolum.setText(data[-1].upper())
        self.ui.txt_kadi.setEnabled(False)
        try:
            import os
            ImageTeacherPath = "ogretmenler/" + self.hoca_kadi + "_1.jpg"
            if not os.path.isfile(ImageTeacherPath):
                ImageTeacherPath = "ogretmenler/" + self.hoca_kadi + "_2.jpg"
            print("ImageStudentPath :", ImageTeacherPath)
            if os.path.isfile(ImageTeacherPath):
                self.ui.lbl_resim.setPixmap(QPixmap(ImageTeacherPath))
            else:
                self.ui.lbl_resim.setPixmap(QPixmap("images/personReal.png"))
            self.ui.lbl_resim.setScaledContents(True)
        except:
            print("Hata Oluştu")

    def UpdateInformations(self):
        sifre = self.ui.txt_sifre.text().strip()
        if sifre in "":
            QMessageBox.warning(self, "Uyarı", "Şifrenizi düzgün giriniz")
        elif sifre in " ":
            QMessageBox.warning(self, "Uyarı", "Şifrenizi düzgün giriniz")
        elif len(sifre) < 6:
            QMessageBox.warning(self, "Uyarı", "Şifreniz en az 6 karakter olmalıdır.")
        else:
            adi = self.ui.txt_adi.text().lower()
            soyadi = self.ui.txt_soyadi.text().lower()
            mail = self.ui.txt_mail.text().lower()
            bolum = self.ui.txt_bolum.text().lower()
            data = (
                adi, soyadi, bolum, sifre, mail, self.id, self.KullaniciAdi
            )
            try:
                res = self.Teacher.UpdateTeacherInformation(data)
            except:
                res = False
            if res:
                QMessageBox.information(self, "Bilgi", "Bilgiler Güncellendi")
                self.getTeacherInformations()
            else:
                QMessageBox.warning(self, "Uyarı", "Güncellemede Sorun Oluştu")

    def YeniResimCek(self):
        # TODO : Path => Ogrement/kadi şeklinde olacak
        QMessageBox.information(self, "Bilgi", "Resim Çekebilmek İçin Klavyenin Boşluk Tuşuna Basınız!!")
        QMessageBox.information(self, "Bilgi", "Resim Çekme İşlemini Sonlandırmak İçin 'q' tuşuna basınız!")
        path = "ogretmenler/"
        print(path)
        impCounter = 0
        cam = cv2.VideoCapture(0)
        while True:
            ret, frame = cam.read()
            cv2.imshow("test", frame)
            key = cv2.waitKey(1) & 0xFF
            if not ret:
                break
            if key == ord("q"):
                break
            elif key % 256 == 32:
                impCounter += 1
                img_name = path + self.ui.txt_kadi.text() + f'_{str(impCounter)}.jpg'
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                QMessageBox.information(self, "Bilgi", f'{img_name} Kayıt Edildi')
            elif impCounter > 2:
                QMessageBox.information(self, "Uyarı", f'{impCounter} adet fotoğraf yeterli')
                break
        cam.release()
        cv2.destroyAllWindows()
        self.getTeacherInformations()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    mainWindow = OgretmenDuzenleWidget("ibrahim", "123456")
    mainWindow.show()
    sys.exit(app.exec_())

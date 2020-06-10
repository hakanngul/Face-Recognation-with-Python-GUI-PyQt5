from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox

import DataBaseManager
from ui_pages.ui_dersEkle import Ui_DersEkleForm


class DersEkleWidget(QWidget):
    def __init__(self, ogretmen_kadi, ogretmen_sifre):
        super().__init__()
        print(ogretmen_kadi)
        print(ogretmen_sifre)
        self.ui = Ui_DersEkleForm()
        self.ui.setupUi(self)
        self.kadi = ogretmen_kadi
        self.sifre = ogretmen_sifre
        self.Teacher = DataBaseManager.Teacher()
        self.Lesson = DataBaseManager.Lessons()
        self.UI_Settings()
        self.getIformation()
        self.ui.btn_DersEkle.clicked.connect(self.HocayaDersEkle)
        self.show()

    def UI_Settings(self):
        self.ui.text_adiSoyadi.setEnabled(False)

    def getIformation(self):
        result = self.Teacher.getTeacherInformation((self.kadi, self.sifre))
        print("Ders Ekle İçi", result)
        if result is not None:
            self.id = result[0][0]
            if result[0][7] is not None:
                verdigiDersler = result[0][7].split(",")
                print(type(verdigiDersler))
                print(verdigiDersler)
            # TODO : Resim Eklemesi Yapılacak
            self.adi_soyadi = result[0][1] + " " + result[0][2]
            if result[0][3] is not None:
                self.bolum = result[0][3]
                self.ui.cmb_Bolum.clear()
                self.ui.cmb_Bolum.addItem(self.bolum.upper())
                self.ui.cmb_Bolum.setEnabled(False)
            self.BilgileriGom()
        else:
            QMessageBox.warning(self, "Uyarı", "Hocanın Bilgileri Çekmede Sorun oldu!!")
        # try:
        #     result = self.Teacher.getTeacherInformation(self.kadi,self.sifre)
        #     print("Ders Ekle İçi", result)
        #     if result is not None:
        #         self.id = result[0][0]
        #         if result[0][7] is not None:
        #             verdigiDersler = result[0][7].split(",")
        #             print(type(verdigiDersler))
        #             print(verdigiDersler)
        #         # TODO : Resim Eklemesi Yapılacak
        #         self.adi_soyadi = result[0][1] + " " + result[0][2]
        #         if result[0][3] is not None:
        #             self.bolum = result[0][3]
        #             self.ui.cmb_Bolum.clear()
        #             self.ui.cmb_Bolum.addItem(self.bolum.upper())
        #             self.ui.cmb_Bolum.setEnabled(False)
        #         self.BilgileriGom()
        #     else:
        #         print("Hocanın Bilgileri Çekmede Sorun oldu!!")
        # except:
        #     print("DersEkleWidget Sorun Oluştu!!!")

    def BilgileriGom(self):
        self.ui.text_adiSoyadi.setText(self.adi_soyadi.upper())
        # data = (
        #     dersAdi, dersKodu, int(kontenjan), dersSube, dersSinif, dersGenelkod, hoca_id, dersBolum, dersProgram,
        #     dersiAlanOgrenciler
        # )

    def DersEkle(self, data):
        # TODO: Dersler Tablosuna Eklenecek Method Burada Yazılacak
        kontenjan = self.ui.spin_Kontenjan.value()
        if kontenjan == 0:
            kontenjan = 60
        print("data :", data)
        # dersAdi, derskodu, sube, program, genelkod, id
        try:
            dersAdi = data[0]
            dersKodu = data[1]
            dersSube = data[2]
            dersProgram = data[3]
            dersGenelkod = data[4]
            hoca_id = data[5]
            dersBolum = self.ui.cmb_Bolum.currentText()
            dersSinif = self.ui.cmb_Sinif.currentText()
        except:
            print("DersEkleFonksiyonu Hatası")
        data = (
            dersAdi, dersKodu, int(kontenjan), dersSube, dersSinif, dersGenelkod, hoca_id, dersBolum, dersProgram)
        result = self.Lesson.AddLesson(data)
        if result:
            QMessageBox.information(self, "Bilgi", "Ders Başarıyla Eklendi")
            return True
        else:
            QMessageBox.warning(self, "Bilgi", "Ders Eklenemedi")
            return False

    def HocayaDersEkle(self):
        # TODO: Bu Öğretmene Ders Ekleme Fonksiyonu
        if self.ui.text_DersKodu.text() != "" or self.ui.text_DersKodu != " ":
            result = self.Teacher.getTeacherInformation((self.kadi, self.sifre))
            result = result[0]
            genelDersler = []
            id = result[0]
            derskodu = self.ui.text_DersKodu.text().lower()
            dersAdi = self.ui.text_DersAdi.text().lower()
            sube = self.ui.cmb_Sube.currentText()
            program = self.ui.cmb_Program.currentText()
            if program in "Sabah":
                print("Sabah Programı ", program)
                program = "S"
            else:
                print("Akşam Programı ", program)
                program = "A"
            genelkod = (derskodu + "-" + sube + "-" + program).upper()
            dersler = result[7]
            genelDersler.append(dersler)
            data = [dersAdi, derskodu, sube, program, genelkod, id]

            if dersler == None:
                dersler = genelkod
                sonuc = self.DersEkle(data)
                if sonuc:
                    self.Teacher.UpdateTeacherLessons((dersler, result[0]))
                    QMessageBox.information(self, "Bilgi", "Ders Başarıyla Eklendi")
                else:
                    QMessageBox.warning(self, "Hata", "Ders Eklenemedi!")
            elif genelkod in dersler:
                QMessageBox.warning(self, "Uyarı", "Bu ders zaten kayıtlı")
            elif ',' in dersler:
                dersler = dersler + ',' + genelkod
                sonuc = self.DersEkle(data)
                if sonuc:
                    self.Teacher.UpdateTeacherLessons((dersler, result[0]))
                    QMessageBox.information(self, "Bilgi", "Ders Başarıyla Eklendi")
                else:
                    QMessageBox.warning(self, "Hata", "Ders Eklenemedi!")
            elif len(genelDersler) < 2:
                dersler = dersler + ',' + genelkod
                sonuc = self.DersEkle(data)
                if sonuc:
                    self.Teacher.UpdateTeacherLessons((dersler, result[0]))
                    QMessageBox.information(self, "Bilgi", "Ders Başarıyla Eklendi")
                else:
                    QMessageBox.warning(self, "Hata", "Ders Eklenemedi!")

            else:
                QMessageBox.critical(self, "Dikkat", "Bir Sorun Oluştu Tekrar Deneyiniz!")

            self.ui.text_GenelKod.setText(genelkod)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    loginWindow = DersEkleWidget("hakn", "123456")
    loginWindow.show()
    sys.exit(app.exec_())

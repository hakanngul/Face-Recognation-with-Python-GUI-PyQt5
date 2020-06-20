import cv2
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

import DataBaseManager
from PyQt5.QtWidgets import QWidget, QMessageBox, QMainWindow, QListWidget, QListView
from ui_pages.ui_ogrenciDuzenle import Ui_OgrenciDuzenleForm


class OgrenciDuzenleWidget(QWidget):
    def __init__(self, ogrenci_no):
        super(OgrenciDuzenleWidget, self).__init__()
        self.ui = Ui_OgrenciDuzenleForm()
        self.ui.setupUi(self)
        self.Student = DataBaseManager.Student()
        self.Teacher = DataBaseManager.Teacher()
        self.Lesson = DataBaseManager.Lessons()
        self.ogrenci_no = ogrenci_no
        self.result = None
        self.UI_Settings()
        self.initSlots()
        self.show()

    def initSlots(self):
        self.ui.btn_dersCikart.clicked.connect(self.DersCikart)
        self.ui.ogrenci_update.clicked.connect(self.OgrenciUpdate)
        self.ui.resimYukle.clicked.connect(self.YeniResimCek)

    def UI_Settings(self):

        try:
            result = self.Student.getStudentInformations(self.ogrenci_no)
            self.result = list(result[0])
            print(self.result)
            self.OgrenciNo = self.result[1]
            self.ui.ogrenci_okulNo.setText(str(self.result[1]))
            self.ui.ogrenci_adi.setText(str(self.result[2]).upper())
            self.ui.ogrenci_soyadi.setText(str(self.result[3].upper()))
            self.ui.txt_bolum.setText(str(self.result[6]))
            self.ui.txt_sinif.setText(f'Sınıf  {str(self.result[5])}')
            self.ui.txt_sube.setText(f'Şube {str(self.result[7])}')
            if str(self.result[4]) == "S":
                self.ui.txt_program.setText("Sabah")
            else:
                self.ui.txt_program.setText("Akşam")

            self.path = self.result[-2]
            path = self.path + "/" + str(self.result[1])
            path = path + "_1.jpg"
            self.ImageStudentPath = path
            self.ui.ogrenci_resim.setPixmap(QPixmap(self.ImageStudentPath))
            self.ui.ogrenci_resim.setScaledContents(True)
            self.dersleriYuke()
        except:
            QMessageBox.critical(self, "Dikkat", "Bir Sorun Oluştu")

    def dersleriYuke(self):
        if self.result[-1] != "" and self.result[-1] is not None:
            self.dersler = self.result[-1].split(",")
            self.ui.ogrenci_aldigiDersler.clear()
            self.ui.ogrenci_aldigiDersler.addItems(self.dersler)
        else:
            self.dersler = []
            QMessageBox.warning(self, "Uyarı", "Öğrenciye Ait Kayıtlı Ders Yok")
            self.ui.btn_dersCikart.setEnabled(False)

    def YeniResimCek(self):
        # TODO : Path => DataBase/OgrenciNO/ olacak şekilde resim pathi düzenle kayıt almada
        QMessageBox.information(self, "Bilgi", "Resim Çekebilmek İçin Klavyenin Boşluk Tuşuna Basınız!!")
        QMessageBox.information(self, "Bilgi", "Resim Çekme İşlemini Sonlandırmak İçin 'q' tuşuna basınız!")
        path = self.path
        imgCunter = 0
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
                imgCunter += 1
                img_name = path + "/" + str(self.ui.ogrenci_okulNo.text()) + f'_{str(imgCunter)}.jpg'
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                # QMessageBox.information(self, "Bilgi", f'{img_name} Kayıt Edildi')
            elif imgCunter >= 3:
                QMessageBox.information(self, "Uyarı", f'{imgCunter} adet fotoğraf yeterli')
                break

        cam.release()
        cv2.destroyAllWindows()

    def OgrenciUpdate(self):
        adi = self.ui.ogrenci_adi.text().lower()
        soyadi = self.ui.ogrenci_soyadi.text().lower()
        bolum = self.ui.cmb_Bolum.currentText()
        sinif = self.ui.cmb_Sinif.currentText()
        program = self.ui.cmb_Program.currentText()
        if program == "Sabah":
            program ="S"
        else:
            program = "A"
        sube = self.ui.cmb_Sube.currentText()
        dersler = self.dersler
        dersler = ",".join(dersler)
        image_path = "database/" + str(self.ogrenci_no) + "/"
        # data = (adi, soyadi, program, sinif, bolum, sube, image_path, dersler, self.ui.ogrenci_okulNo.text())
        data = (
            adi, soyadi, program, sinif, bolum, sube, self.ui.ogrenci_okulNo.text()
        )
        self.UpdateStudent(data)

    def UpdateStudent(self, data):
        try:
            result = self.Student.UpdateStudent(data)
            print("Güncelleme Başarılı")
        except:
            result = False
            print("Güncellemede Sorun Oluştu")
            QMessageBox.critical(self, "Dikkat", "Güncellemede Sorun Oluştu")
        # result = self.Student.UpdateStudent(data)
        if result:
            QMessageBox.information(self, "Bilgi", "Güncelle gerçekleşti")
            self.UI_Settings()
        else:
            QMessageBox.critical(self, "Hata", "Güncellemede Sorun Oluştu")

    def DersCikart(self):
        item = self.ui.ogrenci_aldigiDersler.currentItem()
        self.ders = str(item.text())
        if len(self.ders) > 2:
            self.dersler.remove(self.ders)
            dersler = ",".join(self.dersler)
            # db.StudentDersCikart((dersler, self.ogrenci_no))
            self.Student.removeLessonFromStudent((dersler, self.ogrenci_no))
            QMessageBox.information(self, "Bilgi", f'{self.ders} dersi çıkartıldı')
            self.DerslerdenOgrenciCikart(self.ders)
        else:
            QMessageBox.warning(self, "Uyarı", "Öğrenciye Ait Ders Kaydı Yoktur.")

    def DerslerdenOgrenciCikart(self, ders2):
        try:
            dersiAlanOgrenciler = list(self.Lesson.getLessonTakenStudents(ders2))[0]
            if dersiAlanOgrenciler is None:
                QMessageBox.warning(self,"Uyarı","Öğrenciye Ait Ders Bulunamadı")
            else:
                dersiAlanOgrenciler = dersiAlanOgrenciler.split(",")
                print(dersiAlanOgrenciler)
                dersiAlanOgrenciler.remove(str(self.ogrenci_no))
                dersiAlanOgrenciler = ",".join(dersiAlanOgrenciler)
                print(dersiAlanOgrenciler)
                # db.DerslerdenOgrenciCikart((dersiAlanOgrenciler, ders2))
                self.Lesson.RemoveStudentFromLesson((dersiAlanOgrenciler, ders2))
                # result = db.getStudentInformations(self.ogrenci_no)
                result = self.Student.getStudentInformations(self.ogrenci_no)
                self.result = list(result[0])
                self.ui.ogrenci_aldigiDersler.clear()
                dersler = self.result[-1].split(",")
                self.ui.ogrenci_aldigiDersler.addItems(dersler)
        except:
            QMessageBox.critical(self, "Dikkat", "Öğrenciye Ait Ders Bilgileri Yüklenemedi")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    loginWindow = OgrenciDuzenleWidget("123456789")
    loginWindow.show()
    sys.exit(app.exec_())

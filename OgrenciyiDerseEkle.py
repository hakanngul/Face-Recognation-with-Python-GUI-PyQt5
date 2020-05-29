from PyQt5.QtGui import QIntValidator, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

import DataBaseManager
from ui_pages.ui_derseOgrenciEkle import Ui_DerseOgrenciEkleForm


class DerseOgrenciEkleWidget(QWidget):
    def __init__(self, id, ogretmen_KullaniciAdi):
        super().__init__()
        self.Ogrenci_OkulNo = None
        self.ui = Ui_DerseOgrenciEkleForm()
        self.id = id
        self.Teacher = DataBaseManager.Teacher()
        self.Student = DataBaseManager.Student()
        self.Lesson = DataBaseManager.Lessons()
        self.kadi = ogretmen_KullaniciAdi
        self.initUI()
        self.OgretmenBilgiGetir()
        self.show()

    def initUI(self):
        self.ui.setupUi(self)
        self.ui.txt_OgrNo.setValidator(QIntValidator())
        self.ui.txt_OgrNo.setText("185542008")
        self.ui.frame.setWindowTitle("Deneeme")
        self.initSlots()

    def initSlots(self):
        self.ui.btn_ara.clicked.connect(self.OgrenciAra)
        self.ui.btn_Ekle.clicked.connect(self.DersEkle)

    def OgretmenBilgiGetir(self):
        # result = db.getOgretmenDersler((self.id, self.kadi))
        result = self.Teacher.getTeacherLessons((self.id, self.kadi))
        if result:
            try:
                data = []
                for i in result:
                    data.append(i)
                data = data[0].split(",")
                if data is not None:
                    self.ui.cmb_Dersler.clear()
                    self.ui.cmb_Dersler.addItems(data)
            except:
                QMessageBox.warning(self, "Dikkat !!", "Öğretmen Dersleri Yüklenemedi...")
        else:
            QMessageBox.warning(self, "Dikkat !!", "Öğretmene Ait Dersler Bulunamadı...")

    def OgrenciAra(self):
        self.ui.txt_AdSoyad.clear()
        self.ui.txt_Bolum.clear()
        no = self.ui.txt_OgrNo.text()
        # result = db.getStudentInformations(no)
        result = self.Student.getStudentInformations(no)
        if result:
            self.Ogrenci_OkulNo = result[0][1]
            adi_soyadi = result[0][2] + " " + result[0][3]
            bolum = result[0][6]
            photo = result[0][-2] + str(self.Ogrenci_OkulNo) + "_1.jpg"
            self.ui.label.setPixmap(QPixmap(photo).scaled(272, 292))
            self.ui.label.setScaledContents(True)
            self.ui.txt_AdSoyad.setText(adi_soyadi.upper())
            self.ui.txt_Bolum.setText(bolum.upper())
        else:
            self.ui.txt_AdSoyad.clear()
            self.ui.txt_Bolum.clear()
            self.ui.label.clear()
            QMessageBox.warning(self, "Uyarı", "Böyle Bir Öğrenci Bulunamadı")

    def DersEkle(self):
        if self.Ogrenci_OkulNo is not None:
            # data = self.ui.cmb_Dersler.currentText()
            result = self.Lesson.getLessonTakenStudents(self.ui.cmb_Dersler.currentText())[0]
            print(result)
            if result is None:
                result = []
                print("Result", result)
            else:
                result = result.split(",")
                print(result)
                print(type(result))
            genelkod = self.ui.cmb_Dersler.currentText()
            if str(self.Ogrenci_OkulNo) in result:
                QMessageBox.warning(self, "Uyarı", "Bu Öğrenci Daha önceden kayıt olmuş")
            else:
                result.append(str(self.Ogrenci_OkulNo))
                result = ",".join(result)
                response = self.Lesson.AddStudentToLesson((result, genelkod))
                OgrenciResponse = self.OgrenciDersGuncelle(genelkod)
                if response and OgrenciResponse:
                    QMessageBox.information(self, "Bilgi", "Öğrenci Derse Eklendi")
                else:
                    QMessageBox.warning(self, "Uyarı", "Öğrenciye Ders Ekleme Başarısız")
        else:
            QMessageBox.warning(self, "Uyarı", "Öğrenci Bulunamadı")

    def OgrenciDersGuncelle(self, genelkod):
        # genelkod = self.ui.cmb_Dersler.currentText()
        dersler = list(self.Student.getStudentLessons(self.Ogrenci_OkulNo))[0]
        if dersler is None:
            dersler = []
        else:
            dersler = dersler.split(",")
        print(dersler)
        dersler.append(genelkod)
        print(dersler)
        dersler = ",".join(dersler)
        print(dersler)
        response = self.Student.addLessonToStudent((dersler, self.Ogrenci_OkulNo))
        if response:
            return True
        else:
            return False


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    mainWindow = DerseOgrenciEkleWidget(3, "hakn")
    mainWindow.show()
    sys.exit(app.exec_())

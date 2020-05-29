from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox, QMainWindow

import DataBaseManager
from ui_pages.ui_hocaEkrani import Ui_HocaEkraniMainWindow


class HocaEkraniWidget(QMainWindow):

    def __init__(self, ogretmen_kadi, ogretmen_sifre, parent=None):
        super(HocaEkraniWidget, self).__init__(parent=parent)
        self.id = None
        self.ui = Ui_HocaEkraniMainWindow()
        self.ui.setupUi(self)
        self.Teacher = DataBaseManager.Teacher()
        self.Lesson = DataBaseManager.Lessons()
        self._translate = QtCore.QCoreApplication.translate
        self.kadi = ogretmen_kadi
        self.sifre = ogretmen_sifre
        self.initSlots()
        self.UI()
        self.show()

    def initSlots(self):
        self.ui.actionExit.triggered.connect(lambda: QtCore.QCoreApplication.instance().quit())
        self.ui.action_DersEkle.triggered.connect(self.DersEkleWidget)
        self.ui.action_DerseOgrenciEkle.triggered.connect(self.OgrenciyiDerseEkle)
        self.ui.action_OgrenciEkle.triggered.connect(self.OgrenciEkleWidget)
        self.ui.action_OgrenciDuzenle.triggered.connect(self.OgrenciAraWidget)
        self.ui.action_OgretmenDuzenle.triggered.connect(self.OgretmenDuzenleWidget)
        self.ui.btn_login.clicked.connect(self.AnaPencereWidget)
        self.ui.action_SayfayiYenile.triggered.connect(self.RefreshWidget)

    def RefreshWidget(self):
        QMessageBox.information(self, "Bilgi", "Sayfa Yenileniyor...")
        self.UI()

    def DersEkleWidget(self):
        try:
            if self.kadi and self.sifre is not None:
                from DersEkle import DersEkleWidget
                self.dersEkleWidget = DersEkleWidget(self.kadi, self.sifre)
            else:
                QMessageBox.warning(self, "Uyarı", "Öğretmen Kullanıcı Ad Hatası")
        except:
            print("Öğretmen Kullanıcı Ad Hatası")

    def OgrenciyiDerseEkle(self):
        print("OgrenciyiDerseEkle")
        try:
            print("try içi")
            if self.kadi and self.sifre is not None:
                from OgrenciyiDerseEkle import DerseOgrenciEkleWidget
                self.dersEkleWidget = DerseOgrenciEkleWidget(self.id, self.kadi)

            else:
                QMessageBox.warning(self, "Uyarı", "Öğretmen Kullanıcı Ad Hatası")
        except:
            print("Öğretmen Kullanıcı Ad Hatası")

    def OgrenciEkleWidget(self):
        try:
            from OgrenciEkle import OgrenciEkleWindow
            self.ogrenciEkleWidget = OgrenciEkleWindow()

        except:
            QMessageBox.warning(self, "Uyarı", "Bir Hata Oluştu")

    def OgrenciAraWidget(self):
        try:
            from OgrenciAra import OgrenciAraWidget
            self.ogrenciAraWidget = OgrenciAraWidget()

        except:
            QMessageBox.warning(self, "Uyarı", "Bir Hata Oluştu")

    def OgretmenDuzenleWidget(self):
        try:
            from OgretmenDuzenle import OgretmenDuzenleWidget
            self.ogrenciAraWidget = OgretmenDuzenleWidget(self.kadi, self.sifre)

        except:
            QMessageBox.warning(self, "Uyarı", "Bir Hata Oluştu")

    def BilgileriGetir(self):
        data = (self.kadi, self.sifre)
        try:
            result = self.Teacher.getTeacherInformation(data)
            if result is not None:
                self.id = result[0][0]
                self.adi_soyadi = result[0][1] + " " + result[0][2]
                self.bolum = result[0][3]
            if result[0][7] is not None:
                self.dersler = result[0][7].split(",")
            else:
                self.dersler = None
                print("Hocaya Ait ders bulunmamaktadır.")
            self.BilgileriGom()
        except:
            print("Bilgileri Getirmede Sorun Oluştu")

    def BilgileriGom(self):
        self.ui.text_AdSoyad.setText(self.adi_soyadi.upper())
        self.ui.text_Bolum.setText(self.bolum.upper())
        if self.dersler is not None:
            self.ui.cmb_Dersler.clear()
            self.ui.cmb_Dersler.addItems(self.dersler)
        else:
            _translate = QtCore.QCoreApplication.translate
            QMessageBox.warning(self, "Uyarı", f'{self.adi_soyadi} hocaya ait ders kaydı bulunamadı.')
            self.cmb_Dersler.setItemText(0, _translate("HocaEkraniMainWindow", "Öğretmene Ait Ders Kaydı Bulunamadı"))

    def AnaPencereWidget(self):
        # TODO : Derse Kayıtlı Öğrenci Yoksa AnaWidget ı açmasın
        model_name = self.ui.cmb_Model.currentText()
        distance_metric = self.ui.cmb_Metrik.currentText()
        genelkod = self.ui.cmb_Dersler.currentText()
        countTakenStudents = list(self.Lesson.getLessonTakenStudents(genelkod))
        if None in countTakenStudents:
            QMessageBox.warning(self, "Uyarı", "Derse Kayıtlı Öğrenci Yok Önce Derse Öğrenci Ekleyiniz None")
        elif len(countTakenStudents[0].split(",")) < 1:
            QMessageBox.warning(self, "Uyarı", "Derse Kayıtlı Öğrenci Yok Önce Derse Öğrenci Ekleyiniz")
        else:
            # from mainWindow import MainWindow
            # self.AnaWidget = MainWindow(self.id, self.kadi, self.sifre, genelkod, model_name, distance_metric)
            try:
                from mainWindow import MainWindow
                self.AnaWidget = MainWindow(self.id, self.kadi, self.sifre, genelkod, model_name, distance_metric)
            except:
                QMessageBox.warning(self, "Uyarı", "Ana Pencere Açılamadı")

    def UI(self):
        self.ui.text_Bolum.setEnabled(False)
        self.ui.text_AdSoyad.setEnabled(False)
        self.BilgileriGetir()
        try:
            self.ui.checkBox.hide()
            self.setFixedSize(510, 554)
            ImageStudentPath = f'ogretmenler/{self.kadi}_1.jpg'
            self.ui.image_ogretmen.setPixmap(QPixmap(ImageStudentPath).scaled(263, 211))
            self.ui.image_ogretmen.setScaledContents(True)
            self.setWindowTitle(self._translate("HocaEkraniMainWindow", f'{self.kadi} Hoca Ekranı'))
        except:
            QMessageBox.warning(self, "Uyarı", "Hocaya Ait Resim Bulunamadı")


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    loginWindow = HocaEkraniWidget("hakn", "123456")
    loginWindow.show()
    sys.exit(app.exec_())

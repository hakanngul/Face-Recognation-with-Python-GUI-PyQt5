import os
import sys

import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QIntValidator, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

import DataBaseManager
from ui_pages.ui_ogrenciEkle2 import Ui_OgrenciEkleWindow


class OgrenciEkleWindow(QMainWindow):
    def __init__(self):
        super(OgrenciEkleWindow, self).__init__()
        self.ui = Ui_OgrenciEkleWindow()
        self.ui.setupUi(self)
        self.setFixedSize(542, 873)
        self.Student = DataBaseManager.Student()
        self.ui.btn_kayit.clicked.connect(self.getUserInformation)
        self.UI_Settings()
        self.ui.actionStart_Camera.triggered.connect(self.startCam)
        self.ui.actionStop_Camera.triggered.connect(self.stopCam)
        self.ui.btn_resimCek.clicked.connect(self.ResimKaydet)
        self.sayac = 0
        self.capture = None
        self.ResimKontrol = False
        self.sayacDosya = False
        self.show()

    def getUserInformation(self):
        self.okulno = int(self.ui.txt_Okulno.text())
        self.adi = self.ui.txt_Adi.text().lower()
        self.soyadi = self.ui.txt_Soyadi.text().lower()
        self.bolum = self.ui.cmb_Bolum.currentText()
        self.sube = self.ui.cmb_Sube.currentText()
        self.program = self.ui.cmb_Program.currentText()
        if self.program == "Sabah":
            self.program = "S"
        else:
            self.program = "A"

        self.sinif = self.ui.cmb_Sinif.currentText()
        imagePath = "database/" + str(self.okulno) + "/"
        data = (self.okulno, self.adi, self.soyadi, self.program, self.sinif, self.bolum, self.sube, imagePath)
        kontrol = self.OgrenciKayitKontrol()
        print("Kontrol", kontrol)
        if kontrol:
            self.result = self.Student.addStudent(data)
            if self.result:
                QMessageBox.information(self, "Bilgi", "Kayıt Başarılı Oldu")
                self.ui.actionStart_Camera.setEnabled(True)
                self.kontrol()
                self.ui.txt_Okulno.setEnabled(False)
            else:
                QMessageBox.warning(self, "Uyarı", "Kayıt Başarısız")
            self.Temizle()
        else:
            print("Öğrenci zaten kayıtlı")

    def OgrenciKayitKontrol(self):
        try:
            # resultOgrencilerListesi = db.getAllStudents()
            resultOgrencilerListesi = self.Student.getAllStudents()
            liste = []
            if resultOgrencilerListesi is not None:
                for i in resultOgrencilerListesi:
                    liste.append(i[0])
            else:
                print("Öğrenci Listesi boş döndü")
            if int(self.ui.txt_Okulno.text()) in liste:
                QMessageBox.warning(self, "Uyarı", f'{self.ui.txt_Okulno.text()} öğrenci zaten kayıtlı')
                return False
            else:
                QMessageBox.information(self, "Bilgi",
                                        f'{self.ui.txt_Okulno.text()} adlı öğrenci kayıt kontrolü yapıldı')
                return True
        except:
            QMessageBox.information(self, "Uyarı", "Öğrenci Kayıt Kontrolünde Hata Oluştu")

    def Temizle(self):
        self.okulno = ""
        self.adi = ""
        self.soyadi = ""
        self.bolum = ""
        self.bolum = ""
        self.sube = ""
        self.program = ""
        self.sinif = ""

    def kontrol(self):
        self.ui.btn_resimCek.setEnabled(True)
        self.ui.actionStop_Camera.setEnabled(True)

    def UI_Settings(self):
        self.ui.txt_Okulno.setValidator(QIntValidator())
        self.ui.actionStart_Camera.setEnabled(False)
        self.ui.actionStop_Camera.setEnabled(False)
        self.ui.btn_resimCek.setEnabled(False)
        # self.show()

    def startCam(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000. / 24)

    def update_frame(self):
        ret, self.image = self.capture.read()
        self.displayImage(self.image)

    def ResimKaydet(self):
        if not self.sayacDosya:
            self.FileControl()
            self.sayacDosya = True
        if self.sayacDosya:
            if self.capture is not None:
                self.sayac += 1
                if self.sayac < 4:
                    path = os.getcwd() + "/database/"
                    path += str(self.ui.txt_Okulno.text()) + "/"
                    path += str(self.ui.txt_Okulno.text()) + "_" + str(self.sayac) + ".jpg"
                    try:
                        if not os.path.exists(path):
                            cv2.imwrite(path, self.image)
                            print("Başarılı => ", path)
                    except:
                        print("Olmadı")
                else:
                    QMessageBox.warning(self, "Uyarı", "3 Adet Resim Yeterli")
                    self.stopCam()
            else:
                print("Kamera Kapalı")

    def FileControl(self):
        filename = os.getcwd() + "\\database"
        if not os.path.exists(filename):
            os.mkdir(filename)
            print(filename)
        fname = str(self.ui.txt_Okulno.text())
        filename = filename + "\\" + fname
        if not os.path.exists(filename):
            os.mkdir(filename)
            print(filename)
            print("Dosya Oluşturuldu")
            return True
        else:
            print("Dosya zaten var")
            return False

    def displayImage(self, img):
        qFormat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qFormat = QImage.Format_RGBA8888
            else:
                qFormat = QImage.Format_RGB888
        outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qFormat)
        # BGR to RGB
        self.outImage = outImage.rgbSwapped()
        self.ui.label.setPixmap(QPixmap.fromImage(self.outImage))
        self.ui.label.setScaledContents(True)

    def stopCam(self):
        self.capture.release()
        resim = self.clear_cam()
        self.ui.label.setPixmap(QPixmap.fromImage(resim))
        self.ui.label.setScaledContents(True)
        self.timer.stop()
        self.ui.actionStart_Camera.setEnabled(True)
        self.ui.btn_resimCek.setEnabled(False)

    def clear_cam(self):
        qFormat = QImage.Format_Indexed8
        resim = cv2.imread("images/clear_cam2.png")
        resim = QImage(resim, resim.shape[1], resim.shape[0], resim.strides[0], qFormat)
        return resim


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    mainWindow = OgrenciEkleWindow()
    mainWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator, QPixmap
from PyQt5.QtWidgets import QWidget, QMessageBox

import DataBaseManager
from ui_pages.ui_ogrenciAra import Ui_OgrenciAraWindow
from ogrenciDuzenle import OgrenciDuzenleWidget


class OgrenciAraWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super(OgrenciAraWidget, self).__init__()
        self.ui = Ui_OgrenciAraWindow()
        self.ui.setupUi(self)
        self.ui.txt_ogrNo.setValidator(QIntValidator())
        self.Student = DataBaseManager.Student()
        self.ui.txt_ogrNo.setText("185542008")
        self.ui.text_Bolum.setEnabled(False)
        self.ui.btn_ara.clicked.connect(self.getStudentInformations)
        self.kontrol = False
        self.ui.btn_duzenle.clicked.connect(self.OgrenciDuzenleWidget)
        self.show()

    def getStudentInformations(self):
        try:
            result = self.Student.getStudentInformations(int(self.ui.txt_ogrNo.text()))[0]
            print(result)
            self.adi_soyadi = result[2].upper() + " " + result[3].upper()
            self.OkulNo = result[1]
            path = result[-2] + str(self.OkulNo) + "_1.jpg"
            self.ui.text_Bolum.setText(result[6].upper())
            self.ui.txt_AdSoyad.setText(self.adi_soyadi)
            self.ui.label.setPixmap(QPixmap(path))
            self.ui.label.setScaledContents(True)
            self.kontrol = True
            self.statusbarChanged("Öğrenci Bulundu...")
        except:
            self.ui.txt_AdSoyad.clear()
            self.ui.text_Bolum.clear()
            self.ui.label.clear()
            QMessageBox.warning(self,"Uyarı","Öğrenci Bulunamadı")

    def OgrenciDuzenleWidget(self):
        if self.kontrol:
            self.ogrenciDuzenle = OgrenciDuzenleWidget(self.OkulNo)
        else:
            QMessageBox.warning(self, "Uyarı", "Önce Öğrenciyi Aratınız")

    def statusbarChanged(self, msg):
        self.ui.statusbar.showMessage(msg)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    loginWindow = OgrenciAraWidget()
    loginWindow.show()
    sys.exit(app.exec_())

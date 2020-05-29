from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QTableView

import DataBaseManager
from ui_pages.ui_ogrenciListesi import Ui_OgrenciListesiForm


class OgrenciListesiWidget(QtWidgets.QMainWindow):
    def __init__(self, dersGenelKod):
        super(OgrenciListesiWidget, self).__init__()
        self.ui = Ui_OgrenciListesiForm()
        self.ui.setupUi(self)
        self.Lesson = DataBaseManager.Lessons()
        self.Student = DataBaseManager.Student()
        self.dersGenelKod = dersGenelKod
        self.ui.pushButton.clicked.connect(self.select)
        self.Table()
        self.ui.sinif_listesi.setSelectionBehavior(QTableView.SelectRows)
        self.liste = []

        self.show()

    def select(self):
        selectedItems = []
        for item in self.ui.sinif_listesi.selectedItems():
            selectedItems.append(item.text())
        try:
            okulNo = selectedItems[1]
            from ogrenciDuzenle import OgrenciDuzenleWidget
            self.ogrenciDuzenle = OgrenciDuzenleWidget(okulNo)
        except:
            QMessageBox.warning(self, "Uyarı", "Bir Hata Oluştu ve Öğrenci Seçimi Yapmadınız")

    def Table(self):
        try:
            header = self.ui.sinif_listesi.horizontalHeader()
            result2 = self.Lesson.getLessonTakenStudents(self.dersGenelKod)[0].split(",")
            self.ui.sinif_listesi.setRowCount(0)
            for i in range(len(result2)):
                result = self.Student.getStudentInformations(int(result2[i]))
                for row_number, row_data in enumerate(result):
                    self.ui.sinif_listesi.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.ui.sinif_listesi.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            for j in range(10):
                header.setSectionResizeMode(j, QtWidgets.QHeaderView.ResizeToContents)

        except:
            QMessageBox.warning(self, "Uyarı", "Sınıf Listesi Yüklenemedi")


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    loginWindow = OgrenciListesiWidget("YMT213-A-S")
    loginWindow.show()
    sys.exit(app.exec_())

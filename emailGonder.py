import mimetypes
import smtplib

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QMessageBox
from ui_pages.ui_email import Ui_EMailForm
from validate_email import validate_email
from email_validator import validate_email, EmailNotValidError
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailWidget(QWidget):
    def __init__(self, listWidget, dersGenelKod, email):
        super().__init__()
        self.ui = Ui_EMailForm()
        self.ui.setupUi(self)
        self.setFixedSize(455, 526)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.ui.txt_NewMail.setText("hakanngul@asdasdasdfgsd234dfgsd.com")
        self.listWidget = listWidget
        self.dersGenelKod = dersGenelKod
        self.emailto = email
        self.ui.btn_login.clicked.connect(self.control)

    def control(self):
        res = self.ui.txt_NewMail.text()
        email = res
        try:
            valid = validate_email(email)

        except EmailNotValidError as e:
            # email is not valid, exception message is human-readable
            QMessageBox.warning(self, "Uyarı", f'Böyle Bir Mail Yok {e}')

    def saveFile(self):
        import pandas as pd
        from datetime import datetime
        now = datetime.now()
        df = pd.DataFrame()
        rows = self.listWidget.rowCount()
        columns = self.listWidget.columnCount()

        for i in range(rows):
            for j in range(columns):
                df.loc[i, j] = str(self.listWidget.item(i, j).text())
        path = f'YoklamaKayitlari/{str(self.dersGenelKod)}_{now.day}_{now.month}_{now.year}.xlsx'
        df.columns = ['OkulNo', 'Adı Soyadı', 'Yoklama Durumu', 'Tarih']
        df.to_excel(path, index=False, header=True)
        response = self.SendMail(path)
        if response:
            QMessageBox.information(self, "Bilgi", "Mail Gönderildi")
        else:
            QMessageBox.warning(self, "Bilgi", "Bir Hata Oluştu")

    def SendMail(self, fileToSend, emailto):

        from datetime import datetime
        now = datetime.now()
        emailfrom = "ymh414bitirme@gmail.com"
        username = "ymh414bitirme@gmail.com"
        password = "ymh414Bitirmeprojesi@11"
        msg = MIMEMultipart()
        msg["From"] = emailfrom
        msg["To"] = emailto
        msg["Subject"] = f'{self.dersGenelKod} dersi {now.day}/{now.month}/{now.year}'

        ctype, encoding = mimetypes.guess_type(fileToSend)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"

        maintype, subtype = ctype.split("/", 1)

        if maintype == "text":
            fp = open(fileToSend)
            # Note: we should handle calculating the charset
            attachment = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "image":
            fp = open(fileToSend, "rb")
            attachment = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "audio":
            fp = open(fileToSend, "rb")
            attachment = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
        else:
            fp = open(fileToSend, "rb")
            attachment = MIMEBase(maintype, subtype)
            attachment.set_payload(fp.read())
            fp.close()
            encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
        msg.attach(attachment)

        server = smtplib.SMTP("smtp.gmail.com:587")
        server.starttls()
        server.login(username, password)
        server.sendmail(emailfrom, emailto, msg.as_string())
        server.quit()
        return True


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    loginWindow = EmailWidget()
    loginWindow.show()
    sys.exit(app.exec_())

import os
from pathlib import Path

f = str('C:\\Users\Hhaka/.faceAnalytics/YoklamaKayitlari/YMT213-A-S_5_6_2020.xlsx')
f = f.replace('\\', '/').split('/')[-1].split('.')[0]
# f = f.split('/')
# f = f[-1].split('.')
print(f)

# try:
#     print("emailto =>", emailto)
#     from datetime import datetime
#
#     now = datetime.now()
#     emailfrom = "ymh414bitirme@gmail.com"
#     username = "ymh414bitirme@gmail.com"
#     password = "ymh414Bitirmeprojesi@11"
#     msg = MIMEMultipart()
#     msg["From"] = emailfrom
#     msg["To"] = emailto
#     msg["Subject"] = f'{self.dersGenelKod} dersi {now.day}/{now.month}/{now.year}'
#
#     ctype, encoding = mimetypes.guess_type(fileToSend)
#     if ctype is None or encoding is not None:
#         ctype = "application/octet-stream"
#
#     maintype, subtype = ctype.split("/", 1)
#
#     if maintype == "text":
#         fp = open(fileToSend)
#         # Note: we should handle calculating the charset
#         attachment = MIMEText(fp.read(), _subtype=subtype)
#         fp.close()
#     elif maintype == "image":
#         fp = open(fileToSend, "rb")
#         attachment = MIMEImage(fp.read(), _subtype=subtype)
#         fp.close()
#     elif maintype == "audio":
#         fp = open(fileToSend, "rb")
#         attachment = MIMEAudio(fp.read(), _subtype=subtype)
#         fp.close()
#     else:
#         fp = open(fileToSend, "rb")
#         attachment = MIMEBase(maintype, subtype)
#         attachment.set_payload(fp.read())
#         fp.close()
#         encoders.encode_base64(attachment)
#     attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
#     msg.attach(attachment)
#
#     server = smtplib.SMTP("smtp.gmail.com:587")
#     server.starttls()
#     server.login(username, password)
#     server.sendmail(emailfrom, emailto, msg.as_string())
#     server.quit()
#     return True
# except:
#     QMessageBox.critical(self, "Hata", "Bir Hata Oluştu Lütfen Email veya İnterneti kontrol ediniz")

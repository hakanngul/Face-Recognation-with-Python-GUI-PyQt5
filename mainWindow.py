import mimetypes
import os
import smtplib
import time
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from numba import jit, cuda

import cv2
import numpy as np
import pandas as pd
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from tqdm import tqdm

import DataBaseManager
from ui_pages.ui_mainWindow import Ui_MainWindow

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
os.environ["CUDA_DEVICE_ORDER"] = "0000:01:00.0"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

from model.basemodels import VGGFace, Facenet
from model.extendedmodels import Age, Gender, Emotion
from model.commons import functions, distance as dst


class MainWindow(QMainWindow):
    def __init__(self, hoca_id, hoca_KullaniciAdi, hoca_sifre, GenelKod, model_name, distance_metric, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Teacher = DataBaseManager.Teacher()
        self.Student = DataBaseManager.Student()
        self.Lesson = DataBaseManager.Lessons()
        self.SinifListesi = []
        self.model_name = model_name
        self.distance_metric = distance_metric
        self.hoca_id = hoca_id
        self.sifre = hoca_sifre
        self.kadi = hoca_KullaniciAdi
        self.dersGenelKod = GenelKod
        self.functionsSettings()
        self.UI_Ayar()
        self.initSlots()
        self.show()

    def functionsSettings(self):
        self.timer = QTimer()
        self.FaceAnalysisSettings()
        self.camControl = False
        self.capture = None
        self.Kontrol = False
        self.yoklamaListesi = []
        self.LoadDatabases()
        self.loadSinif()

    def UI_Ayar(self):
        self.setFixedSize(1361, 646)
        self.ImageStudentPath = "images/personReal.png"
        self.ui.profile_picture.setPixmap(QPixmap(self.ImageStudentPath))
        self.statusbarChanged("Ready")
        self.ui.actionYoklamayiBitir.setEnabled(False)

    def initSlots(self):
        self.ui.OgrenciEkle.triggered.connect(self.OgrenciEkleWindow)
        self.ui.actionStartCam.setEnabled(False)
        self.ui.actionStopCam.setEnabled(False)
        self.ui.actiondeneme5.triggered.connect(self.loadModel)
        self.ui.actionStartCam.triggered.connect(self.startCam)
        self.ui.actionStopCam.triggered.connect(self.stopCam)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.ui.actionExit.triggered.connect(self.exitApplication)
        self.ui.OgretmenEkle.triggered.connect(self.OgretmenEkle)
        self.ui.DersEkle.triggered.connect(self.DersEkleWidget)
        self.ui.action_OgrenciListesi.triggered.connect(self.OgrenciListesi)
        self.ui.action_OgrenciAra.triggered.connect(self.OgrenciAra)
        self.ui.actionYoklamayiBitir.triggered.connect(self.saveFile)

    def OgrenciEkleWindow(self):
        try:
            from OgrenciEkle import OgrenciEkleWindow
            self.ogrenciEkleSayfasi = OgrenciEkleWindow()
        except:
            QMessageBox.critical(self, "Uyarı", "Öğrenci Ekle Sayfasında Sorun Oluştu")

    def OgrenciListesi(self):
        try:
            from OgrenciListesi import OgrenciListesiWidget
            self.ogrenciListesi = OgrenciListesiWidget(self.dersGenelKod)
        except:
            QMessageBox.critical(self, "Uyarı", "Öğrenci Listesi Sayfasında Sorun Oluştu")

    def OgrenciAra(self):
        try:
            from OgrenciAra import OgrenciAraWidget
            self.ogrenciAra = OgrenciAraWidget()
        except:
            QMessageBox.critical(self, "Uyarı", "Öğrenci Listesi Sayfasında Sorun Oluştu")

    def OgretmenEkle(self):
        try:
            from OgretmenKayit import KayitWidget
            self.ogrenciEkleSayfasi = KayitWidget()
        except:
            QMessageBox.critical(self, "Uyarı", "Öğrenci Ekle Sayfasında Sorun Oluştu")

    def SinifListesiWidget(self):
        try:
            from OgrenciListesi import OgrenciListesiWidget
            self.OgrenciListesi = OgrenciListesiWidget(self.dersGenelKod)
        except:
            QMessageBox.critical(self, "Uyarı", "Öğrenci Listesi Sayfasında Sorun Oluştu")

    def DersEkleWidget(self):
        try:
            if self.kadi and self.sifre is not None:
                from DersEkle import DersEkleWidget
                self.dersEkleWidget = DersEkleWidget(self.kadi, self.sifre)

            else:
                QMessageBox.critical(self, "Uyarı", "Öğretmen Kullanıcı Ad Hatası")
        except:
            print("Öğretmen Kullanıcı Ad Hatası")

    def LoadDatabases(self):
        try:
            self.LoadClassInformations()
            self.Table() # SinifListesi Yüklemesi İşlemi Yapılıyor
        except:
            print("DB de sorun oluştu")

    def exitApplication(self):
        if self.capture is not None:
            self.stopCam()
        QtCore.QCoreApplication.instance().quit()

    def loadSinif(self):
        self.SinifListesi = self.Lesson.getLessonTakenStudents(self.dersGenelKod)[0].split(",")
        # print("self.SinifListesi =>", self.SinifListesi)

    def loadModelandEmbedding(self, db_path):
        global input_shape
        model_name = self.model_name
        distance_metric = self.distance_metric
        employees = []
        liste = self.SinifListesi
        if len(liste) > 0:
            if os.path.isdir(db_path):
                for r, d, f in os.walk(db_path):  # r=root, d=directories, f = files
                    for file in f:
                        if file.split("_")[0] in liste:
                            if '.jpg' in file:
                                exact_path = r + "/" + file
                                employees.append(exact_path)
                            if '.png' in file:
                                exact_path = r + "/" + file
                                employees.append(exact_path)
            print("employees:", employees)
            if len(employees) > 0:
                if model_name == 'VGG-Face':
                    print("Using VGG-Face model backend and", distance_metric, "distance.")
                    model = VGGFace.loadModel()
                    input_shape = (224, 224)

                elif model_name == 'Facenet':
                    print("Using Facenet model backend", distance_metric, "distance.")
                    model = Facenet.loadModel()
                    input_shape = (160, 160)
                else:
                    raise ValueError("Invalid model_name passed - ", model_name)
                threshold = functions.findThreshold(model_name, distance_metric)
            tic = time.time()
            pbar = tqdm(range(0, len(employees)), desc='Embedingler Bulundu')
            embeddings = []
            for index in pbar:
                employee = employees[index]
                pbar.set_description("Embeding  %s" % (employee.split("/")[-1]))
                embedding = []
                if functions.detectFace(employee, input_shape) is not None:
                    img = functions.detectFace(employee, input_shape)
                    img_representation = model.predict(img)[0, :]
                    embedding.append(employee)
                    embedding.append(img_representation)
                    embeddings.append(embedding)
                else:
                    print(f'Resimde Yüz Bulunamadı :{employee}')
                    continue
            df = pd.DataFrame(embeddings, columns=['employee', 'embedding'])
            df['distance_metric'] = distance_metric
            toc = time.time()
            print("Embedinglerin Okunma Süresi  ", toc - tic, " saniye sürdü")
            return df, model, threshold, input_shape
        else:
            QMessageBox.critical(self, "Dikkat", "Sınıf Listesi Yüklenemedi loadModelandEmbedding")

    def loadModel(self):
        if not self.Kontrol:
            QMessageBox.warning(self, "Uyarı !!!", "Model Yükleniyor ...")
            self.ui.actionStartCam.setEnabled(True)

            self.df, self.model, self.threshold, self.input_shape = self.loadModelandEmbedding("database")
            self.emotion_model, self.age_model, self.gender_model = self.enable_face_analysis()
            self.Kontrol = True

            QMessageBox.information(self, "Model Yüklemesi", "Tamamlandı")
            QMessageBox.information(self, "Sınıf Yüklemesi", "Tamamlandı")
        else:
            QMessageBox.critical(self, "Hata", "Model Zaten Yüklü")

    def enable_face_analysis(self):
        tic = time.time()
        emotion_model = Emotion.loadModel()
        print("Emotion Model Yükleniyor ...")
        age_model = Age.loadModel()
        print("Yaş  Modeli Yükleniyor ...")
        gender_model = Gender.loadModel()
        print("Cinsiyet Modeli Yükleniyor ...")
        toc = time.time()
        print("Yüz analiz modellerin yükleme süresi  ", toc - tic, " saniye sürdü")
        return emotion_model, age_model, gender_model

    def FaceAnalysisSettings(self):
        self.input_shape = (224, 224)
        self.time_threshold = 7
        self.frame_threshold = 5
        self.pivot_img_size = 112
        self.face_detected = False
        self.face_included_frames = 0
        self.freezed_frame = 0
        self.text_color = (67, 67, 67)
        self.freeze = False
        self.tic = time.time()
        face_detector_path = "model/haarcascade_frontalface_default.xml"
        self.face_cascade = cv2.CascadeClassifier(face_detector_path)
        self.text_color = (67, 67, 67)
        self.tic = time.time()
        self.age = None
        self.gender = None
        self.emotion = dict()
        functions.allocateMemory()
        functions.initializeFolder()

    def LoadClassInformations(self):
        result = list(self.Lesson.getLessonAllInformation(self.dersGenelKod)[0])
        # result = list(result[0])
        self.dersId = result[0]
        self.dersAdi = result[1]
        self.dersKodu = result[2]
        self.kontenjan = result[3]
        self.sube = result[4]
        self.sinif = result[5]
        self.OgretmenId = result[7]
        if result[-1] == "NULL":
            QMessageBox.warning(self, "Uyarı", "Bu derse Kayıtlı Öğenci Yok")
            self.dersiAlanOgrenciler = []
        else:
            self.dersiAlanOgrenciler = result[-1].split(",")

        self.dersBolum = result[8]
        self.dersProgram = result[9]
        self.LoadClassToUI()

    def LoadClassToUI(self):
        self.ui.label_dersAdi.setText(self.dersAdi.upper())
        self.ui.label_dersKodu.setText(self.dersKodu)
        self.ui.label_sinifMevcudu.setText(str(self.kontenjan))
        self.ui.label_girilenDers.setText(self.dersGenelKod)

    def statusbarChanged(self, msg):
        if msg == "Ready":
            self.ui.statusbar.showMessage(msg)
        self.ui.statusbar.showMessage(msg, 3000)

    def startCam(self):
        self.ui.actionStartCam.setEnabled(False)
        self.ui.actionStopCam.setEnabled(True)
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 650)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Camera)
        self.timer.start(1000. / 24)
        self.statusbarChanged("Kamera Açıldı")

    def getIformation(self, emp_name):
        folder = emp_name
        self.okulNo = folder.replace("\\", "/").split("/")[1]
        self.yoklamaListesi.append(str(self.okulNo))
        bilgi = self.Student.getStudentAllInformation(int(self.okulNo))[0]
        adi_soyadi = bilgi[0].upper() + " " + bilgi[1].upper()
        print("Name : ", adi_soyadi)
        self.ui.label_adiSoyadi.setText(adi_soyadi)
        self.ui.label_okulNo.setText(str(self.okulNo))
        print("Folder :", folder)
        self.ui.profile_picture.setPixmap(QPixmap(self.employee_name))
        self.yoklamaListesi.append(str(self.okulNo))
        self.YoklamaGuncelle(str(self.okulNo))

    def saveFile(self):
        import pandas as pd
        from datetime import datetime
        now = datetime.now()
        df = pd.DataFrame()
        rows = self.ui.sinif_listesi.rowCount()
        columns = self.ui.sinif_listesi.columnCount()

        for i in range(rows):
            for j in range(columns):
                df.loc[i, j] = str(self.ui.sinif_listesi.item(i, j).text())

        fileName = f'{str(self.dersGenelKod)}_{now.day}_{now.month}_{now.year}'
        home = str(Path.home())
        home = home + "/.faceAnalytics"
        home = home + "/YoklamaKayitlari"
        df.columns = ['OkulNo', 'Adı Soyadı', 'Yoklama Durumu', 'Tarih']
        if os.path.exists(home + "/" + fileName + ".xlsx"):
            print("Bu Kayıt Var")
            df.to_excel(home + "/" + fileName + "_1" + ".xlsx", index=False, header=True)
        else:
            df.to_excel(home + "/" + fileName + ".xlsx", index=False, header=True)

        self.home = home + "/"
        fileName += ".xlsx"
        response = self.SendMail(fileName)
        # print(response)
        if response:
            QMessageBox.information(self, "Bilgi", "Mail Gönderildi")
        else:
            QMessageBox.warning(self, "Bilgi", "Bir Hata Oluştu")

    # noinspection PyBroadException
    def SendMail(self, fileName):
        self.home += fileName
        fileToSend = self.home
        emailto = self.Teacher.getSelectedTeacherMail(self.kadi)[0]
        print("emailto =>", emailto)
        try:
            now = datetime.now()
            subject = f'{self.dersGenelKod} dersi {now.day}/{now.month}/{now.year}'
            print("subject => ", subject)
            emailfrom = "ymh414bitirme@gmail.com"
            username = "ymh414bitirme@gmail.com"
            password = "ymh414Bitirmeprojesi@11"
            msg = MIMEMultipart()
            msg["From"] = emailfrom
            msg["To"] = emailto
            msg["Subject"] = subject
            ctype, encoding = mimetypes.guess_type(fileToSend)
            if ctype is None or encoding is not None:
                ctype = "application/octet-stream"

            maintype, subtype = ctype.split("/", 1)

            if maintype == "text":
                fp = open(fileToSend)
                attachment = MIMEText(fp.read(), _subtype=subtype)
                fp.close()
            else:
                fp = open(fileToSend, "rb")
                attachment = MIMEBase(maintype, subtype)
                attachment.set_payload(fp.read())
                fp.close()
                encoders.encode_base64(attachment)
            f = fileToSend.replace('\\', '/').split('/')[-1].split('.')[0]
            attachment.add_header("Content-Disposition", "attachment", filename=str(f))
            msg.attach(attachment)

            server = smtplib.SMTP("smtp.gmail.com:587")
            server.starttls()
            server.login(username, password)
            server.sendmail(emailfrom, emailto, msg.as_string())
            server.quit()
            return True
        except Exception as e:
            QMessageBox.warning(self, "Uyarı", "İnternet veya Email Adresinizi Kontrol Ediniz :", e)

    def YoklamaGuncelle(self, ogrenciNo):
        from datetime import datetime
        now = datetime.now()
        rowCount = self.ui.sinif_listesi.rowCount()
        for row in range(rowCount):
            if ogrenciNo == self.ui.sinif_listesi.item(row, 0).text():
                if self.ui.sinif_listesi.item(row, 2).text() != "Geldi":
                    self.ui.sinif_listesi.setItem(row, 2, QTableWidgetItem("Geldi"))
                    self.ui.sinif_listesi.setItem(row, 3, QTableWidgetItem(
                        f'{now.hour}:{now.minute} {now.day}/{now.month}/{now.year}'))
                else:
                    QMessageBox.information(self, "Uyarı", f'{ogrenciNo} daha önceden yoklaması alınmış')

    def Table(self):
        try:
            result = self.dersiAlanOgrenciler
            # print(result)
            self.ui.sinif_listesi.setRowCount(len(result))
            for i in range(len(result)):
                # print(i)
                self.ui.sinif_listesi.setItem(i, 0, QTableWidgetItem(result[i]))
                self.ui.sinif_listesi.setItem(i, 2, QTableWidgetItem("Gelmedi"))
                self.ui.sinif_listesi.setItem(i, 3, QTableWidgetItem("NULL"))
                veri = self.Student.getStudentAllInformation(result[int(i)])
                if not veri:
                    print("Sorun oldu")
                veri = list(veri[0])
                veri = veri[0] + " " + veri[1]
                self.ui.sinif_listesi.setItem(i, 1, QTableWidgetItem(veri))
        except:
            QMessageBox.warning(self, "Uyarı", "Sınıf Listesi Yüklenemedi Table")

    def Camera(self):
        global x, y, w, h
        ret, img = self.capture.read()
        raw_img = img.copy()
        if not self.freeze:
            faces = self.face_cascade.detectMultiScale(img, 1.3, 5)
            if len(faces) == 0:
                self.face_included_frames = 0
        else:
            faces = []
        detected_faces = []
        face_index = 0
        for (x, y, w, h) in faces:
            if w > 130:
                self.face_detected = True
                if face_index == 0:
                    self.face_included_frames = self.face_included_frames + 1

                profile_image_copy = img.copy()
                cv2.rectangle(img, (x, y), (x + w, y + h), (67, 67, 67), 1)

                cv2.putText(img, str(self.frame_threshold - self.face_included_frames),
                            (int(x + w / 4), int(y + h / 1.5)),
                            cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2)

                self.profile_image = profile_image_copy[int(y):int(y + h), int(x):int(x + w)]

                detected_faces.append((x, y, w, h))
                face_index = face_index + 1

            # -------------------------------------
        if self.face_detected == True and self.face_included_frames == self.frame_threshold and self.freeze == False:
            self.freeze = True
            self.base_img = raw_img.copy()
            self.detected_faces_final = detected_faces.copy()
            self.tic = time.time()
            self.sayac = 0
        if self.freeze:
            toc = time.time()

            if (toc - self.tic) < self.time_threshold:
                if self.freezed_frame == 0:
                    for detected_face in self.detected_faces_final:
                        x = detected_face[0]
                        y = detected_face[1]
                        w = detected_face[2]
                        h = detected_face[3]

                    cv2.rectangle(img, (x, y), (x + w, y + h), self.text_color, 3)
                    custom_face = self.base_img[y:y + h, x:x + w]

                    self.age, self.gender = self.age_and_gender_find(custom_face, self.age_model, self.gender_model)
                    self.emotion = self.emotion_detection(self.emotion_model, custom_face)

                    custom_face = functions.detectFace(custom_face, self.input_shape)

                    print("Gerçek Emotion :", list(self.emotion)[0])
                    self.ui.lbl_duygu.setText(list(self.emotion)[0])
                    if custom_face.shape[1:3] == self.input_shape:
                        if self.df.shape[0] > 0:  # if there are images to verify, apply face recognition
                            img1_representation = self.model.predict(custom_face)[0, :]

                            def findDistance(row):
                                distance_metric = row['distance_metric']
                                img2_representation = row['embedding']

                                distance = 1000
                                if distance_metric == 'cosine':
                                    distance = dst.findCosineDistance(img1_representation, img2_representation)
                                elif distance_metric == 'euclidean':
                                    distance = dst.findEuclideanDistance(img1_representation, img2_representation)
                                elif distance_metric == 'euclidean_l2':
                                    distance = dst.findEuclideanDistance(dst.l2_normalize(img1_representation),
                                                                         dst.l2_normalize(img2_representation))

                                return distance

                            self.df['distance'] = self.df.apply(findDistance, axis=1)
                            df = self.df.sort_values(by=["distance"])

                            candidate = df.iloc[0]
                            self.employee_name = candidate['employee']
                            self.best_distance = candidate['distance']
                time_left = int(self.time_threshold - (toc - self.tic))

                if self.best_distance <= self.threshold:

                    self.display_img = cv2.imread(self.employee_name)

                    if self.sayac < 1:
                        self.getIformation(self.employee_name)
                        self.sayac += 1

                cv2.rectangle(img, (10, 10), (90, 50), (67, 67, 67), -10)
                cv2.putText(img, str(time_left), (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
                self.freezed_frame = self.freezed_frame + 1
                self.displayImage(img)
            else:
                self.face_detected = False
                self.face_included_frames = 0
                self.freeze = False
                self.freezed_frame = 0
                self.UI_Ayar()
        else:
            self.displayImage(img)

    def age_and_gender_find(self, custom_face, age_model, gender_model):
        gender = ""
        face_224 = functions.detectFace(custom_face, (224, 224), False)
        age_predictions = age_model.predict(face_224)[0, :]
        apparent_age = Age.findApparentAge(age_predictions)
        gender_predictions = gender_model.predict(face_224)[0, :]
        if np.argmax(gender_predictions) == 0:
            gender = "Kadın"
        elif np.argmax(gender_predictions) == 1:
            gender = "Erkek"
        analysis_report = str(int(apparent_age)) + " " + gender
        self.ui.lbl_yas.setText(str(round(apparent_age)))
        self.ui.lbl_cinsiyet.setText(gender)
        print("Analysis report: ", analysis_report)
        return apparent_age, gender

    def emotion_detection(self, emotion_model, custom_face):
        detected_emotion = dict()
        gray_img = functions.detectFace(custom_face, (48, 48), True)
        emotion_labels = ['Kızgın', 'Tiksinti', 'Korku', 'Mutlu', 'Üzgün', 'Şaşırmış', 'Doğal']
        emotion_predictions = emotion_model.predict(gray_img)[0, :]
        sum_of_predictions = emotion_predictions.sum()
        mood_items = []
        for i in range(0, len(emotion_labels)):
            mood_item = []
            emotion_label = emotion_labels[i]
            emotion_prediction = 100 * emotion_predictions[i] / sum_of_predictions
            mood_item.append(emotion_label)
            mood_item.append(emotion_prediction)
            mood_items.append(mood_item)
        emotion_df = pd.DataFrame(mood_items, columns=["emotion", "score"])
        emotion_df = emotion_df.sort_values(by=["score"], ascending=False).reset_index(drop=True)

        for index, instance in emotion_df.iterrows():
            emotion_label = "%s " % (instance["emotion"])
            emotion_score = instance["score"] / 100
            detected_emotion[emotion_label] = emotion_score
        return detected_emotion

    def displayImage(self, img):
        qFormat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qFormat = QImage.Format_RGBA8888
            else:
                qFormat = QImage.Format_RGB888
        outImage = QImage(img, img.shape[1], img.shape[0], img.strides[0], qFormat)
        # BGR to RGB
        outImage = outImage.rgbSwapped()
        self.ui.kamera_ekrani.setPixmap(QPixmap.fromImage(outImage))
        self.ui.kamera_ekrani.setScaledContents(True)

    def stopCam(self):
        self.capture.release()
        resim = self.clear_cam(profil=False)
        self.ui.kamera_ekrani.setPixmap(QPixmap.fromImage(resim))
        self.timer.stop()
        self.ui.actionStartCam.setEnabled(True)
        self.ui.actionYoklamayiBitir.setEnabled(True)

    def clear_cam(self, profil=False):
        qFormat = QImage.Format_Indexed8
        if profil:
            resim = cv2.imread("images/personReal.png")
            resim = cv2.resize(resim, (100, 100))
        else:
            resim = cv2.imread("images/clear_cam.png")
        resim = QImage(resim, resim.shape[1], resim.shape[0], resim.strides[0], qFormat)
        return resim


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

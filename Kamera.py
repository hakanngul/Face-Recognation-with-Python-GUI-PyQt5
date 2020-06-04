import os
import time
from threading import Thread

import pandas as pd
import numpy as np
import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox
from tqdm import tqdm

os.environ["CUDA_DEVICE_ORDER"] = "0000:01:00.0"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

from model.basemodels import VGGFace, Facenet
from model.extendedmodels import Age, Gender, Emotion
from model.commons import functions, distance as dst


class KameraIslemleri(Thread):
    def __init__(self, ui, model_name, distance_metric):
        Thread.__init__(self)
        Thread.start(self)
        self.timer = QTimer()
        self.ui = ui
        self.model_name = model_name
        self.SinifListesi = []
        self.distance_metric = distance_metric

    def loadSinif(self, sinifListesi):
        self.SinifListesi = sinifListesi

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

    def startCam(self):
        self.ui.actionStartCam.setEnabled(False)
        self.ui.actionStopCam.setEnabled(True)
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 650)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Camera)
        self.timer.start(1000. / 24)

    @staticmethod
    def emotion_detection(emotion_model, custom_face):
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

    def loadModelandEmbedding(self, db_path):
        global input_shape, model
        model_name = self.model_name
        distance_metric = self.distance_metric
        employees = []
        # liste = list(db.getDersBilgileri(self.dersGenelKod))[0].split(",")
        liste = self.SinifListesi
        print(liste)
        print(len(liste))
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
            pbar = tqdm(range(0, len(employees)), desc='Finding embeddings')
            embeddings = []
            for index in pbar:
                employee = employees[index]
                pbar.set_description("Finding embedding for %s" % (employee.split("/")[-1]))
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
            print("Embeddings found for given data set in ", toc - tic, " seconds")
            return df, model, threshold, input_shape
        else:
            QMessageBox.critical(self, "Dikkat", "Sınıf Listesi Yüklenemedi loadModelandEmbedding")

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

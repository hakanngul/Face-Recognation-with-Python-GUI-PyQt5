import mysql.connector


def baglantiOlustur():
    cnx = mysql.connector.connect(user="root", password="123456", host="localhost", database="mydatabase",
                                  auth_plugin="mysql_native_password")
    cursor = cnx.cursor(buffered=True)
    return cursor, cnx

mycursor, cnx = baglantiOlustur()

mycursor.execute("show tables")
for i in mycursor:
    print(i)




class Student:
    def __init__(self):
        print("Student Nesnesi Oluşturuldu")

    @staticmethod
    def addStudent(data):
        cursor, connection = baglantiOlustur()
        sql = """
            INSERT INTO student SET  Student_No=%s,Student_Name=%s,Student_SurName=%s,
            Student_Program=%s,Student_Class=%s,Student_Branch=%s,Student_Branch_Office=%s,
            Student_ImagePath=%s
        """
        try:
            cursor.execute(sql, data)
            connection.commit()
            print(f'{cursor.rowcount} tane kayıt eklendi')
            return True
        except mysql.connector.Error as err:
            print("hata :", err)
        finally:
            connection.close()

    @staticmethod
    def addLessonToStudent(data):
        cursor, connection = baglantiOlustur()
        sql = """UPDATE student SET Student_TakenLessons=%s WHERE Student_No=%s"""
        print("Data =>", data)
        try:
            cursor.execute(sql, data)
            connection.commit()
            return True
        except mysql.connector.Error as err:
            print("hata :", err)
            return False
        finally:
            connection.close()

    @staticmethod
    def getStudentInformations(data):
        cursor, connection = baglantiOlustur()
        sql = "SELECT * FROM student WHERE Student_No=%s"
        try:
            cursor.execute(sql, (data,))
            return cursor.fetchall()
        except mysql.connector.Error as err:
            print("hata :", err)
            return err
        finally:
            connection.close()

    @staticmethod
    def getAllStudents():
        cursor, connection = baglantiOlustur()
        try:
            cursor.execute("SELECT Student_No FROM student")
            return cursor.fetchall()
        except mysql.connector.Error as err:
            print("hata :", err)
            return err
        finally:
            connection.close()

    @staticmethod
    def removeLessonFromStudent(data):
        cursor, connection = baglantiOlustur()
        sql = """UPDATE student SET Student_TakenLessons=%s WHERE Student_No=%s"""
        try:
            cursor.execute(sql, data)
            connection.commit()
        except mysql.connector.Error as err:
            print("hata :", err)
            return err
        finally:
            connection.close()

    @staticmethod
    def UpdateStudent(data):
        cursor, connection = baglantiOlustur()
        print(data)
        sql = """UPDATE student SET Student_Name=%s, Student_Surname=%s,Student_Program=%s,Student_Class=%s, 
        Student_Branch=%s, Student_Branch_Office=%s WHERE Student_No =%s
        """
        cursor.execute(sql, data)
        try:
            connection.commit()
            print(f'{cursor.lastrowid} Öğrenci Düzenlendi {cursor.rowcount} adet güncelleme oldu')
            return True
        except mysql.connector.Error as err:
            print("hata :", err)
            return False
        finally:
            connection.close()

    @staticmethod
    def getStudentAllInformation(numara):
        cursor, connection = baglantiOlustur()
        sql = """SELECT Student_Name, Student_Surname FROM student where Student_No=%s"""
        try:
            cursor.execute(sql, (numara,))
            return cursor.fetchall()
        except mysql.connector.Error as err:
            print("hata :", err)
            return err
        finally:
            connection.close()

    @staticmethod
    def getStudentLessons(okulNo):
        cursor, connection = baglantiOlustur()
        sql = """SELECT Student_TakenLessons FROM student
        WHERE Student_No=%s"""
        cursor.execute(sql, (okulNo,))
        try:
            return cursor.fetchone()
        except mysql.connector.Error as err:
            print("Error :", err)
            return err
        finally:
            connection.close()


class Teacher:
    def __init__(self):
        print("Teacher Nesnesi Oluşturuldu ...")

    @staticmethod
    def TeacherSignedUp(data):
        cursor, connection = baglantiOlustur()
        sql = """INSERT INTO teacher SET Teacher_Name=%s,Teacher_SurName=%s,Teacher_Branch=%s,Teacher_UserName=%s,
        Teacher_UserPassword=%s,Teacher_Mail=%s,Teacher_ImagePath=%s
         
        """
        try:
            cursor.execute(sql, data)
            connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f'Kayıt Başarısız oldu hata :{err}')
        finally:
            connection.close()
            print("MySQL connection is closed")

    @staticmethod
    def TeacherLogin(data):
        cursor, connection = baglantiOlustur()
        print("Veri : " + str(data))
        sql = """SELECT * from teacher WHERE Teacher_UserName=%s and Teacher_UserPassword=%s"""
        try:
            cursor.execute(sql, data)
            return cursor.fetchone()
        except mysql.connector.Error as err:
            print("hata :", err)
            return False
        finally:
            connection.close()
            print("MySQL connection is closed")

    @staticmethod
    def getTeacherInformation(data):
        cursor, connection = baglantiOlustur()
        sql = """SELECT * FROM teacher 
        WHERE Teacher_UserName=%s and Teacher_UserPassword=%s"""
        cursor.execute(sql, data)
        try:
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print("MySQL :", err)
        finally:
            connection.close()

    @staticmethod
    def getTeacherLessons(data):
        cursor, connection = baglantiOlustur()
        sql = "SELECT Teacher_LessonGiven from teacher where Teacher_id=%s and Teacher_UserName=%s"
        try:
            cursor.execute(sql, data)
            return cursor.fetchone()
        except mysql.connector.Error as err:
            return print("Hata :", err)
        finally:
            connection.close()
            print("MySQL connection is closed")

    @staticmethod
    def getAllTeacherInformations():
        cursor, connection = baglantiOlustur()
        cursor.execute("SELECT * FROM ogretmen")
        try:
            return cursor.fetchall()
        except mysql.connector.Error as err:
            return err
        finally:
            connection.close()

    @staticmethod
    def UpdateTeacherLessons(data):
        cursor, connection = baglantiOlustur()
        sql = "UPDATE teacher SET Teacher_LessonGiven =%s where Teacher_id=%s"
        try:
            cursor.execute(sql, data)
            connection.commit()
            print(f'{cursor.rowcount} Ders eklendi')
        except mysql.connector.Error as err:
            print("Error =>", err)
            return err
        finally:
            connection.close()

    @staticmethod
    def UpdateTeacherInformation(data):
        cursor, connection = baglantiOlustur()
        sql = """UPDATE teacher 
        SET Teacher_Name=%s,Teacher_SurName=%s,
        Teacher_Branch=%s,Teacher_UserPassword=%s,
        Teacher_Mail=%s WHERE
        Teacher_id=%s AND Teacher_UserName=%s
        """
        cursor.execute(sql, data)
        try:
            connection.commit()
            return True
        except mysql.connector.Error as err:
            print("Hata :", err)
            return False
        finally:
            connection.close()

    @staticmethod
    def getTeacherUserName():
        cursor, connection = baglantiOlustur()
        sql = "SELECT Teacher_UserName from teacher"
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except mysql.connector.Error as err:
            print("Hata :", err)
            return False
        finally:
            connection.close()

    @staticmethod
    def getTeacherMail():
        cursor, connection = baglantiOlustur()
        sql = "SELECT Teacher_Mail from teacher"
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        except mysql.connector.Error as err:
            print("Hata :", err)
            return False
        finally:
            connection.close()

    @staticmethod
    def getSelectedTeacherMail(Teacher_UserName):
        cursor, connection = baglantiOlustur()
        sql = "SELECT Teacher_Mail from teacher WHERE Teacher_UserName=%s "
        try:
            cursor.execute(sql, (Teacher_UserName,))
            return cursor.fetchone()
        except mysql.connector.Error as err:
            print("Hata :", err)
            return False
        finally:
            connection.close()


class Lessons:

    @staticmethod
    def AddLesson(data):
        cursor, connection = baglantiOlustur()
        print("Dtabase Tarafı =>", data)
        sql = """
        INSERT INTO lessons (Lessons_Name,Lessons_Code,Lessons_quota,Lessons_Branch_Office,Lessons_Class,
        Lessons_GeneralCode,Lessons_Teacher,Lessons_Branch,Lessons_Program) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        try:
            cursor.execute(sql, data)
            connection.commit()
            print(f'{cursor.rowcount} adet ders Eklendi')
            return True
        except mysql.connector.Error as err:
            print("Hata :", err)
            return False
        finally:
            connection.close()

    @staticmethod
    def RemoveStudentFromLesson(data):
        cursor, connection = baglantiOlustur()
        sql = """UPDATE lessons SET Lessons_StudentsTaken=%s where Lessons_GeneralCode=%s"""
        try:
            cursor.execute(sql, data)
            connection.commit()
            print(f'{cursor.rowcount} adet ders Çıkartıldı')
        except mysql.connector.Error as err:
            print("Hata :", err)
            return err
        finally:
            connection.close()

    @staticmethod
    def AddStudentToLesson(data):
        cursor, connection = baglantiOlustur()

        sql = """UPDATE lessons SET Lessons_StudentsTaken=%s WHERE Lessons_GeneralCode=%s"""
        try:
            cursor.execute(sql, data)
            connection.commit()
            print(f'{cursor.rowcount} adet Öğrenci eklendi')
            return True
        except mysql.connector.Error as err:
            print("Hata :", err)
            return False
        finally:
            connection.close()

    @staticmethod
    def getLessonTakenStudents(data):
        cursor, connection = baglantiOlustur()
        sql = """SELECT Lessons_StudentsTaken from lessons where Lessons_GeneralCode=%s"""
        try:
            cursor.execute(sql, (data,))
            return cursor.fetchone()
        except mysql.connector.Error as err:
            print("Error :", err)
        finally:
            connection.close()

    @staticmethod
    def getLessonAllInformation(generalCode):
        cursor, connection = baglantiOlustur()
        sql = """SELECT * FROM lessons WHERE Lessons_GeneralCode=%s"""
        try:
            cursor.execute(sql, (generalCode,))
            return cursor.fetchall()
        except mysql.connector.Error as err:
            print("Error :", err)
        finally:
            connection.close()

    @staticmethod
    def getStudentAllInformation(numara):
        cursor, connection = baglantiOlustur()
        sql = """
        SELECT Student_Name,Student_SurName FROM student
        WHERE Student_No=%s
        """
        cursor.execute(sql, (numara,))
        try:
            return cursor.fetchall()
        except mysql.connector.Error as err:
            print("Error :", err)
            return False
        finally:
            connection.close()

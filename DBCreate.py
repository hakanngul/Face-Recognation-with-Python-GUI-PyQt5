import mysql.connector


def DBCreate():
    schema = "CREATE SCHEMA IF NOT EXISTS mydatabase2"

    connection = mysql.connector.connect(user="root", password="123456", host="localhost", database="mydatabase2",
                                         auth_plugin="mysql_native_password")
    cursor = connection.cursor(buffered=True)
    cursor.execute(schema)
    lesson_table = """
    CREATE TABLE IF NOT EXISTS `mydatabase2`.`lessons` (
      `Lessons_id` INT NOT NULL AUTO_INCREMENT,
      `Lessons_Name` VARCHAR(45) NOT NULL,
      `Lessons_Code` VARCHAR(45) NOT NULL,
      `Lessons_quota` INT NULL DEFAULT 60,
      `Lessons_Branch_Office` VARCHAR(5) NOT NULL,
      `Lessons_Class` VARCHAR(5) NOT NULL,
      `Lessons_GeneralCode` VARCHAR(45) NOT NULL,
      `Lessons_Teacher` VARCHAR(45) NOT NULL,
      `Lessons_Branch` VARCHAR(45) NOT NULL,
      `Lessons_Program` VARCHAR(45) NOT NULL,
      `Lessons_StudentsTaken` LONGTEXT NULL,
      PRIMARY KEY (`Lessons_id`),
      UNIQUE INDEX `Lessons_id_UNIQUE` (`Lessons_id` ASC) VISIBLE,
      UNIQUE INDEX `Lessons_GeneralCode_UNIQUE` (`Lessons_GeneralCode` ASC) VISIBLE);
    """
    cursor.execute(lesson_table)
    student_table = """
    CREATE TABLE IF NOT EXISTS `mydatabase2`.`student`  (
      `Student_id` INT NOT NULL AUTO_INCREMENT,
      `Student_No` INT NOT NULL,
      `Student_Name` VARCHAR(45) NOT NULL,
      `Student_SurName` VARCHAR(45) NOT NULL,
      `Student_Program` VARCHAR(45) NOT NULL,
      `Student_Class` VARCHAR(5) NOT NULL,
      `Student_Branch` VARCHAR(45) NOT NULL,
      `Student_Branch_Office` VARCHAR(45) NOT NULL,
      `Student_ImagePath` VARCHAR(100) NULL DEFAULT NULL,
      `Student_TakenLessons` LONGTEXT NULL DEFAULT NULL,
      PRIMARY KEY (`Student_id`),
      UNIQUE INDEX `Student_id_UNIQUE` (`Student_id` ASC) VISIBLE,
      UNIQUE INDEX `Student_No_UNIQUE` (`Student_No` ASC) VISIBLE);
    """
    cursor.execute(student_table)
    teacher_table = """
    CREATE TABLE IF NOT EXISTS `mydatabase2`.`teacher`  (
      `Teacher_id` INT NOT NULL AUTO_INCREMENT,
      `Teacher_Name` VARCHAR(45) NOT NULL,
      `Teacher_SurName` VARCHAR(45) NOT NULL,
      `Teacher_Branch` VARCHAR(45) NOT NULL,
      `Teacher_UserName` VARCHAR(45) NOT NULL,
      `Teacher_UserPassword` VARCHAR(45) NOT NULL,
      `Teacher_Mail` VARCHAR(45) NOT NULL,
      `Teacher_LessonGiven` LONGTEXT NULL DEFAULT NULL,
      `Teacher_ImagePath` VARCHAR(100) NULL DEFAULT NULL,
      PRIMARY KEY (`Teacher_id`),
      UNIQUE INDEX `Teacher_id_UNIQUE` (`Teacher_id` ASC) VISIBLE,
      UNIQUE INDEX `Teacher_UserName_UNIQUE` (`Teacher_UserName` ASC) VISIBLE,
      UNIQUE INDEX `Teacher_Mail_UNIQUE` (`Teacher_Mail` ASC) VISIBLE);
    """
    cursor.execute(teacher_table)

    connection.close()

CREATE DATABASE  IF NOT EXISTS `mydatabase` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `mydatabase`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: mydatabase
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `lessons`
--

DROP TABLE IF EXISTS `lessons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lessons` (
  `Lessons_id` int NOT NULL AUTO_INCREMENT,
  `Lessons_Name` varchar(45) NOT NULL,
  `Lessons_Code` varchar(45) NOT NULL,
  `Lessons_quota` int DEFAULT '60',
  `Lessons_Branch_Office` varchar(5) NOT NULL,
  `Lessons_Class` varchar(5) NOT NULL,
  `Lessons_GeneralCode` varchar(45) NOT NULL,
  `Lessons_Teacher` varchar(50) NOT NULL,
  `Lessons_Branch` varchar(45) NOT NULL,
  `Lessons_Program` varchar(45) NOT NULL,
  `Lessons_StudentsTaken` longtext,
  PRIMARY KEY (`Lessons_id`),
  UNIQUE KEY `Lessons_id_UNIQUE` (`Lessons_id`),
  UNIQUE KEY `Lessons_GeneralCode_UNIQUE` (`Lessons_GeneralCode`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lessons`
--

LOCK TABLES `lessons` WRITE;
/*!40000 ALTER TABLE `lessons` DISABLE KEYS */;
INSERT INTO `lessons` VALUES (22,'algoritma','ymt213',60,'A','1','YMT213-A-S','3','Yazılım Mühendisliği','S','123456,15542508,15542530'),(23,'askdasjdklj','karabakk',60,'A','1','KARABAKK-A-S','3','Yazılım Mühendisliği','S',NULL),(24,'deneme12345','d123',60,'A','1','D123-A-S','3','Yazılım Mühendisliği','S',NULL),(25,'sdfjkasdhfj','kophjhjfk123',60,'A','1','KOPHJHJFK123-A-S','3','Yazılım Mühendisliği','S',NULL),(26,'algoritma','ymt213123',60,'A','1','YMT213123-A-S','6','YAZILIM MÜHENDISLIĞI','S',NULL),(27,'deneme','asd3414',60,'A','1','ASD3414-A-S','6','YAZILIM MÜHENDISLIĞI','S',NULL),(28,'deneme','olay4563',60,'A','1','OLAY4563-A-S','6','YAZILIM MÜHENDISLIĞI','S','123456,15542512,15542530');
/*!40000 ALTER TABLE `lessons` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `Student_id` int NOT NULL AUTO_INCREMENT,
  `Student_No` int NOT NULL,
  `Student_Name` varchar(45) NOT NULL,
  `Student_SurName` varchar(45) NOT NULL,
  `Student_Program` varchar(45) NOT NULL,
  `Student_Class` char(1) NOT NULL,
  `Student_Branch` varchar(45) NOT NULL,
  `Student_Branch_Office` varchar(5) NOT NULL,
  `Student_ImagePath` varchar(100) DEFAULT NULL,
  `Student_TakenLessons` longtext,
  PRIMARY KEY (`Student_id`),
  UNIQUE KEY `Student_id_UNIQUE` (`Student_id`),
  UNIQUE KEY `Student_No_UNIQUE` (`Student_No`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (5,123456,'hakan','gül','S','3','Yazılım Mühendisliği','A','database/123456/','YMT213-A-S,OLAY4563-A-S'),(6,15542508,'chris','xx','S','1','Yazılım Mühendisliği','A','database/15542508/','YMT213-A-S'),(7,15542512,'robert','jun','S','1','Yazılım Mühendisliği','A','database/15542512/','OLAY4563-A-S'),(8,15542530,'scarlett','johansson','S','1','Yazılım Mühendisliği','A','database/15542530/','YMT213-A-S,OLAY4563-A-S');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher` (
  `Teacher_id` int NOT NULL AUTO_INCREMENT,
  `Teacher_Name` varchar(45) NOT NULL,
  `Teacher_SurName` varchar(45) NOT NULL,
  `Teacher_Branch` varchar(45) NOT NULL,
  `Teacher_UserName` varchar(45) NOT NULL,
  `Teacher_UserPassword` varchar(45) NOT NULL,
  `Teacher_Mail` varchar(45) NOT NULL,
  `Teacher_LessonGiven` longtext,
  `Teacher_ImagePath` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Teacher_id`),
  UNIQUE KEY `Teacher_id_UNIQUE` (`Teacher_id`),
  UNIQUE KEY `Teacher_UserName_UNIQUE` (`Teacher_UserName`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (3,'murat','karabatak','yazilim mühendisliği','hakn','123456','hhakangull@gmail.com','YMT213-A-S,KARABAKK-A-S,D123-A-S,KOPHJHJFK123-A-S','ogretmenler/'),(4,'hakan','gül','yazılım mühendisliği','hakn123','123456','eragoln1@gmail.com',NULL,'ogretmenler/'),(6,'hakan','güler','yazilim mühendisliği','hakangul29','123456','hakanngul@icloud.com','YMT213123-A-S,ASD3414-A-S,OLAY4563-A-S','ogretmenler/');
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-29  3:49:16

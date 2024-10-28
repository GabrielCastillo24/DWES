-- MariaDB dump 10.19  Distrib 10.11.6-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mysitedb
-- ------------------------------------------------------
-- Server version	10.11.6-MariaDB-0+deb12u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tCOMENTARIOS`
--

DROP TABLE IF EXISTS `tCOMENTARIOS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tCOMENTARIOS` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comentario` varchar(2000) DEFAULT NULL,
  `usuarioId` int(11) DEFAULT NULL,
  `libroId` int(11) DEFAULT NULL,
  `fechaComentario` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `usuarioId` (`usuarioId`),
  KEY `libroId` (`libroId`),
  CONSTRAINT `tCOMENTARIOS_ibfk_1` FOREIGN KEY (`usuarioId`) REFERENCES `tUSUARIO` (`id`),
  CONSTRAINT `tCOMENTARIOS_ibfk_2` FOREIGN KEY (`libroId`) REFERENCES `tLIBROS` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tCOMENTARIOS`
--

LOCK TABLES `tCOMENTARIOS` WRITE;
/*!40000 ALTER TABLE `tCOMENTARIOS` DISABLE KEYS */;
INSERT INTO `tCOMENTARIOS` VALUES
(1,'comen1',1,1,NULL),
(2,'comen1',2,2,NULL),
(3,'comen1',3,3,NULL),
(4,'comen1',4,4,NULL),
(5,'comen1',5,5,NULL),
(6,'quiero entrar en coment.php\r\n',NULL,3,NULL),
(7,'Este es un nuevo comentario de prueba ',NULL,3,NULL),
(8,'ESte es otro comentario de prueba 2\r\n',NULL,3,NULL),
(9,'Hola',NULL,3,NULL),
(10,'Hola soy un comentario ',NULL,3,'2024-10-28');
/*!40000 ALTER TABLE `tCOMENTARIOS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tLIBROS`
--

DROP TABLE IF EXISTS `tLIBROS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tLIBROS` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `url_imagen` varchar(400) DEFAULT NULL,
  `autor` varchar(50) DEFAULT NULL,
  `numPaginas` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tLIBROS`
--

LOCK TABLES `tLIBROS` WRITE;
/*!40000 ALTER TABLE `tLIBROS` DISABLE KEYS */;
INSERT INTO `tLIBROS` VALUES
(1,'Libro1','https://img.freepik.com/vector-premium/acuarela-pila-antigua-libros-libro-abierto_92810-1041.jpg','autor1',100),
(2,'Libro2','https://img.freepik.com/vector-premium/acuarela-pila-antigua-libros-libro-abierto_92810-1041.jpg','autor2',50),
(3,'Libro3','https://img.freepik.com/vector-premium/acuarela-pila-antigua-libros-libro-abierto_92810-1041.jpg','autor3',90),
(4,'Libro4','https://img.freepik.com/vector-premium/acuarela-pila-antigua-libros-libro-abierto_92810-1041.jpg','autor4',60),
(5,'Libro5','https://img.freepik.com/vector-premium/acuarela-pila-antigua-libros-libro-abierto_92810-1041.jpg','autor5',200);
/*!40000 ALTER TABLE `tLIBROS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tUSUARIO`
--

DROP TABLE IF EXISTS `tUSUARIO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tUSUARIO` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(100) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `contraseña` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tUSUARIO`
--

LOCK TABLES `tUSUARIO` WRITE;
/*!40000 ALTER TABLE `tUSUARIO` DISABLE KEYS */;
INSERT INTO `tUSUARIO` VALUES
(1,'user1','user1','user1@gmail.com','1234'),
(2,'user2','user2','user2@gmail.com','12345'),
(3,'user3','user3','user3@gmail.com','123456'),
(4,'user4','user4','user4@gmail.com','1234567'),
(5,'user4','user4','user5@gmail.com','12345678');
/*!40000 ALTER TABLE `tUSUARIO` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-28 22:22:53

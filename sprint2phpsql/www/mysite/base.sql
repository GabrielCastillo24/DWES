CREATE DATABASE mysitedb;
USE mysitedb;

CREATE TABLE `tUSUARIO` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(100) DEFAULT NULL,
  `email` varchar(200) UNIQUE,
  `contraseña` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `tLIBROS` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `url_imagen` varchar(400) DEFAULT NULL,
  `autor` varchar(50) DEFAULT NULL,
  `numPaginas` int DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `tCOMENTARIOS` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comentario` varchar(2000) DEFAULT NULL,
  `usuarioId` int,
  `libroId` int,
  PRIMARY KEY (`id`),
FOREIGN KEY (usuarioId) REFERENCES tUSUARIO(id),
FOREIGN KEY (libroId) REFERENCES tLIBROS(id)
);

INSERT INTO `tUSUARIO` VALUES
(1,'user1','user1','user1@gmail.com','1234'),
(2,'user2','user2','user2@gmail.com','12345'),
(3,'user3','user3','user3@gmail.com','123456'),
(4,'user4','user4','user4@gmail.com','1234567'),
(5,'user4','user4','user5@gmail.com','12345678');

INSERT INTO `tLIBROS` VALUES
(1,'Libro1','https://img.freepik.com/vector-premium/acuarela-pila-antigua-libros-libro-abierto_92810-1041.jpg','autor1',100),
(2,'Libro2','https://img.freepik.com/vector-premium/acuarela-pila-antigua-libros-libro-abierto_92810-1041.jpg','autor2',50),
(3,'Libro3','https://img.freepik.com/vector-premium/acuarela-pila-antigua-libros-libro-abierto_92810-1041.jpg','autor3',90),
(4,'Libro4','https://img.freepik.com/vector-premium/acuarela-pila-antigua-libros-libro-abierto_92810-1041.jpg','autor4',60),
(5,'Libro5','https://img.freepik.com/vector-premium/acuarela-pila-antigua-libros-libro-abierto_92810-1041.jpg','autor5',200);

INSERT INTO `tCOMENTARIOS` VALUES
(1,'comen1',1,1),
(2,'comen1',2,2),
(3,'comen1',3,3),
(4,'comen1',4,4),
(5,'comen1',5,5);
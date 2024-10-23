
CREATE DATABASE mysitedb;
USE mysitedb;

-- CREA LA TABLA USUARIO
CREATE TABLE tUSUARIO (
    id  INT AUTO_INCREMENT,
    nombre VARCHAR (50),
    apellido VARCHAR(100),
    email VARCHAR(200) UNIQUE,
    contraseña VARCHAR(200),
    PRIMARY KEY (id)
);

-- CREA LA TABLA LIBROS
CREATE TABLE tLIBROS(
    id INT AUTO_INCREMENT,
    nombre VARCHAR(50),
    url_imagen VARCHAR(200),
    autor VARCHAR(50),
    numPaginas INT,
    PRIMARY KEY (id)
);


-- CREA LA TABLA COMENTARIOS
CREATE TABLE tCOMENTARIOS(
    id INT AUTO_INCREMENT,
    comentario VARCHAR(2000),
    usuarioId INT,
    libroId INT,
    PRIMARY KEY (id),
    FOREIGN KEY (usuarioId) REFERENCES tUSUARIO(id),
    FOREIGN KEY (libroId) REFERENCES tLIBROS(id)
);

-- INSERTA DATOS A LA TABLA USUARIO
INSERT INTO tUSUARIO (nombre,apellido,email,contraseña) values("user1","user1","user1@gmail.com","1234");
INSERT INTO tUSUARIO (nombre,apellido,email,contraseña) values("user2","user2","user2@gmail.com","12345");
INSERT INTO tUSUARIO (nombre,apellido,email,contraseña) values("user3","user3","user3@gmail.com","123456");
INSERT INTO tUSUARIO (nombre,apellido,email,contraseña) values("user4","user4","user4@gmail.com","1234567");
INSERT INTO tUSUARIO (nombre,apellido,email,contraseña) values("user4","user4","user5@gmail.com","12345678");

-- INSERTA DATOS A LA TABLA LIBROS 
INSERT INTO tLIBROS (nombre,url_imagen) values("Libro1","url1");
INSERT INTO tLIBROS (nombre,url_imagen) values("Libro2","url1");
INSERT INTO tLIBROS (nombre,url_imagen) values("Libro3","url1");
INSERT INTO tLIBROS (nombre,url_imagen) values("Libro4","url1");
INSERT INTO tLIBROS (nombre,url_imagen) values("Libro5","url1");

-- INSERTA DATOS A LA TABLA COMENTARIOS 
INSERT INTO tCOMENTARIOS (comentario,usuarioId,libroId) values("comen1",1,1);
INSERT INTO tCOMENTARIOS (comentario,usuarioId,libroId) values("comen1",2,2);
INSERT INTO tCOMENTARIOS (comentario,usuarioId,libroId) values("comen1",3,3);
INSERT INTO tCOMENTARIOS (comentario,usuarioId,libroId) values("comen1",4,4);
INSERT INTO tCOMENTARIOS (comentario,usuarioId,libroId) values("comen1",5,5);



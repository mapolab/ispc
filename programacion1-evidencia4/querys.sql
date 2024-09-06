CREATE DATABASE evidencia4;
USE evidencia4;

CREATE TABLE cancion (
  id int NOT NULL AUTO_INCREMENT,
  titulo varchar(45) DEFAULT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE reproductor (
  id int NOT NULL AUTO_INCREMENT,
  encendido tinyint DEFAULT NULL,
  reproduciendo tinyint DEFAULT NULL,
  cancion_actual int DEFAULT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (cancion_actual) REFERENCES cancion(id)
);

INSERT INTO cancion (titulo) VALUES ('Enter Sandman')
INSERT INTO cancion (titulo) VALUES ('Park')
INSERT INTO cancion (titulo) VALUES ('Paranoid')
INSERT INTO cancion (titulo) VALUES ('Stan')
INSERT INTO cancion (titulo) VALUES ('Master of Puppets')
INSERT INTO cancion (titulo) VALUES ('Painkiller')
INSERT INTO cancion (titulo) VALUES ('Iron Man')
INSERT INTO cancion (titulo) VALUES ('South of Heaven')
INSERT INTO cancion (titulo) VALUES ('Meta')
INSERT INTO cancion (titulo) VALUES ('Mil horas')


SELECT COUNT(*) FROM cancion 
SELECT C.titulo FROM reproductor as R, cancion as C Where R.cancion_actual = C.id ;
SELECT * FROM cancion Where titulo LIKE "E%";
SELECT * FROM cancion order by id Desc;
SELECT * FROM cancion where id BETWEEN 3 and 8 ;

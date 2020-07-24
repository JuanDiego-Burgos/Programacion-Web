
CREATE DATABASE IF NOT EXISTS `tarea`;
USE `tarea`;

CREATE TABLE IF NOT EXISTS `grupo` (
  `idgrupo` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) DEFAULT '',
  PRIMARY KEY (`idgrupo`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;


CREATE TABLE IF NOT EXISTS `plancuenta` (
  `idplancuenta` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` varchar(100) NOT NULL DEFAULT '0',
  `grupoid` int(11) NOT NULL,
  `descripcion` varchar(100) DEFAULT '',
  `naturaleza` varchar(100) DEFAULT '',
  `estado` bit(1) NOT NULL,
  PRIMARY KEY (`idplancuenta`),
  KEY `grupoid` (`grupoid`),
  CONSTRAINT `FK_plancuenta_grupo` FOREIGN KEY (`grupoid`) REFERENCES `grupo` (`idgrupo`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;


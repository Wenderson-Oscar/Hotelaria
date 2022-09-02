-- MySQL dump 10.13  Distrib 8.0.30, for Linux (x86_64)
--
-- Host: localhost    Database: hotel
-- ------------------------------------------------------
-- Server version	8.0.30-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alimentos`
--

DROP TABLE IF EXISTS `alimentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alimentos` (
  `idalimentos` int NOT NULL AUTO_INCREMENT,
  `cafe_manha` varchar(20) DEFAULT NULL,
  `almoco` varchar(30) DEFAULT NULL,
  `jantar` varchar(40) DEFAULT NULL,
  `lanche` varchar(21) DEFAULT NULL,
  `pf` int DEFAULT NULL,
  `cliente` int DEFAULT NULL,
  PRIMARY KEY (`idalimentos`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alimentos`
--

LOCK TABLES `alimentos` WRITE;
/*!40000 ALTER TABLE `alimentos` DISABLE KEYS */;
INSERT INTO `alimentos` VALUES (1,'Cafe','Arroz','Churrasco','Sorvete',NULL,0);
/*!40000 ALTER TABLE `alimentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cadastro`
--

DROP TABLE IF EXISTS `cadastro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cadastro` (
  `idcadastro` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `cpf` varchar(15) DEFAULT NULL,
  `telefone` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`idcadastro`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cadastro`
--

LOCK TABLES `cadastro` WRITE;
/*!40000 ALTER TABLE `cadastro` DISABLE KEYS */;
INSERT INTO `cadastro` VALUES (1,'Oscar','12345678900','988000919'),(2,'erivaldo','00964364336','981313163');
/*!40000 ALTER TABLE `cadastro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `frigobar`
--

DROP TABLE IF EXISTS `frigobar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `frigobar` (
  `idfrigobar` int NOT NULL AUTO_INCREMENT,
  `itens` varchar(20) DEFAULT NULL,
  `quantidade` int DEFAULT NULL,
  `preco_item` int DEFAULT NULL,
  PRIMARY KEY (`idfrigobar`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frigobar`
--

LOCK TABLES `frigobar` WRITE;
/*!40000 ALTER TABLE `frigobar` DISABLE KEYS */;
INSERT INTO `frigobar` VALUES (1,'água com gás',10,10),(2,'Haineke',2,70),(3,'Haineke GOLD',2,250),(4,'Refri',3,15);
/*!40000 ALTER TABLE `frigobar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lavanderia`
--

DROP TABLE IF EXISTS `lavanderia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lavanderia` (
  `idlavanderia` int NOT NULL AUTO_INCREMENT,
  `preco_passar` int DEFAULT NULL,
  `preco_lavar` int DEFAULT NULL,
  `quantidade` int DEFAULT NULL,
  PRIMARY KEY (`idlavanderia`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lavanderia`
--

LOCK TABLES `lavanderia` WRITE;
/*!40000 ALTER TABLE `lavanderia` DISABLE KEYS */;
INSERT INTO `lavanderia` VALUES (1,10,25,NULL),(2,10,25,NULL);
/*!40000 ALTER TABLE `lavanderia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `preco_alimentos`
--

DROP TABLE IF EXISTS `preco_alimentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `preco_alimentos` (
  `idpreco` int NOT NULL AUTO_INCREMENT,
  `cafe` int DEFAULT NULL,
  `almoco` int DEFAULT NULL,
  `jantar` int DEFAULT NULL,
  `lanche` int DEFAULT NULL,
  PRIMARY KEY (`idpreco`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `preco_alimentos`
--

LOCK TABLES `preco_alimentos` WRITE;
/*!40000 ALTER TABLE `preco_alimentos` DISABLE KEYS */;
INSERT INTO `preco_alimentos` VALUES (1,20,40,40,40);
/*!40000 ALTER TABLE `preco_alimentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quarto_casal`
--

DROP TABLE IF EXISTS `quarto_casal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quarto_casal` (
  `idquarto_casal` int NOT NULL AUTO_INCREMENT,
  `reservado` char(1) DEFAULT NULL,
  `frigobar` char(1) DEFAULT NULL,
  `nome_funcionario` varchar(20) DEFAULT NULL,
  `servico_quarto` char(1) DEFAULT NULL,
  `banheira` char(1) DEFAULT NULL,
  `wife` char(1) DEFAULT NULL,
  `cama_casal` char(1) DEFAULT NULL,
  `preco` int DEFAULT NULL,
  `tv` char(1) DEFAULT NULL,
  `idromassagem` char(1) DEFAULT NULL,
  `cozinha_americana` char(1) DEFAULT NULL,
  `cama_agua` char(1) DEFAULT NULL,
  `check_in` date DEFAULT NULL,
  `check_an` date DEFAULT NULL,
  PRIMARY KEY (`idquarto_casal`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quarto_casal`
--

LOCK TABLES `quarto_casal` WRITE;
/*!40000 ALTER TABLE `quarto_casal` DISABLE KEYS */;
INSERT INTO `quarto_casal` VALUES (1,'F','V','thiago','V','V','V','V',1000,'F','V','V',NULL,NULL,NULL),(2,'F','V','alana','V','V','V','V',1000,'F','V','V',NULL,NULL,NULL),(3,'F','V','adilson','V','V','V','V',1000,'F','V','V',NULL,NULL,NULL),(4,'F','V','abimael','V','V','V','V',1000,'F','V','V',NULL,NULL,NULL);
/*!40000 ALTER TABLE `quarto_casal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quarto_duplo`
--

DROP TABLE IF EXISTS `quarto_duplo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quarto_duplo` (
  `idquarto_duplo` int NOT NULL AUTO_INCREMENT,
  `reservado` char(1) DEFAULT NULL,
  `frigobar` char(1) DEFAULT NULL,
  `nome_funcionario` varchar(20) DEFAULT NULL,
  `servico_quarto` char(1) DEFAULT NULL,
  `banheira` char(1) DEFAULT NULL,
  `wife` char(1) DEFAULT NULL,
  `cama` int DEFAULT NULL,
  `preco` int DEFAULT NULL,
  `tv` char(1) DEFAULT NULL,
  `check_in` date DEFAULT NULL,
  `check_an` date DEFAULT NULL,
  PRIMARY KEY (`idquarto_duplo`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quarto_duplo`
--

LOCK TABLES `quarto_duplo` WRITE;
/*!40000 ALTER TABLE `quarto_duplo` DISABLE KEYS */;
INSERT INTO `quarto_duplo` VALUES (1,'F','V','julia','V','V','V',2,1000,'F',NULL,NULL),(2,'F','V','juliana','V','V','V',2,1000,'F',NULL,NULL),(3,'F','V','evely','V','V','V',2,1000,'F',NULL,NULL),(4,'F','V','kevely','V','V','V',2,1000,'F',NULL,NULL);
/*!40000 ALTER TABLE `quarto_duplo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quarto_luxo`
--

DROP TABLE IF EXISTS `quarto_luxo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quarto_luxo` (
  `idquarto_luxo` int NOT NULL AUTO_INCREMENT,
  `reservado` char(1) DEFAULT NULL,
  `frigobar` char(1) DEFAULT NULL,
  `nome_funcionario` varchar(20) DEFAULT NULL,
  `servico_quarto` char(1) DEFAULT NULL,
  `banheira` char(1) DEFAULT NULL,
  `wife` char(1) DEFAULT NULL,
  `suite` char(1) DEFAULT NULL,
  `preco` int DEFAULT NULL,
  `tv` char(1) DEFAULT NULL,
  `cama_bolha` char(1) DEFAULT NULL,
  `banheira_idromassagem` char(1) DEFAULT NULL,
  `potrona_idromassagem` int DEFAULT NULL,
  `cozinha_americana` char(1) DEFAULT NULL,
  `aquario_parede` char(1) DEFAULT NULL,
  `piscina` char(1) DEFAULT NULL,
  `mesa_jantar` char(1) DEFAULT NULL,
  `video_game_pro` char(1) DEFAULT NULL,
  `closet` char(1) DEFAULT NULL,
  `check_in` date DEFAULT NULL,
  `check_an` date DEFAULT NULL,
  PRIMARY KEY (`idquarto_luxo`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quarto_luxo`
--

LOCK TABLES `quarto_luxo` WRITE;
/*!40000 ALTER TABLE `quarto_luxo` DISABLE KEYS */;
INSERT INTO `quarto_luxo` VALUES (1,'F','V','gabriel','V','V','V','V',2000,'V','V','V',2,'V','V','V','V','V','V',NULL,NULL),(2,'F','V','corado','V','V','V','V',2000,'V','V','V',2,'V','V','V','V','V','V',NULL,NULL),(3,'F','V','chico','V','V','V','V',2000,'V','V','V',2,'V','V','V','V','V','V',NULL,NULL),(4,'F','V','alexantre','V','V','V','V',2000,'V','V','V',2,'V','V','V','V','V','V',NULL,NULL);
/*!40000 ALTER TABLE `quarto_luxo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quarto_simples`
--

DROP TABLE IF EXISTS `quarto_simples`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quarto_simples` (
  `idquarto_simples` int NOT NULL AUTO_INCREMENT,
  `reservado` char(1) DEFAULT NULL,
  `frigobar` char(1) DEFAULT NULL,
  `nome_funcionario` varchar(20) DEFAULT NULL,
  `servico_quarto` char(1) DEFAULT NULL,
  `banheira` char(1) DEFAULT NULL,
  `wife` char(1) DEFAULT NULL,
  `cama_simples` char(1) DEFAULT NULL,
  `preco` int DEFAULT NULL,
  `check_in` date DEFAULT NULL,
  `check_an` date DEFAULT NULL,
  PRIMARY KEY (`idquarto_simples`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quarto_simples`
--

LOCK TABLES `quarto_simples` WRITE;
/*!40000 ALTER TABLE `quarto_simples` DISABLE KEYS */;
INSERT INTO `quarto_simples` VALUES (1,'V','V','clara','V','V','V','V',800,'2022-09-19','2022-09-20'),(2,'F','V','maria','V','V','V','V',800,'2022-10-13','2022-10-15'),(3,'F','V','alan','V','V','V','V',800,'2022-02-23','2022-02-24'),(4,'F','V','ana','V','V','V','V',800,'2023-01-01','2023-01-02');
/*!40000 ALTER TABLE `quarto_simples` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-02  9:16:29

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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cadastro`
--

LOCK TABLES `cadastro` WRITE;
/*!40000 ALTER TABLE `cadastro` DISABLE KEYS */;
INSERT INTO `cadastro` VALUES (1,'Oscar dos Santos','12345678900','988000919'),(2,'Maria de Jesus','09876543211','988000001'),(3,'daten moura','123321123456','99988763211'),(4,'sol','345678121298','988112321');
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
  `categoria_quarto` varchar(10) DEFAULT NULL,
  `itens` varchar(20) DEFAULT NULL,
  `quantidade` int DEFAULT NULL,
  `preco_item` float DEFAULT NULL,
  `pk_quarto_simples` int DEFAULT NULL,
  `pk_quarto_casal` int DEFAULT NULL,
  `pk_quarto_duplo` int DEFAULT NULL,
  `pk_quarto_luxo` int DEFAULT NULL,
  PRIMARY KEY (`idfrigobar`),
  KEY `frigobar_quarto` (`pk_quarto_simples`),
  KEY `frigobar_quarto_duplo` (`pk_quarto_duplo`),
  KEY `frigobar_quarto_casal` (`pk_quarto_casal`),
  KEY `frigobar_quarto_luxo` (`pk_quarto_luxo`),
  CONSTRAINT `frigobar_quarto` FOREIGN KEY (`pk_quarto_simples`) REFERENCES `quarto_simples` (`idquarto_simples`),
  CONSTRAINT `frigobar_quarto_casal` FOREIGN KEY (`pk_quarto_casal`) REFERENCES `quarto_casal` (`idquarto_casal`),
  CONSTRAINT `frigobar_quarto_duplo` FOREIGN KEY (`pk_quarto_duplo`) REFERENCES `quarto_duplo` (`idquarto_duplo`),
  CONSTRAINT `frigobar_quarto_luxo` FOREIGN KEY (`pk_quarto_luxo`) REFERENCES `quarto_luxo` (`idquarto_luxo`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frigobar`
--

LOCK TABLES `frigobar` WRITE;
/*!40000 ALTER TABLE `frigobar` DISABLE KEYS */;
INSERT INTO `frigobar` VALUES (1,'Simples','água',8,5,NULL,NULL,NULL,NULL),(2,'Simples','refri',12,10,NULL,NULL,NULL,NULL),(3,'Duplo','água',15,5,NULL,NULL,NULL,NULL),(4,'Duplo','regri',15,10,NULL,NULL,NULL,NULL),(5,'Duplo','água com limao',6,15,NULL,NULL,NULL,NULL),(6,'Casal','água',10,5,NULL,NULL,NULL,NULL),(7,'Casal','refri guanara',10,10,NULL,NULL,NULL,NULL),(8,'Casal','serveja',20,18.5,NULL,NULL,NULL,NULL),(9,'Casal','água com limao',20,10,NULL,NULL,NULL,NULL),(10,'Luxo','água',20,5,NULL,NULL,NULL,NULL),(11,'Luxo','água com limao',20,10,NULL,NULL,NULL,NULL),(12,'Luxo','refri gold',20,20,NULL,NULL,NULL,NULL),(13,'Luxo','ice',20,50,NULL,NULL,NULL,NULL),(14,'Luxo','heineke',5,60,NULL,NULL,NULL,NULL);
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
  `preco_lavar_unidade` float DEFAULT NULL,
  `quantidade_lavar` int DEFAULT NULL,
  `preco_passar_unidade` float DEFAULT NULL,
  `quantidade_passar` int DEFAULT NULL,
  PRIMARY KEY (`idlavanderia`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lavanderia`
--

LOCK TABLES `lavanderia` WRITE;
/*!40000 ALTER TABLE `lavanderia` DISABLE KEYS */;
INSERT INTO `lavanderia` VALUES (1,0.8,NULL,1,NULL);
/*!40000 ALTER TABLE `lavanderia` ENABLE KEYS */;
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
  `preco` int DEFAULT NULL,
  `check_in` date DEFAULT NULL,
  `check_an` date DEFAULT NULL,
  `cpf_cliente` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`idquarto_casal`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quarto_casal`
--

LOCK TABLES `quarto_casal` WRITE;
/*!40000 ALTER TABLE `quarto_casal` DISABLE KEYS */;
INSERT INTO `quarto_casal` VALUES (1,'F',250,NULL,NULL,NULL),(2,'F',250,NULL,NULL,NULL),(3,'F',250,NULL,NULL,NULL),(4,'F',250,NULL,NULL,NULL),(5,'F',250,NULL,NULL,NULL);
/*!40000 ALTER TABLE `quarto_casal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quarto_cliente`
--

DROP TABLE IF EXISTS `quarto_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quarto_cliente` (
  `idquartocliente` int NOT NULL AUTO_INCREMENT,
  `pk_cliente` int DEFAULT NULL,
  `pkquarto_simples` int DEFAULT NULL,
  `pkquarto_duplo` int DEFAULT NULL,
  `pkquarto_casal` int DEFAULT NULL,
  `pkquarto_luxo` int DEFAULT NULL,
  PRIMARY KEY (`idquartocliente`),
  KEY `relacao_cliente` (`pk_cliente`),
  KEY `cliente_quarto_s` (`pkquarto_simples`),
  KEY `cliente_quarto_d` (`pkquarto_duplo`),
  KEY `cliente_quarto_c` (`pkquarto_casal`),
  KEY `cliente_quarto_l` (`pkquarto_luxo`),
  CONSTRAINT `cliente_quarto_c` FOREIGN KEY (`pkquarto_casal`) REFERENCES `quarto_casal` (`idquarto_casal`),
  CONSTRAINT `cliente_quarto_d` FOREIGN KEY (`pkquarto_duplo`) REFERENCES `quarto_duplo` (`idquarto_duplo`),
  CONSTRAINT `cliente_quarto_l` FOREIGN KEY (`pkquarto_luxo`) REFERENCES `quarto_luxo` (`idquarto_luxo`),
  CONSTRAINT `cliente_quarto_s` FOREIGN KEY (`pkquarto_simples`) REFERENCES `quarto_simples` (`idquarto_simples`),
  CONSTRAINT `relacao_cliente` FOREIGN KEY (`pk_cliente`) REFERENCES `cadastro` (`idcadastro`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quarto_cliente`
--

LOCK TABLES `quarto_cliente` WRITE;
/*!40000 ALTER TABLE `quarto_cliente` DISABLE KEYS */;
/*!40000 ALTER TABLE `quarto_cliente` ENABLE KEYS */;
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
  `preco` int DEFAULT NULL,
  `check_in` date DEFAULT NULL,
  `check_an` date DEFAULT NULL,
  `cpf_cliente` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`idquarto_duplo`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quarto_duplo`
--

LOCK TABLES `quarto_duplo` WRITE;
/*!40000 ALTER TABLE `quarto_duplo` DISABLE KEYS */;
INSERT INTO `quarto_duplo` VALUES (1,'F',150,NULL,NULL,NULL),(2,'F',150,NULL,NULL,NULL),(3,'F',150,NULL,NULL,NULL),(4,'F',150,NULL,NULL,NULL),(5,'F',150,NULL,NULL,NULL);
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
  `preco` int DEFAULT NULL,
  `check_in` date DEFAULT NULL,
  `check_an` date DEFAULT NULL,
  `cpf_cliente` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`idquarto_luxo`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quarto_luxo`
--

LOCK TABLES `quarto_luxo` WRITE;
/*!40000 ALTER TABLE `quarto_luxo` DISABLE KEYS */;
INSERT INTO `quarto_luxo` VALUES (1,'F',500,NULL,NULL,NULL),(2,'F',500,NULL,NULL,NULL),(3,'F',500,NULL,NULL,NULL),(4,'F',500,NULL,NULL,NULL),(5,'F',500,NULL,NULL,NULL);
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
  `preco` float DEFAULT NULL,
  `check_in` date DEFAULT NULL,
  `check_an` date DEFAULT NULL,
  `cpf_cliente` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`idquarto_simples`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quarto_simples`
--

LOCK TABLES `quarto_simples` WRITE;
/*!40000 ALTER TABLE `quarto_simples` DISABLE KEYS */;
INSERT INTO `quarto_simples` VALUES (1,'F',100,NULL,NULL,NULL),(2,'F',100,NULL,NULL,NULL),(3,'F',100,NULL,NULL,NULL),(4,'F',100,NULL,NULL,NULL),(5,'F',100,NULL,NULL,NULL);
/*!40000 ALTER TABLE `quarto_simples` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servico_quarto`
--

DROP TABLE IF EXISTS `servico_quarto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servico_quarto` (
  `idservico_quarto` int NOT NULL AUTO_INCREMENT,
  `quarto_responsavel` varchar(15) DEFAULT NULL,
  `nome_funcionario` varchar(50) DEFAULT NULL,
  `pk_quarto_simples_sq` int DEFAULT NULL,
  `pk_quarto_duplo_sq` int DEFAULT NULL,
  `pk_quarto_casal_sq` int DEFAULT NULL,
  `pk_quarto_luxo_sq` int DEFAULT NULL,
  `pk_lavanderia` int DEFAULT NULL,
  `pk_alimentos` int DEFAULT NULL,
  PRIMARY KEY (`idservico_quarto`),
  KEY `serv_quart_simples` (`pk_quarto_simples_sq`),
  KEY `serv_quart_duplo` (`pk_quarto_duplo_sq`),
  KEY `serv_quart_casal` (`pk_quarto_casal_sq`),
  KEY `serv_quart_luxo` (`pk_quarto_luxo_sq`),
  KEY `quarto_lavanderia` (`pk_lavanderia`),
  KEY `quarto_alimentos` (`pk_alimentos`),
  CONSTRAINT `quarto_lavanderia` FOREIGN KEY (`pk_lavanderia`) REFERENCES `lavanderia` (`idlavanderia`),
  CONSTRAINT `serv_quart_casal` FOREIGN KEY (`pk_quarto_casal_sq`) REFERENCES `quarto_casal` (`idquarto_casal`),
  CONSTRAINT `serv_quart_duplo` FOREIGN KEY (`pk_quarto_duplo_sq`) REFERENCES `quarto_duplo` (`idquarto_duplo`),
  CONSTRAINT `serv_quart_luxo` FOREIGN KEY (`pk_quarto_luxo_sq`) REFERENCES `quarto_luxo` (`idquarto_luxo`),
  CONSTRAINT `serv_quart_simples` FOREIGN KEY (`pk_quarto_simples_sq`) REFERENCES `quarto_simples` (`idquarto_simples`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servico_quarto`
--

LOCK TABLES `servico_quarto` WRITE;
/*!40000 ALTER TABLE `servico_quarto` DISABLE KEYS */;
INSERT INTO `servico_quarto` VALUES (1,'Simples','Pedro',NULL,NULL,NULL,NULL,NULL,NULL),(2,'duplo','Thiago',NULL,NULL,NULL,NULL,NULL,NULL),(3,'Casal','Maria',NULL,NULL,NULL,NULL,NULL,NULL),(4,'Luxo','Monica',NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `servico_quarto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-03 11:51:02

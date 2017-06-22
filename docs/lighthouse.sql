-- --------------------------------------------------------
-- 主機:                           127.0.0.1
-- 服務器版本:                        10.2.6-MariaDB - mariadb.org binary distribution
-- 服務器操作系統:                      Win32
-- HeidiSQL 版本:                  9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 導出 lighthouse 的資料庫結構
CREATE DATABASE IF NOT EXISTS `lighthouse` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `lighthouse`;

-- 導出  表 lighthouse.location 結構
CREATE TABLE IF NOT EXISTS `location` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `geo_code` varchar(50) DEFAULT NULL,
  `lat` float DEFAULT NULL,
  `lon` float DEFAULT NULL,
  PRIMARY KEY (`location_id`),
  UNIQUE KEY `house_address` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- 資料導出被取消選擇。
-- 導出  表 lighthouse.parameter 結構
CREATE TABLE IF NOT EXISTS `parameter` (
  `parameter_id` int(11) NOT NULL AUTO_INCREMENT,
  `time_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `value` varchar(50) DEFAULT NULL,
  `unit` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`parameter_id`),
  KEY `FK_parameter_time` (`time_id`),
  CONSTRAINT `FK_parameter_time` FOREIGN KEY (`time_id`) REFERENCES `time` (`time_id`)
) ENGINE=InnoDB AUTO_INCREMENT=261 DEFAULT CHARSET=utf8;

-- 資料導出被取消選擇。
-- 導出  表 lighthouse.task 結構
CREATE TABLE IF NOT EXISTS `task` (
  `task_id` int(11) NOT NULL AUTO_INCREMENT,
  `crawl_time` datetime NOT NULL,
  `description` varchar(50) NOT NULL,
  PRIMARY KEY (`task_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- 資料導出被取消選擇。
-- 導出  表 lighthouse.time 結構
CREATE TABLE IF NOT EXISTS `time` (
  `time_id` int(11) NOT NULL AUTO_INCREMENT,
  `task_id` int(11) NOT NULL,
  `location_id` int(11) NOT NULL,
  `weather_element_id` int(11) NOT NULL,
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `data_time` datetime DEFAULT NULL,
  `element_value` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`time_id`),
  KEY `FK_time_location` (`location_id`),
  KEY `FK_time_weather_element` (`weather_element_id`),
  KEY `FK_time_task` (`task_id`),
  CONSTRAINT `FK_time_location` FOREIGN KEY (`location_id`) REFERENCES `location` (`location_id`),
  CONSTRAINT `FK_time_task` FOREIGN KEY (`task_id`) REFERENCES `task` (`task_id`),
  CONSTRAINT `FK_time_weather_element` FOREIGN KEY (`weather_element_id`) REFERENCES `weather_element` (`weather_element_id`)
) ENGINE=InnoDB AUTO_INCREMENT=420 DEFAULT CHARSET=utf8;

-- 資料導出被取消選擇。
-- 導出  表 lighthouse.weather_element 結構
CREATE TABLE IF NOT EXISTS `weather_element` (
  `weather_element_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `measure` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`weather_element_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- 資料導出被取消選擇。
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

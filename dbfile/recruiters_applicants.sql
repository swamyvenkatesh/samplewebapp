-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 22, 2016 at 04:38 PM
-- Server version: 5.5.49-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `Recruiters`
--

-- --------------------------------------------------------

--
-- Table structure for table `recruiters_applicants`
--

CREATE TABLE IF NOT EXISTS `recruiters_applicants` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `resume` tinyint(1) NOT NULL,
  `candidate_name` varchar(250) NOT NULL,
  `mobile` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `experience` decimal(3,2) DEFAULT NULL,
  `current_location` varchar(100) NOT NULL,
  `preferred_location` varchar(100) NOT NULL,
  `expected_ctc` decimal(3,2) DEFAULT NULL,
  `current_employer` varchar(150) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `skills` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=105 ;

--
-- Dumping data for table `recruiters_applicants`
--

INSERT INTO `recruiters_applicants` (`id`, `resume`, `candidate_name`, `mobile`, `email`, `experience`, `current_location`, `preferred_location`, `expected_ctc`, `current_employer`, `designation`, `skills`) VALUES
(101, 0, 'Suraj Kumar', 1234567890, 'suraj@gmail.com', 3.20, 'Mumbai', 'Delhi', 6.00, 'Tata Consultancy Services (TCS)', 'SystemEngineer', 'Had, Hadoop (MapReduce,Hive,Oozie,Sqoop etc), ORACLE,NETEZZA'),
(102, 1, 'Ram Narayan', 1234567891, 'raman@gmail.com', 2.50, 'Mumbai', 'Chennai', 4.80, 'CELLOS INDIA', 'Associate', 'Mainframes, JCL, Cobol,DB2,CICS,VSAM, WebSphere, HADOOP, HBASE, HIVE, zookeeper, Sqoop, MapReduce'),
(103, 1, 'Ramesh', 1234567891, 'ramesh@gmail.com', 3.60, 'kolkata', 'Bangalore', 4.80, 'CELLOS INDIA', 'Associate', 'Mainframes, JCL, Cobol,DB2,CICS,VSAM'),
(104, 1, 'hemanth', 1234567892, 'hemanth@gmail.com', 9.99, 'Gurgaon', 'Delhi', 9.99, 'CELLOS INDIA', 'Solution Architect/Technical Account Manager/TPM\r\n', 'CEM,Presales,Technical Account Management, Solution Architect, Presales, LAN,WAN,VLAN, PCRF, PCEF,IP Core Design, MPBN, MPLS, VPN, MGW, MSC, SGSN,GGSN,HLR, IP Routing, Switching, WLAN, HADOOP, 802 11A, Router, L3, ISIS, OSPF, MapReduce, HDFS\r\n');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

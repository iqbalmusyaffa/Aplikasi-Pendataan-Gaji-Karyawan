-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 24, 2022 at 09:58 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gaji`
--

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `confim` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`, `confim`) VALUES
('admin', 'admina', ''),
('admin', 'admina', ''),
('iqbal', 'iqbal', ''),
('admin', 'admin', ''),
('yusa', 'yusa', 'yusa'),
('halo', 'halo', 'halo'),
('123', '123', '123'),
('aka', 'aka', 'aka'),
('567', '567', '567'),
('fani', 'fani', 'fani'),
('345', '345', '345'),
('444', '444', '444'),
('qqq', 'qqq', 'qqq'),
('777', '777', '777'),
('000', '000', '000'),
('190', '190', '190'),
('', '', ''),
('gagal', 'gagal', 'gagal'),
('', '', ''),
('', '', ''),
('xxx', 'xxx', 'xxx'),
('tes', 'tes', 'tes'),
('', '', ''),
('fetchall', 'fetchall', 'fetchall'),
('arif', 'arif', 'arif'),
('i', 'i', 'i'),
('4646', '4646', '4646');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_gaji`
--

CREATE TABLE `tbl_gaji` (
  `namakaryawan` varchar(255) NOT NULL,
  `jabatan` varchar(255) NOT NULL,
  `gajipokok` int(255) NOT NULL,
  `thnmasuk` int(255) NOT NULL,
  `statuskerja` varchar(255) NOT NULL,
  `thhbskontrak` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tbl_gaji`
--

INSERT INTO `tbl_gaji` (`namakaryawan`, `jabatan`, `gajipokok`, `thnmasuk`, `statuskerja`, `thhbskontrak`) VALUES
('yusa', 'manager', 200000, 2022, 'masih bekerja', 2028);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

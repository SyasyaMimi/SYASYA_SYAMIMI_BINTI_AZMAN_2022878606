-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 01:07 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `hotel_booking`
--

CREATE TABLE `hotel_booking` (
  `Type_Of_Package` char(9) NOT NULL,
  `Packs` int(2) NOT NULL,
  `Customer_Name` char(30) NOT NULL,
  `contact_number` varchar(11) NOT NULL,
  `Ic_Number` varchar(12) NOT NULL,
  `Total_Price` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hotel_booking`
--

INSERT INTO `hotel_booking` (`Type_Of_Package`, `Packs`, `Customer_Name`, `contact_number`, `Ic_Number`, `Total_Price`) VALUES
('Package B', 3, 'Qistina Batrisya Binti Azman', '01270912097', '040210030872', 1500),
('Package C', 7, 'Rumaissa Adnin Binti Rusli', '01128868179', '030530011163', 5250),
('Package A', 5, 'Norhayati Binti Abdullah', '01456789110', '730906035059', 3250),
('Package B', 2, 'Muhammad Dani Bin Ahmad Nizam', '0102347651', '951029026051', 1000),
('Package A', 4, 'Nur Arisya Binti Talib', '0122347651', '990614035058', 2600),
('Package B', 3, 'Alif Daniel Bin Rasyid', '0166327678', '010125034323', 1500);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

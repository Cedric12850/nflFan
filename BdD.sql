-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 25, 2024 at 04:01 PM
-- Server version: 8.0.30
-- PHP Version: 8.3.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nflfan`
--

-- --------------------------------------------------------

--
-- Table structure for table `team_teams`
--

CREATE TABLE `team_teams` (
  `id` bigint NOT NULL,
  `name` varchar(60) NOT NULL,
  `town` varchar(60) NOT NULL,
  `thumbnail` varchar(100) DEFAULT NULL,
  `founded` date NOT NULL,
  `stadium` varchar(60) DEFAULT NULL,
  `division_id` bigint DEFAULT NULL,
  `colorOne` varchar(15) DEFAULT NULL,
  `colorTwo` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `team_teams`
--

INSERT INTO `team_teams` (`id`, `name`, `town`, `thumbnail`, `founded`, `stadium`, `division_id`, `colorOne`, `colorTwo`) VALUES
(1, 'Chiefs', 'Kansas City', 'logo/KC.webp', '1960-01-01', 'Arrowhead Stadium', 1, '#E31837', '#FFB81C'),
(2, 'Broncos', 'Denver', 'logo/Broncos.webp', '1960-01-01', 'Empower Field at Mile high', 1, '#FB4F14', '#002244'),
(3, 'Raiders', 'Los Angeles', 'logo/Raiders.webp', '1960-01-01', 'Allegiant Stadium', 1, '#000000', '#A5ACAF'),
(4, 'Chargers', 'Los Angeles', 'logo/Chargers.webp', '1960-01-01', 'Sofi Stadium', 1, '#0080C6', '#FFC20E'),
(5, 'Bills', 'Buffalo', 'logo/Bills.webp', '1960-01-01', 'Highmark Stadium', 2, '#00338D', '#C60C30'),
(6, 'Dolphins', 'Miami', 'logo/Dolphins.webp', '1966-01-01', 'Hard Rock Stadium', 2, '#008E97', '#FC4C02'),
(7, 'Patriots', 'New England', 'logo/Patriots.webp', '1960-01-01', 'Gillette Stadium', 2, '#002244', '#C60C30'),
(8, 'Jets', 'New York', 'logo/Jets.webp', '1960-01-01', 'MetLife Stadium', 2, '#125740', '#000000'),
(9, 'Ravens', 'Baltimore', 'logo/Ravens.webp', '1996-01-01', 'M&T Bank Stadium', 3, '#241773', '#000000'),
(10, 'Bengals', 'Cincinnati', 'logo/Bengals.webp', '1968-01-01', 'Paycor Stadium', 3, '#fb4f14', '#000000'),
(11, 'Browns', 'Cleveland', 'logo/Browns.webp', '1946-01-01', 'Huntington Stadium', 3, '#311D00', '#ff3c00'),
(12, 'Steelers', 'Pittsburgh', 'logo/Steelers.webp', '1933-01-01', 'Acrisure Stadium', 3, '#FFB612', '#101820'),
(13, 'Texans', 'Houston', 'logo/Texans.webp', '2002-01-01', 'NRG Stadium', 4, '#03202f', '#A71930'),
(14, 'Colts', 'Indianapolis', 'logo/Colts.webp', '1953-01-01', 'Lucas Oil Stadium', 4, '#002C5F', '#A2AAAD'),
(15, 'Jaguars', 'Jacksonville', 'logo/Jaguars.webp', '1995-01-01', 'EverBank Stadium', 4, '#101820', '#D7A22A'),
(16, 'Titans', 'Tennessee', 'logo/Titans.webp', '1960-01-01', 'Nissan Stadium', 4, '#0C2340', '#4B92DB'),
(17, 'Cowboys', 'Dallas', 'logo/Cowboys.webp', '1960-01-01', 'AT&T Stadium', 8, '#003594', '#869397'),
(18, 'Giants', 'New York', 'logo/Giants.webp', '1925-01-01', 'MetLife Stadium', 8, '#0B2265', '#a71930'),
(19, 'Eagles', 'Philadelphie', 'logo/Eagles.webp', '1933-01-01', 'Lincoln Financial Field', 8, '#004C54', '#A5ACAF'),
(20, 'Commanders', 'Washington', 'logo/Commanders.webp', '1932-01-01', 'Northwest Stadium', 8, '#5A1414', '#FFB612'),
(21, 'Bears', 'Chicago', 'logo/Bears.webp', '1920-01-01', 'Soldier Stadium', 5, '#0B162A', '#c83803'),
(22, 'Lions', 'Detroit', 'logo/Lions.webp', '1930-01-01', 'Ford Field', 5, '#0076b6', '#B0B7BC'),
(23, 'Packers', 'Green Bay', 'logo/Packers.webp', '1921-01-01', 'Lambeau Stadium', 5, '#203731', '#FFB612'),
(24, 'Vickings', 'Minnesota', 'logo/Vickings.webp', '1961-01-01', 'US Bank Stadium', 5, '#4F2683', '#FFC62F'),
(25, 'Falcons', 'Atlanta', 'logo/Falcons.webp', '1966-01-01', 'Mercedes_Benz Stadium', 6, '#a71930', '#000000'),
(26, 'Panthers', 'Carolina', 'logo/Panthers.webp', '1995-01-01', 'Bank of America Stadium', 6, '#0085CA', '#101820'),
(27, 'Saints', 'New Orleans', 'logo/Saints.webp', '1967-01-01', 'Ceasars Suerdome', 6, '#D3BC8D', '#101820'),
(28, 'Buccaneers', 'Tampa Bay', 'logo/Buccaneers.webp', '1976-01-01', 'Raymond James Stadium', 6, '#D50A0A', '#FF7900'),
(29, 'Cardinals', 'Arizona', 'logo/Cardinals.webp', '1920-01-01', 'State Farm Stadium', 7, '#97233F', '#000000'),
(30, 'Rams', 'Los Angeles', 'logo/Rams.webp', '1937-01-01', 'SoFi Stadium', 7, '#003594', '#ffa300'),
(31, '49ers', 'San Francisco', 'logo/49ers.webp', '1946-01-01', 'Levi\'s® Stadium', 7, '#AA0000', '#B3995D'),
(32, 'Seahawks', 'Seattle', 'logo/Seahawks.webp', '1976-01-01', 'Lumen Fields', 7, '#002244', '#69BE28');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `team_teams`
--
ALTER TABLE `team_teams`
  ADD PRIMARY KEY (`id`),
  ADD KEY `team_teams_division_id_98ac8356_fk_team_divisions_id` (`division_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `team_teams`
--
ALTER TABLE `team_teams`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `team_teams`
--
ALTER TABLE `team_teams`
  ADD CONSTRAINT `team_teams_division_id_98ac8356_fk_team_divisions_id` FOREIGN KEY (`division_id`) REFERENCES `team_divisions` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

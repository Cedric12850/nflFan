-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 09, 2024 at 03:46 PM
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
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add conferences', 7, 'add_conferences'),
(26, 'Can change conferences', 7, 'change_conferences'),
(27, 'Can delete conferences', 7, 'delete_conferences'),
(28, 'Can view conferences', 7, 'view_conferences'),
(29, 'Can add divisions', 8, 'add_divisions'),
(30, 'Can change divisions', 8, 'change_divisions'),
(31, 'Can delete divisions', 8, 'delete_divisions'),
(32, 'Can view divisions', 8, 'view_divisions'),
(33, 'Can add teams', 9, 'add_teams'),
(34, 'Can change teams', 9, 'change_teams'),
(35, 'Can delete teams', 9, 'delete_teams'),
(36, 'Can view teams', 9, 'view_teams'),
(37, 'Can add superbowls', 10, 'add_superbowls'),
(38, 'Can change superbowls', 10, 'change_superbowls'),
(39, 'Can delete superbowls', 10, 'delete_superbowls'),
(40, 'Can view superbowls', 10, 'view_superbowls'),
(41, 'Can add coachs', 11, 'add_coachs'),
(42, 'Can change coachs', 11, 'change_coachs'),
(43, 'Can delete coachs', 11, 'delete_coachs'),
(44, 'Can view coachs', 11, 'view_coachs'),
(45, 'Can add player_position', 12, 'add_player_position'),
(46, 'Can change player_position', 12, 'change_player_position'),
(47, 'Can delete player_position', 12, 'delete_player_position'),
(48, 'Can view player_position', 12, 'view_player_position'),
(49, 'Can add p layers', 13, 'add_players'),
(50, 'Can change p layers', 13, 'change_players'),
(51, 'Can delete p layers', 13, 'delete_players'),
(52, 'Can view p layers', 13, 'view_players'),
(53, 'Can add stadium', 14, 'add_stadium'),
(54, 'Can change stadium', 14, 'change_stadium'),
(55, 'Can delete stadium', 14, 'delete_stadium'),
(56, 'Can view stadium', 14, 'view_stadium'),
(57, 'Can add play game', 15, 'add_playgame'),
(58, 'Can change play game', 15, 'change_playgame'),
(59, 'Can delete play game', 15, 'delete_playgame'),
(60, 'Can view play game', 15, 'view_playgame'),
(61, 'Can add play game', 16, 'add_playgame'),
(62, 'Can change play game', 16, 'change_playgame'),
(63, 'Can delete play game', 16, 'delete_playgame'),
(64, 'Can view play game', 16, 'view_playgame'),
(65, 'Can add season', 17, 'add_season'),
(66, 'Can change season', 17, 'change_season'),
(67, 'Can delete season', 17, 'delete_season'),
(68, 'Can view season', 17, 'view_season'),
(69, 'Can add superbowls', 18, 'add_superbowls'),
(70, 'Can change superbowls', 18, 'change_superbowls'),
(71, 'Can delete superbowls', 18, 'delete_superbowls'),
(72, 'Can view superbowls', 18, 'view_superbowls'),
(73, 'Can add week', 19, 'add_week'),
(74, 'Can change week', 19, 'change_week'),
(75, 'Can delete week', 19, 'delete_week'),
(76, 'Can view week', 19, 'view_week');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$870000$d1dugXgZah5wyLI7cIxk6E$RFMT1RBZow9oif3G5Oxl1hY8inQC4/7f5++lkdWjIz0=', '2024-12-02 10:09:54.774950', 1, 'SuperAdmin', '', '', 'cedric.deswarte81@gmail.com', 1, 1, '2024-12-02 10:09:33.967165');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-12-02 10:18:40.966331', '1', 'Quarterback (QB)', 1, '[{\"added\": {}}]', 12, 1),
(2, '2024-12-02 10:18:53.700871', '2', 'Running back (RB)', 1, '[{\"added\": {}}]', 12, 1),
(3, '2024-12-02 10:19:04.876016', '3', 'Halfback (HB)', 1, '[{\"added\": {}}]', 12, 1),
(4, '2024-12-02 10:19:16.457749', '4', 'Fullback (FB)', 1, '[{\"added\": {}}]', 12, 1),
(5, '2024-12-02 10:19:27.371627', '5', 'Wide receiver (WR)', 1, '[{\"added\": {}}]', 12, 1),
(6, '2024-12-02 10:19:38.116610', '6', 'Tight-end (TE)', 1, '[{\"added\": {}}]', 12, 1),
(7, '2024-12-02 10:19:52.544202', '7', 'Offensive Linemen (OL)', 1, '[{\"added\": {}}]', 12, 1),
(8, '2024-12-02 10:20:02.212161', '8', 'Centre (C)', 1, '[{\"added\": {}}]', 12, 1),
(9, '2024-12-02 10:20:13.820281', '9', 'Offensive guard (OG)', 1, '[{\"added\": {}}]', 12, 1),
(10, '2024-12-02 10:20:25.671091', '10', 'Offensive tackle (OT)', 1, '[{\"added\": {}}]', 12, 1),
(11, '2024-12-02 10:20:37.017199', '11', 'Defensive linemen (DL)', 1, '[{\"added\": {}}]', 12, 1),
(12, '2024-12-02 10:20:53.206402', '12', 'Defensive tackle (DT)', 1, '[{\"added\": {}}]', 12, 1),
(13, '2024-12-02 10:21:02.425509', '13', 'Nose tackle (NT)', 1, '[{\"added\": {}}]', 12, 1),
(14, '2024-12-02 10:21:13.442484', '14', 'Defensive end (DE)', 1, '[{\"added\": {}}]', 12, 1),
(15, '2024-12-02 10:21:25.616415', '15', 'Linebacker (LB)', 1, '[{\"added\": {}}]', 12, 1),
(16, '2024-12-02 10:21:40.051771', '16', 'Defensive back (DB)', 1, '[{\"added\": {}}]', 12, 1),
(17, '2024-12-02 10:21:49.405456', '17', 'Cornerback (CB)', 1, '[{\"added\": {}}]', 12, 1),
(18, '2024-12-02 10:21:59.224464', '18', 'Safety (S)', 1, '[{\"added\": {}}]', 12, 1),
(19, '2024-12-02 10:22:11.682256', '19', 'Free safety (FS)', 1, '[{\"added\": {}}]', 12, 1),
(20, '2024-12-02 10:22:20.428597', '20', 'Strong safety (SS)', 1, '[{\"added\": {}}]', 12, 1),
(21, '2024-12-02 10:22:32.019278', '21', 'Kicker (K)', 1, '[{\"added\": {}}]', 12, 1),
(22, '2024-12-02 10:22:42.214947', '22', 'Punter (P)', 1, '[{\"added\": {}}]', 12, 1),
(23, '2024-12-02 10:22:52.661770', '23', 'Kick returner (KS)', 1, '[{\"added\": {}}]', 12, 1),
(24, '2024-12-02 10:23:11.460173', '24', 'Kick punter (KP)', 1, '[{\"added\": {}}]', 12, 1),
(25, '2024-12-02 10:23:24.529220', '25', 'Long snapper (LS)', 1, '[{\"added\": {}}]', 12, 1),
(26, '2024-12-02 10:25:52.644707', '1', 'Mahomes Patrick', 1, '[{\"added\": {}}]', 13, 1),
(27, '2024-12-02 10:27:41.005217', '2', 'Hill Tyreek', 1, '[{\"added\": {}}]', 13, 1),
(28, '2024-12-02 10:32:05.025442', '3', 'Achane De\'Von', 1, '[{\"added\": {}}]', 13, 1),
(29, '2024-12-02 10:34:54.337640', '4', 'Barkley Saquon', 1, '[{\"added\": {}}]', 13, 1),
(30, '2024-12-02 10:36:06.126212', '5', 'Jackson Lamar', 1, '[{\"added\": {}}]', 13, 1),
(31, '2024-12-02 10:36:51.180456', '6', 'Burrow Joe', 1, '[{\"added\": {}}]', 13, 1),
(32, '2024-12-02 10:38:20.106432', '7', 'Rodgers Aaron', 1, '[{\"added\": {}}]', 13, 1),
(33, '2024-12-02 10:39:11.182134', '8', 'Daniels Jayden', 1, '[{\"added\": {}}]', 13, 1),
(34, '2024-12-02 10:40:07.155266', '6', 'Burrow Joe', 2, '[{\"changed\": {\"fields\": [\"Thumbnail\"]}}]', 13, 1),
(35, '2024-12-02 11:06:06.974095', '1', 'Arraowhead Stadium', 1, '[{\"added\": {}}]', 14, 1),
(36, '2024-12-02 11:07:32.874155', '1', 'Arraowhead Stadium', 2, '[{\"changed\": {\"fields\": [\"Thumbnail\"]}}]', 14, 1),
(37, '2024-12-02 11:07:47.127024', '1', 'Chiefs', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(38, '2024-12-02 11:57:17.739400', '1', 'Mahomes Patrick', 2, '[{\"changed\": {\"fields\": [\"Number\"]}}]', 13, 1),
(39, '2024-12-02 11:57:37.862940', '7', 'Rodgers Aaron', 2, '[{\"changed\": {\"fields\": [\"Number\"]}}]', 13, 1),
(40, '2024-12-02 11:57:45.135529', '8', 'Daniels Jayden', 2, '[{\"changed\": {\"fields\": [\"Number\"]}}]', 13, 1),
(41, '2024-12-02 11:57:59.397278', '6', 'Burrow Joe', 2, '[{\"changed\": {\"fields\": [\"Number\"]}}]', 13, 1),
(42, '2024-12-02 11:58:13.655542', '5', 'Jackson Lamar', 2, '[{\"changed\": {\"fields\": [\"Number\"]}}]', 13, 1),
(43, '2024-12-02 11:58:27.681321', '4', 'Barkley Saquon', 2, '[{\"changed\": {\"fields\": [\"Number\"]}}]', 13, 1),
(44, '2024-12-02 11:58:40.161422', '3', 'Achane De\'Von', 2, '[{\"changed\": {\"fields\": [\"Number\"]}}]', 13, 1),
(45, '2024-12-02 11:58:52.630699', '2', 'Hill Tyreek', 2, '[{\"changed\": {\"fields\": [\"Number\"]}}]', 13, 1),
(46, '2024-12-02 12:03:41.376946', '2', 'AT&T Stadium', 1, '[{\"added\": {}}]', 14, 1),
(47, '2024-12-02 12:04:21.564400', '17', 'Cowboys', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(48, '2024-12-02 12:06:10.085879', '3', 'Bank of America Stadium', 1, '[{\"added\": {}}]', 14, 1),
(49, '2024-12-02 12:06:18.371326', '26', 'Panthers', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(50, '2024-12-02 12:10:05.042015', '4', 'Empower Field at Mile High', 1, '[{\"added\": {}}]', 14, 1),
(51, '2024-12-02 12:12:54.154876', '3', 'Bank of America Stadium', 2, '[{\"changed\": {\"fields\": [\"Thumbnail\"]}}]', 14, 1),
(52, '2024-12-02 12:14:28.669036', '5', 'Lumen Fields', 1, '[{\"added\": {}}]', 14, 1),
(53, '2024-12-02 12:16:09.286517', '4', 'Empower Field at Mile High', 2, '[{\"changed\": {\"fields\": [\"Capacity\", \"Creation\"]}}]', 14, 1),
(54, '2024-12-02 12:19:52.034716', '4', 'Empower Field at Mile High', 2, '[{\"changed\": {\"fields\": [\"Town\", \"State\"]}}]', 14, 1),
(55, '2024-12-02 12:20:04.466477', '3', 'Bank of America Stadium', 2, '[{\"changed\": {\"fields\": [\"Town\", \"State\"]}}]', 14, 1),
(56, '2024-12-02 12:21:22.324328', '5', 'Lumen Fields', 2, '[{\"changed\": {\"fields\": [\"State\"]}}]', 14, 1),
(57, '2024-12-02 12:21:33.156717', '2', 'AT&T Stadium', 2, '[{\"changed\": {\"fields\": [\"State\"]}}]', 14, 1),
(58, '2024-12-02 12:21:43.242521', '1', 'Arraowhead Stadium', 2, '[{\"changed\": {\"fields\": [\"State\"]}}]', 14, 1),
(59, '2024-12-02 12:24:06.886644', '6', 'Northwest Stadium', 1, '[{\"added\": {}}]', 14, 1),
(60, '2024-12-02 12:24:52.657672', '3', 'Bank of America Stadium', 2, '[{\"changed\": {\"fields\": [\"Creation\"]}}]', 14, 1),
(61, '2024-12-02 12:25:19.209974', '2', 'AT&T Stadium', 2, '[{\"changed\": {\"fields\": [\"Creation\"]}}]', 14, 1),
(62, '2024-12-02 12:25:39.888625', '1', 'Arraowhead Stadium', 2, '[{\"changed\": {\"fields\": [\"Creation\"]}}]', 14, 1),
(63, '2024-12-02 12:27:31.647276', '7', 'Huntington Bank Field', 1, '[{\"added\": {}}]', 14, 1),
(64, '2024-12-02 12:29:03.898491', '8', 'Ford Field', 1, '[{\"added\": {}}]', 14, 1),
(65, '2024-12-02 12:30:30.250919', '9', 'Gilette Stadium', 1, '[{\"added\": {}}]', 14, 1),
(66, '2024-12-02 12:30:39.349462', '7', 'Huntington Bank Field', 2, '[{\"changed\": {\"fields\": [\"Thumbnail\"]}}]', 14, 1),
(67, '2024-12-02 12:32:02.850172', '10', 'Hard Rock Stadium', 1, '[{\"added\": {}}]', 14, 1),
(68, '2024-12-02 12:33:46.532881', '11', 'Acrisure Stadium', 1, '[{\"added\": {}}]', 14, 1),
(69, '2024-12-02 12:35:09.666260', '12', 'Lambeau Field', 1, '[{\"added\": {}}]', 14, 1),
(70, '2024-12-02 12:36:30.291766', '13', 'Levi\'s Stadium', 1, '[{\"added\": {}}]', 14, 1),
(71, '2024-12-02 12:37:45.131476', '14', 'Lincoln Financial Field', 1, '[{\"added\": {}}]', 14, 1),
(72, '2024-12-02 12:38:48.630642', '15', 'SoFi Stadium', 1, '[{\"added\": {}}]', 14, 1),
(73, '2024-12-02 12:40:01.288599', '16', 'Lucas Oil Stadium', 1, '[{\"added\": {}}]', 14, 1),
(74, '2024-12-02 12:41:16.040420', '17', 'M&T Bank Stadium', 1, '[{\"added\": {}}]', 14, 1),
(75, '2024-12-02 12:42:51.082698', '18', 'Mercedes-Benz Stadium', 1, '[{\"added\": {}}]', 14, 1),
(76, '2024-12-02 12:44:18.281533', '19', 'MetLife Stadium', 1, '[{\"added\": {}}]', 14, 1),
(77, '2024-12-02 12:48:18.632810', '20', 'Highmark Stadium', 1, '[{\"added\": {}}]', 14, 1),
(78, '2024-12-02 12:50:37.834710', '21', 'Nissan Stadium', 1, '[{\"added\": {}}]', 14, 1),
(79, '2024-12-02 12:52:23.750404', '22', 'NRG Stadium', 1, '[{\"added\": {}}]', 14, 1),
(80, '2024-12-02 12:56:23.508306', '23', 'Alegiant Stadium', 1, '[{\"added\": {}}]', 14, 1),
(81, '2024-12-02 12:57:32.156945', '24', 'Paycor Stadium', 1, '[{\"added\": {}}]', 14, 1),
(82, '2024-12-02 12:58:39.504291', '25', 'Raymond James Stadium', 1, '[{\"added\": {}}]', 14, 1),
(83, '2024-12-02 13:00:10.153069', '26', 'Soldier Field', 1, '[{\"added\": {}}]', 14, 1),
(84, '2024-12-02 13:01:18.939010', '27', 'State Farm Stadium', 1, '[{\"added\": {}}]', 14, 1),
(85, '2024-12-02 13:02:50.569780', '28', 'EverBank Stadium', 1, '[{\"added\": {}}]', 14, 1),
(86, '2024-12-02 13:04:01.532564', '29', 'U.S Bank Stadium', 1, '[{\"added\": {}}]', 14, 1),
(87, '2024-12-02 13:05:01.118431', '32', 'Seahawks', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(88, '2024-12-02 13:05:16.535824', '31', '49ers', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(89, '2024-12-02 13:05:43.746374', '30', 'Rams', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(90, '2024-12-02 13:06:16.838157', '27', 'State Farm Stadium', 2, '[]', 14, 1),
(91, '2024-12-02 13:06:28.894511', '29', 'Cardinals', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(92, '2024-12-02 13:06:45.375077', '28', 'Buccaneers', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(93, '2024-12-02 13:07:34.489240', '27', 'Saints', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(94, '2024-12-02 13:07:53.345913', '18', 'Ceasar Superdome', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 14, 1),
(95, '2024-12-02 13:12:05.686141', '25', 'Falcons', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(96, '2024-12-02 13:17:07.954451', '24', 'Vickings', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(97, '2024-12-02 13:17:22.066658', '23', 'Packers', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(98, '2024-12-02 13:17:57.092409', '22', 'Lions', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(99, '2024-12-02 13:18:12.661265', '21', 'Bears', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(100, '2024-12-02 13:21:28.455833', '20', 'Commanders', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(101, '2024-12-02 13:21:44.764024', '19', 'Eagles', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(102, '2024-12-02 13:21:59.754728', '18', 'Giants', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(103, '2024-12-02 13:22:20.147658', '16', 'Titans', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(104, '2024-12-02 13:23:16.012074', '15', 'Jaguars', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(105, '2024-12-02 13:23:36.235895', '14', 'Colts', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(106, '2024-12-02 13:23:50.561187', '13', 'Texans', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(107, '2024-12-02 13:24:09.719467', '12', 'Steelers', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(108, '2024-12-02 13:24:41.757962', '11', 'Browns', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(109, '2024-12-02 13:25:13.298936', '10', 'Bengals', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(110, '2024-12-02 13:25:28.427119', '9', 'Ravens', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(111, '2024-12-02 13:25:48.464904', '8', 'Jets', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(112, '2024-12-02 13:26:03.692119', '7', 'Patriots', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(113, '2024-12-02 13:26:20.303248', '6', 'Dolphins', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(114, '2024-12-02 13:26:44.038117', '5', 'Bills', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(115, '2024-12-02 13:26:58.182298', '4', 'Chargers', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(116, '2024-12-02 13:27:19.982978', '3', 'Raiders', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(117, '2024-12-02 13:27:36.880964', '2', 'Broncos', 2, '[{\"changed\": {\"fields\": [\"Stadium\"]}}]', 9, 1),
(118, '2024-12-02 13:27:46.793927', '23', 'Allegiant Stadium', 2, '[{\"changed\": {\"fields\": [\"Name\"]}}]', 14, 1),
(119, '2024-12-06 08:21:32.471212', '1', 'PlayGame object (1)', 1, '[{\"added\": {}}]', 15, 1),
(120, '2024-12-06 08:21:57.988976', '2', 'PlayGame object (2)', 1, '[{\"added\": {}}]', 15, 1),
(121, '2024-12-06 08:22:24.644839', '3', 'PlayGame object (3)', 1, '[{\"added\": {}}]', 15, 1),
(122, '2024-12-06 08:22:47.665690', '4', 'PlayGame object (4)', 1, '[{\"added\": {}}]', 15, 1),
(123, '2024-12-06 08:23:58.233099', '5', 'PlayGame object (5)', 1, '[{\"added\": {}}]', 15, 1),
(124, '2024-12-06 09:48:03.266636', '6', 'PlayGame object (6)', 1, '[{\"added\": {}}]', 15, 1),
(125, '2024-12-06 09:48:20.270821', '7', 'PlayGame object (7)', 1, '[{\"added\": {}}]', 15, 1),
(126, '2024-12-06 09:48:49.240007', '8', 'PlayGame object (8)', 1, '[{\"added\": {}}]', 15, 1),
(127, '2024-12-06 09:49:29.719100', '8', 'PlayGame object (8)', 2, '[{\"changed\": {\"fields\": [\"team_visitor\"]}}]', 15, 1),
(128, '2024-12-06 09:50:00.015361', '9', 'PlayGame object (9)', 1, '[{\"added\": {}}]', 15, 1),
(129, '2024-12-06 09:50:28.839936', '10', 'PlayGame object (10)', 1, '[{\"added\": {}}]', 15, 1),
(130, '2024-12-06 09:50:51.211610', '11', 'PlayGame object (11)', 1, '[{\"added\": {}}]', 15, 1),
(131, '2024-12-06 09:51:16.802254', '12', 'PlayGame object (12)', 1, '[{\"added\": {}}]', 15, 1),
(132, '2024-12-06 09:51:45.608686', '13', 'PlayGame object (13)', 1, '[{\"added\": {}}]', 15, 1),
(133, '2024-12-06 09:52:04.284032', '12', 'PlayGame object (12)', 2, '[{\"changed\": {\"fields\": [\"team_visitor\"]}}]', 15, 1),
(134, '2024-12-06 09:52:21.196512', '14', 'PlayGame object (14)', 1, '[{\"added\": {}}]', 15, 1),
(135, '2024-12-06 09:52:42.766157', '15', 'PlayGame object (15)', 1, '[{\"added\": {}}]', 15, 1),
(136, '2024-12-06 09:53:02.338677', '16', 'PlayGame object (16)', 1, '[{\"added\": {}}]', 15, 1),
(137, '2024-12-06 09:53:14.998448', '17', 'PlayGame object (17)', 1, '[{\"added\": {}}]', 15, 1),
(138, '2024-12-06 09:53:47.248734', '18', 'PlayGame object (18)', 1, '[{\"added\": {}}]', 15, 1),
(139, '2024-12-06 19:48:00.836581', '19', 'PlayGame object (19)', 1, '[{\"added\": {}}]', 15, 1),
(140, '2024-12-06 19:53:15.783194', '20', 'PlayGame object (20)', 1, '[{\"added\": {}}]', 15, 1),
(141, '2024-12-06 19:53:45.882522', '21', 'PlayGame object (21)', 1, '[{\"added\": {}}]', 15, 1),
(142, '2024-12-06 19:54:15.060256', '22', 'PlayGame object (22)', 1, '[{\"added\": {}}]', 15, 1),
(143, '2024-12-06 19:54:15.322225', '23', 'PlayGame object (23)', 1, '[{\"added\": {}}]', 15, 1),
(144, '2024-12-06 19:54:54.314918', '24', 'PlayGame object (24)', 1, '[{\"added\": {}}]', 15, 1),
(145, '2024-12-06 19:55:29.084777', '25', 'PlayGame object (25)', 1, '[{\"added\": {}}]', 15, 1),
(146, '2024-12-06 19:55:58.730591', '26', 'PlayGame object (26)', 1, '[{\"added\": {}}]', 15, 1),
(147, '2024-12-06 19:56:28.901587', '27', 'PlayGame object (27)', 1, '[{\"added\": {}}]', 15, 1),
(148, '2024-12-06 19:57:05.776838', '28', 'PlayGame object (28)', 1, '[{\"added\": {}}]', 15, 1),
(149, '2024-12-06 19:57:41.221441', '29', 'PlayGame object (29)', 1, '[{\"added\": {}}]', 15, 1),
(150, '2024-12-06 19:58:10.361104', '30', 'PlayGame object (30)', 1, '[{\"added\": {}}]', 15, 1),
(151, '2024-12-06 19:58:43.308863', '31', 'PlayGame object (31)', 1, '[{\"added\": {}}]', 15, 1),
(152, '2024-12-06 19:59:15.226141', '32', 'PlayGame object (32)', 1, '[{\"added\": {}}]', 15, 1),
(153, '2024-12-06 19:59:48.009608', '33', 'PlayGame object (33)', 1, '[{\"added\": {}}]', 15, 1),
(154, '2024-12-09 09:24:12.532712', '1', 'Saison 2024-2025', 1, '[{\"added\": {}}]', 17, 1),
(155, '2024-12-09 09:24:24.067301', '1', 'Week 1 - Saison 2024-2025', 1, '[{\"added\": {}}]', 19, 1),
(156, '2024-12-09 09:24:35.261810', '2', 'Week 2 - Saison 2024-2025', 1, '[{\"added\": {}}]', 19, 1),
(157, '2024-12-09 09:24:38.747153', '3', 'Week 3 - Saison 2024-2025', 1, '[{\"added\": {}}]', 19, 1),
(158, '2024-12-09 09:24:42.763542', '4', 'Week 4 - Saison 2024-2025', 1, '[{\"added\": {}}]', 19, 1),
(159, '2024-12-09 09:24:48.499417', '5', 'Week 5 - Saison 2024-2025', 1, '[{\"added\": {}}]', 19, 1),
(160, '2024-12-09 09:24:58.259895', '6', 'Week 6 - Saison 2024-2025', 1, '[{\"added\": {}}]', 19, 1),
(161, '2024-12-09 09:25:01.738202', '7', 'Week 7 - Saison 2024-2025', 1, '[{\"added\": {}}]', 19, 1),
(162, '2024-12-09 09:25:05.148335', '8', 'Week 8 - Saison 2024-2025', 1, '[{\"added\": {}}]', 19, 1),
(163, '2024-12-09 09:25:08.012884', '9', 'Week 9 - Saison 2024-2025', 1, '[{\"added\": {}}]', 19, 1),
(164, '2024-12-09 09:25:11.395851', '10', 'Week 10 - Saison 2024-2025', 1, '[{\"added\": {}}]', 19, 1),
(165, '2024-12-09 09:25:14.414755', '11', 'Week 11 - Saison 2024-2025', 1, '[{\"added\": {}}]', 19, 1),
(166, '2024-12-09 09:25:17.310759', '12', 'Week 12 - Saison 2024-2025', 1, '[{\"added\": {}}]', 19, 1),
(167, '2024-12-09 09:25:20.414935', '13', 'Week 13 - Saison 2024-2025', 1, '[{\"added\": {}}]', 19, 1),
(168, '2024-12-09 09:25:23.285785', '14', 'Week 14 - Saison 2024-2025', 1, '[{\"added\": {}}]', 19, 1),
(169, '2024-12-09 09:25:26.028545', '15', 'Week 15 - Saison 2024-2025', 1, '[{\"added\": {}}]', 19, 1),
(170, '2024-12-09 09:25:29.110416', '16', 'Week 16 - Saison 2024-2025', 1, '[{\"added\": {}}]', 19, 1),
(171, '2024-12-09 09:25:32.223277', '17', 'Week 17 - Saison 2024-2025', 1, '[{\"added\": {}}]', 19, 1),
(172, '2024-12-09 09:25:35.557778', '18', 'Week 18 - Saison 2024-2025', 1, '[{\"added\": {}}]', 19, 1),
(173, '2024-12-09 09:26:43.936349', '1', 'PlayGame object (1)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(174, '2024-12-09 09:28:18.255745', '2', 'PlayGame object (2)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(175, '2024-12-09 09:29:02.086195', '3', 'PlayGame object (3)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(176, '2024-12-09 09:29:29.523393', '4', 'PlayGame object (4)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(177, '2024-12-09 09:29:44.494060', '5', 'PlayGame object (5)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(178, '2024-12-09 09:29:58.313952', '14', 'PlayGame object (14)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(179, '2024-12-09 09:30:29.193949', '6', 'PlayGame object (6)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(180, '2024-12-09 09:30:41.343082', '7', 'PlayGame object (7)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(181, '2024-12-09 09:30:55.076296', '8', 'PlayGame object (8)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(182, '2024-12-09 09:31:06.186333', '9', 'PlayGame object (9)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(183, '2024-12-09 09:31:15.817427', '10', 'PlayGame object (10)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(184, '2024-12-09 09:31:35.107575', '11', 'PlayGame object (11)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(185, '2024-12-09 09:31:44.514080', '12', 'PlayGame object (12)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(186, '2024-12-09 09:31:54.454055', '13', 'PlayGame object (13)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(187, '2024-12-09 09:32:23.963602', '15', 'PlayGame object (15)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(188, '2024-12-09 09:32:42.891735', '16', 'PlayGame object (16)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(189, '2024-12-09 09:33:07.867364', '17', 'PlayGame object (17)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(190, '2024-12-09 09:33:42.485779', '18', 'PlayGame object (18)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(191, '2024-12-09 09:33:52.647230', '19', 'PlayGame object (19)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(192, '2024-12-09 09:34:01.734707', '20', 'PlayGame object (20)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(193, '2024-12-09 09:34:14.295035', '21', 'PlayGame object (21)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(194, '2024-12-09 09:34:26.799506', '22', 'PlayGame object (22)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(195, '2024-12-09 09:34:36.590522', '23', 'PlayGame object (23)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(196, '2024-12-09 09:34:52.507191', '24', 'PlayGame object (24)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(197, '2024-12-09 09:35:04.876457', '25', 'PlayGame object (25)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(198, '2024-12-09 09:35:15.690937', '26', 'PlayGame object (26)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(199, '2024-12-09 09:35:25.722756', '27', 'PlayGame object (27)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(200, '2024-12-09 09:35:40.242628', '28', 'PlayGame object (28)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(201, '2024-12-09 09:35:49.266025', '29', 'PlayGame object (29)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(202, '2024-12-09 09:36:03.099002', '30', 'PlayGame object (30)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(203, '2024-12-09 09:36:12.149268', '31', 'PlayGame object (31)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(204, '2024-12-09 09:36:26.382991', '32', 'PlayGame object (32)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(205, '2024-12-09 09:36:40.198783', '33', 'PlayGame object (33)', 2, '[{\"changed\": {\"fields\": [\"Week\", \"Played at\"]}}]', 16, 1),
(206, '2024-12-09 10:15:42.098325', '25', 'Vickings vs 49ers (Week 2 - Saison 2024-2025)', 2, '[{\"changed\": {\"fields\": [\"Week\"]}}]', 16, 1),
(207, '2024-12-09 10:15:50.440287', '26', 'Patriots vs Seahawks (Week 2 - Saison 2024-2025)', 2, '[{\"changed\": {\"fields\": [\"Week\"]}}]', 16, 1),
(208, '2024-12-09 10:16:02.077487', '29', 'Cardinals vs Rams (Week 2 - Saison 2024-2025)', 2, '[{\"changed\": {\"fields\": [\"Week\"]}}]', 16, 1),
(209, '2024-12-09 14:03:47.153444', '23', 'Packers vs Colts (Week 2 - Saison 2024-2025)', 3, '', 16, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(12, 'players', 'player_position'),
(13, 'players', 'players'),
(16, 'playgames', 'playgame'),
(17, 'playgames', 'season'),
(18, 'playgames', 'superbowls'),
(19, 'playgames', 'week'),
(6, 'sessions', 'session'),
(11, 'team', 'coachs'),
(7, 'team', 'conferences'),
(8, 'team', 'divisions'),
(15, 'team', 'playgame'),
(14, 'team', 'stadium'),
(10, 'team', 'superbowls'),
(9, 'team', 'teams');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-12-02 10:06:58.769293'),
(2, 'auth', '0001_initial', '2024-12-02 10:07:02.832895'),
(3, 'admin', '0001_initial', '2024-12-02 10:07:03.421990'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-12-02 10:07:03.458577'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-12-02 10:07:03.495706'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-12-02 10:07:03.806625'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-12-02 10:07:04.018661'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-12-02 10:07:04.111024'),
(9, 'auth', '0004_alter_user_username_opts', '2024-12-02 10:07:04.151764'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-12-02 10:07:04.383898'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-12-02 10:07:04.414762'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-12-02 10:07:04.443673'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-12-02 10:07:04.666054'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-12-02 10:07:05.025772'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-12-02 10:07:05.104527'),
(16, 'auth', '0011_update_proxy_permissions', '2024-12-02 10:07:05.146124'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-12-02 10:07:05.357315'),
(18, 'team', '0001_initial', '2024-12-02 10:07:07.159070'),
(19, 'players', '0001_initial', '2024-12-02 10:07:07.883522'),
(20, 'sessions', '0001_initial', '2024-12-02 10:07:08.117872'),
(21, 'team', '0002_stadium_superbowls_year_alter_teams_stadium', '2024-12-02 10:54:27.685190'),
(22, 'players', '0002_players_number', '2024-12-02 11:55:20.174943'),
(23, 'team', '0003_stadium_state', '2024-12-02 12:19:17.387219'),
(24, 'players', '0002_players_draft', '2024-12-06 07:02:52.758551'),
(25, 'team', '0002_playgame', '2024-12-06 08:03:07.088087'),
(26, 'team', '0003_delete_playgame', '2024-12-09 08:18:35.852137'),
(27, 'playgames', '0001_initial', '2024-12-09 08:18:46.407362'),
(28, 'team', '0002_delete_superbowls', '2024-12-09 08:55:44.256436'),
(29, 'playgames', '0002_season_playgame_played_at_superbowls_week_and_more', '2024-12-09 08:55:47.475646');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('p9bklu32qs2mqyccy5k5kx5mnkuen8ir', '.eJxVjMsOwiAUBf-FtSGFS6B16d5vIPcBUjWQlHZl_Hdt0oVuz8ycl4q4rSVuPS1xFnVWRp1-N0J-pLoDuWO9Nc2trstMelf0Qbu-NknPy-H-HRTs5VuPVoh8GHAAYHaUACYQnwxJFjR-IrYMzhjxYik4yIEQZATH2YoH9f4A-X44eA:1tI3NK:45lDNR2MSCNErM-zJeT5oiLGdz3pU2D6cHKefreP1Vk', '2024-12-16 10:09:54.799680');

-- --------------------------------------------------------

--
-- Table structure for table `players_player_position`
--

CREATE TABLE `players_player_position` (
  `id` bigint NOT NULL,
  `abrev` varchar(10) NOT NULL,
  `name` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `players_player_position`
--

INSERT INTO `players_player_position` (`id`, `abrev`, `name`) VALUES
(1, 'QB', 'Quarterback'),
(2, 'RB', 'Running back'),
(3, 'HB', 'Halfback'),
(4, 'FB', 'Fullback'),
(5, 'WR', 'Wide receiver'),
(6, 'TE', 'Tight-end'),
(7, 'OL', 'Offensive Linemen'),
(8, 'C', 'Centre'),
(9, 'OG', 'Offensive guard'),
(10, 'OT', 'Offensive tackle'),
(11, 'DL', 'Defensive linemen'),
(12, 'DT', 'Defensive tackle'),
(13, 'NT', 'Nose tackle'),
(14, 'DE', 'Defensive end'),
(15, 'LB', 'Linebacker'),
(16, 'DB', 'Defensive back'),
(17, 'CB', 'Cornerback'),
(18, 'S', 'Safety'),
(19, 'FS', 'Free safety'),
(20, 'SS', 'Strong safety'),
(21, 'K', 'Kicker'),
(22, 'P', 'Punter'),
(23, 'KS', 'Kick returner'),
(24, 'KP', 'Kick punter'),
(25, 'LS', 'Long snapper');

-- --------------------------------------------------------

--
-- Table structure for table `playgames_playgame`
--

CREATE TABLE `playgames_playgame` (
  `id` bigint NOT NULL,
  `score_local` int NOT NULL,
  `score_visitor` int NOT NULL,
  `team_local_id` bigint NOT NULL,
  `team_visitor_id` bigint NOT NULL,
  `played_at` datetime(6) NOT NULL,
  `week_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `playgames_playgame`
--

INSERT INTO `playgames_playgame` (`id`, `score_local`, `score_visitor`, `team_local_id`, `team_visitor_id`, `played_at`, `week_id`) VALUES
(1, 27, 20, 1, 9, '2024-09-06 14:00:00.000000', 1),
(2, 34, 29, 19, 23, '2024-09-07 14:00:00.000000', 1),
(3, 10, 18, 25, 12, '2024-09-08 18:00:00.000000', 1),
(4, 34, 28, 5, 29, '2024-09-08 18:00:00.000000', 1),
(5, 24, 17, 21, 16, '2024-09-08 18:00:00.000000', 1),
(6, 10, 16, 10, 7, '2024-09-08 18:00:00.000000', 1),
(7, 27, 29, 14, 13, '2024-09-08 18:00:00.000000', 1),
(8, 20, 17, 6, 15, '2024-09-08 18:00:00.000000', 1),
(9, 47, 10, 27, 26, '2024-09-08 18:00:00.000000', 1),
(10, 6, 28, 18, 24, '2024-09-08 18:00:00.000000', 1),
(11, 22, 10, 4, 3, '2024-09-08 18:00:00.000000', 1),
(12, 26, 20, 32, 2, '2024-09-08 18:00:00.000000', 1),
(13, 17, 33, 11, 17, '2024-09-08 18:00:00.000000', 1),
(14, 37, 20, 28, 20, '2024-09-08 18:00:00.000000', 1),
(15, 26, 20, 22, 30, '2024-09-09 18:00:00.000000', 1),
(16, 32, 19, 31, 8, '2024-09-10 18:00:00.000000', 1),
(17, 10, 31, 6, 5, '2024-09-13 12:00:00.000000', 2),
(18, 23, 26, 9, 3, '2024-09-15 18:00:00.000000', 2),
(19, 3, 26, 26, 4, '2024-09-15 18:00:00.000000', 2),
(20, 19, 44, 17, 27, '2024-09-15 18:00:00.000000', 2),
(21, 16, 20, 22, 28, '2024-09-15 18:00:00.000000', 2),
(22, 16, 10, 23, 14, '2024-09-15 18:00:00.000000', 2),
(24, 13, 18, 15, 11, '2024-09-15 18:00:00.000000', 2),
(25, 23, 17, 24, 31, '2024-09-15 18:00:00.000000', 2),
(26, 20, 23, 7, 32, '2024-09-15 18:00:00.000000', 2),
(27, 17, 24, 16, 8, '2024-09-15 18:00:00.000000', 2),
(28, 21, 18, 20, 18, '2024-09-15 18:00:00.000000', 2),
(29, 41, 10, 29, 30, '2024-09-15 18:00:00.000000', 2),
(30, 6, 13, 2, 12, '2024-09-15 18:00:00.000000', 2),
(31, 26, 25, 1, 10, '2024-09-15 18:00:00.000000', 2),
(32, 19, 13, 13, 21, '2024-09-16 18:00:00.000000', 2),
(33, 21, 22, 19, 25, '2024-09-17 00:00:00.000000', 2);

-- --------------------------------------------------------

--
-- Table structure for table `playgames_season`
--

CREATE TABLE `playgames_season` (
  `id` bigint NOT NULL,
  `name` varchar(50) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `playgames_season`
--

INSERT INTO `playgames_season` (`id`, `name`, `start_date`, `end_date`) VALUES
(1, 'Saison 2024-2025', '2024-09-06', '2025-02-09');

-- --------------------------------------------------------

--
-- Table structure for table `playgames_superbowls`
--

CREATE TABLE `playgames_superbowls` (
  `id` bigint NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `year` date DEFAULT NULL,
  `town` varchar(60) NOT NULL,
  `stadium` varchar(60) NOT NULL,
  `season_id` bigint NOT NULL,
  `teamOne_id` bigint DEFAULT NULL,
  `teamTwo_id` bigint DEFAULT NULL,
  `winner_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `playgames_week`
--

CREATE TABLE `playgames_week` (
  `id` bigint NOT NULL,
  `week_number` int UNSIGNED NOT NULL,
  `is_playoff` tinyint(1) NOT NULL,
  `season_id` bigint NOT NULL
) ;

--
-- Dumping data for table `playgames_week`
--

INSERT INTO `playgames_week` (`id`, `week_number`, `is_playoff`, `season_id`) VALUES
(1, 1, 0, 1),
(2, 2, 0, 1),
(3, 3, 0, 1),
(4, 4, 0, 1),
(5, 5, 0, 1),
(6, 6, 0, 1),
(7, 7, 0, 1),
(8, 8, 0, 1),
(9, 9, 0, 1),
(10, 10, 0, 1),
(11, 11, 0, 1),
(12, 12, 0, 1),
(13, 13, 0, 1),
(14, 14, 0, 1),
(15, 15, 0, 1),
(16, 16, 0, 1),
(17, 17, 0, 1),
(18, 18, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `team_coachs`
--

CREATE TABLE `team_coachs` (
  `id` bigint NOT NULL,
  `name` varchar(60) NOT NULL,
  `firstName` varchar(60) NOT NULL,
  `poste` varchar(50) DEFAULT NULL,
  `thumbnail` varchar(100) DEFAULT NULL,
  `actif` tinyint(1) NOT NULL,
  `team_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `team_conferences`
--

CREATE TABLE `team_conferences` (
  `id` bigint NOT NULL,
  `name` varchar(80) NOT NULL,
  `shortName` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `team_conferences`
--

INSERT INTO `team_conferences` (`id`, `name`, `shortName`) VALUES
(1, 'American Football Conference', 'AFC'),
(2, 'National Football Conference', 'NFC');

-- --------------------------------------------------------

--
-- Table structure for table `team_divisions`
--

CREATE TABLE `team_divisions` (
  `id` bigint NOT NULL,
  `name` varchar(50) NOT NULL,
  `conferences_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `team_divisions`
--

INSERT INTO `team_divisions` (`id`, `name`, `conferences_id`) VALUES
(1, 'AFC West', 1),
(2, 'AFC East', 1),
(3, 'AFC North', 1),
(4, 'AFC South', 1),
(5, 'NFC North', 2),
(6, 'NFC South', 2),
(7, 'NFC West', 2),
(8, 'NFC East', 2);

-- --------------------------------------------------------

--
-- Table structure for table `team_players`
--

CREATE TABLE `team_players` (
  `id` bigint NOT NULL,
  `name` varchar(60) NOT NULL,
  `firstName` varchar(60) NOT NULL,
  `thumbnail` varchar(100) DEFAULT NULL,
  `age` date NOT NULL,
  `actif` tinyint(1) NOT NULL,
  `injury` tinyint(1) NOT NULL,
  `poste_id` bigint DEFAULT NULL,
  `team_id` bigint DEFAULT NULL,
  `number` int DEFAULT NULL,
  `draft` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `team_players`
--

INSERT INTO `team_players` (`id`, `name`, `firstName`, `thumbnail`, `age`, `actif`, `injury`, `poste_id`, `team_id`, `number`, `draft`) VALUES
(1, 'Mahomes', 'Patrick', 'photo/mahomes.webp', '1995-09-17', 1, 0, 1, 1, 15, NULL),
(2, 'Hill', 'Tyreek', 'photo/tyreek.hill.webp', '1994-03-01', 1, 0, 5, 6, 10, NULL),
(3, 'Achane', 'De\'Von', 'photo/DeVon_Achane.webp', '2001-10-13', 1, 0, 2, 6, 28, NULL),
(4, 'Barkley', 'Saquon', 'photo/s.barkley.webp', '1997-02-07', 1, 0, 2, 19, 26, NULL),
(5, 'Jackson', 'Lamar', 'photo/Lamar_Jackson.webp', '1997-01-07', 1, 0, 1, 9, 8, NULL),
(6, 'Burrow', 'Joe', 'photo/burrow.webp', '1996-12-10', 1, 0, 1, 10, 9, NULL),
(7, 'Rodgers', 'Aaron', 'photo/rodgers.webp', '1983-12-02', 1, 0, 1, 8, 8, NULL),
(8, 'Daniels', 'Jayden', 'photo/j.daniels.webp', '2000-12-18', 1, 0, 1, 20, 5, NULL),
(9, 'Mc Caffrey', 'Christian', 'photo/mc_caffrey.webp', '1996-07-07', 1, 0, 2, 31, 23, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `team_stadium`
--

CREATE TABLE `team_stadium` (
  `id` bigint NOT NULL,
  `name` varchar(60) NOT NULL,
  `town` varchar(60) NOT NULL,
  `capacity` int DEFAULT NULL,
  `toiture` varchar(30) DEFAULT NULL,
  `creation` date NOT NULL,
  `thumbnail` varchar(100) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `team_stadium`
--

INSERT INTO `team_stadium` (`id`, `name`, `town`, `capacity`, `toiture`, `creation`, `thumbnail`, `state`) VALUES
(1, 'Arraowhead Stadium', 'Kansas City', 76416, 'ouverte', '1972-08-12', 'stadium/Chiefsgame.jpg', 'Missouri'),
(2, 'AT&T Stadium', 'Arlington', 80000, 'retractable', '2009-05-27', 'stadium/Cowboys_Stadium_field.jpg', 'Texas'),
(3, 'Bank of America Stadium', 'Charlotte', 75419, 'ouverte', '1996-09-14', 'stadium/Bank_of_America_stadium.jpg', 'Caroline du Nord'),
(4, 'Empower Field at Mile High', 'Denver', 67431, 'ouverte', '2001-09-10', 'stadium/Invesco_Field_at_Mile_High_Stadium.jpg', 'Colorado'),
(5, 'Lumen Fields', 'Seattle', 68740, 'ouverte', '2002-07-28', 'stadium/SeahawksStadium.jpg', 'Washington'),
(6, 'Northwest Stadium', 'Landover', 82000, 'ouverte', '1997-12-14', 'stadium/Northwest_stadium.jpg', 'Maryland'),
(7, 'Huntington Bank Field', 'Cleveland', 67431, 'ouverte', '1999-09-12', 'stadium/Huntington_Bank_Field.jpg', 'Ohio'),
(8, 'Ford Field', 'Detroit', 65000, 'couverte', '2002-08-24', 'stadium/Ford_Field.jpg', 'Michigan'),
(9, 'Gilette Stadium', 'Foxborough', 66829, 'ouverte', '2002-09-09', 'stadium/Gillette_Stadium.jpg', 'Massachusetts'),
(10, 'Hard Rock Stadium', 'Miami', 65326, 'ouverte', '1987-08-16', 'stadium/Hard_Rock_Stadium.jpg', 'Floride'),
(11, 'Acrisure Stadium', 'Pittsburgh', 68400, 'ouverte', '2001-08-25', 'stadium/Acrisure_Stadium.jpg', 'Pennsylvanie'),
(12, 'Lambeau Field', 'Green Bay', 81435, 'ouverte', '1957-09-29', 'stadium/Lambeau_Field.jpg', 'Wisconsin'),
(13, 'Levi\'s Stadium', 'Santa Clara', 68500, 'ouverte', '2014-07-17', 'stadium/Levis_Stadium.jpg', 'Californie'),
(14, 'Lincoln Financial Field', 'Philadephie', 69596, 'ouverte', '2003-08-03', 'stadium/Lincoln_Financial_Field.jpg', 'Pennsylvanie'),
(15, 'SoFi Stadium', 'Inglewood', 70240, 'couverte', '2020-09-08', 'stadium/SoFi_Stadium.jpg', 'Californie'),
(16, 'Lucas Oil Stadium', 'Indinapolis', 67000, 'retractable', '2008-08-16', 'stadium/Lucas_Oil_Stadium.jpg', 'Indinana'),
(17, 'M&T Bank Stadium', 'Baltimore', 71008, 'ouverte', '1998-09-06', 'stadium/MT_Bank_Stadium.jpg', 'Maryland'),
(18, 'Ceasar Superdome', 'Atlanta', 71000, 'retractable', '2017-08-26', 'stadium/Mercedes-Benz_Stadium.jpg', 'Georgie'),
(19, 'MetLife Stadium', 'East Rutherford', 82500, 'ouverte', '2010-04-10', 'stadium/MetLife_Stadium.jpg', 'New Jersey'),
(20, 'Highmark Stadium', 'Orchard Park', 71608, 'ouverte', '1973-08-17', 'stadium/Highmark_Stadium.jpg', 'New York'),
(21, 'Nissan Stadium', 'Nashville', 69143, 'ouverte', '1999-08-27', 'stadium/Nissan_Stadium.jpg', 'Tennessee'),
(22, 'NRG Stadium', 'Houston', 72220, 'retractable', '2002-08-24', 'stadium/NRG_Stadium.jpg', 'Texas'),
(23, 'Allegiant Stadium', 'Paradise', 65000, 'couverte', '2020-07-31', 'stadium/Allegiant_stadium.jpg', 'Nevada'),
(24, 'Paycor Stadium', 'Cincinnati', 65515, 'ouverte', '2000-08-19', 'stadium/Paycor_Stadium.jpg', 'Ohio'),
(25, 'Raymond James Stadium', 'Tampa', 65890, 'ouverte', '1998-09-20', 'stadium/Raymond_James_Stadium.JPG', 'Floride'),
(26, 'Soldier Field', 'Chicago', 61500, 'ouverte', '2003-09-29', 'stadium/Soldier_field.jpg', 'Illinois'),
(27, 'State Farm Stadium', 'Glendale', 63400, 'retractable', '2006-08-01', 'stadium/State_Farm_Stadium.jpg', 'Arizona'),
(28, 'EverBank Stadium', 'Jacksonville', 69132, 'ouverte', '1995-08-18', 'stadium/EverBank_Stadium.JPG', 'Floride'),
(29, 'U.S Bank Stadium', 'Minneapolis', 66655, 'couverte', '2016-07-22', 'stadium/U.S_Bank_Stadium.jpg', 'Minnesota');

-- --------------------------------------------------------

--
-- Table structure for table `team_teams`
--

CREATE TABLE `team_teams` (
  `id` bigint NOT NULL,
  `name` varchar(60) NOT NULL,
  `town` varchar(60) NOT NULL,
  `thumbnail` varchar(100) DEFAULT NULL,
  `stadium_id` bigint DEFAULT NULL,
  `founded` date NOT NULL,
  `owner` varchar(60) DEFAULT NULL,
  `colorOne` varchar(15) DEFAULT NULL,
  `colorTwo` varchar(15) DEFAULT NULL,
  `division_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `team_teams`
--

INSERT INTO `team_teams` (`id`, `name`, `town`, `thumbnail`, `stadium_id`, `founded`, `owner`, `colorOne`, `colorTwo`, `division_id`) VALUES
(1, 'Chiefs', 'Kansas City', 'logo/KC.webp', 1, '1960-01-01', 'Clark Hunt', '#E31837', '#FFB81C', 1),
(2, 'Broncos', 'Denver', 'logo/Broncos.webp', 4, '1960-01-01', NULL, '#FB4F14', '#002244', 1),
(3, 'Raiders', 'Los Angeles', 'logo/Raiders.webp', 23, '1960-01-01', NULL, '#000000', '#A5ACAF', 1),
(4, 'Chargers', 'Los Angeles', 'logo/Chargers.webp', 15, '1960-01-01', NULL, '#0080C6', '#FFC20E', 1),
(5, 'Bills', 'Buffalo', 'logo/Bills.webp', 20, '1960-01-01', NULL, '#00338D', '#C60C30', 2),
(6, 'Dolphins', 'Miami', 'logo/Dolphins.webp', 10, '1966-01-01', NULL, '#008E97', '#FC4C02', 2),
(7, 'Patriots', 'New England', 'logo/Patriots.webp', 9, '1960-01-01', NULL, '#002244', '#C60C30', 2),
(8, 'Jets', 'New York', 'logo/Jets.webp', 19, '1960-01-01', NULL, '#125740', '#000000', 2),
(9, 'Ravens', 'Baltimore', 'logo/Ravens.webp', 17, '1996-01-01', 'Steve Bisciotti', '#241773', '#9E7C0C', 3),
(10, 'Bengals', 'Cincinnati', 'logo/Bengals.webp', 24, '1968-01-01', NULL, '#fb4f14', '#000000', 3),
(11, 'Browns', 'Cleveland', 'logo/Browns.webp', 7, '1946-01-01', NULL, '#311D00', '#ff3c00', 3),
(12, 'Steelers', 'Pittsburgh', 'logo/Steelers.webp', 11, '1933-01-01', NULL, '#FFB612', '#101820', 3),
(13, 'Texans', 'Houston', 'logo/Texans.webp', 22, '2002-01-01', NULL, '#03202f', '#A71930', 4),
(14, 'Colts', 'Indianapolis', 'logo/Colts.webp', 16, '1953-01-01', NULL, '#002C5F', '#A2AAAD', 4),
(15, 'Jaguars', 'Jacksonville', 'logo/Jaguars.webp', 28, '1995-01-01', NULL, '#101820', '#D7A22A', 4),
(16, 'Titans', 'Tennessee', 'logo/Titans.webp', 21, '1960-01-01', NULL, '#0C2340', '#4B92DB', 4),
(17, 'Cowboys', 'Dallas', 'logo/Cowboys.webp', 2, '1960-01-01', NULL, '#003594', '#869397', 8),
(18, 'Giants', 'New York', 'logo/Giants.webp', 19, '1925-01-01', NULL, '#0B2265', '#a71930', 8),
(19, 'Eagles', 'Philadelphie', 'logo/Eagles.webp', 14, '1933-01-01', NULL, '#004C54', '#A5ACAF', 8),
(20, 'Commanders', 'Washington', 'logo/Commanders.webp', 6, '1932-01-01', NULL, '#5A1414', '#FFB612', 8),
(21, 'Bears', 'Chicago', 'logo/Bears.webp', 26, '1920-01-01', NULL, '#0B162A', '#c83803', 5),
(22, 'Lions', 'Detroit', 'logo/Lions.webp', 8, '1930-01-01', NULL, '#0076b6', '#B0B7BC', 5),
(23, 'Packers', 'Green Bay', 'logo/Packers.webp', 12, '1921-01-01', NULL, '#203731', '#FFB612', 5),
(24, 'Vickings', 'Minnesota', 'logo/Vickings.webp', 29, '1961-01-01', NULL, '#4F2683', '#FFC62F', 5),
(25, 'Falcons', 'Atlanta', 'logo/Falcons.webp', 18, '1966-01-01', NULL, '#a71930', '#000000', 6),
(26, 'Panthers', 'Carolina', 'logo/Panthers.webp', 3, '1995-01-01', NULL, '#0085CA', '#101820', 6),
(27, 'Saints', 'New Orleans', 'logo/Saints.webp', 18, '1967-01-01', NULL, '#D3BC8D', '#101820', 6),
(28, 'Buccaneers', 'Tampa Bay', 'logo/Buccaneers.webp', 25, '1976-01-01', NULL, '#D50A0A', '#FF7900', 6),
(29, 'Cardinals', 'Arizona', 'logo/Cardinals.webp', 27, '1920-01-01', NULL, '#97233F', '#000000', 7),
(30, 'Rams', 'Los Angeles', 'logo/Rams.webp', 15, '1937-01-01', NULL, '#003594', '#ffa300', 7),
(31, '49ers', 'San Francisco', 'logo/49ers.webp', 13, '1946-01-01', NULL, '#AA0000', '#B3995D', 7),
(32, 'Seahawks', 'Seattle', 'logo/Seahawks.webp', 5, '1976-01-01', NULL, '#002244', '#69BE28', 7);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `players_player_position`
--
ALTER TABLE `players_player_position`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `playgames_playgame`
--
ALTER TABLE `playgames_playgame`
  ADD PRIMARY KEY (`id`),
  ADD KEY `playgames_playgame_team_local_id_a1f02e87_fk_team_teams_id` (`team_local_id`),
  ADD KEY `playgames_playgame_team_visitor_id_5dab9df3_fk_team_teams_id` (`team_visitor_id`),
  ADD KEY `playgames_playgame_week_id_2febc717_fk_playgames_week_id` (`week_id`);

--
-- Indexes for table `playgames_season`
--
ALTER TABLE `playgames_season`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `playgames_superbowls`
--
ALTER TABLE `playgames_superbowls`
  ADD PRIMARY KEY (`id`),
  ADD KEY `playgames_superbowls_season_id_988639e4_fk_playgames_season_id` (`season_id`),
  ADD KEY `playgames_superbowls_teamOne_id_f54a89d1_fk_team_teams_id` (`teamOne_id`),
  ADD KEY `playgames_superbowls_teamTwo_id_370b9df9_fk_team_teams_id` (`teamTwo_id`),
  ADD KEY `playgames_superbowls_winner_id_2c5994cc_fk_team_teams_id` (`winner_id`);

--
-- Indexes for table `playgames_week`
--
ALTER TABLE `playgames_week`
  ADD PRIMARY KEY (`id`),
  ADD KEY `playgames_week_season_id_7f0be647_fk_playgames_season_id` (`season_id`);

--
-- Indexes for table `team_coachs`
--
ALTER TABLE `team_coachs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `team_coachs_team_id_e56bdb06_fk_team_teams_id` (`team_id`);

--
-- Indexes for table `team_conferences`
--
ALTER TABLE `team_conferences`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `team_divisions`
--
ALTER TABLE `team_divisions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `team_divisions_conferences_id_04070b15_fk_team_conferences_id` (`conferences_id`);

--
-- Indexes for table `team_players`
--
ALTER TABLE `team_players`
  ADD PRIMARY KEY (`id`),
  ADD KEY `team_players_poste_id_7574a215_fk_players_player_position_id` (`poste_id`),
  ADD KEY `team_players_team_id_0d4ad9be_fk_team_teams_id` (`team_id`);

--
-- Indexes for table `team_stadium`
--
ALTER TABLE `team_stadium`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `team_teams`
--
ALTER TABLE `team_teams`
  ADD PRIMARY KEY (`id`),
  ADD KEY `team_teams_division_id_98ac8356_fk_team_divisions_id` (`division_id`),
  ADD KEY `team_teams_stadium_id_285efc46` (`stadium_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=77;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `players_player_position`
--
ALTER TABLE `players_player_position`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `playgames_playgame`
--
ALTER TABLE `playgames_playgame`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `playgames_season`
--
ALTER TABLE `playgames_season`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `playgames_superbowls`
--
ALTER TABLE `playgames_superbowls`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `playgames_week`
--
ALTER TABLE `playgames_week`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `team_coachs`
--
ALTER TABLE `team_coachs`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `team_conferences`
--
ALTER TABLE `team_conferences`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `team_divisions`
--
ALTER TABLE `team_divisions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `team_players`
--
ALTER TABLE `team_players`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `team_stadium`
--
ALTER TABLE `team_stadium`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `team_teams`
--
ALTER TABLE `team_teams`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `playgames_playgame`
--
ALTER TABLE `playgames_playgame`
  ADD CONSTRAINT `playgames_playgame_team_local_id_a1f02e87_fk_team_teams_id` FOREIGN KEY (`team_local_id`) REFERENCES `team_teams` (`id`),
  ADD CONSTRAINT `playgames_playgame_team_visitor_id_5dab9df3_fk_team_teams_id` FOREIGN KEY (`team_visitor_id`) REFERENCES `team_teams` (`id`),
  ADD CONSTRAINT `playgames_playgame_week_id_2febc717_fk_playgames_week_id` FOREIGN KEY (`week_id`) REFERENCES `playgames_week` (`id`);

--
-- Constraints for table `playgames_superbowls`
--
ALTER TABLE `playgames_superbowls`
  ADD CONSTRAINT `playgames_superbowls_season_id_988639e4_fk_playgames_season_id` FOREIGN KEY (`season_id`) REFERENCES `playgames_season` (`id`),
  ADD CONSTRAINT `playgames_superbowls_teamOne_id_f54a89d1_fk_team_teams_id` FOREIGN KEY (`teamOne_id`) REFERENCES `team_teams` (`id`),
  ADD CONSTRAINT `playgames_superbowls_teamTwo_id_370b9df9_fk_team_teams_id` FOREIGN KEY (`teamTwo_id`) REFERENCES `team_teams` (`id`),
  ADD CONSTRAINT `playgames_superbowls_winner_id_2c5994cc_fk_team_teams_id` FOREIGN KEY (`winner_id`) REFERENCES `team_teams` (`id`);

--
-- Constraints for table `playgames_week`
--
ALTER TABLE `playgames_week`
  ADD CONSTRAINT `playgames_week_season_id_7f0be647_fk_playgames_season_id` FOREIGN KEY (`season_id`) REFERENCES `playgames_season` (`id`);

--
-- Constraints for table `team_coachs`
--
ALTER TABLE `team_coachs`
  ADD CONSTRAINT `team_coachs_team_id_e56bdb06_fk_team_teams_id` FOREIGN KEY (`team_id`) REFERENCES `team_teams` (`id`);

--
-- Constraints for table `team_divisions`
--
ALTER TABLE `team_divisions`
  ADD CONSTRAINT `team_divisions_conferences_id_04070b15_fk_team_conferences_id` FOREIGN KEY (`conferences_id`) REFERENCES `team_conferences` (`id`);

--
-- Constraints for table `team_players`
--
ALTER TABLE `team_players`
  ADD CONSTRAINT `team_players_poste_id_7574a215_fk_players_player_position_id` FOREIGN KEY (`poste_id`) REFERENCES `players_player_position` (`id`),
  ADD CONSTRAINT `team_players_team_id_0d4ad9be_fk_team_teams_id` FOREIGN KEY (`team_id`) REFERENCES `team_teams` (`id`);

--
-- Constraints for table `team_teams`
--
ALTER TABLE `team_teams`
  ADD CONSTRAINT `team_teams_division_id_98ac8356_fk_team_divisions_id` FOREIGN KEY (`division_id`) REFERENCES `team_divisions` (`id`),
  ADD CONSTRAINT `team_teams_stadium_id_285efc46_fk_team_stadium_id` FOREIGN KEY (`stadium_id`) REFERENCES `team_stadium` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

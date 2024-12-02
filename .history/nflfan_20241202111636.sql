-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 27, 2024 at 03:55 PM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

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
(25, 'Can add teams', 7, 'add_teams'),
(26, 'Can change teams', 7, 'change_teams'),
(27, 'Can delete teams', 7, 'delete_teams'),
(28, 'Can view teams', 7, 'view_teams'),
(29, 'Can add p layers', 8, 'add_players'),
(30, 'Can change p layers', 8, 'change_players'),
(31, 'Can delete p layers', 8, 'delete_players'),
(32, 'Can view p layers', 8, 'view_players'),
(33, 'Can add conferences', 9, 'add_conferences'),
(34, 'Can change conferences', 9, 'change_conferences'),
(35, 'Can delete conferences', 9, 'delete_conferences'),
(36, 'Can view conferences', 9, 'view_conferences'),
(37, 'Can add divisions', 10, 'add_divisions'),
(38, 'Can change divisions', 10, 'change_divisions'),
(39, 'Can delete divisions', 10, 'delete_divisions'),
(40, 'Can view divisions', 10, 'view_divisions'),
(41, 'Can add coachs', 11, 'add_coachs'),
(42, 'Can change coachs', 11, 'change_coachs'),
(43, 'Can delete coachs', 11, 'delete_coachs'),
(44, 'Can view coachs', 11, 'view_coachs'),
(45, 'Can add superbowls', 12, 'add_superbowls'),
(46, 'Can change superbowls', 12, 'change_superbowls'),
(47, 'Can delete superbowls', 12, 'delete_superbowls'),
(48, 'Can view superbowls', 12, 'view_superbowls'),
(49, 'Can add p layers', 13, 'add_players'),
(50, 'Can change p layers', 13, 'change_players'),
(51, 'Can delete p layers', 13, 'delete_players'),
(52, 'Can view p layers', 13, 'view_players');

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
(1, 'pbkdf2_sha256$870000$HNLynPgqzkexQl2wKSzqDf$t7DAo9EtD2IiJFUub8KivOjFHHkuf0bp/EI1ZB76Pes=', '2024-11-20 09:26:49.000000', 1, 'Cedric', 'Cédric', 'Deswarte', 'cedcile1901@gmail.com', 1, 1, '2024-11-20 09:26:36.000000');

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
(1, '2024-11-20 09:27:23.328466', '1', 'Cedric', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]', 4, 1),
(2, '2024-11-20 13:01:48.260392', '1', 'Chiefs', 1, '[{\"added\": {}}]', 7, 1),
(3, '2024-11-20 14:24:08.100976', '1', 'Chiefs', 2, '[{\"changed\": {\"fields\": [\"Thumbnail\"]}}]', 7, 1),
(4, '2024-11-20 14:24:24.503604', '1', 'Chiefs', 2, '[{\"changed\": {\"fields\": [\"Thumbnail\"]}}]', 7, 1),
(5, '2024-11-26 07:44:22.536803', '1', 'American Football Conference', 1, '[{\"added\": {}}]', 9, 1),
(6, '2024-11-26 07:44:29.566328', '2', 'National Football Conference', 1, '[{\"added\": {}}]', 9, 1),
(7, '2024-11-26 07:45:02.754485', '1', 'AFC West', 1, '[{\"added\": {}}]', 10, 1),
(8, '2024-11-26 07:45:15.912860', '2', 'AFC East', 1, '[{\"added\": {}}]', 10, 1),
(9, '2024-11-26 07:45:37.640985', '3', 'AFC North', 1, '[{\"added\": {}}]', 10, 1),
(10, '2024-11-26 07:45:44.302358', '4', 'AFC South', 1, '[{\"added\": {}}]', 10, 1),
(11, '2024-11-26 07:45:55.743920', '4', 'AFC South', 2, '[{\"changed\": {\"fields\": [\"Conferences\"]}}]', 10, 1),
(12, '2024-11-26 07:46:10.417012', '5', 'NFC East', 1, '[{\"added\": {}}]', 10, 1),
(13, '2024-11-26 07:46:25.584218', '6', 'NFC North', 1, '[{\"added\": {}}]', 10, 1),
(14, '2024-11-26 07:46:31.496199', '7', 'NFC South', 1, '[{\"added\": {}}]', 10, 1),
(15, '2024-11-26 07:46:47.025349', '8', 'NFC West', 1, '[{\"added\": {}}]', 10, 1),
(16, '2024-11-26 11:02:08.261291', '1', 'Harbaugh John', 1, '[{\"added\": {}}]', 11, 1),
(17, '2024-11-26 12:40:53.782460', '9', 'Ravens', 2, '[{\"changed\": {\"fields\": [\"ColorTwo\"]}}]', 7, 1),
(18, '2024-11-27 09:03:28.258397', '1', 'Chiefs', 2, '[{\"changed\": {\"fields\": [\"Owner\"]}}]', 7, 1),
(19, '2024-11-27 10:43:38.422086', '9', 'Ravens', 2, '[{\"changed\": {\"fields\": [\"Owner\"]}}]', 7, 1),
(20, '2024-11-27 14:54:35.553532', '1', 'Mahomes Patrick', 3, '', 13, 1),
(21, '2024-11-27 14:57:01.468071', '3', 'Rodgers Aaron', 2, '[{\"changed\": {\"fields\": [\"Thumbnail\"]}}]', 13, 1),
(22, '2024-11-27 14:57:08.059447', '2', 'Mahomes Patrick', 2, '[{\"changed\": {\"fields\": [\"Thumbnail\"]}}]', 13, 1),
(23, '2024-11-27 15:09:49.913491', '4', 'Barkley Saquon', 3, '', 13, 1),
(24, '2024-11-27 15:11:41.741913', '5', 'Barkley Saquon', 3, '', 13, 1),
(25, '2024-11-27 15:32:57.009739', '9', 'test test', 3, '', 13, 1),
(26, '2024-11-27 15:32:57.009739', '8', 'test test', 3, '', 13, 1),
(27, '2024-11-27 15:33:21.042794', '10', 'test test', 3, '', 13, 1),
(28, '2024-11-27 15:34:03.918222', '11', 'test test', 3, '', 13, 1),
(29, '2024-11-27 15:35:44.652713', '12', 'test test', 3, '', 13, 1),
(30, '2024-11-27 15:43:02.785695', '13', 'Daniels Jayden', 3, '', 13, 1),
(31, '2024-11-27 15:46:41.123414', '7', 'Hill Tyreek', 3, '', 13, 1),
(32, '2024-11-27 15:48:24.522224', '15', 'Hill Tyreek', 3, '', 13, 1),
(33, '2024-11-27 15:50:13.981613', '16', 'Hill Tyreek', 3, '', 13, 1),
(34, '2024-11-27 15:51:12.038553', '17', 'Hill Tyreek', 3, '', 13, 1),
(35, '2024-11-27 15:52:28.330058', '18', 'Hill Tyreek', 3, '', 13, 1);

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
(13, 'players', 'players'),
(6, 'sessions', 'session'),
(11, 'team', 'coachs'),
(9, 'team', 'conferences'),
(10, 'team', 'divisions'),
(8, 'team', 'players'),
(12, 'team', 'superbowls'),
(7, 'team', 'teams');

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
(1, 'contenttypes', '0001_initial', '2024-11-20 09:22:56.006107'),
(2, 'auth', '0001_initial', '2024-11-20 09:22:56.381189'),
(3, 'admin', '0001_initial', '2024-11-20 09:22:56.479853'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-11-20 09:22:56.486229'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-11-20 09:22:56.492169'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-11-20 09:22:56.546914'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-11-20 09:22:56.594017'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-11-20 09:22:56.613583'),
(9, 'auth', '0004_alter_user_username_opts', '2024-11-20 09:22:56.620549'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-11-20 09:22:56.665320'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-11-20 09:22:56.667691'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-11-20 09:22:56.674011'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-11-20 09:22:56.719059'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-11-20 09:22:56.770735'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-11-20 09:22:56.786988'),
(16, 'auth', '0011_update_proxy_permissions', '2024-11-20 09:22:56.793499'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-11-20 09:22:56.840977'),
(18, 'sessions', '0001_initial', '2024-11-20 09:22:56.870880'),
(19, 'team', '0001_initial', '2024-11-20 09:22:56.882693'),
(20, 'team', '0002_teams_founded_teams_stadium_players', '2024-11-20 09:22:56.955699'),
(21, 'team', '0003_conferences_divisions_alter_players_thumbnail_and_more', '2024-11-20 09:22:57.274327'),
(22, 'team', '0004_superbowls_name', '2024-11-20 09:22:57.288868'),
(23, 'team', '0005_divisions_conferences_teams_division', '2024-11-20 09:22:57.383943'),
(24, 'team', '0006_alter_coachs_thumbnail_alter_players_thumbnail_and_more', '2024-11-20 14:23:01.803664'),
(25, 'team', '0007_conferences_shortname', '2024-11-26 07:36:50.553517'),
(26, 'team', '0008_teams_colorone_teams_colortwo', '2024-11-26 07:36:50.598663'),
(27, 'team', '0009_delete_players', '2024-11-26 13:35:15.380778'),
(28, 'players', '0001_initial', '2024-11-26 13:35:15.443257'),
(29, 'team', '0010_teams_owner', '2024-11-27 09:01:17.212585');

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
('9ut72tx9k029t9byc63a64h00fh0w0xi', '.eJxVjEEOwiAQRe_C2pBhGBBcuu8ZCIVBqoYmpV0Z765NutDtf-_9lwhxW2vYOi9hyuIilDj9bmNMD247yPfYbrNMc1uXaZS7Ig_a5TBnfl4P9--gxl6_NSnKYMF6VbAgArFCsmh0ZO08-uLBsmej2DFaTUDOGzyD5hRTKSzeH6BPNrk:1tDgz3:iZdpR2fB1-YFVzujVJk5-l4TSjywp9kgHp7m8rTnsbg', '2024-12-04 09:26:49.493863');

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

--
-- Dumping data for table `team_coachs`
--

INSERT INTO `team_coachs` (`id`, `name`, `firstName`, `poste`, `thumbnail`, `actif`, `team_id`) VALUES
(1, 'Harbaugh', 'John', 'Head Coach', 'photo/harbaugh.jpg', 1, 9);

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
(5, 'NFC East', 2),
(6, 'NFC North', 2),
(7, 'NFC South', 2),
(8, 'NFC West', 2);

-- --------------------------------------------------------

--
-- Table structure for table `team_players`
--

CREATE TABLE `team_players` (
  `id` bigint NOT NULL,
  `name` varchar(60) NOT NULL,
  `firstName` varchar(60) NOT NULL,
  `poste` varchar(50) NOT NULL,
  `thumbnail` varchar(100) DEFAULT NULL,
  `age` date NOT NULL,
  `actif` tinyint(1) NOT NULL,
  `injury` tinyint(1) NOT NULL,
  `team_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `team_players`
--

INSERT INTO `team_players` (`id`, `name`, `firstName`, `poste`, `thumbnail`, `age`, `actif`, `injury`, `team_id`) VALUES
(2, 'Mahomes', 'Patrick', 'QB', 'photo/mahomes.webp', '1995-09-17', 1, 0, 1),
(3, 'Rodgers', 'Aaron', 'QB', 'photo/rodgers.webp', '1983-12-02', 1, 0, 8),
(6, 'Barkley', 'Saquon', 'RB', 'photo/s.barkley.webp', '1997-02-07', 1, 0, 19),
(14, 'Daniels', 'Jayden', 'QB', 'photo/j_xHdpkMl.daniels.webp', '2000-12-18', 1, 0, 20),
(19, 'Hill', 'Tyreek', 'WR', 'photo/tyreek_SXAlJ4u.hill.webp', '1994-03-01', 1, 0, 6);

-- --------------------------------------------------------

--
-- Table structure for table `team_superbowls`
--

CREATE TABLE `team_superbowls` (
  `id` bigint NOT NULL,
  `town` varchar(60) NOT NULL,
  `stadium` varchar(60) NOT NULL,
  `teamOne_id` bigint DEFAULT NULL,
  `teamTwo_id` bigint DEFAULT NULL,
  `winner_id` bigint DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
  `colorTwo` varchar(15) DEFAULT NULL,
  `owner` varchar(60) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `team_teams`
--

INSERT INTO `team_teams` (`id`, `name`, `town`, `thumbnail`, `founded`, `stadium`, `division_id`, `colorOne`, `colorTwo`, `owner`) VALUES
(1, 'Chiefs', 'Kansas City', 'logo/KC.webp', '1960-01-01', 'Arrowhead Stadium', 1, '#E31837', '#FFB81C', 'Clark Hunt'),
(2, 'Broncos', 'Denver', 'logo/Broncos.webp', '1960-01-01', 'Empower Field at Mile high', 1, '#FB4F14', '#002244', NULL),
(3, 'Raiders', 'Los Angeles', 'logo/Raiders.webp', '1960-01-01', 'Allegiant Stadium', 1, '#000000', '#A5ACAF', NULL),
(4, 'Chargers', 'Los Angeles', 'logo/Chargers.webp', '1960-01-01', 'Sofi Stadium', 1, '#0080C6', '#FFC20E', NULL),
(5, 'Bills', 'Buffalo', 'logo/Bills.webp', '1960-01-01', 'Highmark Stadium', 2, '#00338D', '#C60C30', NULL),
(6, 'Dolphins', 'Miami', 'logo/Dolphins.webp', '1966-01-01', 'Hard Rock Stadium', 2, '#008E97', '#FC4C02', NULL),
(7, 'Patriots', 'New England', 'logo/Patriots.webp', '1960-01-01', 'Gillette Stadium', 2, '#002244', '#C60C30', NULL),
(8, 'Jets', 'New York', 'logo/Jets.webp', '1960-01-01', 'MetLife Stadium', 2, '#125740', '#000000', NULL),
(9, 'Ravens', 'Baltimore', 'logo/Ravens.webp', '1996-01-01', 'M&T Bank Stadium', 3, '#241773', '#9E7C0C', 'Steve Bisciotti'),
(10, 'Bengals', 'Cincinnati', 'logo/Bengals.webp', '1968-01-01', 'Paycor Stadium', 3, '#fb4f14', '#000000', NULL),
(11, 'Browns', 'Cleveland', 'logo/Browns.webp', '1946-01-01', 'Huntington Stadium', 3, '#311D00', '#ff3c00', NULL),
(12, 'Steelers', 'Pittsburgh', 'logo/Steelers.webp', '1933-01-01', 'Acrisure Stadium', 3, '#FFB612', '#101820', NULL),
(13, 'Texans', 'Houston', 'logo/Texans.webp', '2002-01-01', 'NRG Stadium', 4, '#03202f', '#A71930', NULL),
(14, 'Colts', 'Indianapolis', 'logo/Colts.webp', '1953-01-01', 'Lucas Oil Stadium', 4, '#002C5F', '#A2AAAD', NULL),
(15, 'Jaguars', 'Jacksonville', 'logo/Jaguars.webp', '1995-01-01', 'EverBank Stadium', 4, '#101820', '#D7A22A', NULL),
(16, 'Titans', 'Tennessee', 'logo/Titans.webp', '1960-01-01', 'Nissan Stadium', 4, '#0C2340', '#4B92DB', NULL),
(17, 'Cowboys', 'Dallas', 'logo/Cowboys.webp', '1960-01-01', 'AT&T Stadium', 8, '#003594', '#869397', NULL),
(18, 'Giants', 'New York', 'logo/Giants.webp', '1925-01-01', 'MetLife Stadium', 8, '#0B2265', '#a71930', NULL),
(19, 'Eagles', 'Philadelphie', 'logo/Eagles.webp', '1933-01-01', 'Lincoln Financial Field', 8, '#004C54', '#A5ACAF', NULL),
(20, 'Commanders', 'Washington', 'logo/Commanders.webp', '1932-01-01', 'Northwest Stadium', 8, '#5A1414', '#FFB612', NULL),
(21, 'Bears', 'Chicago', 'logo/Bears.webp', '1920-01-01', 'Soldier Stadium', 5, '#0B162A', '#c83803', NULL),
(22, 'Lions', 'Detroit', 'logo/Lions.webp', '1930-01-01', 'Ford Field', 5, '#0076b6', '#B0B7BC', NULL),
(23, 'Packers', 'Green Bay', 'logo/Packers.webp', '1921-01-01', 'Lambeau Stadium', 5, '#203731', '#FFB612', NULL),
(24, 'Vickings', 'Minnesota', 'logo/Vickings.webp', '1961-01-01', 'US Bank Stadium', 5, '#4F2683', '#FFC62F', NULL),
(25, 'Falcons', 'Atlanta', 'logo/Falcons.webp', '1966-01-01', 'Mercedes_Benz Stadium', 6, '#a71930', '#000000', NULL),
(26, 'Panthers', 'Carolina', 'logo/Panthers.webp', '1995-01-01', 'Bank of America Stadium', 6, '#0085CA', '#101820', NULL),
(27, 'Saints', 'New Orleans', 'logo/Saints.webp', '1967-01-01', 'Ceasars Suerdome', 6, '#D3BC8D', '#101820', NULL),
(28, 'Buccaneers', 'Tampa Bay', 'logo/Buccaneers.webp', '1976-01-01', 'Raymond James Stadium', 6, '#D50A0A', '#FF7900', NULL),
(29, 'Cardinals', 'Arizona', 'logo/Cardinals.webp', '1920-01-01', 'State Farm Stadium', 7, '#97233F', '#000000', NULL),
(30, 'Rams', 'Los Angeles', 'logo/Rams.webp', '1937-01-01', 'SoFi Stadium', 7, '#003594', '#ffa300', NULL),
(31, '49ers', 'San Francisco', 'logo/49ers.webp', '1946-01-01', '"Levi\'s® Stadium"', 7, '#AA0000', '#B3995D', NULL),
(32, 'Seahawks', 'Seattle', 'logo/Seahawks.webp', '1976-01-01', 'Lumen Fields', 7, '#002244', '#69BE28', NULL);

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
  ADD KEY `team_players_team_id_0d4ad9be_fk_team_teams_id` (`team_id`);

--
-- Indexes for table `team_superbowls`
--
ALTER TABLE `team_superbowls`
  ADD PRIMARY KEY (`id`),
  ADD KEY `team_superbowls_teamOne_id_212451f2_fk_team_teams_id` (`teamOne_id`),
  ADD KEY `team_superbowls_teamTwo_id_2d46c5c1_fk_team_teams_id` (`teamTwo_id`),
  ADD KEY `team_superbowls_winner_id_e1017237_fk_team_teams_id` (`winner_id`);

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
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

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
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `team_coachs`
--
ALTER TABLE `team_coachs`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

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
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `team_superbowls`
--
ALTER TABLE `team_superbowls`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

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
  ADD CONSTRAINT `team_players_team_id_0d4ad9be_fk_team_teams_id` FOREIGN KEY (`team_id`) REFERENCES `team_teams` (`id`);

--
-- Constraints for table `team_superbowls`
--
ALTER TABLE `team_superbowls`
  ADD CONSTRAINT `team_superbowls_teamOne_id_212451f2_fk_team_teams_id` FOREIGN KEY (`teamOne_id`) REFERENCES `team_teams` (`id`),
  ADD CONSTRAINT `team_superbowls_teamTwo_id_2d46c5c1_fk_team_teams_id` FOREIGN KEY (`teamTwo_id`) REFERENCES `team_teams` (`id`),
  ADD CONSTRAINT `team_superbowls_winner_id_e1017237_fk_team_teams_id` FOREIGN KEY (`winner_id`) REFERENCES `team_teams` (`id`);

--
-- Constraints for table `team_teams`
--
ALTER TABLE `team_teams`
  ADD CONSTRAINT `team_teams_division_id_98ac8356_fk_team_divisions_id` FOREIGN KEY (`division_id`) REFERENCES `team_divisions` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

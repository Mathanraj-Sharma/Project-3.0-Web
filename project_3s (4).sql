-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 03, 2019 at 05:39 PM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project_3s`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add mobileusers', 1, 'add_mobileusers'),
(2, 'Can change mobileusers', 1, 'change_mobileusers'),
(3, 'Can delete mobileusers', 1, 'delete_mobileusers'),
(4, 'Can view mobileusers', 1, 'view_mobileusers'),
(5, 'Can add reviews', 2, 'add_reviews'),
(6, 'Can change reviews', 2, 'change_reviews'),
(7, 'Can delete reviews', 2, 'delete_reviews'),
(8, 'Can view reviews', 2, 'view_reviews'),
(9, 'Can add complaints', 3, 'add_complaints'),
(10, 'Can change complaints', 3, 'change_complaints'),
(11, 'Can delete complaints', 3, 'delete_complaints'),
(12, 'Can view complaints', 3, 'view_complaints'),
(13, 'Can add log entry', 4, 'add_logentry'),
(14, 'Can change log entry', 4, 'change_logentry'),
(15, 'Can delete log entry', 4, 'delete_logentry'),
(16, 'Can view log entry', 4, 'view_logentry'),
(17, 'Can add permission', 5, 'add_permission'),
(18, 'Can change permission', 5, 'change_permission'),
(19, 'Can delete permission', 5, 'delete_permission'),
(20, 'Can view permission', 5, 'view_permission'),
(21, 'Can add group', 6, 'add_group'),
(22, 'Can change group', 6, 'change_group'),
(23, 'Can delete group', 6, 'delete_group'),
(24, 'Can view group', 6, 'view_group'),
(25, 'Can add user', 7, 'add_user'),
(26, 'Can change user', 7, 'change_user'),
(27, 'Can delete user', 7, 'delete_user'),
(28, 'Can view user', 7, 'view_user'),
(29, 'Can add content type', 8, 'add_contenttype'),
(30, 'Can change content type', 8, 'change_contenttype'),
(31, 'Can delete content type', 8, 'delete_contenttype'),
(32, 'Can view content type', 8, 'view_contenttype'),
(33, 'Can add session', 9, 'add_session'),
(34, 'Can change session', 9, 'change_session'),
(35, 'Can delete session', 9, 'delete_session'),
(36, 'Can view session', 9, 'view_session'),
(37, 'Can add mobileuser', 1, 'add_mobileuser'),
(38, 'Can change mobileuser', 1, 'change_mobileuser'),
(39, 'Can delete mobileuser', 1, 'delete_mobileuser'),
(40, 'Can view mobileuser', 1, 'view_mobileuser'),
(41, 'Can add review', 2, 'add_review'),
(42, 'Can change review', 2, 'change_review'),
(43, 'Can delete review', 2, 'delete_review'),
(44, 'Can view review', 2, 'view_review'),
(45, 'Can add complaint', 3, 'add_complaint'),
(46, 'Can change complaint', 3, 'change_complaint'),
(47, 'Can delete complaint', 3, 'delete_complaint'),
(48, 'Can view complaint', 3, 'view_complaint');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$150000$fry8szo8NDnk$m30M4TVlmwtkaBxpBIeXugnziek9LIY+kmsiQHRs28g=', '2019-09-03 13:44:46.134023', 1, 'Ajanthy', '', '', '2016csc031@gmail.com', 1, 1, '2019-08-30 19:37:24.722111');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE `complaint` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `geo_tag` longtext NOT NULL,
  `description` varchar(300) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `modified_at` datetime(6) NOT NULL,
  `image` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `complaint`
--

INSERT INTO `complaint` (`id`, `user_id`, `geo_tag`, `description`, `created_at`, `modified_at`, `image`) VALUES
(7, 3, '(Decimal(\'-49.8628865\'), Decimal(\'-46.300571\'))', 'Standard be account see audience. Must study throughout worker certain often between.', '2019-09-03 15:28:22.471856', '2019-09-03 15:28:22.471856', 'application/zip'),
(8, 4, '(Decimal(\'14.872592\'), Decimal(\'10.215575\'))', 'After table behind finally. Past special really car at upon bar. Policy fast yeah Congress consumer.', '2019-09-03 15:28:22.523639', '2019-09-03 15:28:22.523639', 'model/x3d+vrml'),
(9, 5, '(Decimal(\'60.6473415\'), Decimal(\'144.868062\'))', 'Describe relate try view sell reflect boy. Various discussion assume full science need. Discover well world here.', '2019-09-03 15:28:22.565471', '2019-09-03 15:28:22.566474', 'image/jpeg'),
(10, 7, '(Decimal(\'-36.933449\'), Decimal(\'-178.438338\'))', 'Voice into any speech college speak million. Activity cost low modern education cell reality.', '2019-09-03 15:28:22.644040', '2019-09-03 15:28:22.645043', 'model/example'),
(11, 2, '(Decimal(\'-19.987084\'), Decimal(\'-68.731073\'))', 'Participant laugh appear light agency decision pick. Use TV response offer late other show new. Land on cost level.', '2019-09-03 15:28:22.711833', '2019-09-03 15:28:22.711833', 'application/font-woff'),
(12, 2, '(Decimal(\'-10.243108\'), Decimal(\'86.143830\'))', 'Week information cell her across program stay. Exist father identify area house I. One kitchen machine quickly important join heart.', '2019-09-03 15:28:22.744213', '2019-09-03 15:28:22.744213', 'message/http');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2019-09-03 15:26:30.985232', '1', 'complaint object (1)', 3, '', 3, 1),
(2, '2019-09-03 15:26:31.148676', '2', 'complaint object (2)', 3, '', 3, 1),
(3, '2019-09-03 15:26:31.202938', '3', 'complaint object (3)', 3, '', 3, 1),
(4, '2019-09-03 15:26:31.335101', '4', 'complaint object (4)', 3, '', 3, 1),
(5, '2019-09-03 15:26:31.414370', '5', 'complaint object (5)', 3, '', 3, 1),
(6, '2019-09-03 15:26:31.445303', '6', 'complaint object (6)', 3, '', 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(4, 'admin', 'logentry'),
(6, 'auth', 'group'),
(5, 'auth', 'permission'),
(7, 'auth', 'user'),
(3, 'complaint', 'complaint'),
(8, 'contenttypes', 'contenttype'),
(1, 'mobileusers', 'mobileuser'),
(2, 'reviews', 'review'),
(9, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-08-30 19:34:46.334573'),
(2, 'auth', '0001_initial', '2019-08-30 19:34:47.961629'),
(3, 'admin', '0001_initial', '2019-08-30 19:34:53.648883'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-08-30 19:34:55.044714'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-08-30 19:34:55.127359'),
(6, 'contenttypes', '0002_remove_content_type_name', '2019-08-30 19:34:55.981487'),
(7, 'auth', '0002_alter_permission_name_max_length', '2019-08-30 19:34:56.897907'),
(8, 'auth', '0003_alter_user_email_max_length', '2019-08-30 19:34:57.608628'),
(9, 'auth', '0004_alter_user_username_opts', '2019-08-30 19:34:57.712392'),
(10, 'auth', '0005_alter_user_last_login_null', '2019-08-30 19:34:58.369236'),
(11, 'auth', '0006_require_contenttypes_0002', '2019-08-30 19:34:58.441820'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2019-08-30 19:34:58.534347'),
(13, 'auth', '0008_alter_user_username_max_length', '2019-08-30 19:34:59.391977'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2019-08-30 19:35:00.078305'),
(15, 'auth', '0010_alter_group_name_max_length', '2019-08-30 19:35:00.795489'),
(16, 'auth', '0011_update_proxy_permissions', '2019-08-30 19:35:00.890163'),
(17, 'complaint', '0001_initial', '2019-08-30 19:35:01.254974'),
(18, 'mobileusers', '0001_initial', '2019-08-30 19:35:01.555989'),
(19, 'reviews', '0001_initial', '2019-08-30 19:35:01.829298'),
(20, 'sessions', '0001_initial', '2019-08-30 19:35:02.219066'),
(21, 'complaint', '0002_auto_20190831_0111', '2019-08-30 19:41:59.184708'),
(22, 'mobileusers', '0002_auto_20190831_0111', '2019-08-30 19:41:59.315682'),
(23, 'reviews', '0002_auto_20190831_0111', '2019-08-30 19:41:59.618104');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('e4u4df1of9lrdygkj7yl0ag7z9g6xxr5', 'MzZlNDE5M2JmYmU5ODJlYzM4NDQ3YjM4YmI2YWRlMzk5ZGFhZGUwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyYTZmYmFmYzRkN2FiMDdiMWQ1NDJkYjUwZjI5ZTNjNDEyYmM5MjIzIn0=', '2019-09-17 13:44:46.215396');

-- --------------------------------------------------------

--
-- Table structure for table `review`
--

CREATE TABLE `review` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `queAndAnsr` longtext NOT NULL,
  `geo_tag` longtext NOT NULL,
  `device_signature` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `modified_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `review`
--

INSERT INTO `review` (`id`, `user_id`, `queAndAnsr`, `geo_tag`, `device_signature`, `created_at`, `modified_at`) VALUES
(1, 1, '', '(Decimal(\'32.2807765\'), Decimal(\'-151.437257\'))', '8382775772545', '2019-09-03 15:36:11.586042', '2019-09-03 15:36:11.586042'),
(2, 5, '', '(Decimal(\'-39.826557\'), Decimal(\'-132.574408\'))', '3948712771900', '2019-09-03 15:36:11.731459', '2019-09-03 15:36:11.732455'),
(3, 2, '', '(Decimal(\'-15.505417\'), Decimal(\'8.931279\'))', '7834020583082', '2019-09-03 15:36:11.776055', '2019-09-03 15:36:11.777060'),
(4, 5, '', '(Decimal(\'30.2089775\'), Decimal(\'-29.155498\'))', '5817979426671', '2019-09-03 15:36:11.831419', '2019-09-03 15:36:11.831419'),
(5, 7, '', '(Decimal(\'-78.124381\'), Decimal(\'-47.037291\'))', '4651106192272', '2019-09-03 15:36:11.940614', '2019-09-03 15:36:11.940614'),
(6, 3, '', '(Decimal(\'-63.631541\'), Decimal(\'95.375771\'))', '0086072402355', '2019-09-03 15:36:11.974706', '2019-09-03 15:36:11.974706');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `nic` varchar(12) DEFAULT NULL,
  `nickname` varchar(300) NOT NULL,
  `email` varchar(150) NOT NULL,
  `phoneNo` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `modified_at` datetime(6) NOT NULL,
  `image` varchar(300) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`nic`, `nickname`, `email`, `phoneNo`, `created_at`, `modified_at`, `image`) VALUES
('202548702947', 'Joanna', 'annette30@yahoo.com', '001-734-193-2973', '2019-09-03 15:12:24.285185', '2019-09-03 15:12:24.285185', 'audio/mpeg'),
('537529792271', 'Charles', 'billy39@hotmail.com', '614.904.9172', '2019-09-03 15:12:24.350513', '2019-09-03 15:12:24.350513', 'video/quicktime'),
('636399180590', 'Lisa', 'csmith@yahoo.com', '(205)897-8557', '2019-09-03 15:12:24.194616', '2019-09-03 15:12:24.195619', 'application/xml-dtd'),
('391326612319', 'Ashley', 'gregoryanderson@gmail.com', '784-719-7192x731', '2019-09-03 15:12:24.254334', '2019-09-03 15:12:24.254334', 'image/jpeg'),
('118057083034', 'Amanda', 'jonesbryan@hotmail.com', '650.494.3890x871', '2019-09-03 15:12:24.394630', '2019-09-03 15:12:24.394630', 'message/imdn+xml'),
('185390948658', 'Kenneth', 'ycox@hotmail.com', '403-445-7404', '2019-09-03 15:12:24.472838', '2019-09-03 15:12:24.472838', 'video/mp4');

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
-- Indexes for table `complaint`
--
ALTER TABLE `complaint`
  ADD PRIMARY KEY (`id`);

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
-- Indexes for table `review`
--
ALTER TABLE `review`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `complaint`
--
ALTER TABLE `complaint`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `review`
--
ALTER TABLE `review`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

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
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

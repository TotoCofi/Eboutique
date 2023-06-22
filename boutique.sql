-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : jeu. 22 juin 2023 à 09:42
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `boutique`
--

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can view permission', 1, 'view_permission'),
(5, 'Can add group', 2, 'add_group'),
(6, 'Can change group', 2, 'change_group'),
(7, 'Can delete group', 2, 'delete_group'),
(8, 'Can view group', 2, 'view_group'),
(9, 'Can add content type', 3, 'add_contenttype'),
(10, 'Can change content type', 3, 'change_contenttype'),
(11, 'Can delete content type', 3, 'delete_contenttype'),
(12, 'Can view content type', 3, 'view_contenttype'),
(13, 'Can add user', 4, 'add_users'),
(14, 'Can change user', 4, 'change_users'),
(15, 'Can delete user', 4, 'delete_users'),
(16, 'Can view user', 4, 'view_users'),
(17, 'Can add categories', 5, 'add_categories'),
(18, 'Can change categories', 5, 'change_categories'),
(19, 'Can delete categories', 5, 'delete_categories'),
(20, 'Can view categories', 5, 'view_categories'),
(21, 'Can add clients', 6, 'add_clients'),
(22, 'Can change clients', 6, 'change_clients'),
(23, 'Can delete clients', 6, 'delete_clients'),
(24, 'Can view clients', 6, 'view_clients'),
(25, 'Can add commandes', 7, 'add_commandes'),
(26, 'Can change commandes', 7, 'change_commandes'),
(27, 'Can delete commandes', 7, 'delete_commandes'),
(28, 'Can view commandes', 7, 'view_commandes'),
(29, 'Can add mode_payements', 8, 'add_mode_payements'),
(30, 'Can change mode_payements', 8, 'change_mode_payements'),
(31, 'Can delete mode_payements', 8, 'delete_mode_payements'),
(32, 'Can view mode_payements', 8, 'view_mode_payements'),
(33, 'Can add roles', 9, 'add_roles'),
(34, 'Can change roles', 9, 'change_roles'),
(35, 'Can delete roles', 9, 'delete_roles'),
(36, 'Can view roles', 9, 'view_roles'),
(37, 'Can add produits', 10, 'add_produits'),
(38, 'Can change produits', 10, 'change_produits'),
(39, 'Can delete produits', 10, 'delete_produits'),
(40, 'Can view produits', 10, 'view_produits'),
(41, 'Can add payements', 11, 'add_payements'),
(42, 'Can change payements', 11, 'change_payements'),
(43, 'Can delete payements', 11, 'delete_payements'),
(44, 'Can view payements', 11, 'view_payements'),
(45, 'Can add acheter', 12, 'add_acheter'),
(46, 'Can change acheter', 12, 'change_acheter'),
(47, 'Can delete acheter', 12, 'delete_acheter'),
(48, 'Can view acheter', 12, 'view_acheter'),
(49, 'Can add log entry', 13, 'add_logentry'),
(50, 'Can change log entry', 13, 'change_logentry'),
(51, 'Can delete log entry', 13, 'delete_logentry'),
(52, 'Can view log entry', 13, 'view_logentry'),
(53, 'Can add session', 14, 'add_session'),
(54, 'Can change session', 14, 'change_session'),
(55, 'Can delete session', 14, 'delete_session'),
(56, 'Can view session', 14, 'view_session'),
(57, 'Can add log', 15, 'add_log'),
(58, 'Can change log', 15, 'change_log'),
(59, 'Can delete log', 15, 'delete_log'),
(60, 'Can view log', 15, 'view_log');

-- --------------------------------------------------------

--
-- Structure de la table `boutique_acheter`
--

CREATE TABLE `boutique_acheter` (
  `id` bigint(20) NOT NULL,
  `quantite` int(11) NOT NULL,
  `prixcommande` int(11) NOT NULL,
  `Produit_id` bigint(20) NOT NULL,
  `commande_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `boutique_acheter`
--

INSERT INTO `boutique_acheter` (`id`, `quantite`, `prixcommande`, `Produit_id`, `commande_id`) VALUES
(1, 9, 1350, 1, 1),
(2, 200, 30000, 1, 2),
(3, 9, 1350, 1, 3),
(4, 4, 24000, 2, 3),
(5, 9, 1350, 1, 4),
(6, 4, 24000, 2, 4);

-- --------------------------------------------------------

--
-- Structure de la table `boutique_categories`
--

CREATE TABLE `boutique_categories` (
  `id` bigint(20) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `boutique_categories`
--

INSERT INTO `boutique_categories` (`id`, `nom`, `created_at`, `user_id`) VALUES
(1, 'Lait', '2023-06-14 19:04:11.096774', 2),
(2, 'Viande', '2023-06-14 19:04:24.558888', 2);

-- --------------------------------------------------------

--
-- Structure de la table `boutique_clients`
--

CREATE TABLE `boutique_clients` (
  `id` bigint(20) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `adresse` varchar(255) NOT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `boutique_clients`
--

INSERT INTO `boutique_clients` (`id`, `nom`, `adresse`, `phone`, `created_at`, `user_id`) VALUES
(1, 'Debrune', 'AKPAKPA', '90 55 35 57', '2023-06-14 19:03:57.119881', 2),
(2, 'd\'ALMEIDA akpoue', 'AKPAKPA', '90553557', '2023-06-20 08:21:47.813522', 2);

-- --------------------------------------------------------

--
-- Structure de la table `boutique_commandes`
--

CREATE TABLE `boutique_commandes` (
  `id` bigint(20) NOT NULL,
  `prixtotal` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `client_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `is_active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `boutique_commandes`
--

INSERT INTO `boutique_commandes` (`id`, `prixtotal`, `created_at`, `client_id`, `user_id`, `is_active`) VALUES
(1, 1350, '2023-06-19 14:19:55.477858', 1, 2, 0),
(2, 30000, '2023-06-20 16:23:03.853309', 2, 2, 1),
(3, 25350, '2023-06-21 16:31:37.841004', 1, 2, 1),
(4, 25350, '2023-06-21 16:32:17.150893', 1, 2, 1);

-- --------------------------------------------------------

--
-- Structure de la table `boutique_log`
--

CREATE TABLE `boutique_log` (
  `id` bigint(20) NOT NULL,
  `message` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `boutique_log`
--

INSERT INTO `boutique_log` (`id`, `message`, `created_at`, `user_id`, `type`) VALUES
(2, 'modification des informations du client Debrune', '2023-06-20 10:17:38.607109', 2, 'client'),
(3, 'Commande effectué par le clientd\'ALMEIDA akpoue', '2023-06-20 16:23:04.192513', 2, 'commande'),
(4, 'Commande effectué par le clientDebrune', '2023-06-21 16:31:38.114400', 2, 'commande'),
(5, 'Commande effectué par le clientDebrune', '2023-06-21 16:32:17.588784', 2, 'commande');

-- --------------------------------------------------------

--
-- Structure de la table `boutique_mode_payements`
--

CREATE TABLE `boutique_mode_payements` (
  `id` bigint(20) NOT NULL,
  `mode` varchar(255) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `boutique_mode_payements`
--

INSERT INTO `boutique_mode_payements` (`id`, `mode`, `user_id`) VALUES
(1, 'espèce', 2);

-- --------------------------------------------------------

--
-- Structure de la table `boutique_payements`
--

CREATE TABLE `boutique_payements` (
  `id` bigint(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `commande_id` bigint(20) NOT NULL,
  `mode_payement_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `boutique_payements`
--

INSERT INTO `boutique_payements` (`id`, `created_at`, `commande_id`, `mode_payement_id`, `user_id`) VALUES
(1, '2023-06-19 14:19:55.511566', 1, 1, 2),
(2, '2023-06-20 16:23:03.949973', 2, 1, 2),
(3, '2023-06-21 16:31:37.896862', 3, 1, 2),
(4, '2023-06-21 16:32:17.196267', 4, 1, 2);

-- --------------------------------------------------------

--
-- Structure de la table `boutique_produits`
--

CREATE TABLE `boutique_produits` (
  `id` bigint(20) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `prix` int(11) NOT NULL,
  `quantite` int(11) NOT NULL,
  `seuil` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `categorie_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `boutique_produits`
--

INSERT INTO `boutique_produits` (`id`, `nom`, `description`, `prix`, `quantite`, `seuil`, `created_at`, `categorie_id`, `user_id`) VALUES
(1, 'dolait', 'lsjdkjkksdlj', 150, 52, 5, '2023-06-14 19:05:14.258821', 1, 2),
(2, 'pintade', 'sdfssvdddgfdx', 6000, 483, 2, '2023-06-14 19:05:44.732695', 2, 2);

-- --------------------------------------------------------

--
-- Structure de la table `boutique_roles`
--

CREATE TABLE `boutique_roles` (
  `id` bigint(20) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `created_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `boutique_roles`
--

INSERT INTO `boutique_roles` (`id`, `nom`, `created_at`) VALUES
(1, 'Admin', '0000-00-00 00:00:00.000000'),
(2, 'Caissier', '0000-00-00 00:00:00.000000'),
(3, 'Gerant', '0000-00-00 00:00:00.000000');

-- --------------------------------------------------------

--
-- Structure de la table `boutique_users`
--

CREATE TABLE `boutique_users` (
  `id` bigint(20) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `password` longtext NOT NULL,
  `role_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `boutique_users`
--

INSERT INTO `boutique_users` (`id`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `phone`, `password`, `role_id`) VALUES
(2, '2023-06-21 15:38:41.700145', 1, 'dalmeidakevin910@gmail.com', 'kevin ', 'kevin', 'dalmeidakevin910@gmail.com', 1, 1, '2023-06-14 19:01:50.541948', '90553557', 'pbkdf2_sha256$600000$IElOukhp0t2nI7JX06gf33$QqPwH90unaACuarYwCnMdMg/ND8kA29smw9qhKP8L6U=', 1),
(3, '2023-06-16 10:53:21.826938', 1, 'nicoledebrune@gmail.com', 'nil', 'nicole', 'nicoledebrune@gmail.com', 1, 1, '2023-06-16 10:49:50.308488', '+22990553557', 'pbkdf2_sha256$600000$6kwh4peTGO31PVBJ42i79A$5gSDWHlNoh3kdTE6prr1SiwCDqpyUaJ/3BVMaUAVw1E=', 2);

-- --------------------------------------------------------

--
-- Structure de la table `boutique_users_groups`
--

CREATE TABLE `boutique_users_groups` (
  `id` bigint(20) NOT NULL,
  `users_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `boutique_users_user_permissions`
--

CREATE TABLE `boutique_users_user_permissions` (
  `id` bigint(20) NOT NULL,
  `users_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(13, 'admin', 'logentry'),
(2, 'auth', 'group'),
(1, 'auth', 'permission'),
(12, 'boutique', 'acheter'),
(5, 'boutique', 'categories'),
(6, 'boutique', 'clients'),
(7, 'boutique', 'commandes'),
(15, 'boutique', 'log'),
(8, 'boutique', 'mode_payements'),
(11, 'boutique', 'payements'),
(10, 'boutique', 'produits'),
(9, 'boutique', 'roles'),
(4, 'boutique', 'users'),
(3, 'contenttypes', 'contenttype'),
(14, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-06-14 18:48:53.257704'),
(2, 'contenttypes', '0002_remove_content_type_name', '2023-06-14 18:48:53.776990'),
(3, 'auth', '0001_initial', '2023-06-14 18:48:57.898228'),
(4, 'auth', '0002_alter_permission_name_max_length', '2023-06-14 18:48:58.935056'),
(5, 'auth', '0003_alter_user_email_max_length', '2023-06-14 18:48:58.977602'),
(6, 'auth', '0004_alter_user_username_opts', '2023-06-14 18:48:59.006191'),
(7, 'auth', '0005_alter_user_last_login_null', '2023-06-14 18:48:59.118025'),
(8, 'auth', '0006_require_contenttypes_0002', '2023-06-14 18:48:59.147945'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2023-06-14 18:48:59.171908'),
(10, 'auth', '0008_alter_user_username_max_length', '2023-06-14 18:48:59.228730'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2023-06-14 18:48:59.255685'),
(12, 'auth', '0010_alter_group_name_max_length', '2023-06-14 18:48:59.361152'),
(13, 'auth', '0011_update_proxy_permissions', '2023-06-14 18:48:59.418130'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2023-06-14 18:48:59.457056'),
(15, 'auth', '0013_alter_user_email', '2023-06-14 18:48:59.510349'),
(16, 'boutique', '0001_initial', '2023-06-14 18:49:20.004884'),
(17, 'admin', '0001_initial', '2023-06-14 18:52:01.379727'),
(18, 'admin', '0002_logentry_remove_auto_add', '2023-06-14 18:52:01.429280'),
(19, 'admin', '0003_logentry_add_action_flag_choices', '2023-06-14 18:52:01.478559'),
(20, 'sessions', '0001_initial', '2023-06-14 18:52:01.978040'),
(21, 'boutique', '0002_commandes_is_active', '2023-06-19 15:36:39.107114'),
(22, 'boutique', '0002_log', '2023-06-20 07:36:23.680315'),
(23, 'boutique', '0003_log_type', '2023-06-20 09:22:08.506800');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('petrj1joxubh1hrjedf1ylz9t11rzcuv', '.eJxVjUEOgjAQRe_StWkGWil1ZVy4MHoGMu2MUoFiqBiN8e6WxI3L-e_9P2_BA4ZebARhP3Ag7PgRoi1ge1mA9OMgVsKPxNk57K_HAfLdJE4pjLHh5y1ML7ExJYCEDHC-t82ceGoC5UYp_jKHvuO4ALpivIx5Pt6n4OSiyB9N8pTf9buf-zfQYmpzG71eE5CtC-UqxdZrdDUasNqca6XsugR0WhmTM48atFVIttJnQKKyAPH5Ar9kUJo:1q9Vm8:m2Z8UPmAJ3CGUC-CufkRZZjWm4g0Er0lw36v5gMS5VM', '2023-06-14 21:03:24.346439'),
('w7uso5xxz19t9yudml6msyjhgwq7qt46', '.eJxVjEEOwiAQRe_C2hDKTAu4dN8zkIGhUjWQlHZlvLtt0oVu33v_v4Wnbc1-a2nxM4ur0OLyywLFZyqH4AeVe5WxlnWZgzwSedomx8rpdTvbv4NMLe9ritizYmc7CAMkF5GCJaMcmskCuF4rCgjG7CwSKnRA7AacFDHrTonPF9hLN2U:1qA75Z:WC7EHUh2cuI-kNJ0VunoBbXmOGNRUgxaTELDPZub6Bw', '2023-06-30 10:53:57.942387'),
('yzoi3dqc6jq4l52wyn3ekzscryva8o4k', '.eJxVjEEOwiAQRe_C2hDKTAu4dN8zkIGhUjWQlHZlvLtt0oVu33v_v4Wnbc1-a2nxM4ur0OLyywLFZyqH4AeVe5WxlnWZgzwSedomx8rpdTvbv4NMLe9ritizYmc7CAMkF5GCJaMcmskCuF4rCgjG7CwSKnRA7AacFDHrTonPF9hLN2U:1qBzur:6h-ZOZCGL3C4w--hvOjcwMxWzIygfjF55RVzUCrxc1Q', '2023-07-05 15:38:41.759337');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Index pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Index pour la table `boutique_acheter`
--
ALTER TABLE `boutique_acheter`
  ADD PRIMARY KEY (`id`),
  ADD KEY `boutique_acheter_Produit_id_59a9e49b_fk_boutique_produits_id` (`Produit_id`),
  ADD KEY `boutique_acheter_commande_id_54fb06b2_fk_boutique_commandes_id` (`commande_id`);

--
-- Index pour la table `boutique_categories`
--
ALTER TABLE `boutique_categories`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`),
  ADD KEY `boutique_categories_user_id_3eff3083_fk_boutique_users_id` (`user_id`);

--
-- Index pour la table `boutique_clients`
--
ALTER TABLE `boutique_clients`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`),
  ADD UNIQUE KEY `phone` (`phone`),
  ADD KEY `boutique_clients_user_id_d89a1d21_fk_boutique_users_id` (`user_id`);

--
-- Index pour la table `boutique_commandes`
--
ALTER TABLE `boutique_commandes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `boutique_commandes_client_id_cc55fabe_fk_boutique_clients_id` (`client_id`),
  ADD KEY `boutique_commandes_user_id_bc7d0cbe_fk_boutique_users_id` (`user_id`);

--
-- Index pour la table `boutique_log`
--
ALTER TABLE `boutique_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `boutique_log_user_id_67a1ea95_fk_boutique_users_id` (`user_id`);

--
-- Index pour la table `boutique_mode_payements`
--
ALTER TABLE `boutique_mode_payements`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `mode` (`mode`),
  ADD KEY `boutique_mode_payements_user_id_fdd1075d_fk_boutique_users_id` (`user_id`);

--
-- Index pour la table `boutique_payements`
--
ALTER TABLE `boutique_payements`
  ADD PRIMARY KEY (`id`),
  ADD KEY `boutique_payements_commande_id_c0bf4bae_fk_boutique_commandes_id` (`commande_id`),
  ADD KEY `boutique_payements_mode_payement_id_5e22c0a6_fk_boutique_` (`mode_payement_id`),
  ADD KEY `boutique_payements_user_id_920ae670_fk_boutique_users_id` (`user_id`);

--
-- Index pour la table `boutique_produits`
--
ALTER TABLE `boutique_produits`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`),
  ADD KEY `boutique_produits_categorie_id_de41aa63_fk_boutique_` (`categorie_id`),
  ADD KEY `boutique_produits_user_id_2374a3f9_fk_boutique_users_id` (`user_id`);

--
-- Index pour la table `boutique_roles`
--
ALTER TABLE `boutique_roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`);

--
-- Index pour la table `boutique_users`
--
ALTER TABLE `boutique_users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `phone` (`phone`),
  ADD KEY `boutique_users_role_id_f9d06dc3_fk_boutique_roles_id` (`role_id`);

--
-- Index pour la table `boutique_users_groups`
--
ALTER TABLE `boutique_users_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `boutique_users_groups_users_id_group_id_86822a62_uniq` (`users_id`,`group_id`),
  ADD KEY `boutique_users_groups_group_id_2944bd9f_fk_auth_group_id` (`group_id`);

--
-- Index pour la table `boutique_users_user_permissions`
--
ALTER TABLE `boutique_users_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `boutique_users_user_perm_users_id_permission_id_027bfa31_uniq` (`users_id`,`permission_id`),
  ADD KEY `boutique_users_user__permission_id_2d0f73c2_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_boutique_users_id` (`user_id`);

--
-- Index pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Index pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT pour la table `boutique_acheter`
--
ALTER TABLE `boutique_acheter`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `boutique_categories`
--
ALTER TABLE `boutique_categories`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `boutique_clients`
--
ALTER TABLE `boutique_clients`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `boutique_commandes`
--
ALTER TABLE `boutique_commandes`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `boutique_log`
--
ALTER TABLE `boutique_log`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `boutique_mode_payements`
--
ALTER TABLE `boutique_mode_payements`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `boutique_payements`
--
ALTER TABLE `boutique_payements`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `boutique_produits`
--
ALTER TABLE `boutique_produits`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `boutique_roles`
--
ALTER TABLE `boutique_roles`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `boutique_users`
--
ALTER TABLE `boutique_users`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `boutique_users_groups`
--
ALTER TABLE `boutique_users_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `boutique_users_user_permissions`
--
ALTER TABLE `boutique_users_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Contraintes pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Contraintes pour la table `boutique_acheter`
--
ALTER TABLE `boutique_acheter`
  ADD CONSTRAINT `boutique_acheter_Produit_id_59a9e49b_fk_boutique_produits_id` FOREIGN KEY (`Produit_id`) REFERENCES `boutique_produits` (`id`),
  ADD CONSTRAINT `boutique_acheter_commande_id_54fb06b2_fk_boutique_commandes_id` FOREIGN KEY (`commande_id`) REFERENCES `boutique_commandes` (`id`);

--
-- Contraintes pour la table `boutique_categories`
--
ALTER TABLE `boutique_categories`
  ADD CONSTRAINT `boutique_categories_user_id_3eff3083_fk_boutique_users_id` FOREIGN KEY (`user_id`) REFERENCES `boutique_users` (`id`);

--
-- Contraintes pour la table `boutique_clients`
--
ALTER TABLE `boutique_clients`
  ADD CONSTRAINT `boutique_clients_user_id_d89a1d21_fk_boutique_users_id` FOREIGN KEY (`user_id`) REFERENCES `boutique_users` (`id`);

--
-- Contraintes pour la table `boutique_commandes`
--
ALTER TABLE `boutique_commandes`
  ADD CONSTRAINT `boutique_commandes_client_id_cc55fabe_fk_boutique_clients_id` FOREIGN KEY (`client_id`) REFERENCES `boutique_clients` (`id`),
  ADD CONSTRAINT `boutique_commandes_user_id_bc7d0cbe_fk_boutique_users_id` FOREIGN KEY (`user_id`) REFERENCES `boutique_users` (`id`);

--
-- Contraintes pour la table `boutique_log`
--
ALTER TABLE `boutique_log`
  ADD CONSTRAINT `boutique_log_user_id_67a1ea95_fk_boutique_users_id` FOREIGN KEY (`user_id`) REFERENCES `boutique_users` (`id`);

--
-- Contraintes pour la table `boutique_mode_payements`
--
ALTER TABLE `boutique_mode_payements`
  ADD CONSTRAINT `boutique_mode_payements_user_id_fdd1075d_fk_boutique_users_id` FOREIGN KEY (`user_id`) REFERENCES `boutique_users` (`id`);

--
-- Contraintes pour la table `boutique_payements`
--
ALTER TABLE `boutique_payements`
  ADD CONSTRAINT `boutique_payements_commande_id_c0bf4bae_fk_boutique_commandes_id` FOREIGN KEY (`commande_id`) REFERENCES `boutique_commandes` (`id`),
  ADD CONSTRAINT `boutique_payements_mode_payement_id_5e22c0a6_fk_boutique_` FOREIGN KEY (`mode_payement_id`) REFERENCES `boutique_mode_payements` (`id`),
  ADD CONSTRAINT `boutique_payements_user_id_920ae670_fk_boutique_users_id` FOREIGN KEY (`user_id`) REFERENCES `boutique_users` (`id`);

--
-- Contraintes pour la table `boutique_produits`
--
ALTER TABLE `boutique_produits`
  ADD CONSTRAINT `boutique_produits_categorie_id_de41aa63_fk_boutique_` FOREIGN KEY (`categorie_id`) REFERENCES `boutique_categories` (`id`),
  ADD CONSTRAINT `boutique_produits_user_id_2374a3f9_fk_boutique_users_id` FOREIGN KEY (`user_id`) REFERENCES `boutique_users` (`id`);

--
-- Contraintes pour la table `boutique_users`
--
ALTER TABLE `boutique_users`
  ADD CONSTRAINT `boutique_users_role_id_f9d06dc3_fk_boutique_roles_id` FOREIGN KEY (`role_id`) REFERENCES `boutique_roles` (`id`);

--
-- Contraintes pour la table `boutique_users_groups`
--
ALTER TABLE `boutique_users_groups`
  ADD CONSTRAINT `boutique_users_groups_group_id_2944bd9f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `boutique_users_groups_users_id_017582f4_fk_boutique_users_id` FOREIGN KEY (`users_id`) REFERENCES `boutique_users` (`id`);

--
-- Contraintes pour la table `boutique_users_user_permissions`
--
ALTER TABLE `boutique_users_user_permissions`
  ADD CONSTRAINT `boutique_users_user__permission_id_2d0f73c2_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `boutique_users_user__users_id_f40a0f6e_fk_boutique_` FOREIGN KEY (`users_id`) REFERENCES `boutique_users` (`id`);

--
-- Contraintes pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_boutique_users_id` FOREIGN KEY (`user_id`) REFERENCES `boutique_users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

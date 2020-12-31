DROP TABLE IF EXISTS `post_codes`;

CREATE TABLE `post_codes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `postcode` varchar(20) DEFAULT NULL,
  `outcode` varchar(10) DEFAULT NULL,
  `incode` varchar(10) DEFAULT NULL,
  `quality` int(11) DEFAULT NULL,
  `eastings` int(11) DEFAULT NULL,
  `northings` int(11) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `nhs_ha` varchar(100) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  `latitude` varchar(20) DEFAULT NULL,
  `parish` varchar(150) DEFAULT NULL,
  `codes` json DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `postcode` (`postcode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `upload_files`;

CREATE TABLE `upload_files` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `path` varchar(200) DEFAULT NULL,
  `processed_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

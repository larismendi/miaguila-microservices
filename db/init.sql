CREATE DATABASE IF NOT EXISTS db_miaguila;
USE db_miaguila;

DROP TABLE IF EXISTS upload_files;
DROP TABLE IF EXISTS post_codes;

CREATE TABLE upload_files (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100),
  path VARCHAR(200),
  processed_at TIMESTAMP NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NULL
);

CREATE TABLE post_codes (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  postcode VARCHAR(20) UNIQ,
  outcode VARCHAR(10),
  incode VARCHAR(10),
  quality INTEGER,
  eastings INTEGER NULL,
  northings INTEGER NULL,
  country VARCHAR(50),
  nhs_ha VARCHAR(100) NULL,
  longitude VARCHAR(50),
  latitude VARCHAR(20),
  parish VARCHAR(150),
  codes JSON NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NULL,
  UNIQUE(postcode)
);

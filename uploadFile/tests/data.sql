INSERT INTO `upload_files` (`name`, `path`)
VALUES
  ('test.csv', '/shared_folder/test.csv');

INSERT INTO `post_codes` (`postcode`, `outcode`, `incode`, `quality`, `eastings`, `northings`,
  `country`, `nhs_ha`, `longitude`, `latitude`, `parish`, `codes`)
VALUES
  ('CF24 2BT', 'CF24', '2BT', 1, '319675', '176305', 'Wales', 'Cardiff and Vale University Health Board',
   '-3.158076',	'51.479976', 'Splott', {"ccg": "W11000029", "ced": "W99999999", "lau2": "W05000879", "lsoa": "W01001874", "msoa": "W02000404", "nuts": "UKL22", "ccg_id": "7A4", "parish": "W04001005", "admin_ward": "W05000879", "admin_county": "W99999999", "admin_district": "W06000015", "parliamentary_constituency": "W07000080"});
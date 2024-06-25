-- This module is the MySQL server setup script for development environment.
--   It creates a new user and a new database for the application.

CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- Create a user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Setting a password for hbnb_test user
ALTER USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Granting all privileges to hbnb_test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Granting SELECT privileges to hbnb_test user on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

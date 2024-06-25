-- This module is the MySQL server setup script for development environment.
--   It creates a new user and a new database for the application.

CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

-- Create a user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Setting a password for hbnb_dev user
ALTER USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Granting all privileges to hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Granting SELECT privileges to hbnb_dev user on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

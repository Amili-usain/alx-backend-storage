-- This SQL script creates a table 'users' with the specified attributes.
-- If the table already exists, the script will not fail and will continue executing.

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);

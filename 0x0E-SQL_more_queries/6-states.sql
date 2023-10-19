-- Crée la base de données 'hbtn_0d_usa' si elle n'existe pas
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Utilise la base de données 'hbtn_0d_usa'
USE hbtn_0d_usa;

-- Crée la table 'states' si elle n'existe pas
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (id)
);


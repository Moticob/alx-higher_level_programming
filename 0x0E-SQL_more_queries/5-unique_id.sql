-- Crée la table 'unique_id' si elle n'existe pas
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1,
    name VARCHAR(256),
    UNIQUE (id)
);


-- Crée l'utilisateur 'user_0d_1' s'il n'existe pas
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Accorde tous les privilèges à 'user_0d_1'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Recharge les privilèges pour que les modifications prennent effet
FLUSH PRIVILEGES;


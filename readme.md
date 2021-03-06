# Wallet
Wallet connector for trading bot


## Wallet_Connector :
  - getUSDTbalance() : retourne Le Balance future, Unrealized PNL, Available Balance
  - addBalance(Balance, UnrealizedPNL, availUSDT): Requete vers la base de données et ajoute dans la table wallet une ligne avec le current timestamp et les elements
 
 
 ## Main 
  - Appel des deux fonctions Wallet connector
  - Doit etre utilisé comme un cron jobs pour effectuer des relevés tout les X temps


## Config
  - Pour faire fonctionner ce programme il faut ajouter un fichier config avec 7 paramètres :
      - API_KEY_BINANCE
      - API_SECRET_BINANCE
      - host_db
      - user_db
      - port_db
      - password_db
      - database
  - Fichier config dans gitignore

## Base de données
  - Base de données situés sur la variable host_db:port_db du fichier config.py
  - Il faut créer une table dans une base de données nommé Wallet
```SQL
CREATE TABLE wallet (ID INT PRIMARY KEY AUTO_INCREMENT, Balance FLOAT, Unrealized_PNL FLOAT, availableUSDT FLOAT, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
```
  - Création d'un utilisateur user_db qui accède en INSERT, SELECT à database.wallet 
```SQL
CREATE USER wallet@host IDENTIFIED BY 'password_db';
   # host est l'ip du serveur avec le programme wallet, localhost si la base de données est situé en local
GRANT SELECT, INSERT on database.wallet to wallet@host;
```
  - Firewall à ouvrir avec port_db sur la machine base de données host_db
  - Utilisation du module python mysql.connector
```BASH
python3 -m pip install mysql.connector
```

## Connection avec Binance
  - La connection avec Binance se fait grace à paire de clés (public/privée) situé dans le fichier config.py, pour obtenir ces clés API, rendez vous sur votre compte Binance
  - Un module python est utilisé pour communiquer avec l'API, python-binance, il faut le télécharger
```BASH
python3 -m pip install python-binance
```

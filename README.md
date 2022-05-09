# Wallet
Wallet connector for trading bot

Si vous avez un bot de trading sur votre compte Binance Futures, ce module python vous permet de sauvegarder vos gains / pertes et l'état de votre balance dans une table de votre base de données

## Installation
  - Cloner ce dépot
  - Installer les modules python
  - Créer une table dans votre base de données
  - Créer un cronjob pour éxécuter le script de facon régulière

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
## Cronjob
  - Créer un cronjob (éxécution à intervalle de temps réguliers) :
  - */<font color="green">X</font> * * * * /bin/python3 /home/user/Wallet/main.py
## Base de données
  - Base de données situés sur la variable host_db:port_db du fichier config.py
  - Il faut créer une table dans une base de données nommé Wallet
```SQL
CREATE TABLE wallet (ID INT PRIMARY KEY AUTO_INCREMENT, Balance FLOAT, Unrealized_PNL FLOAT, availableUSDT FLOAT, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
```
  - Création d'un utilisateur user_db qui accède en INSERT, SELECT à database.wallet 
```SQL
CREATE USER wallet@host IDENTIDIEF BY 'password_db';
   # host est l'ip du serveur avec le programme wallet, localhost si la base de données est situé en local
GRANT SELEXT, INSERT on database.wallet to wallet@host;
```
  - Firewall à ouvrir avec port_db sur la machine base de données host_db
```BASH
sudo firewall-cmd --add-service=mysql --permanent
```
  - Utilisation du module python mysql.connector
```BASH
python3 -m pip install mysql.connector
```
 ## Connection avec Binance
  - Utilisation du module python 
 ```BASH
python3 -m pip install python-binance
```
  - Utilisation des clés API disponible depuis votre compte Binance, à mettre dans le fichier config.py
 
 ## Wallet_Connector :
  - getUSDTbalance() : retourne Le Balance future, Unrealized PNL, Available Balance
  - addBalance(Balance, UnrealizedPNL, availUSDT): Requete vers la base de données et ajoute dans la table wallet une ligne avec le current timestamp et les elements
 
 
 ## Main 
  - Appel des deux fonctions Wallet connector
  - Doit etre utilisé comme un cron jobs pour effectuer des relevés tout les X temps

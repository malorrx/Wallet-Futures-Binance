# Wallet
Wallet connector for trading bot


## Wallet_Connector :
  - getUSDTbalance() : retourne Le Balance future, Unrealized PNL, Available Balance
  - addBalance(Balance, UnrealizedPNL, availUSDT): Requete vers la base de données et ajoute dans la table wallet une ligne avec le current timestamp et les elements
 
 
 ## Main 
  - Appel des deux fonctions Wallet connector
  - Doit etre utilisé comme un cron jobs pour effectuer des relevés tout les X temps


## Config
  - Pour faire fonctionner ce programme il faut ajouter un fichier config avec 7 paramètres

import Wallet_connector

Balance = Wallet_connector.getUSDTbalance()
Wallet_connector.addBalance(Balance[0], Balance[1], Balance[2])

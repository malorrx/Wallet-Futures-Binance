from asyncio import futures
from binance.client import Client
from binance.enums import *
import time
import numpy as np
import talib
import config
import mysql.connector

#connexion à l'API de Binance
client = Client(config.API_KEY_BINANCE, config.API_SECRET_BINANCE)

connection_params = {
        'host' : config.host_db,
        'user': config.user_db,
        'password' : config.password_db,
        'database' : config.database,
        'port' : config.port_db,
    }


def getUSDTbalance():
    balance = client.futures_account_balance()
    futures_account = client.futures_account()
    totalWalletBalance = 0
    availableBalance = 0
    for actif in balance:
        totalWalletBalance = totalWalletBalance + float(actif['balance'])
        availableBalance = availableBalance + float(actif['withdrawAvailable'])
    time.sleep(0.2)
    unrealizedPNL = 0
    for actif in futures_account['assets']:
        unrealizedPNL = unrealizedPNL + float(actif['unrealizedProfit'])
    return totalWalletBalance, unrealizedPNL, availableBalance

def addBalance(Balance, unrealizedPNL, availUSDT):
    request = """insert into wallet
             (Balance, Unrealized_PNL, availableUSDT)
             values (%s, %s, %s)"""
    params = (Balance, unrealizedPNL, availUSDT)
    try:
        with mysql.connector.connect(**connection_params) as db :
            with db.cursor() as c:
                c.execute(request, params)
                db.commit()
                return True
    except Exception as err:
        print('mysql_connector.addBallance Error : ' + str(err))
        return False
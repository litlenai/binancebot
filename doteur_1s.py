import time
import math
import itertools
from binance.client import Client
from binance.streams import BinanceSocketManager
from twisted.internet import reactor
from binance.enums import *
import mysql.connector
from datetime import datetime
from datetime import timedelta
import time
##################CONEXION CON LA API BINANCE###################################
api_key    = 'VGck9bmV6qj54MJMuimqYmXvJ0IBc6OgPbMdvPPWek5036EsMR9pHeuLlnIcT3RX'#
api_secret = 'xt9ytOKWit3FTBPRhruYJoWAqliZc42fM9QWywiOwkXfVesajLoXBnwPcJ7ntnm5'#
client = Client(api_key, api_secret)                                           #
################################################################################

#####################VARIABLES#####################
moneda="DOTEUR"
btc_price = client.get_symbol_ticker(symbol=moneda)
price_actual=float(btc_price["price"])
now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
valor_original = price_actual
<<<<<<< HEAD
porcentaje_aumento = 8
=======
porcentaje_aumento = 9
>>>>>>> 6a4fb584313436b4d280b725d0ec7d5782442bd9
descuento = valor_original * (porcentaje_aumento / 100)
valor_con_descuento = valor_original - descuento
valor_con_aumento = valor_con_descuento + descuento
format_buy = "{:.2f}".format(valor_con_descuento)
format_sell = "{:.2f}".format(valor_con_aumento)

mydb = mysql.connector.connect(
  host="192.168.1.150",
  user="root",
  password="21Mayo2k",
  database="trade"
)
  
while 1 == 1:
    btc_price = client.get_symbol_ticker(symbol=moneda)
    price_actual=float(btc_price["price"])  
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    mycursor = mydb.cursor()
    sql = "INSERT INTO doteur_1s (price, time, comprar) VALUES (%s, %s, %s)"
    val = (price_actual, formatted_date, format_buy)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    time.sleep(1)

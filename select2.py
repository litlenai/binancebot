import mysql.connector
import os
os.linesep
import time
from datetime import datetime
from datetime import timedelta
from binance.client import Client
from binance.streams import BinanceSocketManager
from twisted.internet import reactor
from binance.enums import *
##################CONEXION CON LA API BINANCE###################################
api_key    = 'VGck9bmV6qj54MJMuimqYmXvJ0IBc6OgPbMdvPPWek5036EsMR9pHeuLlnIcT3RX'#
api_secret = 'xt9ytOKWit3FTBPRhruYJoWAqliZc42fM9QWywiOwkXfVesajLoXBnwPcJ7ntnm5'#
client = Client(api_key, api_secret)                                           #
################################################################################
moneda="DOTEUR"
btc_price = client.get_symbol_ticker(symbol=moneda)
price_actual=float(btc_price["price"])
################################################################################
connection = mysql.connector.connect(host='192.168.1.150', database='trade', user='root', password='21Mayo2k')
################################################################################
cursor = connection.cursor()
cursor.execute("select count(*) from doteur_1s")
fixture_count = cursor.fetchone()[0]
print ("Hay un total de: ", fixture_count, "registros")
time.sleep(3)
################################################################################
valor_original = 10
porcentaje_aumento = 1
descuento = valor_original * (porcentaje_aumento / 100)
valor_con_descuento = valor_original - descuento
valor_con_aumento = valor_con_descuento + descuento
format_buy = "{:.2f}".format(valor_con_descuento)
format_sell = "{:.2f}".format(valor_con_aumento)
################################################################################
for i in range(fixture_count):
    sql_select_Query = """SELECT price FROM `doteur_1s` LIMIT 1 OFFSET %s""" %(i)
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    for row in records:
        # print("value: ", row[0])
        var1=row[0]
    if var1 > float(format_buy):
        print(var1, "Es mayor que ", format_buy)
        f = open("Bigger.txt", "a")
        f.write(str(i))
        f.write('\n')
        f.close()
    else:
        print(var1, "No es mayor a ", format_buy)
        f = open("Lowest.txt", "a")
        f.write(str(i))
        f.write('\n')
        
        f.close()
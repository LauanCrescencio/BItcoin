from flask import Blueprint,Flask,render_template
import requests #type: ignore
import datetime
time_out = 0
pagina_princial = Blueprint(__name__,"home")

@pagina_princial.route("/")
def Pegar_cotacao():
    global time_out 
    global btc
    global dolar
    global eth
    if(datetime.datetime.now().minute >= time_out):
        time_out = datetime.datetime.now().minute + 3
        btc = requests.get("https://economia.awesomeapi.com.br/json/last/btc-brl").json()
        dolar = requests.get("https://economia.awesomeapi.com.br/json/last/usd-brl").json()
        eth = requests.get("https://economia.awesomeapi.com.br/json/last/eth-brl").json()
        if (btc and dolar and eth):
            return render_template("index.html",btc_bid=btc["BTCBRL"]
                                  ["bid"],btc_min=btc["BTCBRL"]
                                  ['low'],
                                  btc_max=btc["BTCBRL"]["high"],
                                    dolar_bid=dolar["USDBRL"]["bid"],
                                    dolar_high=dolar["USDBRL"]["high"],
                                    dolar_low=dolar["USDBRL"]["low"],
                                    eth_bid=eth["ETHBRL"]["bid"],
                                    eth_low=eth["ETHBRL"]["low"],
                                    eth_max=eth["ETHBRL"]["high"],
                                    Horario=datetime.datetime.now().hour,
                                    minuto=datetime.datetime.now().minute
                                    )
    else : 
      return render_template("index.html",btc_bid=btc["BTCBRL"]
                                  ["bid"],btc_min=btc["BTCBRL"]
                                  ['low'],
                                  btc_max=btc["BTCBRL"]["high"],
                                    dolar_bid=dolar["USDBRL"]["bid"],
                                    dolar_high=dolar["USDBRL"]["high"],
                                    dolar_low=dolar["USDBRL"]["low"],
                                    eth_bid=eth["ETHBRL"]["bid"],
                                    eth_low=eth["ETHBRL"]["low"],
                                    eth_max=eth["ETHBRL"]["high"],
                                    Horario=datetime.datetime.now().hour,
                                    minuto=datetime.datetime.now().minute)



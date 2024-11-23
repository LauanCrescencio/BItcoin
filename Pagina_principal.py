import threading
from flask import Blueprint,Flask,render_template
import requests #type: ignore
import datetime
time_out = 0
pagina_princial = Blueprint(__name__,"home")
dados_request = requests.get("https://economia.awesomeapi.com.br/json/last/btc-brl,usd-brl,eth-brl").json()

@pagina_princial.route("/")
def Pegar_cotacao():
    global time_out 
    global dados_request,testandoo
    if(datetime.datetime.now().minute >= time_out):
            time_out = datetime.datetime.now().minute + 6
            dados_request = requests.get("https://economia.awesomeapi.com.br/json/last/btc-brl,usd-brl,eth-brl,eur-brl,doge-brl,rub-brl").json()
            testandoo = dados_request
    if (dados_request):
            return render_template("index.html",btc_bid=dados_request["BTCBRL"]
                                  ["bid"],btc_min=dados_request["BTCBRL"]
                                  ['low'],
                                  btc_max=dados_request["BTCBRL"]["high"],
                                    dolar_bid=dados_request["USDBRL"]["bid"],
                                    dolar_high=dados_request["USDBRL"]["high"],
                                    dolar_low=dados_request["USDBRL"]["low"],
                                    eth_bid=dados_request["ETHBRL"]["bid"],
                                    eth_low=dados_request["ETHBRL"]["low"],
                                    eth_max=dados_request["ETHBRL"]["high"],
                                    Horario=dados_request["ETHBRL"]["create_date"],
                                    euro_bid=dados_request["EURBRL"]["bid"],
                                    euro_max=dados_request["EURBRL"]["high"],
                                    euro_min=dados_request["EURBRL"]["low"],
                                    doge_bid=dados_request["DOGEBRL"]["bid"],
                                    doge_max=dados_request["DOGEBRL"]["high"],
                                    doge_min=dados_request["DOGEBRL"]["low"],
                                    rublo_bid=dados_request["RUBBRL"]["bid"],
                                    rublo_max=dados_request["RUBBRL"]["high"],
                                    rublo_min=dados_request["RUBBRL"]["low"],                                      
                                    ),200
    else : 
      return render_template("index.html",btc_bid=dados_request["BTCBRL"]
                                  ["bid"],btc_min=dados_request["BTCBRL"]['low'],
                                    btc_max=dados_request["BTCBRL"]["high"],
                                    dolar_bid=dados_request["USDBRL"]["bid"],
                                    dolar_high=dados_request["USDBRL"]["high"],
                                    dolar_low=dados_request["USDBRL"]["low"],
                                    eth_bid=dados_request["ETHBRL"]["bid"],
                                    eth_low=dados_request["ETHBRL"]["low"],
                                    eth_max=dados_request["ETHBRL"]["high"],
                                    Horario=dados_request["ETHBRL"]["create_date"],
                                    euro_bid=dados_request["EURBRL"]["bid"],
                                    euro_max=dados_request["EURBRL"]["high"],
                                    euro_min=dados_request["EURBRL"]["low"],
                                    doge_bid=dados_request["DOGEBRL"]["bid"],
                                    doge_max=dados_request["DOGEBRL"]["high"],
                                    doge_min=dados_request["DOGEBRL"]["low"],
                                    rublo_bid=dados_request["RUBBRL"]["bid"],
                                    rublo_max=dados_request["RUBBRL"]["high"],
                                    rublo_min=dados_request["RUBBRL"]["low"], ),200



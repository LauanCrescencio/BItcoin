
import datetime
import os
from flask import Blueprint,request,redirect,render_template
import peewee
from Database.database import Usuarios
app = Blueprint("Salvando email",__name__)
caracteres_proibidos = ['%','*','/','(','#','`']

@app.route("/",methods=["POST"])
def Salvando_email_db():
    nome = request.form.get("nome")
    email = request.form.get("email")
    if verificando_valores(nome,email) and not os.path.exists("log.txt"):
        with open("log.txt",'w') as arquivo:
            arquivo.write("")
        Enviar_pra_db(nome,email)
        os.remove("log.txt")
        return '22'
    return 'aa'

def verificando_valores(nome : str, email : str): 
    if not isinstance(nome,str) or not isinstance(email,str):
        return False
    if len(nome) < 2 or len(nome) > 30:
        return False # false e erro de nome invalido
    if len(email) > 30 or len(email) < 4  :
        return None #  none e erro de email invalido
    for caracter in caracteres_proibidos:
        if caracter in email :
            return None
        if caracter in nome:
            return False
    if not '@' in email or not ".com" in email:
        return None
    if not email.split(".")[1] == 'com':
        return None
    if Usuarios.select().where((Usuarios.email == email)).exists():
        return False
    return True

def Enviar_pra_db(nome : str, email : str):
    Usuarios.create(nome=nome,email=email,inserido_data=datetime.datetime.now().date())


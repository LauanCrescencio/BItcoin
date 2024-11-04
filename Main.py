import flask
from Pagina_principal import pagina_princial
from Enviar_emails import app as comando
from Salvar_email_page import app as page2

app = flask.Flask(__name__)

app.register_blueprint(pagina_princial,url_prefix="/")
app.register_blueprint(comando)
app.register_blueprint(page2,url_prefix="/Enviar")



@app.route("/cadastro",methods=['GET','POST'])
def Pagina_de_cadastro():
    return flask.render_template("page2.html"),200
app.run(debug=True)
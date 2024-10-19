import flask
from Pagina_principal import pagina_princial

app = flask.Flask(__name__)

app.register_blueprint(pagina_princial,url_prefix="/")


@app.route("/cadastro")
def Pagina_de_cadastro():
    return flask.render_template("page2.html")


@app.route("/Enviar",methods=["POST"])
def enviando():
    nome = flask.request.form.get('Nome')
    email = flask.request.form.get("Email")
    return f"{nome} + {email}"




app.run(debug=True)
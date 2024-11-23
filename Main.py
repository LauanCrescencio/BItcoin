import flask
from Pagina_principal import pagina_princial
from Script_cotacoes_6_25 import app as Atualizar_cotacoes, Funcao_principal 
from Page_cadastro import app as Pagina_cadastro
from apscheduler.schedulers.background import BackgroundScheduler  # type: ignore
from Page_Desinscrever import app as Pagina_desinscrever
from Page_codigos_mail import app as Pagina_codigos
app = flask.Flask(__name__)

# Registra as páginas como blueprints
app.register_blueprint(pagina_princial, url_prefix="/")
app.register_blueprint(Pagina_cadastro, url_prefix="/Enviar")
app.register_blueprint(Atualizar_cotacoes)
app.register_blueprint(Pagina_desinscrever, url_prefix="/desinscrever")
app.register_blueprint(Pagina_codigos, url_prefix="/codigo")


# Configuração do APScheduler
scheduler = BackgroundScheduler()
scheduler.add_job(Funcao_principal, 'cron', hour=22, minute=34)
scheduler.start()

# Adicione um gancho para parar o scheduler quando o app for finalizado
@app.teardown_appcontext
def shutdown_scheduler(exception=None):
    if scheduler.running:  # Verifique se o scheduler está ativo antes de tentar desligá-lo
        scheduler.shutdown(wait=False)

# Define a página de cadastro
@app.route("/cadastro")
def Pagina_de_cadastro():
    return flask.render_template("page2.html"), 200

# Executa a aplicação Flask
if __name__ == "__main__":
    app.run(debug=True)

import email.message as email
import smtplib
from codigo_login_gmail import codigo
body_email = f''' <!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cotação do Bitcoin</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }}

        .container {{
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}

        .header {{
            text-align: center;
            padding: 20px;
            background-color: #f7931a;
            color: #ffffff;
        }}

        .header h1 {{
            margin: 0;
        }}

        .content {{
            text-align: center; /* Centraliza o conteúdo e o botão */
        }}

        .content a {{
            margin: 20px 0;
        }}

        .content p {{
            font-size: 18px;
            color: #333333;
            line-height: 1.6;
        }}

        .cta-button {{
            display: inline-block;
            background-color: #f7931a;
            color: #ffffff;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            font-size: 16px;
            text-align: center;
            margin: 20px auto; /* Centraliza o botão com margem automática */
        }}

        .footer {{
            text-align: center;
            padding: 10px;
            background-color: #f4f4f4;
            font-size: 14px;
            color: #777777;
        }}

    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Resumo do valor do bitcoin Hoje</h1>
        </div>
        <div class="content">
            <p>Olá, Senhor {{ nome_cadastrado }}</p>
            <p>Este e um breve resumo do valor do bitcoin hoje dia {{ dia_hoje }}, para mais informacoes sobre cotacoes de outras moedas, acesse nosso site clicando abaixo</p>
            <ul>
                <li><strong> A maior Alta de hoje :</strong> R$ {{ alta }}</li>
                <li><strong> A maior baixa de hoje :</strong> R$ {{ baixa }}</li>
                <li><strong> Valor de Compra Atual :</strong> R$ {{ valor_compra }}</li>

            </ul>
            <p>Acompanhe as cotacoes em tempo real em nosso site</p>
            <p><a href="https://www.seusite.com" class="cta-button">Confira a Cotação Atual</a></p>
        </div>
        <div class="footer">
            <p>Você está recebendo este e-mail porque se inscreveu para receber atualizações sobre o Bitcoin.</p>
            <p><a href="https://www.seusite.com/unsubscribe">Cancelar inscrição</a></p>
        </div>
    </div>
</body>
</html>
'''
coneccao = smtplib.SMTP("smtp.gmail.com",587)
coneccao.starttls()
coneccao.login("verificar254@gmail.com",codigo)


corpo_email = email.Message()
corpo_email["from"] = "verificar254@gmail.com"
corpo_email['subject'] = "Resumo das Moedas"
corpo_email.add_header("Content-Type","text/html")
corpo_email.set_payload(body_email,"utf-8")
def Enviar_email(addres : str):
    corpo_email["to"] = addres
    coneccao.sendmail("verificar254@gmail.com",addres,corpo_email.as_string())
Enviar_email("smtmw47@gmail.com")
    




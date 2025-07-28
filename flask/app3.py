from datetime import datetime
from flask import Flask, request, jsonify, make_response, redirect, url_for, render_template

app = Flask(__name__)

# herança de template
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

# componentes
@app.route("/teste")
def teste():
    return render_template("teste.html")

# form
@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        # processando forms

        # 1 - resgata variaveis
        nome = request.form.get("nome")
        email = request.form.get("email")
        msg = request.form.get("mensagem")

        # 2 - trata / valida os dados

        # 3 - se algo der errado, volta msg para o usuário

        # 4 - faz o processo final (email, redirecionar pag., salvar banco)
        return render_template("resultado.html", nome=nome, email=email, msg=msg)

    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)

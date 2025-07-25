from datetime import datetime
from flask import Flask, request, jsonify, make_response, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/api", methods=["GET", "POST", "PUT", "DELETE"])
def api():
    if request.method == "GET":
        return jsonify({"message": "Método GET ativado."})
    elif request.method == "POST":
        return jsonify({"message": "Método POST ativado."})
    elif request.method == "PUT":
        return jsonify({"message": "Método PUT ativado."})
    elif request.method == "DELETE":
        return jsonify({"message": "Método DELETE ativado."})

# criando views
@app.route("/custom-response")
def custom_response():
    resposta = make_response("Texto com cabeçalhos personalizados", 200)
    resposta.headers["Custom-Header"] = "OlaFlask"
    return resposta

@app.route("/")
def home():
    return "Bem-vindo ao seu primeiro app de Flask"

@app.route("/redirect")
def redirecionamento():
    return redirect(url_for("home"))

# Iniciando com Jinja
@app.route("/teste-jinja")
def teste_jinja():
    return render_template("index.html", nome="Diego", idade=39)

# Loops
@app.route("/usuarios")
def usuarios():
    lista_usuarios = [
        {"nome": "Ana", "email": "ana@gmail.com"},
        {"nome": "Pedro", "email": "pedro@gmail.com"},
        {"nome": "João", "email": "joao@gmail.com"}
    ]

    return render_template("usuarios.html", usuarios=lista_usuarios, data=datetime.now())

if __name__ == "__main__":
    app.run(debug=True)

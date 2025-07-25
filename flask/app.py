from flask import Flask, jsonify

app = Flask(__name__)

# rota login -> site.com/login

@app.route("/")
def home():
    return "Bem-vindo ao seu primeiro app de Flask"

# rotas

@app.route("/api/data")
def api_data():
    data = {"nome": "Flask", "versao": "3.1"}
    return jsonify(data)

@app.route("/user/<username>")
def user_profile(username):
    return f"Perfil do usuario: {username}"

if __name__ == "__main__":
    app.run(debug=True)

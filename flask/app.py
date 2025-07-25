from flask import Flask, jsonify

app = Flask(__name__)

# rota login -> site.com/login

@app.route("/")
def home():
    return "Bem-vindo ao seu primeiro app de Flask"

if __name__ == "__main__":
    app.run(debug=True)

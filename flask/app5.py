from wtforms import StringField, PasswordField, SubmitField, ValidationError
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, make_response, redirect, url_for, render_template, request, flash, get_flashed_messages
from datetime import datetime
import os
from dotenv import load_dotenv

# conexao com banco
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///meubanco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# model
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)

# criação de estrutura de banco
with app.app_context():
    db.create_all()

print("Banco de dados criado com sucesso!")

# criação de usuários e listagem
@app.route("/criar_usuario", methods=["GET", "POST"])
def criar_usuario():

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")

        novo_usuario = Usuario(nome=nome, email=email)

        db.session.add(novo_usuario)

        db.session.commit()

        return redirect(url_for("listar_usuarios"))

    return render_template("criar_usuario.html")

@app.route("/listar_usuarios")
def listar_usuarios():
    usuarios = Usuario.query.all()

    return render_template("listar_usuarios.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)

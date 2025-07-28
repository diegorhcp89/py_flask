from wtforms import StringField, PasswordField, SubmitField, ValidationError
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from flask import Flask, jsonify, make_response, redirect, url_for, render_template, flash, get_flashed_messages
from datetime import datetime

app = Flask(__name__)
# ajuda a proteger contra CSRF
app.config["SECRET_KEY"] = 'chave-secreta'

# aula 1 - iniciando com flask wtf
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Entrar")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return redirect(url_for("sucesso"))
    else:
        print("USUARIO E SENHA NAO ENCONTRADOS!")

    return render_template("login.html", form=form)

@app.route("/sucesso")
def sucesso():
    return "Login realizado com sucesso!"

# validação personalizada
def validar_nome(form, field):
    if len(field.data) < 3:
        raise ValidationError("O nome deve ter pelo menos 3 caracteres")

class CadastroForm(FlaskForm):
    nome = StringField("Nome", validators=[validar_nome])
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Entrar")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form = CadastroForm()

    if form.validate_on_submit():
        return redirect(url_for("sucesso"))

    return render_template("cadastro.html", form=form)

# flash messages
@app.route("/mensagem")
def mensagem():
    flash("Esta é uma mensagem flash!", "sucess")
    return render_template("mensagem.html")

if __name__ == "__main__":
    app.run(debug=True)

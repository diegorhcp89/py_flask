from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from flask import Flask, jsonify, make_response, redirect, url_for, render_template
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

if __name__ == "__main__":
    app.run(debug=True)

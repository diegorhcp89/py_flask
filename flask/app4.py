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
    submit = SubmitField("Entar")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)

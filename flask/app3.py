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

if __name__ == "__main__":
    app.run(debug=True)

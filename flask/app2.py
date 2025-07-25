from flask import Flask, request, jsonify

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

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, request

app = Flask(__name__)


# A simple route
@app.route("/")
def home():
    return "Flask is running!"


# Example API route
@app.route("/api/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({"you_sent": data})


if __name__ == "__main__":
    app.run(debug=True)

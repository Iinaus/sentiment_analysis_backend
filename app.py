from flask import Flask, jsonify, request
from flask_cors import CORS
import jwt
import datetime
import bcrypt

from model_training import train_model
from config import Config


app = Flask(__name__)
CORS(app)

JWT_SECRET = Config.JWT_SECRET
USERNAME = Config.USERNAME
PASSWORD_HASH = Config.PASSWORD_HASH

@app.route('/')
def hello_world():
    return "<p> Hello World! Webhook test</p>"

@app.route('/login', methods=['POST'])
def login():
    auth = request.json
    if auth and auth.get("username") == USERNAME:
        if bcrypt.checkpw(auth.get("password").encode('utf-8'), PASSWORD_HASH.encode('utf-8')):
            token = jwt.encode(
                {'user': auth["username"], 'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)},
                JWT_SECRET, algorithm="HS256"
            )
            return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/evaluate', methods=['POST'])
def evaluate():
    try:
        model = train_model()
        data = request.json

        if "sentence" not in data:
            return jsonify({"error": "No sentence provided in the request"}), 400

        sentence = data["sentence"]
        result = model.predict([sentence])
        sentiment = result[0]

        response = {
            "message": "Sentiment analysis complete",
            "sentence": sentence,
            "sentiment": sentiment
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
        

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=False)
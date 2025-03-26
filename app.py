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

def authorize(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Token is missing!"}), 403
        
        try:
            token = token.split(" ")[1]
            data = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired!"}), 403

        except Exception as e:
            return jsonify({"error": "Invalid token!"}), 403
        
        return func(*args, **kwargs)
    return wrapper


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
@authorize
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
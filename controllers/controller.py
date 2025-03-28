import bcrypt
from flask import jsonify, request

from config import Config
from decorators.authorize import authorize
from services.auth_service import create_token
from services.model_training import get_model


def login():
    auth = request.json
    if auth and auth.get("username") == Config.USERNAME:
        if bcrypt.checkpw(auth.get("password").encode('utf-8'), Config.PASSWORD_HASH.encode('utf-8')):
            token = token = create_token(auth.get("username"), auth.get("password"))
            return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401

@authorize
def evaluate():
    try:
        model = get_model()
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
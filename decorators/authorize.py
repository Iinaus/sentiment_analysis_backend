from flask import jsonify, request
import jwt

from config import Config

def authorize(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Token is missing!"}), 403
        
        try:
            token = token.split(" ")[1]
            data = jwt.decode(token, Config.JWT_SECRET, algorithms=["HS256"])
        
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired!"}), 403

        except Exception as e:
            return jsonify({"error": "Invalid token!"}), 403
        
        return func(*args, **kwargs)
    return wrapper
import bcrypt
import jwt
import datetime
from config import Config

def create_token(username):
    payload = {
        'user': username,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, Config.JWT_SECRET, algorithm="HS256")

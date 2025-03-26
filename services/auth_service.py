import bcrypt
import jwt
import datetime
from config import Config

def create_token(username, password):
    if username == Config.USERNAME and bcrypt.checkpw(password.encode('utf-8'), Config.PASSWORD_HASH.encode('utf-8')):
        token = jwt.encode(
            {'user': username, 'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)},
            Config.JWT_SECRET, algorithm="HS256"
        )
        return token
    return None

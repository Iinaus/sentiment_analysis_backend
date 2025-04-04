import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    JWT_SECRET = os.getenv('JWT_SECRET')
    USERNAME = os.getenv('USERNAME')
    PASSWORD_HASH = os.getenv('PASSWORD_HASH')
from flask import Flask
from flask_cors import CORS

from controllers import controller


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://sentiment-analysis-frontend-o7e4.onrender.com"}})

app.add_url_rule('/login', endpoint='login', view_func=controller.login, methods=['POST'])
app.add_url_rule('/evaluate', endpoint='evaluate', view_func=controller.evaluate, methods=['POST'])      

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=False)
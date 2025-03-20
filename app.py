from flask import Flask, request

from model_training import train_model

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p> Hello World!</p>"

@app.route('/data', methods=['POST'])
def get_data():
    model = train_model()
    data = request.json
    sentence = data["sentence"]
    sentiment = model.predict([sentence])
    print(sentiment)
    return {"message": "Data received", "data": data}
    

if __name__ == '__main__':
    app.run()
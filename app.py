from flask import Flask, jsonify, request

from model_training import train_model

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p> Hello World!</p>"

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
    app.run()
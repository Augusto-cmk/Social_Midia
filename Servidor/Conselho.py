from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)


@app.route('/advice/', methods=['GET'])
def advice():
    advice_json = json.loads(requests.get("https://api.adviceslip.com/advice").content)['slip']['advice']
    return jsonify({'data': advice_json})

def startAPI():
    app.run()
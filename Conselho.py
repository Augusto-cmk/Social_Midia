from flask import Flask, jsonify
import requests
from googletrans import Translator
import json

app = Flask(__name__)


@app.route('/advice/', methods=['GET'])
def advice():
    advice_json = json.loads(requests.get("https://api.adviceslip.com/advice").content)['slip']['advice']
    info_data = Translator().translate(advice_json, dest="pt").text.encode("utf-8")
    return jsonify({'data': info_data})


if __name__ == "__main__":
    app.run()

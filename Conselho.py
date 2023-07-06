import requests
from googletrans import Translator
import json


def get_conselho()->str:
    conselho = json.loads(requests.get("https://api.adviceslip.com/advice").content)['slip']['advice']
    return Translator().translate(conselho,dest="pt").text



print(get_conselho())
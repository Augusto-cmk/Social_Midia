import requests
import json
import Pyro5

@Pyro5.api.expose
class API:
    @Pyro5.api.expose
    def get_advice(self)->str:
        return json.loads(requests.get("http://127.0.0.1:5000/advice/").content)['data']





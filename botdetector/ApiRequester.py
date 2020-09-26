import requests
import json

class ApiRequester:

    def __init__(self):
        pass

    def get(self, url, is_json, parameters):
        if is_json:
            if parameters != None:
                return json.loads(requests.get(url, params=parameters).content)
            else:
                return json.loads(requests.get(url).content)
        else:
            return requests.get(url)
import requests
import json

class ApiRequester:

    def __init__(self):
        pass

    def get(self, url, is_json, parameters):
        response = None

        if parameters != None:
            response = requests.get(url, params=parameters).content)
        else:
            response = requests.get(url)

import requests
import json

class ApiRequester:

    def __init__(self):
        pass

    def get(self, url, is_json, parameters):
        response = None

        if parameters != None:
            response = requests.get(url, params=parameters)
        else:
            response = requests.get(url)

        if is_json == True:
            response_json = json.loads(response.content)

            return response_json
        else:
            return response
        

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

        print("Error code: {0}".format(response))

        if is_json == True:
            return json.loads(response.content)
        else:
            return response
        

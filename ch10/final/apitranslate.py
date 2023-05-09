import requests
import json
import apikey

class Translaterapi:
    def __init__(self):
        self.url= "https://translate.googleapis.com/language/translate/v2?key=" + apikey.API_KEY

    def translate(self, input):
        data = {
            'q': input,
            'target': 'ja',
            'format': 'text'}
        response = requests.post(self.url, data=json.dumps(data))
        return response.json()['data']['translations'][0]['translatedText']


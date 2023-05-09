import requests

class GenshinCharacterapi:
    def __init__(self):
        self.url= "https://api.genshin.dev/characters"

    def get(self):
        r=requests.get(self.url)
        response = r.json()
        return response
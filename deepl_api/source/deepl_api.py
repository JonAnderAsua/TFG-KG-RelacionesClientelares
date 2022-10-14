import requests
import json

class DeeplApi:
    def __init__(self):
        #APIaren gakoa lortu
        with open('deepl_api/files/key.txt') as f:
            for linea in f:
                self.key = linea
        self.uri = 'https://api-free.deepl.com/v2/translate'

    def itzulpenaEgin(self, testua):
        datuak = {'auth_key': self.key, 'text': testua, 'target_lang': 'EN'}
        res = requests.post(self.uri, data=datuak)
        return json.loads(res.text)['translations'][0]['text']
import requests
import json

#APIaren gakoa lortu
with open('../files/key') as f:
    for linea in f:
        key = linea

#Itzuli behar den testua lortu
texto_a_traducir = ""
with open('../files/texto_a_traducir.txt') as f:
    for linea in f:
        texto_a_traducir += linea + "\n"

#Itzulpena
uri = 'https://api-free.deepl.com/v2/translate'
datuak = {'auth_key':key,'text':texto_a_traducir,'target_lang':'EN'}

res = requests.post(uri, data=datuak)

print('Itzulpena hurrengoa da:')
print(json.loads(res.text)['translations'][0]['text'])



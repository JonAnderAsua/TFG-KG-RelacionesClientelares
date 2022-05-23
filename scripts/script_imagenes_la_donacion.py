import json
import sys
from SPARQLWrapper import SPARQLWrapper, BASIC, INSERT, POST


def jsonaKargatu(path):
    try:
        with open(path, "r") as a:
            return json.load(a)
    except:
        print("JSONa ez da kargatu, programaren exekuzioa bukatuko da...\n")
        sys.exit(1)


def deskargatuIrudia(label):


    eskaera = '''
    SELECT ?person
    WHERE
    {
        ?person rdfs:label "%s"@es .
    }
    '''%(label)

    sparql = SPARQLWrapper('https://query.wikidata.org/bigdata/namespace/wdq/sparql')
    sparql.setQuery(eskaera)
    sparql.queryType = INSERT
    sparql.method = POST
    sparql.setHTTPAuth(BASIC)
    # try:
    sparql.query()
    # except:
    #     print("AAA")
    #     exit(1)

    # try:
    # r = requests.get('https://query.wikidata.org/bigdata/namespace/wdq/sarql', params={'format': 'json', 'query': eskaera})
    # data = r.json()
    # print(data['results'])
    # except:
    #     print(label + "aren irudia ezin izan da kargatu")



def jsonaKudeatu(path):
    jsona = jsonaKargatu(path)

    elementua = 'entities'
    if 'persons.json' in path:
        elementua = 'persons'
    elif 'places.json' in path:
        elementua = 'places'

    for i in jsona[elementua]:
        try:
            deskargatuIrudia(i['names'][0])
        except:
            deskargatuIrudia(i['title'])


if __name__ == "__main__":
    print("Pertsonen irudiak kudeatuko dira...")
    entitateak = jsonaKudeatu('../data/ladonacion.es/persons.json')

# try:
#     with open("../data/ladonacion.es/persons.json", "r") as a:
#         pertsonak = json.load(a)
# except:
#     print("Pertsonen JSONa ez da kargatu, programaren exekuzioa bukatuko da...\n")
#     sys.exit(1)
#
# try:
#     with open("../data/ladonacion.es/places.json", "r") as a:
#         lekuak = json.load(a)
# except:
#     print("Lekuen JSONa ez da kargatu, programaren exekuzioa bukatuko da...\n")
#     sys.exit(1)


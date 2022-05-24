import json
import sys
from SPARQLWrapper import SPARQLWrapper, BASIC, INSERT, POST
import requests
from qwikidata.sparql import (get_subclasses_of_item, return_sparql_query_results)


def jsonaKargatu(path):

    try:
        with open(path, "r",encoding='utf-8') as a:
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

    try:
        res = return_sparql_query_results(eskaera)

        # URIa ateratzeko
        zerrenda = list(res.values())  # https://stackoverflow.com/questions/16228248/how-can-i-get-list-of-values-from-dict
        entitatea = zerrenda[0]['vars'][0]
        link = zerrenda[1]["bindings"][0][entitatea]["value"]

        eskaera = '''
            SELECT ?pic
			WHERE
			{
			<%s> wdt:P18 ?pic .
			}
		`
        '''%(link)

        print(eskaera)

        r = requests.get('https://query.wikidata.org/bigdata/namespace/wdq/sparql',params={'format': 'json', 'query': eskaera})
        data = r.json()
        print(data)

    except Exception as s:
        print(s)



def jsonaKudeatu(path):
    jsona = jsonaKargatu(path)

    elementua = 'entities'
    if 'persons.json' in path:
        elementua = 'persons'
    elif 'places.json' in path:
        elementua = 'places'

    for i in jsona[elementua]:
        if len(i['title'].split()) > 2:
            try:
                deskargatuIrudia(i['names'][0])
            except:
                deskargatuIrudia(i['title'])
        else:
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


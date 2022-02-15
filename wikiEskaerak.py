from qwikidata.sparql import (get_subclasses_of_item, return_sparql_query_results)
import requests

query = '''
SELECT ?person
WHERE
{
    ?person wdt:P31 wd:Q5 .
    ?person rdfs:label "Juan Carlos I de España"@es .
}
'''

res = return_sparql_query_results(query)

#URIa ateratzeko
zerrenda = list(res.values()) #https://stackoverflow.com/questions/16228248/how-can-i-get-list-of-values-from-dict
entitatea = zerrenda[0]['vars'][0]
link = zerrenda[1]["bindings"][0][entitatea]["value"]

#Orrialde hori daukan identifikatzailea ateratzeko
zenbakId = link.split("/")[-1]

# sending get request and saving the response as response object
r = requests.get(url=link)

# extracting data in json format
data = r.json()
print(data["entities"][zenbakId]["pageid"])

wikiLink = "https://en.wikipedia.org/w/api.php?action=query&pageids="+str(data["entities"][zenbakId]["pageid"])+"&format=json&formatversion=2"

r = requests.get(url=wikiLink)

# extracting data in json format
data = r.json()
print(data)


'''
Q_RIVER = "Q19943"
subclasses_of_river = get_subclasses_of_item(Q_RIVER)
print(subclasses_of_river)
'''
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

#https://stackoverflow.com/questions/16228248/how-can-i-get-list-of-values-from-dict
link = list(res.values())[1]["bindings"][0]["person"]["value"]

# sending get request and saving the response as response object
r = requests.get(url=link)

# extracting data in json format
data = r.json()
print(data["entities"]["Q19943"]["pageid"])

wikiLink = "https://en.wikipedia.org/w/api.php?action=query&pageids="+str(data["entities"]["Q19943"]["pageid"])+"&format=json&formatversion=2"

r = requests.get(url=wikiLink)

# extracting data in json format
data = r.json()
print(data)


'''
Q_RIVER = "Q19943"
subclasses_of_river = get_subclasses_of_item(Q_RIVER)
print(subclasses_of_river)
'''
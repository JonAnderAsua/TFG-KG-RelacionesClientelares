from qwikidata.sparql import (get_subclasses_of_item, return_sparql_query_results)

query = '''
SELECT ?item ?itemLabel
WHERE
{
    ?item wdt:P31 wd:Q116.
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE], esp". }

}
'''

res = return_sparql_query_results(query)
print(res.values())

Q_RIVER = "Q4022"
subclasses_of_river = get_subclasses_of_item(Q_RIVER)
print(subclasses_of_river)
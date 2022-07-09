import pandas as pd
from csv import reader
from SPARQLWrapper import SPARQLWrapper, BASIC, INSERT, POST, GET, SELECT, JSON
from rdflib import Graph

# erlazioak = pd.read_csv('/home/jonander/PycharmProjects/TFG-KG-RelacionesClientelares/data/leaks/relationships.csv')

# open file

csvak = ['/nodes-addresses.csv', '/nodes-entities.csv', '/nodes-intermediaries.csv', '/nodes-officers.csv',
         '/nodes-others.csv']
for i in csvak:
    with open("/home/jonander/PycharmProjects/TFG-KG-RelacionesClientelares/data/leaks" + i, "r") as my_file:
        file_reader = reader(my_file)
        lista = []
        for i in file_reader:
            # print the rows

            if(i[2]):

                eskaera = '''
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                SELECT ?s WHERE{
                    ?s rdfs:label ?o .FILTER regex(str(?o),"''' + i[2] + '''").
                }
                '''

                sparql = SPARQLWrapper('http://localhost:7200/repositories/LaDonacion')

                sparql.setQuery(eskaera)
                sparql.setReturnFormat(JSON)

                sparql.queryType = SELECT
                sparql.method = GET
                sparql.setHTTPAuth(BASIC)
                try:
                    ret = sparql.query().convert()
                    if(ret['results']['bindings']):
                        print(ret['results']['bindings'][0])
                except:
                    pass
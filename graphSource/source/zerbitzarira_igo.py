import logging
import sys
from SPARQLWrapper import SPARQLWrapper, BASIC, INSERT, POST
from rdflib import Graph

class Zerbitzarira_igo:
    def __init__(self,rdf_output,triple_store,logs,delete_graph):
        self.triple_store = triple_store
        self.delete_graph = delete_graph

        # Grafoa
        self.grafo = Graph()
        self.grafo.parse(rdf_output) #https://rdflib.readthedocs.io/en/stable/intro_to_parsing.html

        # Log
        logging.basicConfig(filename=logs, filemode='w', level=logging.DEBUG)

    def ezabatuZerbitzarikoGrafoa(self):
    #In: -
    #Out: Repoan aurretik zegoen grafoa ezabatzen da
        eskaera = '''
        DELETE {
            ?s ?p ?o .
        } WHERE {
            ?s ?p ?o .
        }
        '''
        sparql = SPARQLWrapper(self.triple_store)
        sparql.setQuery(eskaera)
        sparql.queryType = INSERT
        sparql.method = POST
        sparql.setHTTPAuth(BASIC)
        try:
            sparql.query()
        except:
            logging.error("Ezin izan dira ezabatu aurretik zeuden tripleak...")
            exit(1)

    def zerbitzariraIgo(self):
    #In: -
    #Out: Aurretik sortutako fitxategia zerbitzariaren Graphdb instantziara igo

        zerbaitSartuDa = False

        if(self.delete_graph):
            logging.info("Repoan zegoen grafoa ezabatuko da...")
            self.ezabatuZerbitzarikoGrafoa()

        for s,p,o in self.grafo:
            if("http://" in o or "https://" in o):
                queryStringUpload = 'INSERT DATA  { <%s> <%s> <%s> }' %(s,p,o)
            else:
                queryStringUpload = 'INSERT DATA  { <%s> <%s> "%s" }' % (s, p, o)
            sparql = SPARQLWrapper(self.triple_store)
            sparql.setQuery(queryStringUpload)
            sparql.queryType = INSERT
            sparql.method = POST
            sparql.setHTTPAuth(BASIC)

            try:
                sparql.query()
                zerbaitSartuDa = True
            except:
                logging.error("Ezin izan da " + str((s, p, o)) + " triplea grafoan sartu...\n")

        if not zerbaitSartuDa:
            print("Triple Storea txarto sartu da")
            sys.exit(1)
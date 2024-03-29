import sys

import yaml
import os
import validators
from SPARQLWrapper import SPARQLWrapper, BASIC,SELECT, GET


class Procesador:

    def __init__(self, izena): #Eraikitzailea
        #YAML fitxategia kargatu
        fichero = open('doc/config.yml')
        self.fitxategia = yaml.load(fichero, Loader=yaml.FullLoader)

        if not '/home/runner/work/' in os.path.dirname(os.path.abspath(__file__)):
            #Klasearen objektuak sortu
            self.workspace = self.fitxategia[izena]['workspace']
            self.images = self.workspace + self.fitxategia[izena]['images']
            self.proiektuIzena = self.fitxategia[izena]["project_name"]
            self.data_source = self.workspace + self.fitxategia[izena]["data_source"]
            self.validate = self.workspace + self.fitxategia[izena]["validate"]
            self.named_graph = self.konprobatuUria(self.fitxategia[izena]["named_graph"])
            self.run = self.konprobatuFitxategia(self.workspace + self.fitxategia[izena]["run"], False)
            self.metadata_file = self.workspace + self.fitxategia[izena]["metadata_file"]
            self.delete_graph = self.fitxategia[izena]["delete_graph"]
            self.triple_store = self.konprobatuTripleStore(self.fitxategia[izena]["triple_store"])
            self.logs = self.konprobatuFitxategia(self.workspace + self.fitxategia[izena]["logs"], True)
            self.rdf_output = self.konprobatuTripleenFItxategia(self.workspace + self.fitxategia[izena]["rdf_output"])
        else:
            # Klasearen objektuak sortu
            self.proiektuIzena = self.fitxategia[izena]["project_name"]
            self.images = self.fitxategia[izena]['images']
            self.data_source = self.fitxategia[izena]["data_source"]
            self.validate = self.fitxategia[izena]["validate"]
            self.named_graph = self.konprobatuUria(self.fitxategia[izena]["named_graph"])
            self.run = self.konprobatuFitxategia(self.fitxategia[izena]["run"], False)
            self.metadata_file = self.fitxategia[izena]["metadata_file"]
            self.delete_graph = self.fitxategia[izena]["delete_graph"]
            self.triple_store = self.konprobatuTripleStore(self.fitxategia[izena]["triple_store"])
            self.logs = self.konprobatuFitxategia(self.fitxategia[izena]["logs"], True)
            self.rdf_output = self.konprobatuTripleenFItxategia(self.fitxategia[izena]["rdf_output"])


    def konprobatuTripleStore(self,tripleStoreUri):
        if not '/home/runner/work/' in os.path.dirname(os.path.abspath(__file__)):
            eskaera = '''
                SELECT ?s
                WHERE{
                    ?s ?p ?o .
                }
            '''
            sparql = SPARQLWrapper(tripleStoreUri)
            sparql.setQuery(eskaera)
            sparql.queryType = SELECT
            sparql.method = GET
            sparql.setHTTPAuth(BASIC)
            try:
                sparql.query()
                return tripleStoreUri
            except:
                print("Sartutako triplestorea ez da zuzena...")
                sys.exit(1)
        else:
            return tripleStoreUri

    def konprobatuTripleenFItxategia(self,fitx):
        try:
            f = open(fitx)
            return fitx
        except:
            f = open(fitx,'x')
            return fitx

    def konprobatuFitxategia(self,fitxategia,logBoolean):
        try:
            f = open(fitxategia)
            return fitxategia
        except IOError:
            if logBoolean:
                print(self.proiektuIzena + " proiektuan sartutako log fitxategia ez da existitzen...")
                return './logs/unekoLog.log'

            else:
                print(self.proiektuIzena + " proiektuan sartutako " + fitxategia + " fitxategia ez da existitzen...")
                sys.exit(1)

    def konprobatuUria(self,uria):
        if validators.url(uria): #https://www.codespeedy.com/check-if-a-string-is-a-valid-url-or-not-in-python/
            return uria
        else:
            return 'http://defaultUri.es/'

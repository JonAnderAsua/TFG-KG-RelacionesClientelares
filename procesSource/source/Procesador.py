import sys
import yaml
import os
import validators
from SPARQLWrapper import SPARQLWrapper, BASIC, INSERT, POST

class Procesador:

    def __init__(self, izena): #Eraikitzailea


        #YAML fitxategia kargatu
        fichero = open('doc/config.yml')
        self.fitxategia = yaml.load(fichero, Loader=yaml.FullLoader)

        #Klasearen objektuak sortu
        self.proiektuIzena = self.fitxategia[izena]["project_name"]
        self.data_source = self.fitxategia[izena]["data_source"]
        self.validate = self.fitxategia[izena]["validate"]
        self.named_graph = self.konprobatuUria(self.fitxategia[izena]["named_graph"])
        self.run = self.konprobatuFitxategia(self.fitxategia[izena]["run"], False)
        self.metadata_file = self.fitxategia[izena]["metadata_file"]
        self.delete_graph = self.fitxategia[izena]["delete_graph"]
        self.triple_store = self.konprobatuTripleStore(self.fitxategia[izena]["triple_store"])
        self.logs = self.konprobatuFitxategia(self.fitxategia[izena]["logs"], True)
        self.rdf_output = self.konprobatuFitxategia(self.fitxategia[izena]["rdf_output"],False)

    def konprobatuTripleStore(self,tripleStoreUri):
        eskaera = ""
        sparql = SPARQLWrapper(tripleStoreUri)
        sparql.setQuery(eskaera)
        sparql.queryType = INSERT
        sparql.method = POST
        sparql.setHTTPAuth(BASIC)
        try:
            sparql.query()
            return tripleStoreUri
        except:
            print("Sartutako triplestorea ez da zuzena...")
            sys.exit(1)

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

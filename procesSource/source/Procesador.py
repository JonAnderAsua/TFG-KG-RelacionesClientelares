import sys
import yaml
import os
import validators
from SPARQLWrapper import SPARQLWrapper, BASIC, INSERT, POST

class Procesador:

    def __init__(self, izena): #Eraikitzailea
        #Root path-a ezarri
        path_nagusia = os.path.dirname(os.path.abspath(__file__)).split('/')  # https://stackoverflow.com/questions/25389095/python-get-path-of-root-project-structure
        path_nagusia = path_nagusia[0:len(path_nagusia) - 2]
        ROOT_DIR = ""
        for i in path_nagusia:
            # if i == 'TFG-KG-RelacionesClientelares': #Honekin bermatzen da aldi bakarrez agertzen dela 'TFG-KG-RelacionesClientelares'
            #     ROOT_DIR += i + "/"
            #     # ROOT_DIR += i + "/"
            #     break
            ROOT_DIR += i + "/"

        print(ROOT_DIR)

        #Yaml fitxategia kargatu
        fichero = open(ROOT_DIR + "./doc/config.yml")

        self.fitxategia = yaml.load(fichero, Loader=yaml.FullLoader)

        #Klasearen objektuak sortu
        self.proiektuIzena = self.fitxategia[izena]["project_name"]
        self.data_source = self.fitxategia[izena]["data_source"]
        self.validate = self.fitxategia[izena]["validate"]

        if validators.url(self.fitxategia[izena]["named_graph"]): #https://www.codespeedy.com/check-if-a-string-is-a-valid-url-or-not-in-python/
            self.named_graph = self.fitxategia[izena]["named_graph"]
        else:
            self.named_graph = 'http://defaultUri.es/'

        try:
            f = open(self.fitxategia[izena]["run"])
            self.run = self.fitxategia[izena]["run"]
        except IOError:
            print(self.proiektuIzena + " proiektuan sartutako exekuzio programa ez da existitzen...")
            sys.exit(1)

        self.metadata_file = self.fitxategia[izena]["metadata_file"]
        self.delete_graph = self.fitxategia[izena]["delete_graph"]
        self.triple_store = self.konprobatuTripleStore(self.fitxategia[izena]["triple_store"])
        self.logs = self.fitxategia[izena]["logs"]
        self.rdf_output = self.fitxategia[izena]["rdf_output"]

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
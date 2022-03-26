import termios

import yaml

class Procesador:

    def __init__(self, izena): #Eraikitzailea
        #Yaml fitxategia kargatu
        fichero = open("../doc/config.yml")

        fitxategia = yaml.load(fichero, Loader=yaml.FullLoader)

        #Klasearen objektuak sortu
        self.data_source = fitxategia[izena]["data_source"]
        self.validate = fitxategia[izena]["validate"]
        self.named_graph = fitxategia[izena]["named_graph"]
        self.processor = fitxategia[izena]["processor"]
        self.metadata_file = fitxategia[izena]["metadata_file"]
        self.delete_graph = fitxategia[izena]["delete_graph"]
        self.triple_store = fitxategia[izena]["triple_store"]
        self.logs = fitxategia[izena]["logs"]
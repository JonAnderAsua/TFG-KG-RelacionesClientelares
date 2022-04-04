import yaml

class Procesador:

    def __init__(self, izena): #Eraikitzailea
        #Yaml fitxategia kargatu
        fichero = open("/home/jonander/PycharmProjects/TFG-KG-RelacionesClientelares/doc/config.yml")

        self.fitxategia = yaml.load(fichero, Loader=yaml.FullLoader)

        #Klasearen objektuak sortu
        self.data_source = self.fitxategia[izena]["data_source"]
        self.validate = self.fitxategia[izena]["validate"]
        self.named_graph = self.fitxategia[izena]["named_graph"]
        self.run = self.fitxategia[izena]["run"]
        self.metadata_file = self.fitxategia[izena]["metadata_file"]
        self.delete_graph = self.fitxategia[izena]["delete_graph"]
        self.triple_store = self.fitxategia[izena]["triple_store"]
        self.logs = self.fitxategia[izena]["logs"]
        self.rdf_output = self.fitxategia[izena]["rdf_output"]


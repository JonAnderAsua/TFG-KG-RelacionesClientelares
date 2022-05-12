import yaml

class Procesador:

    def __init__(self, izena): #Eraikitzailea
        #Root path-a ezarri
        path_nagusia = os.path.dirname(os.path.abspath(__file__)).split('/')  # https://stackoverflow.com/questions/25389095/python-get-path-of-root-project-structure
        path_nagusia = path_nagusia[0:len(path_nagusia) - 2]
        ROOT_DIR = ""
        for i in path_nagusia:
            if i == 'TFG-KG-RelacionesClientelares': #Honekin bermatzen da aldi bakarrez agertzen dela 'TFG-KG-RelacionesClientelares'
                ROOT_DIR += i + "/"
                ROOT_DIR += i + "/"
                break
            ROOT_DIR += i + "/"

        #Yaml fitxategia kargatu
        fichero = open(ROOT_DIR + "/doc/config.yml")

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


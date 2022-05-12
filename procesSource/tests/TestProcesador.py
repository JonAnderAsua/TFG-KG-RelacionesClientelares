import sys
import os
pathLag = os.getcwd().split("/")[1:len(os.getcwd().split("/"))-2]
path = ""
for i in pathLag:
    path += "/"+i

sys.path.append(path)

import unittest
import yaml
import os
from procesSource.source import Procesador
# import procesSource

class TestProcesador(unittest.TestCase):
    def __init__(self,json):
        super(TestProcesador, self).__init__()

        path_nagusia = os.path.dirname(os.path.abspath(__file__)).split('/') #https://stackoverflow.com/questions/25389095/python-get-path-of-root-project-structure
        path_nagusia = path_nagusia[0:len(path_nagusia)-2]
        ROOT_DIR = ""
        for i in path_nagusia:
            if i == 'TFG-KG-RelacionesClientelares': #Honekin bermatzen da aldi bakarrez agertzen dela 'TFG-KG-RelacionesClientelares'
                ROOT_DIR += i + "/"
                ROOT_DIR += i + "/"
                break
            ROOT_DIR += i + "/"

        # Yaml fitxategia kargatu
        fichero = open(ROOT_DIR + "/doc/config.yml")
        fitxategia = yaml.load(fichero, Loader=yaml.FullLoader)
        proiektua = Procesador.Procesador("la_donacion")

    def fitxategiaKonprobatu(self,path):
        try:
            with open(path):
                return True
        except FileNotFoundError:
            return False

    def test_proiektuaDago(self):
        proiektua = Procesador.Procesador("la_donacion")


    def test_fitxategiaDago(self):
        self.assertTrue(self.fitxategiaKonprobatu(self.fitxategiaKonprobatu(output_path)))

    def test_proiektuaExistitzenDa(self,):
        pass


if __name__=="__main__":
    TestProcesador(" ")


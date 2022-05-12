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
# from procesSource.source import Procesador

class TestProcesador(unittest.TestCase):
    def __init__(self,json):
        super(TestProcesador, self).__init__()

        path_nagusia = os.path.dirname(os.path.abspath(__file__)).split('/') #https://stackoverflow.com/questions/25389095/python-get-path-of-root-project-structure
        path_nagusia = path_nagusia[0:path_nagusia-2]
        ROOT_DIR = ""
        for i in path_nagusia:
            ROOT_DIR += i

        print(ROOT_DIR)

        # Yaml fitxategia kargatu
        fichero = open(ROOT_DIR + "/doc/config.yml")
        fitxategia = yaml.load(fichero, Loader=yaml.FullLoader)
        proiektua = procesSource.source.Procesador("la_donacion")

    def fitxategiaKonprobatu(self,path):
        try:
            with open(path):
                return True
        except FileNotFoundError:
            return False

    def test_proiektuaDago(self):
        proiektua = procesSource.source.Procesador("la_donacion")


    def test_fitxategiaDago(self):
        self.assertTrue(self.fitxategiaKonprobatu(self.fitxategiaKonprobatu(output_path)))

    def test_proiektuaExistitzenDa(self,):
        pass


if __name__=="__main__":
    TestProcesador(" ")


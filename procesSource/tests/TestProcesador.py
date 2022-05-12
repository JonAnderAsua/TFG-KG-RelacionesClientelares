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

        # Yaml fitxategia kargatu
        fichero = open("/home/jonander/PycharmProjects/TFG-KG-RelacionesClientelares/doc/config.yml")
        fitxategia = yaml.load(fichero, Loader=yaml.FullLoader)

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


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
# import procesSource


from procesSource.source import Procesador


class TestProcesador(unittest.TestCase):
    def __init__(self,json):
        super(TestProcesador, self).__init__()

        # Yaml fitxategia kargatu
        fichero = open("/home/jonander/PycharmProjects/TFG-KG-RelacionesClientelares/doc/config.yml")
        fitxategia = yaml.load(fichero, Loader=yaml.FullLoader)
        for proiektuIzena in fitxategia:
            output_path = procesSource.source.Procesador(proiektuIzena).rdf_output
            os.system("python3 ../source/ejecutador.py "+proiektuIzena)

            #Testak exekutatu
            self.test_fitxategiaDago(output_path)

    def fitxategiaKonprobatu(self,path):
        try:
            with open(path):
                return True
        except FileNotFoundError:
            return False

    def test_fitxategiaDago(self,output_path):
        self.assertTrue(self.fitxategiaKonprobatu(self.fitxategiaKonprobatu(output_path)))

if __name__=="__main__":
    TestProcesador("Holi")


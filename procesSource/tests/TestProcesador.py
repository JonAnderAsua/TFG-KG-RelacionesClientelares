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

        self.proiektuOna = Procesador("la_donacion_local_JonAnder")
        self.fallaDataSource = Procesador("falla_data_source")

    def test_data_source_dago(self):
        with self.assertRaises(SystemExit) as fallaDatSource:
            pass



    def test_fitxategiaDago(self):
        # self.assertTrue(self.fitxategiaKonprobatu(self.fitxategiaKonprobatu(output_path)))
        pass

    def test_proiektuaExistitzenDa(self,):
        pass


if __name__=="__main__":
    TestProcesador(" ")


import unittest
import yaml
import os
from procesSource import Procesador

class TestProcesador(unittest.TestCase):

    def __init__(self,json):
        super(TestProcesador, self).__init__()

        # Yaml fitxategia kargatu
        fichero = open("/home/jonander/PycharmProjects/TFG-KG-RelacionesClientelares/doc/config.yml")
        fitxategia = yaml.load(fichero, Loader=yaml.FullLoader)
        for proiektuIzena in fitxategia:
            output_path = Procesador.Procesador(proiektuIzena).rdf_output
            os.system("python3 ../ejecutador.py la_donacion ")

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


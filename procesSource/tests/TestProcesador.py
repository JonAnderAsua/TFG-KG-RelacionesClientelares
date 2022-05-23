import sys
import os
pathLag = os.getcwd().split("/")[1:len(os.getcwd().split("/"))-2]
path = ""
for i in pathLag:
    path += "/"+i

sys.path.append(path)

import unittest
import os
from procesSource.source import Procesador
from graphSource.source import grafo_objektua_sortu,fitxategia_sortu,zerbitzarira_igo

class TestProcesador(unittest.TestCase):
    def setUp(self): #https://techoverflow.net/2020/04/21/how-to-fix-python-unittest-__init__-takes-1-positional-argument-but-2-were-given/
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

        self.proiektuOna = Procesador("test_la_donacion")
        self.fallaDataSource = Procesador("test_data_source")
        self.fallaNamedGraph = Procesador('test_named_graph')
        self.fallaLogs = Procesador('test_logs')
        self.fallaRdfOutput = Procesador('test_rdf_output')


        self.grafoOna = grafo_objektua_sortu.Grafo_fitxategia_sortu(self.proiektuOna.data_source,self.proiektuOna.logs,self.proiektuOna.named_graph,self.proiektuOna.triple_store)

    def test_data_source_dago(self):
        #Programak ez baditu fitxategiak aurkitzen exekuzioa bukatzen du eta errore kodea 1 bueltatzen du,
        #horregatik hurrengo tresnarekin frogatzen da ea errore kode hori bueltatzen duen
        with self.assertRaises(SystemExit) as fallaDataSource:
            grafo_data_source = grafo_objektua_sortu.Grafo_fitxategia_sortu(self.fallaDataSource.data_source,self.fallaDataSource.logs,self.fallaDataSource.named_graph,self.fallaDataSource.triple_store)
            grafo_data_source.jsonakKargatu()
        self.assertEqual(fallaDataSource.exception.code, 1)

    def test_named_graph(self):
        #Tripleak izendatzeko uria txarto sartzen bada (ez bada URI bat) eraikitzaile berak
        # 'http://defaultUri.es' uria ezartzen du, konprobatu behar da uri hori duela

        self.assertEqual(self.fallaNamedGraph.named_graph,'http://defaultUri.es/')
        self.assertEqual(self.proiektuOna.named_graph,'http://ehu.eus/')

    def test_run(self):
        with self.assertRaises(SystemExit) as fallaRunExc:
            fallaRun = Procesador('test_run')
        self.assertEqual(fallaRunExc.exception.code, 1)


    def test_triple_store(self):
        with self.assertRaises(SystemExit) as fallaTSExc:
            fallaTripleStore = Procesador('test_triple_store')
        self.assertEqual(fallaTSExc.exception.code, 1)

    def test_logs(self):
        grafo_logs = grafo_objektua_sortu.Grafo_fitxategia_sortu(self.fallaLogs.data_source,self.fallaLogs.logs,self.fallaLogs.named_graph,self.fallaLogs.triple_store)

    def test_rdf_output(self):
        grafo_rdf_output = grafo_objektua_sortu.Grafo_fitxategia_sortu(self.fallaRdfOutput.data_source,self.fallaRdfOutput.logs,self.fallaRdfOutput.named_graph,self.fallaRdfOutput.triple_store)

if __name__=="__main__":
    unittest.main()


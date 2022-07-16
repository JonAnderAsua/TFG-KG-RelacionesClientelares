import unittest
from procesSource.source import Procesador
from graphSource.source import grafo_objektua_sortu,fitxategia_sortu,zerbitzarira_igo

class TestProcesador(unittest.TestCase):
    def setUp(self): #https://techoverflow.net/2020/04/21/how-to-fix-python-unittest-__init__-takes-1-positional-argument-but-2-were-given/
        super(TestProcesador, self).__init__()

    def test_data_source_dago(self):
        #Programak ez baditu fitxategiak aurkitzen exekuzioa bukatzen du eta errore kodea 1 bueltatzen du,
        #horregatik hurrengo tresnarekin frogatzen da ea errore kode hori bueltatzen duen
        self.fallaDataSource = Procesador.Procesador("test_data_source")
        with self.assertRaises(SystemExit) as fallaDataSource:
            grafo_data_source = grafo_objektua_sortu.Grafo_fitxategia_sortu(self.fallaDataSource.data_source,self.fallaDataSource.logs,self.fallaDataSource.named_graph,self.fallaDataSource.triple_store)
            grafo_data_source.jsonakKargatu()
        self.assertEqual(fallaDataSource.exception.code, 1)

    def test_named_graph(self):
        #Tripleak izendatzeko uria txarto sartzen bada (ez bada URI bat) eraikitzaile berak
        # 'http://defaultUri.es' uria ezartzen du, konprobatu behar da uri hori duela

        self.fallaNamedGraph = Procesador.Procesador('test_named_graph')
        self.assertEqual(self.fallaNamedGraph.named_graph,'http://defaultUri.es/')

    def test_run(self):
        with self.assertRaises(SystemExit) as fallaRunExc:
            fallaRun = Procesador.Procesador('test_run')
        self.assertEqual(fallaRunExc.exception.code, 1)
    #
    # def test_triple_store(self):
    #     with self.assertRaises(SystemExit) as fallaTSExc:
    #         fallaTripleStore = Procesador.Procesador('test_triple_store')
    #     self.assertEqual(fallaTSExc.exception.code, 1)

    def test_logs(self):
        #Kasu honetan existitzen ez den log fitxategi bat pasatzen zaio. Programak ez badu fitxategi
        #hori aurkitzen berri bat sortzen du log fitxategian. Konprobatu behar da fitxategi hori ondo
        #sortu duen ala ez
        self.fallaLogs = Procesador.Procesador('test_logs')
        print(self.fallaLogs.logs)


    def test_rdf_output(self):
        #Fitxategia ez bada existitzen sortzen du, ondorioz irekitzean ez du errorerik sortuko
        fallaRdfOutput = Procesador.Procesador('test_rdf_output')
        open(fallaRdfOutput.rdf_output)
        self.assertTrue(True)


if __name__=="__main__":
    unittest.main()
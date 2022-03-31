import Procesador
from graphSource import grafo_fitxategia_sortu,json2rdf,zerbitzarira_igo
from graphSource.tests import TestJson2rdf

if __name__ == "__main__":

    procesador = Procesador.Procesador("la_donacion")

    programa = grafo_fitxategia_sortu.Grafo_fitxategia_sortu(procesador.data_source,procesador.logs,procesador.rdf_output)
    programa.main()

    zerbitzariraIgo = zerbitzarira_igo.Zerbitzarira_igo(procesador.rdf_output,procesador.triple_store,procesador.logs)
    zerbitzariraIgo.zerbitzariraIgo()
    #
    # if "json2rdf" in procesador.processor:
    #     programa = json2rdf.Json2rdf(procesador.data_source,procesador.logs,procesador.rdf_output)
    #     programa.main()
    #
    # if "TestJson2rdf" in procesador.validate:
    #     test = TestJson2rdf.TestJson2rdf()

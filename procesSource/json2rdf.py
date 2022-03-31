import Procesador
from graphSource import grafo_fitxategia_sortu,json2rdf,zerbitzarira_igo
from graphSource.tests import TestJson2rdf

if __name__ == "__main__":
    proiektua = input("Mesedez, sartu proiektuaren izena \n")
    procesador = Procesador.Procesador(proiektua)

    print("Grafo fitxategia sortuko da...")
    programa = grafo_fitxategia_sortu.Grafo_fitxategia_sortu(procesador.data_source,procesador.logs,procesador.rdf_output)
    programa.main()
    print("Grafo fitxategia sortu da hurrengo helbidean: " + procesador.rdf_output)

    print("Grafoa zerbitzarira igoko da...")
    zerbitzariraIgo = zerbitzarira_igo.Zerbitzarira_igo(procesador.rdf_output,procesador.triple_store,procesador.logs)
    zerbitzariraIgo.zerbitzariraIgo()
    print("Grafoa " + procesador.triple_store + " helbidera igo da...")

    print("Grafoaren egitura bermatzeko testak exekutatuko dira...")
    test = TestJson2rdf.TestJson2rdf(programa)
    test.exekutatuTestak()
    print("Grafoaren testak exekutatu dira... Todo OK Jose Luis")
import sys
import os

pathLag = os.getcwd().split("/")[1:len(os.getcwd().split("/")) - 2]
path = ""
for i in pathLag:
    path += "/" + i

sys.path.append(path)
sys.path.append(path + "/source")

import procesSource.source.Procesador as Procesador
from graphSource.source import fromCsvToGraph, fitxategia_sortu, zerbitzarira_igo

if __name__ == "__main__":
    procesador = Procesador(sys.argv[1])  # https://programmerclick.com/article/54591141924/

    print("Grafo fitxategia sortuko da...")
    programa = fromCsvToGraph.FromCsvToGraph(procesador.data_source, procesador.logs, procesador.named_graph)
    programa.main()

    grafoa = programa.getGrafoa()
    fitxategia_programa = fitxategia_sortu.Grafo_fitxategia_sortu(procesador.rdf_output, grafoa)
    fitxategia_programa.main()
    print("Grafo fitxategia sortu da hurrengo helbidean: " + procesador.rdf_output)

    print("Grafoa zerbitzarira igoko da...")
    zerbitzariraIgo = zerbitzarira_igo.Zerbitzarira_igo(procesador.rdf_output, procesador.triple_store,
                                                        procesador.delete_graph)
    zerbitzariraIgo.zerbitzariraIgo()
    print("Grafoa " + procesador.triple_store + " helbidera igo da...")

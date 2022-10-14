import sys
import procesSource.source.Procesador as Procesador
from graphSource.source import grafo_objektua_sortu, fitxategia_sortu, zerbitzarira_igo

if __name__ == "__main__":
    procesador = Procesador.Procesador(sys.argv[1]) #https://programmerclick.com/article/54591141924/

    print("Grafo fitxategia sortuko da...")
    programa = grafo_objektua_sortu.Grafo_fitxategia_sortu(procesador.data_source, procesador.logs, procesador.named_graph, procesador.triple_store)
    programa.main()

    grafoa = programa.grafo
    fitxategia_programa = fitxategia_sortu.Grafo_fitxategia_sortu(procesador.rdf_output,grafoa)
    fitxategia_programa.main()
    print("Grafo fitxategia sortu da hurrengo helbidean: " + procesador.rdf_output)

    print("Grafoa zerbitzarira igoko da...")
    zerbitzariraIgo = zerbitzarira_igo.Zerbitzarira_igo(procesador.rdf_output, procesador.triple_store,  procesador.delete_graph)
    zerbitzariraIgo.zerbitzariraIgo()
    print("Grafoa " + procesador.triple_store + " helbidera igo da...")
    
    #Aquí habría que añadir lo de SHACL (No es prioritario)

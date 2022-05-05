import Procesador
import sys
from graphSource import grafo_fitxategia_sortu,zerbitzarira_igo
from graphSource.tests import TestJson2rdf

if __name__ == "__main__":
    procesador = Procesador.Procesador(sys.argv[1]) #https://programmerclick.com/article/54591141924/

    print("Grafo fitxategia sortuko da...")
    programa = grafo_fitxategia_sortu.Grafo_fitxategia_sortu(procesador.data_source,procesador.logs,procesador.rdf_output)
    programa.main()
    print("Grafo fitxategia sortu da hurrengo helbidean: " + procesador.rdf_output)

    print("Grafoa zerbitzarira igoko da...")
    zerbitzariraIgo = zerbitzarira_igo.Zerbitzarira_igo(procesador.rdf_output,procesador.triple_store,procesador.logs)
    zerbitzariraIgo.zerbitzariraIgo()
    print("Grafoa " + procesador.triple_store + " helbidera igo da...")
    
    #Aquí habría que añadir lo de SHACL (No es prioritario)

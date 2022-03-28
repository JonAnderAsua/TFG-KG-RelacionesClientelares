import Procesador
from graphSource import json2rdf
from graphSource.tests import TestJson2rdf

if __name__ == "__main__":
    procesador = Procesador.Procesador("la_donacion")

    if "json2rdf" in procesador.processor:
        programa = json2rdf.Json2rdf(procesador.data_source,procesador.logs)
        programa.main()

    if "TestJson2rdf" in procesador.validate:
        test = TestJson2rdf.TestJson2rdf()

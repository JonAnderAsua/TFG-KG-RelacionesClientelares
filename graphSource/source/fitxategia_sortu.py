class Grafo_fitxategia_sortu:

    def __init__(self, rdf_output,grafoa):

        # Grafoa
        self.grafo = grafoa

        #Irteera fitxategia
        self.rdf_output = rdf_output


    #Main metodoa
    def main(self):
        self.grafo.serialize(destination=self.rdf_output, format="nt")
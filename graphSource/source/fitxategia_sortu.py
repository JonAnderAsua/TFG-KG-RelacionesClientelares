class Grafo_fitxategia_sortu:

    def __init__(self, rdf_output,grafoa):
        # Grafoa
        self.grafo = grafoa

        #Irteera fitxategia
        self.rdf_output = rdf_output

    def ezabatuAurrekoTestua(self): #https://www.delftstack.com/es/howto/python/python-clear-file/
        with open(self.rdf_output,'r+') as f:
            f.truncate(0)

    #Main metodoa
    def main(self):

        self.ezabatuAurrekoTestua()
        self.grafo.serialize(destination=self.rdf_output, format="nt")
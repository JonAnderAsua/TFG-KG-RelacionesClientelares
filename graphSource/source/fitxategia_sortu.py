import sys

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

        try:
            with open(self.rdf_output):
                print("Fitxategia existitzen da...")
                self.ezabatuAurrekoTestua()
                self.grafo.serialize(destination=self.rdf_output, format="nt")
        except FileNotFoundError:
            print("Grafoaren fitxategia ez da existitzen, sortuko da...")
            grafo = open(self.rdf_output,'x')
            self.grafo.serialize(destination=self.rdf_output, format="nt")
            exit()

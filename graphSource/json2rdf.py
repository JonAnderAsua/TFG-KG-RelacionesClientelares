from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import FOAF, RDF
import json
import Sinpleak
import Erlaziodunak

#Elementuen hasieraketa
#JSONak
artikuluak = ""
dokumentuak = ""
entitateak = ""
ekitaldiak = ""
pertsonak = ""
lekuak = ""
erlazioak = ""
iturriak = ""

#Objektuen zerrenda
entZer = []
ekiZer = []
iturZer = []
lekZer = []
perZer = []
dokZer = []
artZer = []

#Grafoa
g = Graph()
g.bind("foaf",FOAF)


def jsonakKargatu():#JSONak kargatu
#In: -
#Out: JSONak kargatuta
    global artikuluak,dokumentuak,entitateak,ekitaldiak,pertsonak,lekuak,erlazioak,iturriak

    with open("./data/ladonacion.es/articles.json","r") as a:
        artikuluak = json.load(a)

    with open("./data/ladonacion.es/documents.json","r") as d:
        dokumentuak = json.load(d)

    with open("./data/ladonacion.es/entities.json","r") as e:
        entitateak = json.load(e)

    with open("./data/ladonacion.es/events.json","r") as ek:
        ekitaldiak = json.load(ek)

    with open("./data/ladonacion.es/persons.json","r") as pe:
        pertsonak = json.load(pe)

    with open("./data/ladonacion.es/places.json","r") as pl:
        lekuak = json.load(pl)

    with open("./data/ladonacion.es/relations.json","r") as re:
        erlazioak = json.load(re)

    with open("./data/ladonacion.es/sources.json","r") as so:
        iturriak = json.load(so)


def grafoaEraiki():
#In: -
#Out: Dauden artikuluekin sortutako grafoa
    global g, artikuluak,dokumentuak,entitateak,ekitaldiak,pertsonak,lekuak,erlazioak,iturriak

    link = "http://ehu.eus/"
    for i in artikuluak["articles"]:
        a = URIRef(link + i["id"])
        for j in i["relations"]:
            b = URIRef(link + j["type"].split("/")[2])
            c = URIRef(link + j["subject"].split("/")[2])
            g.add((a,b,c))

    g.serialize(destination = "./froga.nt", format = "nt")

#Main metodoa
if __name__ == "__main__":
    print("JSONak kargatuko dira")
    jsonakKargatu()

    print("Grafoa eraikiko da")
    grafoaEraiki()


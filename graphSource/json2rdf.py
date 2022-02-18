from rdflib import Graph, URIRef, Namespace
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

#URIak
uri_base = "http://ehu.eus/"
per = Namespace("https://schema.org/Person")
ekit = Namespace("https://schema.org/Event")
doku = Namespace("https://schema.org/Documentation")
leku = Namespace("https://schema.org/Place")
enti = Namespace(uri_base + "entitate/") #Este no lo encuentro
arti = Namespace("https://schema.org/NewsArticle")

#Grafoa
g = Graph()
g.bind("foaf",FOAF)

#Miscelanea
tuplak = []


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


def setNamespace(a, x): # https://rdflib.readthedocs.io/en/stable/intro_to_creating_rdf.html
#In: URIRef objektu bat / Zein motatako objektua den (pertsona, lekua,...)
#Out: Objektu hori namespace batera esleitu
    global per, ekit, doku, leku, enti, arti
    if(x == "persons"):
        per.a
    elif(x == "event"):
        ekit.a
    elif(x == "documents"):
        doku.a
    elif(x == "places"):
        leku.a
    elif(x == "entities"):
        enti.a
    else:
        arti.a


def forPersonsToPeople(s):
#In: String bat adierazten zein motatako objektua den (place, persons,...)
#Out: String-a "persons" bada "people" bueltatzen du, bestela string bera
    if s == "persons":
        return "people"
    else:
        return s

def tuplakSortu(i):
#In: Dokumentu bat
#Out: Dokumentu horren erlazio guztiak grafoan sartu
    global tuplak,g, uri_base
    for j in i["relations"]:  # Artikulu/dokumentu bakoitzak dauzkan erlazioak atera
        a = URIRef(uri_base + forPersonsToPeople(j["subject"].split("/")[1]) + "/" + j["subject"].split("/")[2])  # Subjektua
        setNamespace(a, j["subject"].split("/")[1])

        b = URIRef(uri_base + j["type"].split("/")[1] + "/" + j["type"].split("/")[2])  # Predikatua
        #setNamespace(b, j["type"].split("/")[1])

        c = URIRef(uri_base + forPersonsToPeople(j["object"].split("/")[1]) + "/" + j["object"].split("/")[2])  # Objektua
        setNamespace(c, j["object"].split("/")[1])

        #Tupla sortu eta grafoan ez badago sartu
        tupla = (a, b, c)
        if (tupla not in tuplak):  # Tuplak ez bikoizteko
            g.add((a, b, c))

def grafoaEraiki():
#In: -
#Out: Dauden artikuluekin sortutako grafoa
    global g, artikuluak,dokumentuak #,entitateak,ekitaldiak,pertsonak,lekuak,erlazioak,iturriak

    for i in artikuluak["articles"]: #Artikuluen artean iteratzeko
        tuplakSortu(i)

    for i in dokumentuak["documents"]:
        tuplakSortu(i)

    g.serialize(destination = "./data/ladonacion.es/grafoa.nt", format = "nt")



#Main metodoa
if __name__ == "__main__":
    print("JSONak kargatuko dira")
    jsonakKargatu()

    print("Grafoa eraikiko da")
    grafoaEraiki()


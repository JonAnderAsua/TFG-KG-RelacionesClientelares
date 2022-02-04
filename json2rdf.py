from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import FOAF, RDF
import json
import Sinpleak
import Erlaziodunak

#Elementuen hasieraketa
artikuluak = ""
dokumentuak = ""
entitateak = ""
ekitaldiak = ""
pertsonak = ""
lekuak = ""
erlazioak = ""
iturriak = ""

entZer = []
ekiZer = []
iturZer = []
lekZer = []
perZer = []
dokZer = []


'''
g = Graph()
g.bind("foaf",FOAF)
a = BNode()
b = BNode
c = "c"
g.add((a,b,c))
print(g.serialize())
'''
def jsonakKargatu():#JSONak kargatu
    global artikuluak,dokumentuak,entitateak,ekitaldiak,pertsonak,lekuak,erlazioak,iturriak

    with open("data/ladonacion.es/articles.json","r") as a:
        artikuluak = json.load(a)

    with open("data/ladonacion.es/documents.json","r") as d:
        dokumentuak = json.load(d)

    with open("data/ladonacion.es/entities.json","r") as e:
        entitateak = json.load(e)

    with open("data/ladonacion.es/events.json","r") as ek:
        ekitaldiak = json.load(ek)

    with open("data/ladonacion.es/persons.json","r") as pe:
        pertsonak = json.load(pe)

    with open("data/ladonacion.es/places.json","r") as pl:
        lekuak = json.load(pl)

    with open("data/ladonacion.es/relations.json","r") as re:
        erlazioak = json.load(re)

    with open("data/ladonacion.es/sources.json","r") as so:
        iturriak = json.load(so)

def entitateakAtera():
    global entitateak
    zerrenda = []
    for i in entitateak["entities"]:
        x = Sinpleak.Entitatea(i["title"],i["description"])
        zerrenda.append(x)
    return zerrenda

def ekitaldiakAtera():
    global ekitaldiak
    zerrenda = []
    for i in ekitaldiak["events"]:
        x = Sinpleak.Ekitaldi(i["title"],i["date"],i["description"])
        zerrenda.append(x)
    return zerrenda

def aldizkariakAtera():
    global iturriak
    zerrenda = []
    for i in iturriak["sources"]:
        x = Sinpleak.Aldizkari(i["name"], i["origin"])
        zerrenda.append(x)
    return zerrenda

def lekuakAtera():
    global lekuak
    zerrenda = []
    for i in lekuak["places"]:
        x = Sinpleak.Lekua(i["title"], i["town"], i["country"], i["google"]["link"]) #Da error en town
        zerrenda.append(x)
    return zerrenda

def pertsonakAtera():
    global pertsonak
    zerrenda = []
    for i in pertsonak["persons"]:
        x = Sinpleak.Pertsona(i["title"], i["gender"], i["nationality"]) #Da error en nationality
        zerrenda.append(x)
    return zerrenda

def bilatuObjektua(s, zerrenda):
#In: Id bat eta zein zerrendan bilatu behar den
#Out: Objektua
    emaitza = ""
    for i in zerrenda:
        if s == i.getId:
            emaitza = i
            break
    return emaitza

def getErlazioak(lista):
#In: Erlazioen zerrenda JSON eran
#Out: Erlazioen zerrenda objektu eran
    global entZer, dokZer, perZer, lekZer, ekiZer
    zerrenda = []
    for i in lista:
        ida = i["object"].split("/")[2]
        if "persons/" in i["object"]:  # Pertsona bat da
            erabilZer = perZer
        elif "entities/" in i["object"]:  # Entitate bat da
            erabilZer = entZer
        elif "document/" in i["object"]:  # Dokumentu bat da
            erabilZer = dokZer
        elif "places/" in i["object"]: #Leku bat da
            erabilZer = lekZer
        elif "events/" in i["object"]: # Ekitaldi bat da
            erabilZer = ekiZer
        zerrenda.append(bilatuObjektua(ida, erabilZer))

def dokumentuakAtera():
#In: -
#Out: Dokumentu objetuen zerrenda bat
    global dokumentuak
    for i in dokumentuak["documents"]:
        erlazioak = getErlazioak(i["relations"])
        x = Erlaziodunak.Dokumentua(i["id"],i["title"],i["description"],i["date"],erlazioak)


def tuplakAtera():
    global entZer,dokZer, perZer, artikuluak, dokumentuak
    erabilZer = []
    for i in artikuluak["articles"]:
        for j in i["relations"]:
            ida = j["object"].split("/")[2]
            if "persons/" in j["object"]: #Pertsona bat da
                erabilZer = perZer
            elif "entities/" in j["object"]: #Entitate bat da
                erabilZer = entZer
            else: #Dokumentu bat da
                erabilZer = dokZer


#Main metodoa
if __name__ == "__main__":
    print("JSONak kargatuko dira")
    jsonakKargatu()

    print("Erlaziorik ez dituzten elementuak aterako dira")
    entZer = entitateakAtera()
    ekiZer = ekitaldiakAtera()
    iturZer = aldizkariakAtera()
    #lekZer = lekuakAtera()
    #perZer = pertsonakAtera()

    print("Dokumentuak aterako dira")
    dokZer = dokumentuakAtera()
    print("Tuplak sortuko dira")
    tuplakAtera()


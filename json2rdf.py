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
#In: -
#Out: Entitateak zerrendako JSONak entitate objektua bihurtu
    global entitateak
    zerrenda = []
    for i in entitateak["entities"]:
        x = Sinpleak.Entitatea(i["id"],i["title"],i["description"])
        zerrenda.append(x)
    return zerrenda

def ekitaldiakAtera():
# In: -
# Out: Ekitaldiak zerrendako JSONak ekitaldi objektua bihurtu
    global ekitaldiak
    zerrenda = []
    for i in ekitaldiak["events"]:
        x = Sinpleak.Ekitaldi(i["id"],i["title"],i["date"],i["description"])
        zerrenda.append(x)
    return zerrenda

def aldizkariakAtera():
# In: -
# Out: Iturriak zerrendako JSONak aldizkari objektua bihurtu
    global iturriak
    zerrenda = []
    for i in iturriak["sources"]:
        x = Sinpleak.Aldizkari(i["id"],i["name"], i["origin"])
        zerrenda.append(x)
    return zerrenda

def lekuakAtera():
# In: -
# Out: Lekuak zerrendako JSONak lekua objektua bihurtu
    global lekuak
    zerrenda = []
    for i in lekuak["places"]:
        x = Sinpleak.Lekua(i["id"],i["title"], i["town"], i["country"], i["google"]["link"]) #Da error en town
        zerrenda.append(x)
    return zerrenda

def pertsonakAtera():
# In: -
# Out: Pertsonak zerrendako JSONak pertsona objektua bihurtu
    global pertsonak
    zerrenda = []
    for i in pertsonak["persons"]:
        x = Sinpleak.Pertsona(i["id"],i["title"], i["gender"], i["nationality"]) #Da error en nationality
        zerrenda.append(x)
    return zerrenda

def bilatuObjektua(s, zerrenda):
#In: Id bat eta zein zerrendan bilatu behar den
#Out: Objektua
    return (x for x in zerrenda if s == x.getId)

def getErlazioak(lista):
#In: Erlazioen zerrenda JSON eran
#Out: Erlazioen zerrenda objektu eran
    global entZer, dokZer, perZer, lekZer, ekiZer
    zerrenda = []
    erabilZer = []
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
    emaitza = []
    for i in dokumentuak["documents"]:
        erlazioak = getErlazioak(i["relations"])
        x = Erlaziodunak.Dokumentua(i["id"],i["title"],i["description"],i["date"],erlazioak)
        emaitza.append(x)
    return emaitza


def tuplakAtera():
#In: -
#Out: Artikulu objektuen zerrenda bat
    global artikuluak, iturZer
    erabilZer = []
    for i in artikuluak["articles"]: #Cambiar esto
        erlazioak = getErlazioak(i["relations"])
        x = Erlaziodunak.Artikulua(i["url"],bilatuObjektua(i["source"].split("/")[2], iturZer),i["title"],i["date"],erlazioak)
        erabilZer.append(x)
    return erabilZer

def grafoaEraiki():
#In: -
#Out: Dauden artikuluekin sortutako grafoa
    global g, artZer
    txibatoa = True
    for i in artZer: #Elementuak zeharkatzeko
        print(i)
        a = BNode()
        b = BNode(i.getTitulua())
        for j in i.getErlazioak():
            if txibatoa: #Nukleoa da
                txibatoa = False
                a = BNode(j)
            else: #Nukleoa edukita haren erlazioak sartuko dira
                g.add((a,b,j))



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
    artZer = tuplakAtera()

    print("Grafoa eraikiko da")
    grafoaEraiki()


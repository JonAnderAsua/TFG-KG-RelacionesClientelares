import rdflib
from rdflib import Graph, URIRef, Literal, Namespace, RDFS
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
per = URIRef("https://schema.org/Person")
ekit = URIRef("https://schema.org/Event")
doku = URIRef("https://schema.org/Documentation")
leku = URIRef("https://schema.org/Place")
enti = URIRef("https://schema.org/Organization")
arti = URIRef("https://schema.org/NewsArticle")

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


def getLabel(a,x,json):
#In: Identifikatzaile bat / Zein motatako objektua den (pertsona, lekua,...) / Objektu horren JSONa
#Out: Identifikatzaile horretarako Label-a

    emaitza = ""

    for i in json[x]:
        if a == i['id']:
            emaitza = i["title"]
            break
    return emaitza

def setTypeAndLabel(a, x): # https://rdflib.readthedocs.io/en/stable/intro_to_creating_rdf.html
#In: URIRef objektu bat / Zein motatako objektua den (pertsona, lekua,...)
#Out: Objektu hori namespace batera esleitu
    global per, ekit, doku, leku, enti, arti,g , entitateak,ekitaldiak,pertsonak,lekuak,erlazioak,iturriak, dokumentuak, artikuluak

    c = None #Type
    d = None #Label

    if(x == "persons"):
        c = per
        d = getLabel(a.split("/")[-1],x, pertsonak)
    elif(x == "events"):
        c = ekit
        d = getLabel(a.split("/")[-1], x, ekitaldiak)
    elif(x == "documents"):
        c = doku
        d = getLabel(a.split("/")[-1], x, dokumentuak)
    elif(x == "places"):
        c = leku
        d = getLabel(a.split("/")[-1], x, lekuak)
    elif(x == "entities"):
        c = enti
        d = getLabel(a.split("/")[-1], x, entitateak)
    else:
        c = arti
        d = getLabel(a.split("/")[-1], "articles", artikuluak) #Lo meto a mano por sea caso

    tuplaType = (a,RDF.type,c)
    tuplaLabel = (a,RDFS.label,Literal(d))

    print(tuplaType)
    print(tuplaLabel)
    g.add(tuplaType)
    g.add(tuplaLabel)


def forPersonsToPeople(s):
#In: String bat adierazten zein motatako objektua den (place, persons,...)
#Out: String-a "persons" bada "people" bueltatzen du, bestela string bera
    if s == "persons":
        return "people"
    else:
        return s

def setType(x):
#In:
#Out: Grafoa elementuarekin gehituta
    global tuplak,g
    lista = x.split("/")

    if(lista[4] == "person"):
        tupla = ((x,RDF.type,FOAF.Person))


def tuplakSortu(i):
#In: Dokumentu bat
#Out: Dokumentu horren erlazio guztiak grafoan sartu
    global tuplak,g, uri_base
    for j in i["relations"]:  # Artikulu/dokumentu bakoitzak dauzkan erlazioak atera

        #Subjektua
        aux = j["subject"].split("/")[1]
        if aux == "entities": aux = "entitys"
        a = URIRef(uri_base + "id/"+ aux[0:len(aux)-1] + "/" + j["subject"].split("/")[2])
        setTypeAndLabel(a, j["subject"].split("/")[1])
        setType(a)

        #Predikatua
        b = URIRef(uri_base +"prop/" + j["type"].split("/")[2])
        #setNamespace(b, j["type"].split("/")[1])

        #Objektua
        aux = j["object"].split("/")[1]
        if aux == "entities": aux = "entitys"
        c = URIRef(uri_base +"id/"+ aux[0:len(aux)-1] + "/" + j["object"].split("/")[2])
        setTypeAndLabel(c, j["object"].split("/")[1])

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


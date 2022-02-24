import rdflib
from rdflib import Graph, URIRef, Literal, RDFS
from rdflib.namespace import RDF
import json

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

def jsonakKargatu():
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

    if(x == "persons"):
        type = per
        label = getLabel(a.split("/")[-1],x, pertsonak)
    elif(x == "events"):
        type = ekit
        label = getLabel(a.split("/")[-1], x, ekitaldiak)
    elif(x == "documents"):
        type = doku
        label = getLabel(a.split("/")[-1], x, dokumentuak)
    elif(x == "places"):
        type = leku
        label = getLabel(a.split("/")[-1], x, lekuak)
    elif(x == "entities"):
        type = enti
        label = getLabel(a.split("/")[-1], x, entitateak)
    else:
        type = arti
        label = getLabel(a.split("/")[-1], "articles", artikuluak) #Lo meto a mano por sea caso

    #Tripleak sortu
    tripleType = (a,RDF.type,type)
    tripleLabel = (a,RDFS.label,Literal(label))

    #Tripleak grafora gehitu
    g.add(tripleLabel)
    g.add(tripleType)



def forPersonsToPeople(s):
#In: String bat adierazten zein motatako objektua den (place, persons,...)
#Out: String-a "persons" bada "people" bueltatzen du, bestela string bera

    if s == "persons":
        return "people"
    else:
        return s

def erlazioaAldatu(s):
#In: Erlazioaren URIren azkenengo zatia
#Out: URI hori aldatuta

    #URIak deklaratu
    schema = "https://schema.org/"
    lag = "http://ehu.eus/transparentrelations#"

    #Schema + kasu nabariak
    if s == "takes_part":
        emaitza = schema + "participant"
    elif s == "authors":
        emaitza = schema + "author"
    elif s == "works_for":
        emaitza = schema + "worksFor"

    #Schema + kasu orokorrak
    elif(s == "mentions" or s == "parent" or s == "owns" or s == "spouse" or s == "knows"):
        emaitza = schema + s

    #Lag + kasu orokorrak
    else:
        emaitza = lag + s

    return emaitza

def tripleakSortu(i):
#In: Dokumentu bat
#Out: Dokumentu horren erlazio guztiak grafoan sartu
    global g, uri_base

    aldatu = False

    for j in i["relations"]:  # Artikulu/dokumentu bakoitzak dauzkan erlazioak atera

        #Subjektua
        aux = j["subject"].split("/")[1]
        if aux == "entities": aux = "entitys" #Hecha la trampa por que el singular de entities es entity
        a = URIRef(uri_base + "id/"+ aux[0:len(aux)-1] + "/" + j["subject"].split("/")[2])
        setTypeAndLabel(a, j["subject"].split("/")[1])

        #Predikatua
        erlazioa = erlazioaAldatu((uri_base +"prop/" + j["type"].split("/")[2]).split("/")[-1])
        b = URIRef(erlazioa)
        if("author" in erlazioa): #Aldatu behar da triplearen ordena
            aldatu = True

        #Objektua
        aux = j["object"].split("/")[1]
        if aux == "entities": aux = "entitys"
        c = URIRef(uri_base +"id/"+ aux[0:len(aux)-1] + "/" + j["object"].split("/")[2])
        setTypeAndLabel(c, j["object"].split("/")[1])

        #Triplea sortu eta grafoan ez badago sartu
        if(aldatu):
            triple = (c,b,a)
        else:
            triple = (a, b, c)

        if ("mohamed_vi" not in a and "gives" not in b and "marrakech" not in c):  # Tripleak ez bikoizteko
            g.add(triple)

def grafoaEraiki():
#In: -
#Out: Dauden artikuluekin sortutako grafoa
    global g, artikuluak,dokumentuak

    for i in artikuluak["articles"]: #Artikuluen artean iteratzeko
        tripleakSortu(i)

    for i in dokumentuak["documents"]:
        tripleakSortu(i)

    g.serialize(destination = "./data/ladonacion.es/grafoa.nt", format = "nt")

def zerbitzariraIgo():
#In: -
#Out: Aurretik sortutako fitxategia zerbitzariaren Graphdb instantziara igo
    pass

#Main metodoa
if __name__ == "__main__":
    print("JSONak kargatuko dira...")
    jsonakKargatu()

    print("Grafoa eraikiko da...")
    grafoaEraiki()

    print("Sortutako fitxategia zerbitzariaren graphdb instantziara igoko da...")
    zerbitzariraIgo()


from SPARQLWrapper import SPARQLWrapper, BASIC
from rdflib import Graph, URIRef, Literal, RDFS
from rdflib.namespace import RDF
import json

class JSON2RDF:

    def constructor(self,data,logs):
        #JSONak
        self.artikuluak = ""
        self.dokumentuak = ""
        self.entitateak = ""
        self.ekitaldiak = ""
        self.pertsonak = ""
        self.lekuak = ""
        self.erlazioak = ""
        self.iturriak = ""

        #URIak
        self.uri_base = "http://ehu.eus/"
        self.per = URIRef("https://schema.org/Person")
        self.ekit = URIRef("https://schema.org/Event")
        self.doku = URIRef("https://schema.org/Documentation")
        self.leku = URIRef("https://schema.org/Place")
        self.enti = URIRef("https://schema.org/Organization")
        self.arti = URIRef("https://schema.org/NewsArticle")

        #Grafoa
        self.grafo = Graph()

        #Miscelanea
        self.log = open(logs,"w")
        self.data = data

    def jsonakKargatu(self):
    #In: -
    #Out: JSONak kargatuta
        try:
            with open(self.data + "/articles.json","r") as a:
                self.artikuluak = json.load(a)
                self.log.write("Artikuluen JSONa kargatu da...\n")
        except:
            self.log.write("Artikuluen JSONa ez da kargatu...\n")

        try:
            with open( self.data + "/documents.json","r") as d:
                self.dokumentuak = json.load(d)
                self.log.write("Dokumentuen JSONa kargatu da...\n")
        except:
            self.log.write("Dokumentuen JSONa ez da kargatu...\n")

        try:
            with open(self.data + "/entities.json","r") as e:
                self.entitateak = json.load(e)
                self.log.write("Entitateen JSONa kargatu da...\n")
        except:
            self.log.write("Entitateen JSONa ez da kargatu...\n")

        try:
            with open( self.data + "/events.json","r") as ek:
                self.ekitaldiak = json.load(ek)
                self.log.write("Ekitaldien JSONa kargatu da...\n")
        except:
            self.log.write("Ekitaldien JSONa ez da kargatu...\n")

        try:
            with open("../data/ladonacion.es/persons.json","r") as pe:
                self.pertsonak = json.load(pe)
                self.log.write("Pertsonen JSONa kargatu da...\n")
        except:
            self.log.write("Pertsonen JSONa ez da kargatu...\n")

        try:
            with open(self.data + "/places.json","r") as pl:
                self.lekuak = json.load(pl)
                self.log.write("Lekuen JSONa kargatu da...\n")
        except:
            self.log.write("Lekuen JSONa ez da kargatu...\n")

        try:
            with open(self.data + "/relations.json","r") as re:
                self.erlazioak = json.load(re)
                self.log.write("Erlazioen JSONa kargatu da...\n")
        except:
            self.log.write("Erlazioen JSONa ez da kargatu...\n")

        try:
            with open(self.data + "/sources.json","r") as so:
                self.iturriak = json.load(so)
                self.log.write("Iturrien JSONa kargatu da")
        except:
            self.log.write("Iturrien JSONa ez da kargatu")

    def setType(self,uri,typeUrl):
    #In: Objektu bati esleitutako URIa / Zein motatako objektua den (pertsona, lekua,...)
    #Out: Grafoan objektu horren rdfs:type-aren triplea sartu

        triple = (uri,RDF.type,typeUrl)
        self.log.write("Sartuko den triplea hurrengoa da...\n" + str(triple) + "\n")
        self.grafo.add(triple)

    def setLabel(self,uri,json,tipoa):
    #In: Objektu bati esleitutako URIa / Zein JSONean bilatu behar da informazioa /Zein motatako objektua den (pertsona, lekua,...)
    #Out: Grafoan objektu horren rdfs:label-aren triplea sartu
        label = ""
        for i in json[tipoa]:
            if i["id"] == uri.split("/")[-1]:
                label = i["title"]
                break
        triple = (uri,RDFS.label,Literal(label))
        self.log.write("Sartuko den triplea hurrengoa da...\n" + str(triple) + "\n")
        self.grafo.add(triple)


    def setComent(self,uri,json,tipoa):
    # In: Objektu bati esleitutako URIa / Zein JSONean bilatu behar da informazioa /Zein motatako objektua den (pertsona, lekua,...)
    # Out: Grafoan objektu horren rdfs:comment-aren triplea sartu
        for i in json[tipoa]:
            if i["id"] == uri.split("/")[-1]:
                if("description" in i.keys()): #Elementu batzuk ez daukate "description" giltza
                    comment = i["description"]
                    triple = (uri, RDFS.comment, Literal(comment))
                    self.grafo.add(triple)
                    self.log.write("Sartuko den triplea hurrengoa da...\n" + str(triple) + "\n")
                    break

    def setTypeLabelComent(self,uri, tipoa): # https://rdflib.readthedocs.io/en/stable/intro_to_creating_rdf.html
    #In: Objektu bati esleitutako URIa / Zein motatako objektua den (pertsona, lekua,...)
    #Out: Grafoan rdfs:type,label eta comment sartu

        #Defektuz pertsona bat bezala hartuko da
        typeUrl = self.per #Defektuz pertsonen JSONa hartuko da
        json = self.pertsonak

        if(tipoa == "events"):
            typeUrl = self.ekit
            json = self.ekitaldiak
        elif(tipoa == "documents"):
            typeUrl = self.doku
            json = self.dokumentuak
        elif(tipoa == "places"):
            typeUrl = self.leku
            json = self.lekuak
        elif(tipoa == "entities"):
            typeUrl = self.enti
            json = self.entitateak
        elif(tipoa == "articles"):
            typeUrl = self.arti
            json = self.artikuluak

        self.setType(uri,typeUrl)
        self.setLabel(uri,json,tipoa)
        self.setComent(uri,json,tipoa)

    def forPersonsToPeople(self,tipoa):
    #In: String bat adierazten zein motatako objektua den (place, persons,...)
    #Out: String-a "persons" bada "people" bueltatzen du, bestela string bera

        if tipoa == "persons":
            return "people"
        else:
            return tipoa

    def erlazioaAldatu(self,erlazioa):
    #In: Erlazioaren URIren azkenengo zatia
    #Out: URI hori aldatuta

        #URIak deklaratu
        schema = "https://schema.org/"
        erlazioPropioa = "http://ehu.eus/transparentrelations#"

        #Schema + kasu nabariak
        if erlazioa == "takes_part":
            emaitza = schema + "participant"
        elif erlazioa == "authors":
            emaitza = schema + "author"
        elif erlazioa == "works_for":
            emaitza = schema + "worksFor"

        #Schema + kasu orokorrak
        elif(erlazioa == "mentions" or erlazioa == "parent" or erlazioa == "owns" or erlazioa == "spouse" or erlazioa == "knows"):
            emaitza = schema + erlazioa

        #Lag + kasu orokorrak
        else:
            emaitza = erlazioPropioa + erlazioa

        return emaitza

    def subjektuaObjektuaTratatu(self,uri):
    #In: Objektu batekin erlazionatutako URI bat
    #Out: URIRef objektu bat zuzendutako elementuekin
        tipoa = uri.split("/")[1]
        if tipoa == "entities": tipoa = "entitys"# Hecha la trampa por que el singular de entities es entity
        #if tipoa == "articles": tipoa = "articless" #Por que falla
        entitate = URIRef(self.uri_base + "id/" + tipoa[0:len(tipoa) - 1] + "/" + uri.split("/")[2])
        self.setTypeLabelComent(entitate, uri.split("/")[1])
        return entitate

    def tripleakSortu(self,i):
    #In: Dokumentu bat
    #Out: Dokumentu horren erlazio guztiak grafoan sartu

        aldatu = False

        for j in i["relations"]:  # Artikulu/dokumentu bakoitzak dauzkan erlazioak atera
            #Subjektua
            subjektu = self.subjektuaObjektuaTratatu(j["subject"])

            #Predikatua
            erlazioa = self.erlazioaAldatu((self.uri_base +"prop/" + j["type"].split("/")[2]).split("/")[-1])
            predikatu = URIRef(erlazioa)
            if("author" in erlazioa): #Aldatu behar da triplearen ordena
                aldatu = True

            #Objektua
            objektu = self.subjektuaObjektuaTratatu(j["object"])

            #Triplea sortu eta grafoan ez badago sartu
            if(aldatu):
                triple = (objektu,predikatu,subjektu)
            else:
                triple = (subjektu, predikatu, objektu)

            if ("mohamed_vi" not in subjektu and "gives" not in predikatu and "marrakech" not in objektu):  # Tripleak ez bikoizteko
                self.log.write("Sartuko den triplea hurrengoa da...\n" + str(triple) + "\n")
                self.grafo.add(triple)

    def grafoaEraiki(self):
    #In: -
    #Out: Dauden artikuluekin sortutako grafoa

        self.log.write("Artikuluen tripleak sortuko dira...\n")
        for i in self.artikuluak["articles"]: #Artikuluen artean iteratzeko
            self.log.write("Hurrengo artikulua kudeatujo da...\n" + str(i) + "\n")
            self.tripleakSortu(i)


        self.log.write("Dokumentuen tripleak sortuko dira...\n")
        for i in self.dokumentuak["documents"]:
            self.tripleakSortu(i)

        self.grafo.serialize(destination = self.data + "/grafoa.nt", format ="nt")

    def zerbitzariraIgo(self):
    #In: -
    #Out: Aurretik sortutako fitxategia zerbitzariaren Graphdb instantziara igo

        '''
        datuak = "/data/ladonacion.es/grafoa.nt"
        base_url = "http://localhost:7200"
        repo_id = "Froga"

        eskaera = "curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{fileNames:[" + datuak + "]}' "+base_url+"/rest/data/import/server/"+repo_id
        print(eskaera)
        os.system(eskaera)
        '''

        graphdb_url = "http://localhost:7200/repositories/laDonacion/statements"
        #graphdb_url = "http://158.227.69.119:7200/repositories/laDonacion/statements"
        for s,p,o in self.grafo:
            triple = (s,p,o)
            print(triple)
            queryStringUpload = 'INSERT DATA { %s, %s, %s }' %(s,p,o)
            print(queryStringUpload)
            sparql = SPARQLWrapper(graphdb_url)
            sparql.setQuery(queryStringUpload)
            sparql.setMethod('POST')
            sparql.setHTTPAuth(BASIC)
            sparql.setCredentials('login', 'password')

            #try:
            ret = sparql.query()
            #except:
                #log.write("Ezin izan da " + str((s,p,o)) + " triplea grafoan sartu...\n")

    #Testearako metodoak
    def getGrafoa(self):
    #In: -
    #Out: Proiektu honen grafoa
        return self.grafo

    def getJsonak(self):
    #In: -
    #Out: Proiektuaren JSONak
        return[self.artikuluak,self.dokumentuak,self.entitateak,self.ekitaldiak,self.pertsonak,self.lekuak,self.erlazioak,self.iturriak]



    #Main metodoa
    def main(self):
        self.log.write("JSONak kargatuko dira...\n")
        self.jsonakKargatu()

        self.log.write("Grafoa eraikiko da...\n")
        self.grafoaEraiki()

        self.log.write("Sortutako fitxategia zerbitzariaren graphdb instantziara igoko da...\n")
        self.zerbitzariraIgo()


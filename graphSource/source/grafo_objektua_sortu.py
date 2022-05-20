import logging
import re
from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, URIRef, Literal, RDFS
from rdflib.namespace import RDF
import json
import os
import unidecode
import sys

class Grafo_fitxategia_sortu:

    def __init__(self, data, logs,uri_base,triple_store):
        # JSONak
        self.artikuluak = ""
        self.dokumentuak = ""
        self.entitateak = ""
        self.ekitaldiak = ""
        self.pertsonak = ""
        self.lekuak = ""
        self.erlazioak = ""
        self.iturriak = ""

        # URIak
        self.uri_base = uri_base
        self.per = URIRef("https://schema.org/Person")
        self.ekit = URIRef("https://schema.org/Event")
        self.doku = URIRef("https://schema.org/Documentation")
        self.leku = URIRef("https://schema.org/Place")
        self.enti = URIRef("https://schema.org/Organization")
        self.arti = URIRef("https://schema.org/NewsArticle")

        # Grafoa
        self.grafo = Graph()

        # Log
        logging.basicConfig(filename=logs, filemode='w', level=logging.DEBUG)
        self.data = data

        self.triple_store = triple_store

        uriTest = self.triple_store.split("/")[:len(self.triple_store.split("/"))-1]
        self.testTripleStore = ""
        for i in uriTest:
            self.testTripleStore += i + "/"
        self.testTripleStore = self.testTripleStore[:len(self.testTripleStore)-1]

    def getPath(self):
    #In: -
    #Out: Fitxategian dauden path-a
        cwd = os.getcwd()
        if "test" in cwd: #Test
            cwd = cwd.split("/")[0:-2]
        else:
            cwd = cwd.split("/")[0:-2]

        path = ""
        for i in cwd:
            path += "/" + i
        return path

    def jsonakKargatu(self):
    #In: -
    #Out: JSONak kargatuta
        try:
            with open(self.data + "/articles.json","r") as a:
                self.artikuluak = json.load(a)
                logging.info("Artikuluen JSONa kargatu da...\n")
        except:
            logging.error("Artikuluen JSONa ez da kargatu, programaren exekuzioa bukatuko da...\n")
            sys.exit(1) #https://pythonguides.com/python-exit-command/

        try:
            with open(self.data + "/documents.json","r") as d:
                self.dokumentuak = json.load(d)
                logging.info("Dokumentuen JSONa kargatu da...\n")
        except:
            logging.error("Dokumentuen JSONa ez da kargatu, programaren exekuzioa bukatuko da...\n")
            sys.exit(1)

        try:
            with open(self.data + "/entities.json","r") as e:
                self.entitateak = json.load(e)
                logging.info("Entitateen JSONa kargatu da...\n")
        except:
            logging.error("Entitateen JSONa ez da kargatu, programaren exekuzioa bukatuko da...\n")
            sys.exit(1)

        try:
            with open(self.data + "/events.json","r") as ek:
                self.ekitaldiak = json.load(ek)
                logging.info("Ekitaldien JSONa kargatu da...\n")
        except:
            logging.error("Ekitaldien JSONa ez da kargatu, programaren exekuzioa bukatuko da...\n")
            sys.exit(1)

        try:
            with open(self.data + "/persons.json","r") as pe:
                self.pertsonak = json.load(pe)
                logging.info("Pertsonen JSONa kargatu da...\n")
        except:
            logging.error("Pertsonen JSONa ez da kargatu, programaren exekuzioa bukatuko da...\n")
            sys.exit(1)

        try:
            with open(self.data + "/places.json","r") as pl:
                self.lekuak = json.load(pl)
                logging.info("Lekuen JSONa kargatu da...\n")
        except:
            logging.error("Lekuen JSONa ez da kargatu, programaren exekuzioa bukatuko da...\n")
            sys.exit(1)

        try:
            with open(self.data + "/relations.json","r") as re:
                self.erlazioak = json.load(re)
                logging.info("Erlazioen JSONa kargatu da...\n")
        except:
            logging.error("Erlazioen JSONa ez da kargatu, programaren exekuzioa bukatuko da...\n")
            sys.exit(1)

        try:
            with open(self.data + "/sources.json","r") as so:
                self.iturriak = json.load(so)
                logging.info("Iturrien JSONa kargatu da")
        except:
            logging.error("Iturrien JSONa ez da kargatu, programaren exekuzioa bukatuko da...")
            sys.exit(1)
    def setType(self,uri,typeUrl):
    #In: Objektu bati esleitutako URIa / Zein motatako objektua den (pertsona, lekua,...)
    #Out: Grafoan objektu horren rdfs:type-aren triplea sartu

        triple = (uri,RDF.type,typeUrl)
        logging.info("Sartuko den triplea hurrengoa da...\n" + str(triple) + "\n")
        self.grafo.add(triple)

    def setLabel(self,uri,json,tipoa):
    #In: Objektu bati esleitutako URIa / Zein JSONean bilatu behar da informazioa /Zein motatako objektua den (pertsona, lekua,...)
    #Out: Grafoan objektu horren rdfs:label-aren triplea sartu

        label = ""
        for i in json[tipoa]:
            if i["id"] == uri.split("/")[-1]:
                label = unidecode.unidecode(i["title"])
                break
        triple = (uri,RDFS.label,Literal(label))
        logging.info("Sartuko den triplea hurrengoa da...\n" + str(triple) + "\n")
        self.grafo.add(triple)

    def ezabatuLinka(self,string):
    #In: HTML etiketak izan ahal dituen string-a
    #Out: String bera HTML etiketa gabe

        zerrenda = string.split("<")
        emaitza = ""
        for i in zerrenda:
            if ">" in i:
                emaitza += i.split(">")[1]
            else:
                emaitza += i
        return emaitza

    def setComent(self,uri,json,tipoa):
    # In: Objektu bati esleitutako URIa / Zein JSONean bilatu behar da informazioa /Zein motatako objektua den (pertsona, lekua,...)
    # Out: Grafoan objektu horren rdfs:comment-aren triplea sartu
        for i in json[tipoa]:
            if i["id"] == uri.split("/")[-1]:
                if("description" in i.keys()): #Elementu batzuk ez daukate "description" giltza
                    comment = unidecode.unidecode(i["description"])
                    comment = re.sub('</a>','',comment)
                    comment = self.ezabatuLinka(comment)
                    triple = (uri, RDFS.comment, Literal(comment))
                    self.grafo.add(triple)
                    logging.info("Sartuko den triplea hurrengoa da...\n" + str(triple) + "\n")
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
    #In:
    #Out:
        tipoa = uri.split("/")[1]
        if tipoa == "entities": tipoa = "entitys"  # Hecha la trampa por que el singular de entities es entity
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
                logging.info("Sartuko den triplea hurrengoa da...\n" + str(triple) + "\n")
                self.grafo.add(triple)

    def grafoaEraiki(self):
    #In: -
    #Out: Dauden artikuluekin sortutako grafoa

        logging.info("Artikuluen tripleak sortuko dira...\n")
        for i in self.artikuluak["articles"]: #Artikuluen artean iteratzeko
            logging.info("Hurrengo artikulua kudeatujo da...\n" + str(i) + "\n")
            self.tripleakSortu(i)


        logging.info("Dokumentuen tripleak sortuko dira...\n")
        for i in self.dokumentuak["documents"]:
            self.tripleakSortu(i)

        # self.grafo.serialize(destination = self.rdf_output, format ="nt")
    def getGrafoa(self):
        # In: -
        # Out: Proiektu honen grafoa
        return self.grafo


    def getJsonak(self):
        # In: -
        # Out: Proiektuaren JSONak
        return [self.artikuluak, self.dokumentuak, self.entitateak, self.ekitaldiak, self.pertsonak, self.lekuak, self.erlazioak, self.iturriak]


    def getLabelFromGraph(self, id):
        sparql = SPARQLWrapper(self.testTripleStore)

        sparql.setQuery('''
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    SELECT ?label
                    WHERE
                    {
                        <%s> rdfs:label ?label .
                    }           
                    ''' % (id))

        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        return results['results']['bindings'][0]["label"]['value']


    def getCommentFromGraph(self, id):
        sparql = SPARQLWrapper(self.testTripleStore)

        sparql.setQuery('''
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    SELECT ?comment
                    WHERE
                    {
                        <%s> rdfs:comment ?comment .
                    }           
                    ''' % (id))

        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        return results['results']['bindings'][0]["comment"]['value']


    def getTypeFromGraph(self,id):

        sparql = SPARQLWrapper(self.testTripleStore)

        sparql.setQuery('''
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    SELECT ?type
                    WHERE
                    {
                        <%s> rdf:type ?type .
                    }           
                    ''' % (id))


        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        return results['results']['bindings'][0]["type"]['value']


    #Main metodoa
    def main(self):

        logging.info("JSONak kargatuko dira...\n")
        self.jsonakKargatu()

        logging.info("Grafoa eraikiko da...\n")
        self.grafoaEraiki()
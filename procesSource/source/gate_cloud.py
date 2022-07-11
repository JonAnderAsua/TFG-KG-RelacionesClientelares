from procesSource.source import Procesador
import os
import sys
from SPARQLWrapper import SPARQLWrapper, BASIC, INSERT, POST, SELECT, GET, JSON,RDF
from rdflib import Graph,URIRef, RDFS, Literal
from rdflib.namespace import RDF
from unidecode import unidecode
import json
from graphSource.source import fitxategia_sortu,zerbitzarira_igo

class BezeroaSortu(object):
    def __init__(self,tripleStore):
        self.eskaera = '''
        PREFIX txtm: <http://www.ontotext.com/textmining#>
        PREFIX txtm-inst: <http://www.ontotext.com/textmining/instance#>
        INSERT DATA {
            txtm-inst:gateService txtm:connect txtm:Gate;
                             txtm:service "https://cloud-api.gate.ac.uk/process-document/annie-named-entity-recognizer?annotations=:Address&annotations=:Date&annotations=:Location&annotations=:Organization&annotations=:Person&annotations=:Money&annotations=:Percent&annotations=:Sentence" .
        }   
        '''

        self.tripleStore = tripleStore

    def sortu(self):
        sparql = SPARQLWrapper(self.tripleStore + '/statements')
        sparql.setQuery(self.eskaera)
        sparql.queryType = INSERT
        sparql.method = POST
        sparql.setHTTPAuth(BASIC)

        try:
            sparql.query()
        except ValueError as e:
            print(e)

class TextToTriple(object):
    def __init__(self, tripleStore, testua, named_graph):
        self.tripleStore = tripleStore
        self.grafoa = Graph()

        file = open(testua, 'r')
        self.testua = ""
        for i in file:
            self.testua += i + '\n'

        self.testua = unidecode(self.testua)
        self.testua = self.testua.replace("\"","")
        self.testua = self.testua.replace("\n","")
        self.uri = named_graph

    def getType(self,erlazioa):
        base = 'https://schema.org/'
        emaitza = ""

        if erlazioa == 'Location':
            emaitza = base + 'Place'
        else:
            emaitza = base + erlazioa
        return emaitza

    def balioztatu(self,subj,obj):
        baiEz = input(subj + " elementua " + obj + " bezala klasifikatu da, ondo dago? [B/E] \n")

        if baiEz.lower() == 'b': #https://j2logo.com/python/convertir-a-mayusculas-y-minusculas-en-python/
            return True,obj
        elif baiEz.lower() == 'e':
            zuzendu = input('Zuzendu nahi duzu? [B/E] \n')
            if zuzendu.lower() == 'b':
                type = input('Nola klasifikatu nahi duzu? \n 1.Person \n 2.Place \n 3.Entity \n')
                typeBerria = ""
                if type == '1':
                    typeBerria = 'Person'
                elif type == '2':
                    typeBerria = 'Place'
                elif typeBerria == '3':
                    typeBerria = 'Entity'
                return True, typeBerria
            else:
                return False,""

    def grafoaSortu(self,json):
        for i in json:
            try:
                if(i['annotationType']['value'] != 'Sentence' and i['annotationType']['value'] != 'Money' and i['annotationType']['value'] != 'Date'):
                    balioztatu, obj = self.balioztatu(i['annotationText']['value'],i['annotationType']['value'])
                    if(balioztatu):
                        id = i['annotationText']['value'].replace(' ','_')
                        subjektua = URIRef(self.uri + id)
                        objektua = URIRef(self.getType(obj))
                        self.grafoa.add((subjektua,RDF.type,objektua))
                        self.grafoa.add((subjektua,RDFS.label,Literal(i['annotationText']['value'])))
            except:
                pass

    def eskaeraEgin(self):
        eskaera = '''
            PREFIX txtm: <http://www.ontotext.com/textmining#>
            PREFIX txtm-inst: <http://www.ontotext.com/textmining/instance#>
            SELECT distinct ?annotationText ?annotationType
            WHERE {
                    ?searchDocument a txtm-inst:gateService;
                                       txtm:text \'\'\''''+ self.testua + '''\'\'\'.
            
                graph txtm-inst:gateService {
                    ?annotatedDocument txtm:annotations ?annotation .
            
                    ?annotation txtm:annotationText ?annotationText ;
                        txtm:annotationType ?annotationType ;
                        txtm:annotationStart ?annotationStart ;
                        txtm:annotationEnd ?annotationEnd ;
                    optional { ?annotation txtm:features ?item . ?item ?feature ?value }
                }
            }
                        '''
        sparql = SPARQLWrapper(self.tripleStore)
        sparql.setQuery(eskaera)
        sparql.setReturnFormat(JSON)

        try:
            res = sparql.queryAndConvert()
            self.grafoaSortu(res['results']['bindings'])
            return self.grafoa
        except ValueError as e:
            print(e)

class GateCloud(BezeroaSortu,TextToTriple):

    def irudiaDeskargatu(label,triple_store):
        #Konprobatuko da elementua dban ez dagoela
        eskaera = '''
        SELECT ?s ?p ?o
        WHERE{
            ?s rdfs:label "%s"
        }
        ''' %(label)

        sparql = SPARQLWrapper(triple_store)
        sparql.setQuery(eskaera)
        sparql.setReturnFormat(JSON)

        try:
            res = sparql.queryAndConvert()
            print(res)
            if not res['results']['bindings']: #Elementua ez da existitzen datu basean, irudia deskargatuko da
                os.system('python3 graphSource/source/irudiak_deskargatu.py ' + label)
        except ValueError as e:
            print(e)

    def sortuErlazioa(erlazioa):
        # URIak deklaratu
        schema = "https://schema.org/"
        erlazioPropioa = "http://ehu.eus/transparentrelations#"

        # Schema + kasu nabariak
        if erlazioa == "takes_part":
            emaitza = schema + "participant"
        elif erlazioa == "authors":
            emaitza = schema + "author"
        elif erlazioa == "works_for":
            emaitza = schema + "worksFor"

        # Schema + kasu orokorrak
        elif (erlazioa == "mentions" or erlazioa == "parent" or erlazioa == "owns" or erlazioa == "spouse" or erlazioa == "knows"):
            emaitza = schema + erlazioa

        # kasu orokorrak
        else:
            emaitza = erlazioPropioa + erlazioa

        return emaitza


    if __name__ == '__main__':
        procesador = Procesador(sys.argv[1])

        print('Gate Cloud bezeroa deklaratuko da...')
        deklarazioa = BezeroaSortu(procesador.triple_store)
        deklarazioa.sortu()

        print('Testua prozesatuko da...')
        textToTriple = TextToTriple(procesador.triple_store, procesador.data_source,procesador.named_graph)
        grafoa = textToTriple.eskaeraEgin()
        print("Lortutako entitateak hurrengoak izan dira")
        entitateak = []
        entiIzenak = []
        i = 1
        for s,p,o in grafoa:
            if 'label' in p:
                print(str(i) + ". " + o)
                entitateak.append(s)
                entiIzenak.append(o)
                i += 1

        subjektua = ""
        objektua = ""
        predZerrenda = ['parent','sibling','related_to','spouse','partner','knows','kontrolls','manages','represents','beneficiary_of','has_bank_account_in','worksFor','pays','part_of','registered_in','owns','gives','author','mentions','participant']
        atera = False
        print('Ateratzeko zenbaki bat ez den edozein giltza sakatu...')
        while not atera:
            subjektua = input('Sartu subjektuaren zenbakia...')
            objektua = input('Sartu objektuaren zenbakia...')

            try:
                subjektua = entitateak[int(subjektua) - 1]
                objektua = entitateak[int(objektua) - 1]

                for j in predZerrenda:
                    print(str(predZerrenda.index(j) + 1) + ". " + j)
                predikatua = predZerrenda[int(input('Aukeratu nahi duzun predikatua...'))-1]
                grafoa.add((URIRef(subjektua),URIRef(sortuErlazioa(predikatua)),URIRef(objektua)))

            except ValueError as e:
                print(e)
                atera = True

        deskargatu = input('Nodoen irudiak deskargatu nahí dituzu? [B/E]')
        if deskargatu.lower() == 'b':
            print('Irudiak deskargatuko dira...')
            for enti in entiIzenak:
                print(enti + ' elementuaren irudia deskargatuko da...')
                irudiaDeskargatu(enti,procesador.triple_store)


        fitx_prog = fitxategia_sortu.Grafo_fitxategia_sortu(procesador.rdf_output,grafoa)
        fitx_prog.main()

        zerb_igo = zerbitzarira_igo.Zerbitzarira_igo(procesador.rdf_output,procesador.triple_store,procesador.delete_graph)
        zerb_igo.zerbitzariraIgo()



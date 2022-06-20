from procesSource.source import Procesador
import os
import sys
from SPARQLWrapper import SPARQLWrapper, BASIC, INSERT, POST, SELECT, GET, JSON,RDF
from rdflib import Graph,URIRef
from rdflib.namespace import RDF
from unidecode import unidecode
import json

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
        sparql = SPARQLWrapper(self.tripleStore)
        sparql.setQuery(self.eskaera)
        sparql.queryType = INSERT
        sparql.method = POST
        sparql.setHTTPAuth(BASIC)

        try:
            sparql.query()
        except:
            not print('Algo ha ido mal...')

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

    def grafoaSortu(self,json):
        for i in json:
            if(i['annotationType']['value'] != 'Sentence' and i['annotationType']['value'] != 'Money'):
                id = i['annotationText']['value'].replace(' ','_')
                subjektua = URIRef(self.uri + id)
                objektua = URIRef(self.getType(i['annotationType']['value']))

                self.grafoa.add((subjektua,RDF.type,objektua))

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

        res = sparql.queryAndConvert()
        self.grafoaSortu(res['results']['bindings'])

        try:
            res = sparql.queryAndConvert()
            self.grafoaSortu(res['results']['bindings'])

            return self.grafoa
        except:
            print('Algo ha ido mal...')


class GateCloud(BezeroaSortu,TextToTriple):
    if __name__ == '__main__':

        procesador = Procesador(sys.argv[1])

        print('Gate Cloud bezeroa deklaratuko da...')
        deklarazioa = BezeroaSortu(procesador.triple_store)
        deklarazioa.sortu()

        print('Testua prozesatuko da...')
        textToTriple = TextToTriple(procesador.triple_store, procesador.data_source,procesador.named_graph)
        grafoa = textToTriple.eskaeraEgin()
        print(grafoa)


import os
import sys
from SPARQLWrapper import SPARQLWrapper, BASIC, INSERT, POST, SELECT, GET
from procesSource.source import Procesador
from rdflib import Graph


# pathLag = os.getcwd().split("/")[1:len(os.getcwd().split("/"))-2]
# path = ""
# for i in pathLag:
#     path += "/"+i
#
# sys.path.append(path)
# sys.path.append(path+"/source")

class SpacyDeklaratu(object):
    def __init__(self,tripleStore):
        self.eskaera = '''
            PREFIX txtm: <http://www.ontotex.com/textmining#>
            PREFIX txtm-inst: <http://www.ontotex.com/textmining/instance#>
            INSERT DATA{
                txtm-inst:localSpacy txtm:connect txtm:Spacy;
                    txtm:service "http://localhost:8000" .
            }
        '''
        self.tripleStore =tripleStore

    def deklaratu(self):
        sparql = SPARQLWrapper(self.tripleStore)
        sparql.setQuery(self.eskaera)
        sparql.queryType = INSERT
        sparql.method = POST
        sparql.setHTTPAuth(BASIC)

        try:
            sparql.query()
        except:
            not print('Algo ha ido mal...')

class FromTextToTriple(object):
    def __init__(self,tripleStore,testua):
        self.tripleStore = tripleStore
        self.grafoa = Graph()

        file = open(testua,'r')
        self.testua = ""
        for i in file:
            self.testua += i + '\n'

    def eskaeraEgin(self):
        eskaera = '''
        PREFIX txtm: <http://www.ontotext.com/textmining#>
        PREFIX txtm-inst: <http://www.ontotext.com/textmining/instance#>
        SELECT ?annotationText ?sentence ?annotationType ?annotationStart ?annotationEnd
        WHERE {
            ?searchDocument a txtm-inst:localSpacy;
                               txtm:text '''+self.testua+''' .
            graph txtm-inst:localSpacy {
                ?annotatedDocument txtm:annotations ?annotation .
                ?annotation txtm:annotationText ?annotationText ;
                        txtm:annotationKey ?annotationKey;
                        txtm:annotationType ?annotationType ;
                        txtm:annotationStart ?annotationStart ;
                        txtm:annotationEnd ?annotationEnd ;
                        optional {
                    ?annotation txtm:hasSentence/:sentenceText ?sentence.
                }
            }
        }
        '''

        print(eskaera)
        sparql = SPARQLWrapper(self.tripleStore)
        sparql.setQuery(eskaera)
        sparql.queryType = SELECT
        sparql.method = GET
        sparql.setHTTPAuth(BASIC)

        res = sparql.query()
        return self.grafoa.parse(res)

        try:
            res = sparql.query()
            return self.grafoa.parse(res)
        except:
            print('Algo ha ido mal...')

class SpacyServer(SpacyDeklaratu,FromTextToTriple):
    if __name__ == '__main__':
        print('SpaCy zerbitzaria martxan jarriko da...')
        komandoa = 'sh ./spacy_server/source/bash/docker_irudia_deskargatu.sh &'
        os.system(komandoa)

        procesador = Procesador(sys.argv[1])

        print('SpaCy zerbitzaria deklaratuko da...')
        deklarazioa = SpacyDeklaratu(procesador.triple_store)

        deklarazioa.deklaratu()

        print('Testua prozesatuko da...')
        textToTriple = FromTextToTriple(procesador.triple_store, procesador.data_source)
        grafoa = textToTriple.eskaeraEgin()
        print(grafoa)

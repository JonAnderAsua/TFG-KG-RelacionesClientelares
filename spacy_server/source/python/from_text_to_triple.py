from SPARQLWrapper import SPARQLWrapper, BASIC
from rdflib import Graph

class FromTextToTriple:
    def __init__(self,tripleStore,rdfOutput,testua):
        self.tripleStore = tripleStore
        self.rdfOutput = rdfOutput
        self.testua = testua
        self.grafoa = Graph()

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

        sparql = SPARQLWrapper(self.tripleStore)
        sparql.setQuery(eskaera)
        sparql.queryType = SELECT
        sparql.method = GET
        sparql.setHTTPAuth(BASIC)

        try:
            res = sparql.query()
            return self.grafoa.parse(res)
        except:
            print('Algo ha ido mal...')
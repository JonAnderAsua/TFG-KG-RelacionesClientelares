from SPARQLWrapper import SPARQLWrapper, BASIC, INSERT, POST

class spacyDeklaratu:
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
            print('Algo ha ido mal...')
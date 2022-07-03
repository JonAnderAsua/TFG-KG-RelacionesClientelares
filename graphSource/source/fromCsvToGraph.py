import logging
from rdflib import Graph, URIRef, Literal, RDFS
from rdflib.namespace import RDF
import os
import sys
from csv import reader


class FromCsvToGraph:

    def __init__(self,data,logs,named_graph):
        #CSVak
        self.helbideak = ""
        self.entitateak = ""
        self.bitartekariak = ""
        self.ofizialak = ""
        self.bestelakoak = ""
        self.erlazioak = ""

        #URIak
        self.uri_base = named_graph
        self.per = URIRef('https://schema.org/Person')
        self.ekit = URIRef('https://schema.org/Event')
        self.doku = URIRef('https://schema.org/Documentation')
        self.leku = URIRef('https://schema.org/Place')
        self.enti = URIRef('https://schema.org/Organization')
        self.arti = URIRef('https://schema.org/NewsArticle')

        self.grafo = Graph()

        if not '/home/runner/work/' in os.path.dirname(os.path.abspath(__file__)):
            logging.basicConfig(filename = logs, filemode = 'w', level = logging.DEBUG)
        self.data = data

    def setLabelAndType(self,csv):
        try:
            with open(self.data + csv) as file:
                csv_file = reader(file)
                for lerro in csv_file:
                    if(lerro[0] != 'node_id'):
                        triple = (URIRef(self.uri_base + '/' + lerro[0]), RDFS.label, Literal(lerro[2]))
                        logging.info("Sartutako triplea hurrengoa da...\n" + str(triple) + '\n')
                        self.grafo.add(triple)

                        if (int(lerro[0]) % 1000000 == 1): #Entitate bat da
                            type = self.enti
                        elif int(lerro[0]) % 100000 == 24:
                            type = self.leku
                        else:
                            type = self.per

                        triple = (URIRef(self.uri_base + '/' + lerro[0]), RDF.type, type)
                        logging.info("TYPE: Sartutako triplea hurrengoa da...\n" + str(triple) + '\n')
                        self.grafo.add(triple)
        except:
            logging.error('LABEL: Ezin izan da ' + csv + ' CSVa kargatu, programaren exekuzioa bukatuko da...\n')
            sys.exit(1)

    def getErlazioa(self,erlazioa):
        schema = 'https://schema.org/'
        erlazioPropioa = 'http://ehu.eus/transparentrelations#'

        if ('shareholder' in erlazioa.lower()):
            emaitza = schema + 'participant'
        elif 'registered' in erlazioa.lower():
            emaitza = erlazioPropioa + 'registered_in'
        elif 'director' in erlazioa.lower() or 'president' in erlazioa.lower() or 'owner' in erlazioa.lower():
            emaitza = schema + 'owns'
        elif 'control' in erlazioa.lower():
            emaitza = erlazioPropioa + 'controlls'
        elif 'manage' in erlazioa.lower():
            emaitza = erlazioPropioa + 'manages'
        elif 'beneficiary' in erlazioa.lower():
            emaitza = erlazioPropioa + 'beneficiary_of'
        else:
            emaitza = schema + 'worksFor'
        return emaitza

    def erlazioakAtera(self):
        try:
            with open(self.data + '/relationships.csv') as file:
                csv_file = reader(file)
                for lerro in csv_file:
                    erlazioa = self.getErlazioa(lerro[3])
                    triple = (self.uri_base + '/' + lerro[0], URIRef(erlazioa), self.uri_base + '/' + lerro[1])
                    logging.info("Sartutako triplea hurrengoa da...\n" + str(triple) + '\n')
                    self.grafo.add(triple)
        except:
            logging.error('Ezin izan da erlazioen CSVa kargatu, programaren exekuzioa bukatuko da...\n')
            sys.exit(1)

    def main(self):
        csvak = ['/nodes-addresses.csv','/nodes-entities.csv','/nodes-intermediaries.csv','/nodes-officers.csv','/nodes-others.csv']

        for i in csvak:
            self.setLabelAndType(i)

        # #Erlazioak ezarri
        self.erlazioakAtera()
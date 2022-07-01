import logging
import re
from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, URIRef, Literal, RDFS
from rdflib.namespace import RDF
import json
import os
import unidecode
import sys
import pandas as pd

class FromCsvToGraph:

    def __init__(self):
        #CSVak
        self.helbideak = ""
        self.entitateak = ""
        self.bitartekariak = ""
        self.ofizialak = ""
        self.bestelakoak = ""
        self.erlazioak = ""

        #URIak
        self.uri_base = 'http://ehu.eus/'
        self.per = URIRef('https://schema.org/Person')
        self.ekit = URIRef('https://schema.org/Event')
        self.doku = URIRef('https://schema.org/Documentation')
        self.leku = URIRef('https://schema.org/Place')
        self.enti = URIRef('https://schema.org/Organization')
        self.arti = URIRef('https://schema.org/NewsArticle')

        self.grafo = Graph()

        if not '/home/runner/work/' in os.path.dirname(os.path.abspath(__file__)):
            logging.basicConfig(filename = '/home/jonander/PycharmProjects/TFG-KG-RelacionesClientelares/logs/unekoLog.log', filemode = 'w', level = logging.DEBUG)
        self.data = '/home/jonander/PycharmProjects/TFG-KG-RelacionesClientelares/data/leaks'
        self.triple_store = 'http://localhost:7200/repositories/LaDonacion'

        uriTest = self.triple_store.split("/")[:len(self.triple_store.split("/")) - 1]
        self.testTripleStore = ""
        for i in uriTest:
            self.testTripleStore += i + "/"
        self.testTripleStore = self.testTripleStore[:len(self.testTripleStore) - 1]

    def csvakKargatu(self):
    #In: -
    #Out: CSVak kargatuta
        try:
            self.helbideak = pd.read_csv(self.data + '/nodes-addresses.csv')
        except:
            logging.error('Helbideen CSVa ez da kargatu, programaren exekuzioa bukatuko da...\n')
            sys.exit(1)

        try:
            self.entitateak = pd.read_csv(self.data + '/nodes-entities.csv')
        except:
            logging.error('Entitateen CSVa ez da kargatu, programaren exekuzioa bukatuko da...\n')
            sys.exit(1)

        try:
            self.bitartekariak = pd.read_csv(self.data + '/nodes-intermediaries.csv')
        except:
            logging.error('Bitartekarien CSVa ez da kargatu, programaren exekuzioa bukatuko da...\n')
            sys.exit(1)

        try:
            self.ofizialak = pd.read_csv(self.data + '/nodes-officers.csv')
        except:
            logging.error('Ofizialen CSVa ez da kargatu, programaren exekuzioa bukatuko da...\n')
            sys.exit(1)

        try:
            self.bestelakoak = pd.read_csv(self.data + '/nodes-others.csv')
        except:
            logging.error('Bestelakoen CSVa ez da kargatu, programaren exekuzioa bukatuko da...\n')
            sys.exit(1)

        try:
            self.erlazioak = pd.read_csv(self.data + '/nodes-relationships.csv')
        except:
            logging.error('Erlazioen CSVa ez da kargatu, programaren exekuzioa bukatuko da...\n')
            sys.exit(1)

    def setLabel(self,csv):
        for lerro in csv:
            triple = (self.uri_base + '/' + lerro['node_id'], RDFS.label, lerro['name'])
            logging.info("Sartutako triplea hurrengoa da...\n" + str(triple) + '\n')
            self.grafo.add(triple)

    def setType(self,csv):
        for lerro in csv:
            type = ''
            if (int(lerro['node_id']) % 1000000 == 1): #Entitate bat da
                type = self.enti
            elif int(lerro['node_id']) % 100000 == 24:
                type = self.leku
            else:
                type = self.per

            triple = (self.uri_base + '/' + lerro['node_id'], RDFS.label, type)
            logging.info("Sartutako triplea hurrengoa da...\n" + str(triple) + '\n')
            self.grafo.add(triple)


    def main(self):
        #CSVak kargatu
        self.csvakKargatu()

        #Labelak ezarri
        self.setLabel(self.helbideak)
        self.setLabel(self.entitateak)
        self.setLabel(self.ofizialak)
        self.setLabel(self.bitartekariak)
        self.setLabel(self.bestelakoak)
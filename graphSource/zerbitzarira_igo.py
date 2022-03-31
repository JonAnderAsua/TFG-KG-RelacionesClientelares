import logging
from SPARQLWrapper import SPARQLWrapper, BASIC, INSERT, POST, JSON
from rdflib import Graph, URIRef, Literal, RDFS
from rdflib.namespace import RDF
import json
import re
import os

class Zerbitzarira_igo:
    def __init__(self,rdf_output,triple_store,logs):
        self.triple_store = triple_store

        # Grafoa
        self.grafo = Graph()
        self.grafo.parse(rdf_output) #https://rdflib.readthedocs.io/en/stable/intro_to_parsing.html

        # Log
        logging.basicConfig(filename=logs, filemode='w', level=logging.DEBUG)

    def zerbitzariraIgo(self):
    #In: -
    #Out: Aurretik sortutako fitxategia zerbitzariaren Graphdb instantziara igo

        for s,p,o in self.grafo:
            if("http://ehu.eus" in o or "https://schema.org" in o):
                queryStringUpload = 'INSERT DATA  { <%s> <%s> <%s> }' %(s,p,o)
            else:
                queryStringUpload = 'INSERT DATA  { <%s> <%s> "%s" }' % (s, p, o)
            sparql = SPARQLWrapper(self.triple_store)
            sparql.setQuery(queryStringUpload)
            sparql.queryType = INSERT
            sparql.method = POST
            sparql.setHTTPAuth(BASIC)

            try:
                ret = sparql.query()
            except:
                logging.error("Ezin izan da " + str((s, p, o)) + " triplea grafoan sartu...\n")
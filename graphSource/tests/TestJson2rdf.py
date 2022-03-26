import unittest
import rdflib

import sys

sys.path.append("/home/jonander/PycharmProjects/TFG-KG-RelacionesClientelares/graphSource")
from graphSource import json2rdf

class TestJson2rdf(unittest.TestCase):
    json2rdf.jsonakKargatu()
    jsonZerrenda = json2rdf.getJsonak()


    def test_setType(self):
        json2rdf.setType(rdflib.term.URIRef("http://ehu.eus/id/article/larazon_dajbkoztojbfnn5rdokylamu7i"),rdflib.term.URIRef("https://schema.org/NewsArticle"))
        json2rdf.setType(rdflib.term.URIRef("http://ehu.eus/id/document/carta_kobre_kim_3"),rdflib.term.URIRef("https://schema.org/Documentation"))
        json2rdf.setType(rdflib.term.URIRef("http://ehu.eus/id/entity/ohl"),rdflib.term.URIRef("https://schema.org/Organization"))
        json2rdf.setType(rdflib.term.URIRef("http://ehu.eus/id/event/disolucion_de_apollonia"),rdflib.term.URIRef("https://schema.org/Event"))
        json2rdf.setType(rdflib.term.URIRef("http://ehu.eus/id/person/elena"),rdflib.term.URIRef("https://schema.org/Person"))
        json2rdf.setType(rdflib.term.URIRef("http://ehu.eus/id/place/princes_gate_5"),rdflib.term.URIRef("https://schema.org/Place"))

        self.assertEqual('https://schema.org/NewsArticle',json2rdf.getTypeFromGraph("http://ehu.eus/id/article/larazon_dajbkoztojbfnn5rdokylamu7i"))
        self.assertEqual('https://schema.org/Documentation',json2rdf.getTypeFromGraph("http://ehu.eus/id/document/carta_kobre_kim_3"))
        self.assertEqual('https://schema.org/Organization', json2rdf.getTypeFromGraph("http://ehu.eus/id/entity/ohl"))
        self.assertEqual('https://schema.org/Event',json2rdf.getTypeFromGraph("http://ehu.eus/id/event/disolucion_de_apollonia"))
        self.assertEqual('https://schema.org/Person',json2rdf.getTypeFromGraph("http://ehu.eus/id/person/juan_carlos"))
        self.assertEqual('https://schema.org/Place',json2rdf.getTypeFromGraph("http://ehu.eus/id/place/princes_gate_5"))


    def test_setLabel(self):
        #Datuak sartuko dira
        json2rdf.setLabel(rdflib.term.URIRef("http://ehu.eus/id/article/larazon_dajbkoztojbfnn5rdokylamu7i"), self.jsonZerrenda[0], "articles")
        json2rdf.setLabel(rdflib.term.URIRef("http://ehu.eus/id/document/carta_kobre_kim_3"), self.jsonZerrenda[1], "documents")
        json2rdf.setLabel(rdflib.term.URIRef("http://ehu.eus/id/entity/ohl"), self.jsonZerrenda[2], "entities")
        json2rdf.setLabel(rdflib.term.URIRef("http://ehu.eus/id/event/disolucion_de_apollonia"), self.jsonZerrenda[3], "events")
        json2rdf.setLabel(rdflib.term.URIRef("http://ehu.eus/id/person/juan_carlos"), self.jsonZerrenda[4], "persons")
        json2rdf.setLabel(rdflib.term.URIRef("http://ehu.eus/id/place/princes_gate_5"), self.jsonZerrenda[5], "places")

        self.assertEquals('Corinna y Zanganeh  Dos versiones contradictorias de la supuesta comisi n del Rey', json2rdf.getLabelFromGraph("http://ehu.eus/id/article/larazon_dajbkoztojbfnn5rdokylamu7i"))
        self.assertEquals('Primera carta a Zarzuela de los abogados de Corinna', json2rdf.getLabelFromGraph("http://ehu.eus/id/document/carta_kobre_kim_3"))
        self.assertEquals('OHL', json2rdf.getLabelFromGraph("http://ehu.eus/id/entity/ohl"))
        self.assertEquals('Corinna disuelve Apollonia Associates', json2rdf.getLabelFromGraph("http://ehu.eus/id/event/disolucion_de_apollonia"))
        self.assertEquals('S M  el Rey Don Juan Carlos', json2rdf.getLabelFromGraph("http://ehu.eus/id/person/juan_carlos"))
        self.assertEquals('Princes Gate  5', json2rdf.getLabelFromGraph("http://ehu.eus/id/place/princes_gate_5"))



    def test_setComent(self):
        self.maxDiff = None

        # Datuak sartuko dira (Artikuluak eta dokumentuak ez daukate komentariorik)
        json2rdf.setComent(rdflib.term.URIRef("http://ehu.eus/id/entity/ohl"), self.jsonZerrenda[2], "entities")
        json2rdf.setComent(rdflib.term.URIRef("http://ehu.eus/id/event/disolucion_de_apollonia"), self.jsonZerrenda[3],"events")
        json2rdf.setComent(rdflib.term.URIRef("http://ehu.eus/id/person/elena"), self.jsonZerrenda[4], "persons")
        json2rdf.setComent(rdflib.term.URIRef("http://ehu.eus/id/place/princes_gate_5"), self.jsonZerrenda[5], "places")

        self.assertEquals('Empresa constructora multinacional espa ola  fundada y presidida por  a href    persons villar mir  Juan Miguel Villar Mir  a  y cotizada en el IBEX 35  OHL es una de las compa  as adjudicatarias del  a href    events anuncio adjudicacion ave  hist rico contrato para construir el AVE a La Meca  a   un acuerdo comercial para el que se vali  del asesoramiento de la saud   a href    persons zanganeh  Shahphari Zanganeh  a  ', json2rdf.getCommentFromGraph("http://ehu.eus/id/entity/ohl"))
        self.assertEquals('Tan solo unas semanas de la adjudicaci n del  em megacontrato  em  para la  a href    events anuncio adjudicacion ave  construcci n del AVE a La Meca  a    a href    persons corinna  Corinna zu Sayn Wittgenstein  a  disuelve sus sociedad  a href    entities apollonia  Apollonia Ventures  a   que hab a constituido en noviembre de 2005 ', json2rdf.getCommentFromGraph("http://ehu.eus/id/event/disolucion_de_apollonia"))
        self.assertEquals('La hija mayor de los reyes de Espa a   a href    persons juan carlos  Juan Carlos  a  y  a href    persons sofia de grecia  Sof a  a   figura junto con su padre y sus hermanos  a href    persons felipe vi  el rey Felipe VI  a  y  a href    persons cristina  Cristina de Borb n  a   como beneficiaria de la  a href    entities zagatka  fundaci n Zagatka  a   una entidad dada de alta en  a href    places liechtenstein  Liechtenstein  a  bajo el control de un pariente lejano   a href    persons alvaro de orleans   lvaro de Orleans Borb n  a  ', json2rdf.getCommentFromGraph("http://ehu.eus/id/person/elena"))
        self.assertEquals('Exclusivo  tico en el barrio de Knightsbride  que el  a href    persons qabus bin said  sult n de Om n  a  adquiri  por 50 millones de libras  62 7 millones de euros  un r cord del momento  para ponerlo a disposici n del  a href    persons juan carlos  rey Juan Carlos  a   quien  a href    events viaje a oman  hab a visitado el pa s  rabe  a  apenas dos meses antes ', json2rdf.getCommentFromGraph("http://ehu.eus/id/place/princes_gate_5"))




    #setTypeLabelComent metodoa aurreko hiru metodoetan frogatzen da

    def test_forPersonsToPeople(self):
        self.assertEquals("people",json2rdf.forPersonsToPeople("persons"))
        self.assertEquals("events",json2rdf.forPersonsToPeople("events"))
        self.assertEquals("documents", json2rdf.forPersonsToPeople("documents"))
        self.assertEquals("places", json2rdf.forPersonsToPeople("places"))
        self.assertEquals("entities", json2rdf.forPersonsToPeople("entities"))
        self.assertEquals("articles", json2rdf.forPersonsToPeople("articles"))

    def test_erlazioaAldatu(self):
        #Kasu nabariak
        self.assertEquals("https://schema.org/participant", json2rdf.erlazioaAldatu("takes_part"))
        self.assertEquals("https://schema.org/author", json2rdf.erlazioaAldatu("authors"))
        self.assertEquals("https://schema.org/worksFor", json2rdf.erlazioaAldatu("works_for"))

        #Schema + kasu orokorrak
        self.assertEquals("https://schema.org/mentions", json2rdf.erlazioaAldatu("mentions"))
        self.assertEquals("https://schema.org/parent", json2rdf.erlazioaAldatu("parent"))
        self.assertEquals("https://schema.org/owns", json2rdf.erlazioaAldatu("owns"))
        self.assertEquals("https://schema.org/spouse", json2rdf.erlazioaAldatu("spouse"))
        self.assertEquals("https://schema.org/knows", json2rdf.erlazioaAldatu("knows"))

        #Ontologia propioa + kasu orokorrak
        self.assertEquals("http://ehu.eus/transparentrelations#has_bank_account_in", json2rdf.erlazioaAldatu("has_bank_account_in"))
        self.assertEquals("http://ehu.eus/transparentrelations#partner", json2rdf.erlazioaAldatu("partner"))
        self.assertEquals("http://ehu.eus/transparentrelations#represents", json2rdf.erlazioaAldatu("represents"))
        self.assertEquals("http://ehu.eus/transparentrelations#pays", json2rdf.erlazioaAldatu("pays"))
        self.assertEquals("http://ehu.eus/transparentrelations#controls", json2rdf.erlazioaAldatu("controls"))
        self.assertEquals("http://ehu.eus/transparentrelations#registered_in", json2rdf.erlazioaAldatu("registered_in"))
        self.assertEquals("http://ehu.eus/transparentrelations#gives", json2rdf.erlazioaAldatu("gives"))
        self.assertEquals("http://ehu.eus/transparentrelations#beneficiary_of", json2rdf.erlazioaAldatu("beneficiary_of"))
        self.assertEquals("http://ehu.eus/transparentrelations#related_to", json2rdf.erlazioaAldatu("related_to"))
        self.assertEquals("http://ehu.eus/transparentrelations#sibling", json2rdf.erlazioaAldatu("sibling"))
        self.assertEquals("http://ehu.eus/transparentrelations#happens_in", json2rdf.erlazioaAldatu("happens_in"))
        self.assertEquals("http://ehu.eus/transparentrelations#manages", json2rdf.erlazioaAldatu("manages"))


    def test_subjektuaObjektuaTratatu(self):
        #Pertsona
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/person/mariano_rajoy"), json2rdf.subjektuaObjektuaTratatu("#/persons/mariano_rajoy"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/person/cristina"), json2rdf.subjektuaObjektuaTratatu("#/persons/cristina"))

        #Ekitaldi
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/event/retirada_ducado_cristina"), json2rdf.subjektuaObjektuaTratatu("#/events/retirada_ducado_cristina"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/event/disolucion_de_apollonia"),json2rdf.subjektuaObjektuaTratatu("#/events/disolucion_de_apollonia"))

        #Entitateak
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/entity/apollonia"),json2rdf.subjektuaObjektuaTratatu("#/entities/apollonia"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/entity/sanchez_junco_abogados"),json2rdf.subjektuaObjektuaTratatu("#/entities/sanchez_junco_abogados"))

        #Dokumentuak
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/document/aeat_juan_carlos_2018"),json2rdf.subjektuaObjektuaTratatu("#/documents/aeat_juan_carlos_2018"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/document/segundo_comunicado_regularizacion_fiscal"),json2rdf.subjektuaObjektuaTratatu("#/documents/segundo_comunicado_regularizacion_fiscal"))

        #Places
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/place/georges_favon_29"),json2rdf.subjektuaObjektuaTratatu("#/places/georges_favon_29"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/place/belgrave"),json2rdf.subjektuaObjektuaTratatu("#/places/belgrave"))

        #Artikuluak
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/article/elespanol_503950285"),json2rdf.subjektuaObjektuaTratatu("#/articles/elespanol_503950285"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/article/elespanol_320468523"), json2rdf.subjektuaObjektuaTratatu("##/articles/elespanol_320468523"))

        #Sortutako adibide propio batzuk
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/person/jon_ander_asua"),json2rdf.subjektuaObjektuaTratatu("#/persons/jon_ander_asua"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/place/gallarta"),json2rdf.subjektuaObjektuaTratatu("#/places/gallarta"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/event/ekitaldi"),json2rdf.subjektuaObjektuaTratatu("#/events/ekitaldi"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/entity/entitatea"),json2rdf.subjektuaObjektuaTratatu("#/entities/entitatea"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/document/dokumentua"),json2rdf.subjektuaObjektuaTratatu("#/documents/dokumentua"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/article/artikulua"),json2rdf.subjektuaObjektuaTratatu("#/articles/artikulua"))

    def test_grafoaEraiki(self):
        pass

# test_zerbitzariraIgo(self) beste metodoen barnean frogatzen da eskaerak zerbitzariaren kontra egiten direlako












if __name__ == '__main__':
    unittest.main()
import unittest
import rdflib

import sys
from graphSource.source import grafo_objektua_sortu
from procesSource.source import Procesador

sys.path.append("/home/jonander/PycharmProjects/TFG-KG-RelacionesClientelares")
from graphSource import json2rdf
class TestJson2rdf(unittest.TestCase):

    def setUp(self) :
        super(TestJson2rdf, self).__init__()
        procesador = Procesador.Procesador("la_donacion")
        self.grafo_objektua = grafo_objektua_sortu.Grafo_fitxategia_sortu(procesador.data_source,procesador.logs,procesador.named_graph,procesador.triple_store)
        self.grafo_objektua.jsonakKargatu()
        self.jsonZerrenda = self.grafo_objektua.getJsonak()


    def test_setType(self):
        self.grafo_objektua.setType(rdflib.term.URIRef("http://ehu.eus/id/article/larazon_dajbkoztojbfnn5rdokylamu7i"),rdflib.term.URIRef("https://schema.org/NewsArticle"))
        self.grafo_objektua.setType(rdflib.term.URIRef("http://ehu.eus/id/document/carta_kobre_kim_3"),rdflib.term.URIRef("https://schema.org/Documentation"))
        self.grafo_objektua.setType(rdflib.term.URIRef("http://ehu.eus/id/entity/ohl"),rdflib.term.URIRef("https://schema.org/Organization"))
        self.grafo_objektua.setType(rdflib.term.URIRef("http://ehu.eus/id/event/disolucion_de_apollonia"),rdflib.term.URIRef("https://schema.org/Event"))
        self.grafo_objektua.setType(rdflib.term.URIRef("http://ehu.eus/id/person/elena"),rdflib.term.URIRef("https://schema.org/Person"))
        self.grafo_objektua.setType(rdflib.term.URIRef("http://ehu.eus/id/place/princes_gate_5"),rdflib.term.URIRef("https://schema.org/Place"))

# <<<<<<< HEAD
#         self.assertEqual('https://schema.org/NewsArticle',json2rdf.getTypeFromGraph("http://ehu.eus/id/article/larazon_dajbkoztojbfnn5rdokylamu7i"))
#         self.assertEqual('https://schema.org/Documentation',json2rdf.getTypeFromGraph("http://ehu.eus/id/document/carta_kobre_kim_3"))
#         self.assertEqual('https://schema.org/Organization', json2rdf.getTypeFromGraph("http://ehu.eus/id/entity/ohl"))
#         self.assertEqual('https://schema.org/Event',json2rdf.getTypeFromGraph("http://ehu.eus/id/event/disolucion_de_apollonia"))
#         self.assertEqual('https://schema.org/Person',json2rdf.getTypeFromGraph("http://ehu.eus/id/person/juan_carlos"))
#         self.assertEqual('https://schema.org/Place',json2rdf.getTypeFromGraph("http://ehu.eus/id/place/princes_gate_5"))
# =======
        self.assertEquals('https://schema.org/NewsArticle',self.grafo_objektua.getTypeFromGraph("http://ehu.eus/id/article/larazon_dajbkoztojbfnn5rdokylamu7i"))
        self.assertEquals('https://schema.org/Documentation',self.grafo_objektua.getTypeFromGraph("http://ehu.eus/id/document/carta_kobre_kim_3"))
        self.assertEquals('https://schema.org/Organization', self.grafo_objektua.getTypeFromGraph("http://ehu.eus/id/entity/ohl"))
        self.assertEquals('https://schema.org/Event',self.grafo_objektua.getTypeFromGraph("http://ehu.eus/id/event/disolucion_de_apollonia"))
        self.assertEquals('https://schema.org/Person',self.grafo_objektua.getTypeFromGraph("http://ehu.eus/id/person/juan_carlos"))
        self.assertEquals('https://schema.org/Place',self.grafo_objektua.getTypeFromGraph("http://ehu.eus/id/place/princes_gate_5"))
# >>>>>>> develop


    def test_setLabel(self):
        #Datuak sartuko dira
        self.grafo_objektua.setLabel(rdflib.term.URIRef("http://ehu.eus/id/article/larazon_dajbkoztojbfnn5rdokylamu7i"), self.jsonZerrenda[0], "articles")
        self.grafo_objektua.setLabel(rdflib.term.URIRef("http://ehu.eus/id/document/carta_kobre_kim_3"), self.jsonZerrenda[1], "documents")
        self.grafo_objektua.setLabel(rdflib.term.URIRef("http://ehu.eus/id/entity/ohl"), self.jsonZerrenda[2], "entities")
        self.grafo_objektua.setLabel(rdflib.term.URIRef("http://ehu.eus/id/event/disolucion_de_apollonia"), self.jsonZerrenda[3], "events")
        self.grafo_objektua.setLabel(rdflib.term.URIRef("http://ehu.eus/id/person/juan_carlos"), self.jsonZerrenda[4], "persons")
        self.grafo_objektua.setLabel(rdflib.term.URIRef("http://ehu.eus/id/place/princes_gate_5"), self.jsonZerrenda[5], "places")

        self.assertEquals('Corinna y Zanganeh: Dos versiones contradictorias de la supuesta comision del Rey', self.grafo_objektua.getLabelFromGraph("http://ehu.eus/id/article/larazon_dajbkoztojbfnn5rdokylamu7i"))
        self.assertEquals('Primera carta a Zarzuela de los abogados de Corinna', self.grafo_objektua.getLabelFromGraph("http://ehu.eus/id/document/carta_kobre_kim_3"))
        self.assertEquals('OHL', self.grafo_objektua.getLabelFromGraph("http://ehu.eus/id/entity/ohl"))
        self.assertEquals('Corinna disuelve Apollonia Associates', self.grafo_objektua.getLabelFromGraph("http://ehu.eus/id/event/disolucion_de_apollonia"))
        self.assertEquals('S.M. el Rey Don Juan Carlos', self.grafo_objektua.getLabelFromGraph("http://ehu.eus/id/person/juan_carlos"))
        self.assertEquals('Princes Gate, 5', self.grafo_objektua.getLabelFromGraph("http://ehu.eus/id/place/princes_gate_5"))



    def test_setComent(self):
        self.maxDiff = None

        # Datuak sartuko dira (Artikuluak eta dokumentuak ez daukate komentariorik)
        self.grafo_objektua.setComent(rdflib.term.URIRef("http://ehu.eus/id/entity/ohl"), self.jsonZerrenda[2], "entities")
        self.grafo_objektua.setComent(rdflib.term.URIRef("http://ehu.eus/id/event/disolucion_de_apollonia"), self.jsonZerrenda[3],"events")
        self.grafo_objektua.setComent(rdflib.term.URIRef("http://ehu.eus/id/person/elena"), self.jsonZerrenda[4], "persons")
        self.grafo_objektua.setComent(rdflib.term.URIRef("http://ehu.eus/id/place/princes_gate_5"), self.jsonZerrenda[5], "places")

        self.assertEquals('Empresa constructora multinacional espanola, fundada y presidida por Juan Miguel Villar Mir y cotizada en el IBEX 35. OHL es una de las companias adjudicatarias del historico contrato para construir el AVE a La Meca, un acuerdo comercial para el que se valio del asesoramiento de la saudi Shahphari Zanganeh.', self.grafo_objektua.getCommentFromGraph("http://ehu.eus/id/entity/ohl"))
        self.assertEquals('Tan solo unas semanas de la adjudicacion del megacontrato para la construccion del AVE a La Meca, Corinna zu Sayn-Wittgenstein disuelve sus sociedad Apollonia Ventures, que habia constituido en noviembre de 2005.', self.grafo_objektua.getCommentFromGraph("http://ehu.eus/id/event/disolucion_de_apollonia"))
        self.assertEquals('La hija mayor de los reyes de Espana, Juan Carlos y Sofia, figura junto con su padre y sus hermanos el rey Felipe VI y Cristina de Borbon, como beneficiaria de la fundacion Zagatka, una entidad dada de alta en Liechtenstein bajo el control de un pariente lejano: Alvaro de Orleans-Borbon.', self.grafo_objektua.getCommentFromGraph("http://ehu.eus/id/person/elena"))
        self.assertEquals('Exclusivo atico en el barrio de Knightsbride, que el sultan de Oman adquirio por 50 millones de libras (62,7 millones de euros, un record del momento) para ponerlo a disposicion del rey Juan Carlos, quien habia visitado el pais arabe apenas dos meses antes.', self.grafo_objektua.getCommentFromGraph("http://ehu.eus/id/place/princes_gate_5"))
    #setTypeLabelComent metodoa aurreko hiru metodoetan frogatzen da

    def test_forPersonsToPeople(self):
        self.assertEquals("people",self.grafo_objektua.forPersonsToPeople("persons"))
        self.assertEquals("events",self.grafo_objektua.forPersonsToPeople("events"))
        self.assertEquals("documents", self.grafo_objektua.forPersonsToPeople("documents"))
        self.assertEquals("places", self.grafo_objektua.forPersonsToPeople("places"))
        self.assertEquals("entities", self.grafo_objektua.forPersonsToPeople("entities"))
        self.assertEquals("articles", self.grafo_objektua.forPersonsToPeople("articles"))

    def test_erlazioaAldatu(self):
        #Kasu nabariak
        self.assertEquals("https://schema.org/participant", self.grafo_objektua.erlazioaAldatu("takes_part"))
        self.assertEquals("https://schema.org/author", self.grafo_objektua.erlazioaAldatu("authors"))
        self.assertEquals("https://schema.org/worksFor", self.grafo_objektua.erlazioaAldatu("works_for"))

        #Schema + kasu orokorrak
        self.assertEquals("https://schema.org/mentions", self.grafo_objektua.erlazioaAldatu("mentions"))
        self.assertEquals("https://schema.org/parent", self.grafo_objektua.erlazioaAldatu("parent"))
        self.assertEquals("https://schema.org/owns", self.grafo_objektua.erlazioaAldatu("owns"))
        self.assertEquals("https://schema.org/spouse", self.grafo_objektua.erlazioaAldatu("spouse"))
        self.assertEquals("https://schema.org/knows", self.grafo_objektua.erlazioaAldatu("knows"))

        #Ontologia propioa + kasu orokorrak
        self.assertEquals("http://ehu.eus/transparentrelations#has_bank_account_in", self.grafo_objektua.erlazioaAldatu("has_bank_account_in"))
        self.assertEquals("http://ehu.eus/transparentrelations#partner", self.grafo_objektua.erlazioaAldatu("partner"))
        self.assertEquals("http://ehu.eus/transparentrelations#represents", self.grafo_objektua.erlazioaAldatu("represents"))
        self.assertEquals("http://ehu.eus/transparentrelations#pays", self.grafo_objektua.erlazioaAldatu("pays"))
        self.assertEquals("http://ehu.eus/transparentrelations#controls", self.grafo_objektua.erlazioaAldatu("controls"))
        self.assertEquals("http://ehu.eus/transparentrelations#registered_in", self.grafo_objektua.erlazioaAldatu("registered_in"))
        self.assertEquals("http://ehu.eus/transparentrelations#gives", self.grafo_objektua.erlazioaAldatu("gives"))
        self.assertEquals("http://ehu.eus/transparentrelations#beneficiary_of", self.grafo_objektua.erlazioaAldatu("beneficiary_of"))
        self.assertEquals("http://ehu.eus/transparentrelations#related_to", self.grafo_objektua.erlazioaAldatu("related_to"))
        self.assertEquals("http://ehu.eus/transparentrelations#sibling", self.grafo_objektua.erlazioaAldatu("sibling"))
        self.assertEquals("http://ehu.eus/transparentrelations#happens_in", self.grafo_objektua.erlazioaAldatu("happens_in"))
        self.assertEquals("http://ehu.eus/transparentrelations#manages", self.grafo_objektua.erlazioaAldatu("manages"))


    def test_subjektuaObjektuaTratatu(self):
        #Pertsona
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/person/mariano_rajoy"), self.grafo_objektua.subjektuaObjektuaTratatu("#/persons/mariano_rajoy"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/person/cristina"), self.grafo_objektua.subjektuaObjektuaTratatu("#/persons/cristina"))

        #Ekitaldi
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/event/retirada_ducado_cristina"), self.grafo_objektua.subjektuaObjektuaTratatu("#/events/retirada_ducado_cristina"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/event/disolucion_de_apollonia"),self.grafo_objektua.subjektuaObjektuaTratatu("#/events/disolucion_de_apollonia"))

        #Entitateak
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/entity/apollonia"),self.grafo_objektua.subjektuaObjektuaTratatu("#/entities/apollonia"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/entity/sanchez_junco_abogados"),self.grafo_objektua.subjektuaObjektuaTratatu("#/entities/sanchez_junco_abogados"))

        #Dokumentuak
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/document/aeat_juan_carlos_2018"),self.grafo_objektua.subjektuaObjektuaTratatu("#/documents/aeat_juan_carlos_2018"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/document/segundo_comunicado_regularizacion_fiscal"),self.grafo_objektua.subjektuaObjektuaTratatu("#/documents/segundo_comunicado_regularizacion_fiscal"))

        #Places
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/place/georges_favon_29"),self.grafo_objektua.subjektuaObjektuaTratatu("#/places/georges_favon_29"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/place/belgrave"),self.grafo_objektua.subjektuaObjektuaTratatu("#/places/belgrave"))

        #Artikuluak
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/article/elespanol_503950285"),self.grafo_objektua.subjektuaObjektuaTratatu("#/articles/elespanol_503950285"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/article/elespanol_320468523"), self.grafo_objektua.subjektuaObjektuaTratatu("##/articles/elespanol_320468523"))

        #Sortutako adibide propio batzuk
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/person/jon_ander_asua"),self.grafo_objektua.subjektuaObjektuaTratatu("#/persons/jon_ander_asua"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/place/gallarta"),self.grafo_objektua.subjektuaObjektuaTratatu("#/places/gallarta"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/event/ekitaldi"),self.grafo_objektua.subjektuaObjektuaTratatu("#/events/ekitaldi"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/entity/entitatea"),self.grafo_objektua.subjektuaObjektuaTratatu("#/entities/entitatea"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/document/dokumentua"),self.grafo_objektua.subjektuaObjektuaTratatu("#/documents/dokumentua"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/article/artikulua"),self.grafo_objektua.subjektuaObjektuaTratatu("#/articles/artikulua"))

# test_zerbitzariraIgo(self) beste metodoen barnean frogatzen da eskaerak zerbitzariaren kontra egiten direlako

if __name__ == '__main__':
    unittest.main()
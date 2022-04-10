import unittest
import rdflib

class TestJson2rdf(unittest.TestCase):

    def __init__(self,json2rdf):
        super(TestJson2rdf,self).__init__() #https://stackoverflow.com/questions/52369509/attributeerror-object-has-no-attribute-type-equality-funcs
        self.json2rdf = json2rdf
        self.json2rdf.jsonakKargatu()
        self.jsonZerrenda = self.json2rdf.getJsonak()
        self.exekutatuTestak()

    def test_setType(self):
        self.json2rdf.setType(rdflib.term.URIRef("http://ehu.eus/id/article/larazon_dajbkoztojbfnn5rdokylamu7i"),rdflib.term.URIRef("https://schema.org/NewsArticle"))
        self.json2rdf.setType(rdflib.term.URIRef("http://ehu.eus/id/document/carta_kobre_kim_3"),rdflib.term.URIRef("https://schema.org/Documentation"))
        self.json2rdf.setType(rdflib.term.URIRef("http://ehu.eus/id/entity/ohl"),rdflib.term.URIRef("https://schema.org/Organization"))
        self.json2rdf.setType(rdflib.term.URIRef("http://ehu.eus/id/event/disolucion_de_apollonia"),rdflib.term.URIRef("https://schema.org/Event"))
        self.json2rdf.setType(rdflib.term.URIRef("http://ehu.eus/id/person/elena"),rdflib.term.URIRef("https://schema.org/Person"))
        self.json2rdf.setType(rdflib.term.URIRef("http://ehu.eus/id/place/princes_gate_5"),rdflib.term.URIRef("https://schema.org/Place"))

        self.assertEqual('https://schema.org/NewsArticle',self.json2rdf.getTypeFromGraph("http://ehu.eus/id/article/20minutos_1382624"))
        self.assertEqual('https://schema.org/Documentation',self.json2rdf.getTypeFromGraph("http://ehu.eus/id/document/2_reglamento_zagatka"))
        self.assertEqual('https://schema.org/Organization', self.json2rdf.getTypeFromGraph("http://ehu.eus/id/entity/aeat"))
        self.assertEqual('https://schema.org/Event',self.json2rdf.getTypeFromGraph("http://ehu.eus/id/event/abdicacion_anuncio"))
        self.assertEqual('https://schema.org/Person',self.json2rdf.getTypeFromGraph("http://ehu.eus/id/person/juan_carlos"))
        self.assertEqual('https://schema.org/Place',self.json2rdf.getTypeFromGraph("http://ehu.eus/id/place/princes_gate_5"))


    def test_setLabel(self):
        #Datuak sartuko dira
        self.json2rdf.setLabel(rdflib.term.URIRef("http://ehu.eus/id/article/larazon_dajbkoztojbfnn5rdokylamu7i"), self.jsonZerrenda[0], "articles")
        self.json2rdf.setLabel(rdflib.term.URIRef("http://ehu.eus/id/document/carta_kobre_kim_3"), self.jsonZerrenda[1], "documents")
        self.json2rdf.setLabel(rdflib.term.URIRef("http://ehu.eus/id/entity/ohl"), self.jsonZerrenda[2], "entities")
        self.json2rdf.setLabel(rdflib.term.URIRef("http://ehu.eus/id/event/disolucion_de_apollonia"), self.jsonZerrenda[3], "events")
        self.json2rdf.setLabel(rdflib.term.URIRef("http://ehu.eus/id/person/juan_carlos"), self.jsonZerrenda[4], "persons")
        self.json2rdf.setLabel(rdflib.term.URIRef("http://ehu.eus/id/place/princes_gate_5"), self.jsonZerrenda[5], "places")

        self.assertEquals('Corinna y Zanganeh  Dos versiones contradictorias de la supuesta comisi n del Rey', self.json2rdf.getLabelFromGraph("http://ehu.eus/id/article/larazon_dajbkoztojbfnn5rdokylamu7i"))
        self.assertEquals('Primera carta a Zarzuela de los abogados de Corinna', self.json2rdf.getLabelFromGraph("http://ehu.eus/id/document/carta_kobre_kim_3"))
        self.assertEquals('OHL', self.json2rdf.getLabelFromGraph("http://ehu.eus/id/entity/ohl"))
        self.assertEquals('Corinna disuelve Apollonia Associates', self.json2rdf.getLabelFromGraph("http://ehu.eus/id/event/disolucion_de_apollonia"))
        self.assertEquals('S M  el Rey Don Juan Carlos', self.json2rdf.getLabelFromGraph("http://ehu.eus/id/person/juan_carlos"))
        self.assertEquals('Princes Gate  5', self.json2rdf.getLabelFromGraph("http://ehu.eus/id/place/princes_gate_5"))



    def test_setComent(self):
        # Datuak sartuko dira (Artikuluak eta dokumentuak ez daukate komentariorik)
        self.json2rdf.setComent(rdflib.term.URIRef("http://ehu.eus/id/entity/ohl"), self.jsonZerrenda[2], "entities")
        self.json2rdf.setComent(rdflib.term.URIRef("http://ehu.eus/id/event/disolucion_de_apollonia"), self.jsonZerrenda[3],"events")
        self.json2rdf.setComent(rdflib.term.URIRef("http://ehu.eus/id/person/elena"), self.jsonZerrenda[4], "persons")
        self.json2rdf.setComent(rdflib.term.URIRef("http://ehu.eus/id/place/princes_gate_5"), self.jsonZerrenda[5], "places")

        self.assertEquals('Empresa constructora multinacional espa ola  fundada y presidida por  a href    persons villar mir  Juan Miguel Villar Mir  a  y cotizada en el IBEX 35  OHL es una de las compa  as adjudicatarias del  a href    events anuncio adjudicacion ave  hist rico contrato para construir el AVE a La Meca  a   un acuerdo comercial para el que se vali  del asesoramiento de la saud   a href    persons zanganeh  Shahphari Zanganeh  a  ', self.json2rdf.getCommentFromGraph("http://ehu.eus/id/entity/ohl"))
        self.assertEquals('Tan solo unas semanas de la adjudicaci n del  em megacontrato  em  para la  a href    events anuncio adjudicacion ave  construcci n del AVE a La Meca  a    a href    persons corinna  Corinna zu Sayn Wittgenstein  a  disuelve sus sociedad  a href    entities apollonia  Apollonia Ventures  a   que hab a constituido en noviembre de 2005 ', self.json2rdf.getCommentFromGraph("http://ehu.eus/id/event/disolucion_de_apollonia"))
        self.assertEquals('La hija mayor de los reyes de Espa a   a href    persons juan carlos  Juan Carlos  a  y  a href    persons sofia de grecia  Sof a  a   figura junto con su padre y sus hermanos  a href    persons felipe vi  el rey Felipe VI  a  y  a href    persons cristina  Cristina de Borb n  a   como beneficiaria de la  a href    entities zagatka  fundaci n Zagatka  a   una entidad dada de alta en  a href    places liechtenstein  Liechtenstein  a  bajo el control de un pariente lejano   a href    persons alvaro de orleans   lvaro de Orleans Borb n  a  ', self.json2rdf.getCommentFromGraph("http://ehu.eus/id/person/elena"))
        self.assertEquals('Exclusivo  tico en el barrio de Knightsbride  que el  a href    persons qabus bin said  sult n de Om n  a  adquiri  por 50 millones de libras  62 7 millones de euros  un r cord del momento  para ponerlo a disposici n del  a href    persons juan carlos  rey Juan Carlos  a   quien  a href    events viaje a oman  hab a visitado el pa s  rabe  a  apenas dos meses antes ', self.json2rdf.getCommentFromGraph("http://ehu.eus/id/place/princes_gate_5"))




    #setTypeLabelComent metodoa aurreko hiru metodoetan frogatzen da

    def test_forPersonsToPeople(self):
        self.assertEquals("people",self.json2rdf.forPersonsToPeople("persons"))
        self.assertEquals("events",self.json2rdf.forPersonsToPeople("events"))
        self.assertEquals("documents", self.json2rdf.forPersonsToPeople("documents"))
        self.assertEquals("places", self.json2rdf.forPersonsToPeople("places"))
        self.assertEquals("entities", self.json2rdf.forPersonsToPeople("entities"))
        self.assertEquals("articles", self.json2rdf.forPersonsToPeople("articles"))

    def test_erlazioaAldatu(self):
        #Kasu nabariak
        self.assertEquals("https://schema.org/participant", self.json2rdf.erlazioaAldatu("takes_part"))
        self.assertEquals("https://schema.org/author", self.json2rdf.erlazioaAldatu("authors"))
        self.assertEquals("https://schema.org/worksFor", self.json2rdf.erlazioaAldatu("works_for"))

        #Schema + kasu orokorrak
        self.assertEquals("https://schema.org/mentions", self.json2rdf.erlazioaAldatu("mentions"))
        self.assertEquals("https://schema.org/parent", self.json2rdf.erlazioaAldatu("parent"))
        self.assertEquals("https://schema.org/owns", self.json2rdf.erlazioaAldatu("owns"))
        self.assertEquals("https://schema.org/spouse", self.json2rdf.erlazioaAldatu("spouse"))
        self.assertEquals("https://schema.org/knows", self.json2rdf.erlazioaAldatu("knows"))

        #Ontologia propioa + kasu orokorrak
        self.assertEquals("http://ehu.eus/transparentrelations#has_bank_account_in", self.json2rdf.erlazioaAldatu("has_bank_account_in"))
        self.assertEquals("http://ehu.eus/transparentrelations#partner", self.json2rdf.erlazioaAldatu("partner"))
        self.assertEquals("http://ehu.eus/transparentrelations#represents", self.json2rdf.erlazioaAldatu("represents"))
        self.assertEquals("http://ehu.eus/transparentrelations#pays", self.json2rdf.erlazioaAldatu("pays"))
        self.assertEquals("http://ehu.eus/transparentrelations#controls", self.json2rdf.erlazioaAldatu("controls"))
        self.assertEquals("http://ehu.eus/transparentrelations#registered_in", self.json2rdf.erlazioaAldatu("registered_in"))
        self.assertEquals("http://ehu.eus/transparentrelations#gives", self.json2rdf.erlazioaAldatu("gives"))
        self.assertEquals("http://ehu.eus/transparentrelations#beneficiary_of", self.json2rdf.erlazioaAldatu("beneficiary_of"))
        self.assertEquals("http://ehu.eus/transparentrelations#related_to", self.json2rdf.erlazioaAldatu("related_to"))
        self.assertEquals("http://ehu.eus/transparentrelations#sibling", self.json2rdf.erlazioaAldatu("sibling"))
        self.assertEquals("http://ehu.eus/transparentrelations#happens_in", self.json2rdf.erlazioaAldatu("happens_in"))
        self.assertEquals("http://ehu.eus/transparentrelations#manages", self.json2rdf.erlazioaAldatu("manages"))


    def test_subjektuaObjektuaTratatu(self):
        #Pertsona
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/person/mariano_rajoy"), self.json2rdf.subjektuaObjektuaTratatu("#/persons/mariano_rajoy"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/person/cristina"), self.json2rdf.subjektuaObjektuaTratatu("#/persons/cristina"))

        #Ekitaldi
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/event/retirada_ducado_cristina"), self.json2rdf.subjektuaObjektuaTratatu("#/events/retirada_ducado_cristina"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/event/disolucion_de_apollonia"),self.json2rdf.subjektuaObjektuaTratatu("#/events/disolucion_de_apollonia"))

        #Entitateak
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/entity/apollonia"),self.json2rdf.subjektuaObjektuaTratatu("#/entities/apollonia"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/entity/sanchez_junco_abogados"),self.json2rdf.subjektuaObjektuaTratatu("#/entities/sanchez_junco_abogados"))

        #Dokumentuak
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/document/aeat_juan_carlos_2018"),self.json2rdf.subjektuaObjektuaTratatu("#/documents/aeat_juan_carlos_2018"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/document/segundo_comunicado_regularizacion_fiscal"),self.json2rdf.subjektuaObjektuaTratatu("#/documents/segundo_comunicado_regularizacion_fiscal"))

        #Places
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/place/georges_favon_29"),self.json2rdf.subjektuaObjektuaTratatu("#/places/georges_favon_29"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/place/belgrave"),self.json2rdf.subjektuaObjektuaTratatu("#/places/belgrave"))

        #Artikuluak
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/article/elespanol_503950285"),self.json2rdf.subjektuaObjektuaTratatu("#/articles/elespanol_503950285"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/article/elespanol_320468523"), self.json2rdf.subjektuaObjektuaTratatu("##/articles/elespanol_320468523"))

        #Sortutako adibide propio batzuk
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/person/jon_ander_asua"),self.json2rdf.subjektuaObjektuaTratatu("#/persons/jon_ander_asua"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/place/gallarta"),self.json2rdf.subjektuaObjektuaTratatu("#/places/gallarta"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/event/ekitaldi"),self.json2rdf.subjektuaObjektuaTratatu("#/events/ekitaldi"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/entity/entitatea"),self.json2rdf.subjektuaObjektuaTratatu("#/entities/entitatea"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/document/dokumentua"),self.json2rdf.subjektuaObjektuaTratatu("#/documents/dokumentua"))
        self.assertEqual(rdflib.term.URIRef("http://ehu.eus/id/article/artikulua"),self.json2rdf.subjektuaObjektuaTratatu("#/articles/artikulua"))

    def test_grafoaEraiki(self):
        pass

    def exekutatuTestak(self):
        self.test_setType()
        self.test_setLabel()
        self.test_setComent()
        self.test_erlazioaAldatu()
        self.test_forPersonsToPeople()
        self.test_subjektuaObjektuaTratatu()

# test_zerbitzariraIgo(self) beste metodoen barnean frogatzen da eskaerak zerbitzariaren kontra egiten direlako
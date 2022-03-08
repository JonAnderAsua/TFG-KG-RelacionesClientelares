import unittest
from graphSource import json2rdf

class TestJson2rdf(unittest.TestCase):

    uri1 = ""
    uri2 = ""
    uri3 = ""
    uri4 = ""

    type1 = ""
    type2 = ""
    type3 = ""
    type4 = ""

    label1 = ""
    label2 = ""
    label3 = ""
    label4 = ""

    comment1 = ""
    comment2 = ""
    comment3 = ""
    comment4 = ""

    def test_setType(self):
        json2rdf.setType()

    def test_setLabel(self):
        json2rdf.setLabel()

    def test_setComment(self):
        json2rdf.setComent()

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









if __name__ == '__main__':
    unittest.main()
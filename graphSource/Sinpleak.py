class Entitatea:
    def __init__(self, id, izena, desk):
        self.id = id
        self.izena = izena
        self.deskribapena = desk

    def getId(self):
        return self.id

    def getIzena(self):
        return self.izena

    def getDesk(self):
        return self.deskribapena

class Ekitaldi:
    def __init__(self, id, izena, data, desk):
        self.id = id
        self.izena = izena
        self.data = data
        self.deskribapena = desk

    def getId(self):
        return self.id

    def getIzena(self):
        return self.izena

    def getData(self):
        return self.data

    def getDesk(self):
        return self.deskribapena

class Aldizkari:
    def __init__(self, id, izena, web):
        self.id = id
        self.izena = izena
        self.webgune = web

    def getId(self):
        return self.id

    def getIzena(self):
        return self.izena

    def getWeb(self):
        return self.webgune

class Lekua:
    def __init__(self,id, izena, hiria, herri, link):
        self.id = id
        self.izena = izena
        self.hiria = hiria
        self.herrialdea = herri
        self.link = link

    def getId(self):
        return self.id

    def getIzena(self):
        return self.izena

    def getHiria(self):
        return self.hiria

    def getHerrialdea(self):
        return self.herrialdea

    def getLink(self):
        return self.link

class Pertsona:
    def __init__(self, id, izena, nazi, gene):
        self.id = id
        self.izena = izena
        self.nazionalitatea = nazi
        self.generoa = gene

    def getId(self):
        return self.id

    def getIzena(self):
        return self.izena

    def getNazioa(self):
        return self.nazionalitatea

    def getGeneroa(self):
        return self.generoa

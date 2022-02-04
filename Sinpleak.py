class Entitatea:
    def __init__(self, izena, desk):
        self.izena = izena
        self.deskribapena = desk

    def getIzena(self):
        return self.izena

    def getDesk(self):
        return self.deskribapena

class Ekitaldi:
    def __init__(self, izena, data, desk):
        self.izena = izena
        self.data = data
        self.deskribapena = desk

    def getIzena(self):
        return self.izena

    def getData(self):
        return self.data

    def getDesk(self):
        return self.deskribapena

class Aldizkari:
    def __init__(self, izena, web):
        self.izena = izena
        self.webgune = web

    def getIzena(self):
        return self.izena

    def getWeb(self):
        return self.webgune

class Lekua:
    def __init__(self, izena, hiria, herri, link):
        self.izena = izena
        self.hiria = hiria
        self.herrialdea = herri
        self.link = link

    def getIzena(self):
        return self.izena

    def getHiria(self):
        return self.hiria

    def getHerrialdea(self):
        return self.herrialdea

    def getLink(self):
        return self.link

class Pertsona:
    def __init__(self, izena, nazi, gene):
        self.izena = izena
        self.nazionalitatea = nazi
        self.generoa = gene

    def getIzena(self):
        return self.izena

    def getNazioa(self):
        return self.nazionalitatea

    def getGeneroa(self):
        return self.generoa

class Artikulua:
    def __init__(self, id, url, iturria, titulua, data, erlazioak):
        self.id = id
        self.url = url
        self.iturria = iturria
        self.titulua = titulua
        self.data = data
        self.erlazioak = erlazioak

    def getId(self):
        return self.id

    def getTitulua(self):
        return self.titulua

    def getErlazioak(self):
        return self.erlazioak


class Dokumentua:
    def __init__(self, id, tit, desc, data, erlaz):
        self.id = id
        self.titulua = tit
        self.deskribapena = desc
        self.data = data
        self.erlazioak = erlaz
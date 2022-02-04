class Artikulua:
    def __init__(self, url, iturria, titulua, data, erlazioak):
        self.url = url
        self.iturria = iturria
        self.titulua = titulua
        self.data = data
        self.erlazioak = erlazioak


class Dokumentua:
    def __init__(self, id, tit, desc, data, erlaz):
        self.id = id
        self.titulua = tit
        self.deskribapena = desc
        self.data = data
        self.erlazioak = erlaz
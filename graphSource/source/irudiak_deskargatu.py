from google_images_download import google_images_download
import unidecode
import os

class IrudiakDeskargatu:
    def __init__(self, izena,pathIrudiak):
        self.response = google_images_download.googleimagesdownload()
        self.izena = izena
        self.arguments = {"keywords":unidecode.unidecode(izena),"limit":1,"print_urls":True}
        self.paths = self.response.download(self.arguments)
        self.irudiIZena = izena.replace(' ','_')

    def irudiaDeskargatu(self):
        os.system('mv downloads/"' + self.izena + '"/* ' + self.paths + '/' + self.izena+'.jpg')
        print(self.izena + '(r)en irudia deskargatu da')
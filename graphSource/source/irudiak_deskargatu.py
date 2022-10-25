import sys

from google_images_download import google_images_download
import unidecode
import os


class IrudiakDeskargatu:
    def __init__(self, izena):

        self.izena = izena
        self.paths = self.response.download(self.arguments)

        self.irudiIzena = self.izena.replace(' ','_')

    def irudiaDeskargatu(self):
        self.response = google_images_download.googleimagesdownload()
        self.arguments = {"keywords": unidecode.unidecode(self.izena), "limit": 1, "print_urls":True}
        try:
            self.paths = self.response.download(self.arguments)

            print('mv downloads/"' + self.izena + '"/* ' + self.paths + '/' + self.izena+'.jpg')
            os.system('mv downloads/"' + self.izena + '"/* ' + self.paths + '/' + self.izena+'.jpg')
            print(self.izena + '(r)en irudia deskargatu da')

        except:
            os.system("googleimagesdownload --k '" + self.izena +"' -l 1")
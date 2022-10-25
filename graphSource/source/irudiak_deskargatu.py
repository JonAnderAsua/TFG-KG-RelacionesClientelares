import sys

from google_images_download import google_images_download
import unidecode
import os


class IrudiakDeskargatu:
    def __init__(self, izena):

        self.izena = izena
        self.irudiIzena = self.izena.replace(' ','_')
        self.response = google_images_download.googleimagesdownload()
        self.arguments = {"keywords": unidecode.unidecode(self.izena), "limit": 1, "print_urls":True}

    def irudiaDeskargatu(self):
        try:
            self.paths = self.response.download(self.arguments)
            os.system('mv downloads/"' + self.izena + '"/* grafoavis/public/images/' + self.irudiIzena+'.jpg')
            print(self.izena + '(r)en irudia deskargatu da')

        except:
            # os.system("googleimagesdownload --k '" + self.izena +"' -l 1")
            print(self.izena + "-ren irudia ezin izan da deskargatu")
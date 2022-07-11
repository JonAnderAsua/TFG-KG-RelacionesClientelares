from google_images_download import google_images_download
import unidecode
import sys
import os

response = google_images_download.googleimagesdownload()

izena = sys.argv[1]
arguments = {"keywords":unidecode.unidecode(izena),"limit":1,"print_urls":True}
paths = response.download(arguments)

if sys.argv[2]:
    irudiIzena = sys.argv[2]
else:
    irudiIzena = izena.replace(' ','_')

os.system('mv downloads/"' + izena + '"/* grafoavis/public/images/'+irudiIzena+'.jpg')
print(irudiIzena + '(r)en irudia deskargatu da')
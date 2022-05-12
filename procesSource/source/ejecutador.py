import os
import sys
import yaml

pathLag = os.getcwd().split("/")[1:len(os.getcwd().split("/"))-2]
path = ""
for i in pathLag:
    path += "/"+i

sys.path.append(path)
sys.path.append(path+"/source")

import procesSource
if __name__ == "__main__":
    proiektu_izena = ""
    if len(sys.argv) > 1:
        proiektu_izena = sys.argv[1]
    else:
        proiektu_izena = input("Sartu proiektuaren izena \n")

    try:

        procesador = procesSource.source.Procesador(proiektu_izena)
        interpretatzaile = ""

        if (".py" in procesador.run):
            interpretatzaile = "python3"
        else:
            print("Perdon seño, no hemos hecho más tarea \n")

        #Programa exekutatu
        try:
            os.system(interpretatzaile + " " + procesador.run + " " + proiektu_izena)
        except:
            print("Sartutako programa ezin da exekutatu")
    except:
        print("Sartu duzun proiektua ez da existitzen, sartu hurrengo zerrendan agertzen den proiektuaren izen bat mesedez:")

        # Yaml fitxategia kargatu
        fichero = open("/home/jonander/PycharmProjects/TFG-KG-RelacionesClientelares/doc/config.yml")
        fitxategia = yaml.load(fichero, Loader=yaml.FullLoader)

        for proiektuIzena in fitxategia:
            print(proiektuIzena)

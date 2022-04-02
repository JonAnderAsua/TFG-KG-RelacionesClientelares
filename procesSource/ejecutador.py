import os,sys,yaml,Procesador

if __name__ == "__main__":
    proiektu_izena = ""
    if len(sys.argv) > 1:
        proiektua_izena = sys.argv[1]
    else:
        proiektu_izena = input("Sartu proiektuaren izena \n")

    try:

        procesador = Procesador.Procesador(proiektu_izena)
        interpretatzaile = ""

        if (".py" in procesador.run):
            interpretatzaile = "python3"
        else:
            print("Perdon seño, no hemos hecho más tarea \n")

        #Programa exekutatu
        os.system(interpretatzaile + " " + procesador.run + " " + proiektu_izena)

    except:
        print("Sartu duzun proiektua ez da existitzen, sartu hurrengo zerrendan agertzen den proiektuaren izen bat mesedez:")

        # Yaml fitxategia kargatu
        fichero = open("../doc/config.yml")
        fitxategia = yaml.load(fichero, Loader=yaml.FullLoader)

        for proiektuIzena in fitxategia:
            print(proiektuIzena)


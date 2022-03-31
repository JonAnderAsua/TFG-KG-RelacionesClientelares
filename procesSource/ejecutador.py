import os
import Procesador

if __name__ == "__main__":
    proiektu_izena = input("Sartu proiektuaren izena \n")

    procesador = Procesador.Procesador(proiektu_izena)

    interpretatzaile = ""

    if (".py" in procesador.run):
        interpretatzaile = "python3"
    else:
        print("Perdon seño, no hemos hecho más tarea \n")


    #Programa exekutatu
    print(interpretatzaile + " " + procesador.run)
    os.system(interpretatzaile + " " + procesador.run)


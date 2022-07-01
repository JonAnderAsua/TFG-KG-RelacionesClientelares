import pandas as pd
from csv import reader

# erlazioak = pd.read_csv('/home/jonander/PycharmProjects/TFG-KG-RelacionesClientelares/data/leaks/relationships.csv')

# open file
with open("/home/jonander/PycharmProjects/TFG-KG-RelacionesClientelares/data/leaks/relationships.csv", "r") as my_file:
    file_reader = reader(my_file)
    lista = []
    for i in file_reader:
        # print the rows
        if i[3] not in lista:
            print('Entra')
            lista.append(i[3])
    print(lista)


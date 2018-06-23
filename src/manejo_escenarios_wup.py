from pandas import pandas
import os

def main():

    print ('iniciando...')
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../data/FormatoDeAlmacenamiento.csv')
    
    print ('leyendo data...')
    dataRead = pandas.read_csv(filename, sep=';', header=None, na_values=" NaN")

    step1=pandas.DataFrame(dataRead)
    print ('agrupando data')
    dataGroup=step1.groupby(['hora']).sum()

    print (dataGroup)

if __name__ == '__main__':
    main()
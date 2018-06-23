from pandas \
import pandas as pd
import os

def main():
    print ('carga de archivo')
    print ('................')
    print('\n')
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../data/FormatoDeAlmacenamiento1.csv')
    df = pd.read_csv(filename, sep=';', header=None, na_values=" NaN")

    #print (df)
    #imprimo la informacion del archivo que cargo
    print (df.info())
    print ('\n'*2)
    print(df.describe())
    #limpio datos
    #
    print ('\n'*2)
    #nuevo=pd.DataFrame(df)
    #nuevo=nuevo.replace("","NO")
    #print (nuevo)
    columna =df[df[1]!='NaN']
    #print(columna)
if __name__ == '__main__':
    main()
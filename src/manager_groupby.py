from pandas \
import pandas as pd
import datetime 
import os
import matplotlib.pyplot as plt
import seaborn as sns




def main():
    print ('carga de archivo')
    print ('................')
    print('\n')
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../data/FormatoDeAlmacenamiento1.csv')
    df = pd.read_csv(filename, sep=';', header=None, na_values=" NaN")

    #print (df)
    hora=df[0].str.extract('((?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d)')
    #print (hora)
    #remplazo los na por cero
    df2=pd.DataFrame()
    df2=df2.fillna(0)
    df2[0]=df[0].str.extract('((?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d)')
    df2[1]=df[1]
    #print(df2)
    print("se agrupa por minutos")
    df2[0]=pd.DatetimeIndex(df2[0])
    df2.set_index(keys=0,inplace=True)
    ini=datetime.time(00,18,0)
    fin=datetime.time(23,59,0)
    df3=df2[[1]].between_time(ini,fin)
    df3=df3.groupby([1])[[1]].count()
    print(df3)
    
    #nuevo=pd.DataFrame(df)
    #nuevo=nuevo.replace("","NO")
   # print (nuevo)
  #  columna =df[df[1]!='NaN']
    #print(columna)
if __name__ == '__main__':
    main()
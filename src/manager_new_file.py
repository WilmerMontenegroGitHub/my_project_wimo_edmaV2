from pandas \
import pandas as pd
import datetime as dt
import dateutil
import os
import matplotlib.pyplot as plt
import seaborn as sns




def main():
    print ('carga de archivo')
    print ('................')
    print('\n')
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../data/FormatoDeAlmacenamiento1.csv')
    df1 = pd.read_csv(filename, sep=';', header=None, na_values=" NaN")
    df=pd.DataFrame(df1)
    
   # print(df)
    total=df.groupby(df[0]).count()
    
   # total.reset_index().to_csv('../data/grupo.csv',header=True,index=False)
    

    print (total)
    print("*****************************************************")
    #df[0]= df[0].apply(dateutil.parser.parse, dayfirst = True)
    #df2[0]=df[0].apply(dateutil.parser.parse,dayfirst =True)
    #df1=df.groupby([0,1,2]).count()
    #print(df1)
   
   #df2 = df.groupby([ periodo, df.index.time]).sum()
   #print(df2)
    
    #nuevo=pd.DataFrame(df)
    #nuevo=nuevo.replace("","NO")
   # print (nuevo)
  #  columna =df[df[1]!='NaN']
    #print(columna)
if __name__ == '__main__':
    main()
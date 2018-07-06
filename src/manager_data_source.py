# importando librerias
import pandas as pd
import numpy as np
import csv

# abriendo archivo .csv con la data recopilada
datos=pd.read_csv('../data/Ambiente_general.csv',sep=';',header=0)
# pasando la informacion del archivo .csv a un DataFrame
df=pd.DataFrame(datos, columns=['fecha_hora','app_1'])
# convirtiendo el campo fecha_hora a datetime para poder agrupar
df['fecha_hora'] =  pd.to_datetime(df['fecha_hora'])
# seteando como indice al campo fecha_hora
df = df.set_index(['fecha_hora'])
# agrupando en el dataframe df2 por una hora = 3600 segundos (3600S) y promediando 
df2 = df.resample('3600S').mean()
########### inicio dataframe to .csv
# 1.- remplazamos NaN por - en el dataframe df2 _nuevo
df2_nuevo = df2.fillna(value='-')
#my_df = pd.DataFrame(df2_nuevo) 
df2_nuevo.to_csv('../data/DataOrigenAgrupadaPorHora_y_Promediado.csv', index=True, header=True,sep=';',decimal='.')
########### fin dataframe to .csv
# imprimo en pantalla el resultado de mi dataframe agrupado por horas
print (df2_nuevo) 
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 11:08:30 2018

@author: wmontenegro
"""

import pandas as pd

print("Ingrese el numero de columnas que va a listar")
columnas = input()
miEntradaColumnas = int(columnas)

print("Ingrese el tiempo en segundos que desea agrupar")
tiempo = input()

print("Ingrese la columna a agrupar")
columnaAgrupar = input()

lista_recorrer = []
datos=pd.read_csv('../data/FormatoDeAlmacenamiento_enviadoEM.csv',sep=';',header=0)
df=pd.DataFrame(datos, columns=['fecha_hora', columnaAgrupar])
df=df.dropna()
df['fecha_hora'] =  pd.to_datetime(df['fecha_hora'])
df = df.set_index(['fecha_hora'])
df2 = df.resample(tiempo+'S').sum()
df2 = df2.dropna()

df2.to_csv('datosAgrupados.csv', sep=';')
datos2 = pd.read_csv('datosAgrupados.csv',sep=';',header=0)

df3 = pd.DataFrame(datos2, columns=[columnaAgrupar])
df3[columnaAgrupar] = df3[columnaAgrupar].astype(float)

df31 = pd.DataFrame(datos2, columns=['fecha_hora'])

aux = 0
valor = miEntradaColumnas

while (aux < int(df3.count())):
    while (valor >= 0):
        if ((aux - valor)< 0):
            #print ('NaN')
            lista_recorrer.append('NaN')
            valor = valor - 1
        else:
            #print (df3['calidad_aire'][aux-valor])
            lista_recorrer.append(df3[columnaAgrupar][aux-valor])
            valor = valor - 1
    valor = miEntradaColumnas
    aux = aux + 1

    
lista_total =[]

total = len (lista_recorrer)

d= {'Fecha': df31['fecha_hora']}
df5 = pd.DataFrame(d)

matriz = []
s = 0
for i in range(int(df5.count())):
    matriz.append([])
    for j in range(valor+1):          
        matriz[i].append(float(lista_recorrer[s]))
        #print (matriz[i])
        s = s + 1


dfinal = pd.DataFrame(matriz)


frames = [df5, dfinal, dfinal]
print ('imprimiendo frames...')
print (frames)
resultado = pd.concat(frames, axis=1)

resultado = resultado.dropna()
print ('imprimiendo resultado...')
print (resultado)
resultado.to_csv('escenario.csv', sep=';')
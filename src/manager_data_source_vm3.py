import pandas as pd
import numpy as np

# genera_archivo_app1():
print("Ingrese el numero en minutos para agrupar su data:")
tmp_val_in_min = input()
print("Ingrese el numero de columnas para trasponer (minutos ingresados atras):")
num_cols_transp = input()
############################################################################
numero_de_columnas = int(num_cols_transp)
lista_recorrer = []
val_in_min = tmp_val_in_min
val_in_seg = str(int(val_in_min) * 60)
val_in_seg = val_in_seg + 'S'
datos=pd.read_csv('../data/FormatoDeAlmacenamiento_enviadoEM.csv',sep=';',header=0)
df=pd.DataFrame(datos, columns=['fecha_hora','app_1'])
df=df.dropna()
df['fecha_hora'] =  pd.to_datetime(df['fecha_hora'])
df = df.set_index(['fecha_hora'])
df2 = df.resample(val_in_seg).sum()
df2_nuevo=df2.dropna()
df2_nuevo.to_csv('../data/DataOrigenAgrupada_y_Sumando_APP01_Activo'+val_in_min+'m.csv', index=True, header=True,sep=';',decimal='.')
print ('Generado archivo DataOrigenAgrupada_y_Sumando_APP01_Activo'+val_in_min+'m.csv') 

df_tmp = pd.read_csv('../data/DataOrigenAgrupada_y_Sumando_APP01_Activo'+val_in_min+'m.csv',sep=';',header=0)
df_tmp2 = pd.DataFrame(df_tmp, columns=['app_1'])
df_tmp2['app_1'] = df_tmp2['app_1'].astype(float)
df_tmp_aux = pd.DataFrame(df_tmp, columns=['fecha_hora'])
cont = 0
idx = numero_de_columnas
idx = int(idx)
while (cont < int(df_tmp2.count())):
    while (idx >= 0):
        if ((cont - idx)< 0):
            lista_recorrer.append('NaN')
            idx = idx - 1
        else:
            lista_recorrer.append(df_tmp2['app_1'][cont-idx])
            idx = idx - 1
    idx = numero_de_columnas
    cont = cont + 1
lista_total =[]
total = len (lista_recorrer)
d= {'Fecha': df_tmp_aux['fecha_hora']}
df5 = pd.DataFrame(d)
matriz = []
s = 0
for i in range(int(df5.count())):
    matriz.append([])
    for j in range(idx+1):          
        matriz[i].append(float(lista_recorrer[s]))
        s = s + 1
dfinal = pd.DataFrame(matriz)
frames = [df5, dfinal]
escenario1_var_app1 = pd.concat(frames, axis=1)
escenario1_var_app1 = escenario1_var_app1.dropna()
#print (escenario1_var_app1)
escenario1_var_app1.to_csv('../data/DataOrigenAgrupada__Escenario_1__APP01_Activo'+val_in_min+'m.csv', index=True, header=True,sep=';',decimal='.')
print ('Generado archivo DataOrigenAgrupada__Escenario_1__APP01_Activo'+val_in_min+'m.csv') 

#############################################################

numero_de_columnas = int(num_cols_transp)
lista_recorrer = []
val_in_min = tmp_val_in_min
val_in_seg = str(int(val_in_min) * 60)
val_in_seg = val_in_seg + 'S'
datos=pd.read_csv('../data/FormatoDeAlmacenamiento_enviadoEM.csv',sep=';',header=0)
df=pd.DataFrame(datos, columns=['fecha_hora','app_2'])
df=df.dropna()
df['fecha_hora'] =  pd.to_datetime(df['fecha_hora'])
df = df.set_index(['fecha_hora'])
df2 = df.resample(val_in_seg).sum()
df2_nuevo=df2.dropna()
df2_nuevo.to_csv('../data/DataOrigenAgrupada_y_Sumando_APP02_Activo'+val_in_min+'m.csv', index=True, header=True,sep=';',decimal='.')
print ('Generado archivo DataOrigenAgrupada_y_Sumando_APP02_Activo'+val_in_min+'m.csv') 

df_tmp = pd.read_csv('../data/DataOrigenAgrupada_y_Sumando_APP02_Activo'+val_in_min+'m.csv',sep=';',header=0)
df_tmp2 = pd.DataFrame(df_tmp, columns=['app_2'])
df_tmp2['app_2'] = df_tmp2['app_2'].astype(float)
df_tmp_aux = pd.DataFrame(df_tmp, columns=['fecha_hora'])
cont = 0
idx = numero_de_columnas
idx = int(idx)
while (cont < int(df_tmp2.count())):
    while (idx >= 0):
        if ((cont - idx)< 0):
            lista_recorrer.append('NaN')
            idx = idx - 1
        else:
            lista_recorrer.append(df_tmp2['app_2'][cont-idx])
            idx = idx - 1
    idx = numero_de_columnas
    cont = cont + 1
lista_total =[]
total = len (lista_recorrer)
d= {'Fecha': df_tmp_aux['fecha_hora']}
df5 = pd.DataFrame(d)
matriz = []
s = 0
for i in range(int(df5.count())):
    matriz.append([])
    for j in range(idx+1):          
        matriz[i].append(float(lista_recorrer[s]))
        s = s + 1
dfinal_app2 = pd.DataFrame(matriz)
frames = [df5, dfinal_app2]
escenario1_var_app2 = pd.concat(frames, axis=1)
escenario1_var_app2 = escenario1_var_app2.dropna()
#print (escenario1_var_app1)
escenario1_var_app2.to_csv('../data/DataOrigenAgrupada__Escenario_1__APP02_Activo'+val_in_min+'m.csv', index=True, header=True,sep=';',decimal='.')
print ('Generado archivo DataOrigenAgrupada__Escenario_1__APP02_Activo'+val_in_min+'m.csv') 

#############################################

frames = [df5, dfinal, dfinal_app2]

escenario1_var_app1y2 = pd.concat(frames, axis=1)
escenario1_var_app1y2 = escenario1_var_app1y2.dropna()

escenario1_var_app1y2.to_csv('../data/DataOrigenAgrupada__Escenario_1__APP01y2_Activo'+val_in_min+'m.csv', index=True, header=True,sep=';',decimal='.')
print ('Generado archivo DataOrigenAgrupada__Escenario_1__APP01y2_Activo'+val_in_min+'m.csv') 

# INACTIVOS

############################################################################
numero_de_columnas = int(num_cols_transp)
lista_recorrer = []
val_in_min = tmp_val_in_min
val_in_seg = str(int(val_in_min) * 60)
val_in_seg = val_in_seg + 'S'
datos=pd.read_csv('../data/FormatoDeAlmacenamiento_enviadoEM.csv',sep=';',header=0)
#
#datos = np.array(["1" if e == 1 else "x" for e in df])
#datos = datos_aaux.replace({'app_1': {1: "1", 0: "--"}},  inplace = True)
#datos = datos['app_1'] = np.where(datos['app_1'], '1', '--')
#
df=pd.DataFrame(datos, columns=['fecha_hora','app_1'])
df=df.dropna()
df['fecha_hora'] =  pd.to_datetime(df['fecha_hora'])
df = df.set_index(['fecha_hora'])
df2 = df.resample(val_in_seg).count()-df.resample(val_in_seg).sum()
df2_nuevo=df2.dropna()
df2_nuevo.to_csv('../data/DataOrigenAgrupada_y_Sumando_APP01_inActivo'+val_in_min+'m.csv', index=True, header=True,sep=';',decimal='.')
print ('Generado archivo DataOrigenAgrupada_y_Sumando_APP01_inActivo'+val_in_min+'m.csv') 

df_tmp = pd.read_csv('../data/DataOrigenAgrupada_y_Sumando_APP01_inActivo'+val_in_min+'m.csv',sep=';',header=0)
df_tmp2 = pd.DataFrame(df_tmp, columns=['app_1'])
df_tmp2['app_1'] = df_tmp2['app_1'].astype(float)
df_tmp_aux = pd.DataFrame(df_tmp, columns=['fecha_hora'])
cont = 0
idx = numero_de_columnas
idx = int(idx)
while (cont < int(df_tmp2.count())):
    while (idx >= 0):
        if ((cont - idx)< 0):
            lista_recorrer.append('NaN')
            idx = idx - 1
        else:
            lista_recorrer.append(df_tmp2['app_1'][cont-idx])
            idx = idx - 1
    idx = numero_de_columnas
    cont = cont + 1
lista_total =[]
total = len (lista_recorrer)
d= {'Fecha': df_tmp_aux['fecha_hora']}
df5 = pd.DataFrame(d)
matriz = []
s = 0
for i in range(int(df5.count())):
    matriz.append([])
    for j in range(idx+1):          
        matriz[i].append(float(lista_recorrer[s]))
        s = s + 1
dfinal = pd.DataFrame(matriz)
frames = [df5, dfinal]
escenario1_var_app1 = pd.concat(frames, axis=1)
escenario1_var_app1 = escenario1_var_app1.dropna()
#print (escenario1_var_app1)
escenario1_var_app1.to_csv('../data/DataOrigenAgrupada__Escenario_1__APP01_inActivo'+val_in_min+'m.csv', index=True, header=True,sep=';',decimal='.')
print ('Generado archivo DataOrigenAgrupada__Escenario_1__APP01_inActivo'+val_in_min+'m.csv') 


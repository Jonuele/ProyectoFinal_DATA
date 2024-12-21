
import pandas as pd
import numpy as np
import pandas_ta as ta

import missingno as msno

import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://raw.githubusercontent.com/Jonuele/ProyectoFinal_DATA/de4be10172ac5c1863247fa47d7ccdc76952714d/Historico%20Tesla.xlsx'

data = pd.read_excel(url, engine='openpyxl')
#print(data.head())
#Imprimimos las columnas
#print(data.columns)
#Observamos la composicion del dataset
#print(data.info())

#Convertimos las fecha en indice
data['Fecha Cotización'] = pd.to_datetime(data['Fecha Cotización'])
data.set_index('Fecha Cotización', inplace=True)
#Ordenamos los datos por fecha de más antiguo a más reciente
data.sort_index(ascending=True, inplace=True)
#Preparamos nuevas columnas / Medias Moviles Exponenciales de CORTO PLAZO.
data['EMA_5'] = ta.ema(data['Cierre'], length=5)
data['EMA_10'] = ta.ema(data['Cierre'], length=10)
data['EMA_20'] = ta.ema(data['Cierre'], length=20)
#Preparamos nuevas columnas / Medias Moviles Exponenciales de LARGO PLAZO.
data['EMA_50'] = ta.ema(data['Cierre'], length=50)
data['EMA_100'] = ta.ema(data['Cierre'], length=100)
data['EMA_200'] = ta.ema(data['Cierre'], length=200)
#Preparacion de nuevas columnas / Indice de Fuerza Relativa
data['RSI'] = ta.rsi(data['Cierre'], length=14)
#Verificamos la posibilidad y existencia de nulos
#print(data.isnull().sum())
#Reemplazamos nulos por ceros
data.fillna(0, inplace=True)
#Importamos MSNO y verificamos el impacto de los DATOS AUSENTES

msno.matrix(data)
plt.title('Matriz de Datos Faltantes')
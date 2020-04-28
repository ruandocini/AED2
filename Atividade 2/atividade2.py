import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

#importando o csv com as informações necessárias

raw = pd.read_csv('data.csv')

#usando o loop para explorar as colunas
for x in raw.columns:
    print(x)

#separando somente as colunas a serem usadas, para maior eficiência
nedded_data = pd.DataFrame(data={'id_pessoa':raw['ID_PESS'],'coordenada_x':raw['CO_DOM_X'],'coordenada_y':raw['CO_DOM_Y']})

#criando uma coluna de localização através da coordenada x e y
nedded_data['loc'] = nedded_data['coordenada_x'].apply(str) + ',' + nedded_data['coordenada_y'].apply(str)

print(nedded_data)
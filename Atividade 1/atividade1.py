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

#agrupando o dataframe por localizações iguais, para descobrir quantas pessoas frequentam aquele local
pessoas_por_espaço = nedded_data.groupby(['loc']).count().sort_values(by=['id_pessoa'],ascending=False)
pessoas_por_espaço = pessoas_por_espaço.rename({'id_pessoa':'quantidade_de_pessoas',
                                                'coordenada_x':'quantidade_de_pessoas1',
                                                'coordenada_y':'quantidade_de_pessoas2'},axis=1)
                                                
#agrupando os locais pela quantidade de pessoas que frequentam aquele local
pessoas_por_espaço = pessoas_por_espaço.groupby(['quantidade_de_pessoas1']).count()
pessoas_por_espaço = pd.DataFrame(data={'quantidade_de_lugares':pessoas_por_espaço.index,
                                        'quantidade_de_pessoas':pessoas_por_espaço['quantidade_de_pessoas']})
pessoas_por_espaço = pessoas_por_espaço.reset_index(drop=True,inplace=False)
pessoas_por_espaço = pessoas_por_espaço.sort_values(by=['quantidade_de_lugares'],ascending=True)

#gerando um grafico de barras que mostra a relação de lugares foram visitadas por quantas pessoas 
img = sns.barplot(x=pessoas_por_espaço['quantidade_de_lugares'],y=pessoas_por_espaço['quantidade_de_pessoas'],color='b')
img = img.set_xticklabels(labels=pessoas_por_espaço['quantidade_de_lugares'],rotation=90)
plt.show()
print(pessoas_por_espaço)
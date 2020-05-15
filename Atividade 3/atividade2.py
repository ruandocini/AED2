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
locais_domicilio = pd.DataFrame(data={'id_pessoa':raw['ID_PESS'],'coordenada_x':raw['CO_DOM_X'],'coordenada_y':raw['CO_DOM_Y']})
locais_trabalho1 = pd.DataFrame(data={'id_pessoa':raw['ID_PESS'],'coordenada_x':raw['CO_TR1_X'],'coordenada_y':raw['CO_TR1_Y']})
locais_trabalho2 = pd.DataFrame(data={'id_pessoa':raw['ID_PESS'],'coordenada_x':raw['CO_TR2_X'],'coordenada_y':raw['CO_TR2_Y']})
locais_origem = pd.DataFrame(data={'id_pessoa':raw['ID_PESS'],'coordenada_x':raw['CO_O_X'],'coordenada_y':raw['CO_O_Y']})
locais_destino = pd.DataFrame(data={'id_pessoa':raw['ID_PESS'],'coordenada_x':raw['CO_D_X'],'coordenada_y':raw['CO_D_Y']})
locais_transferencia1 = pd.DataFrame(data={'id_pessoa':raw['ID_PESS'],'coordenada_x':raw['CO_T1_X'],'coordenada_y':raw['CO_T1_Y']})
locais_transferencia2 = pd.DataFrame(data={'id_pessoa':raw['ID_PESS'],'coordenada_x':raw['CO_T2_X'],'coordenada_y':raw['CO_T2_Y']})
locais_transferencia3 = pd.DataFrame(data={'id_pessoa':raw['ID_PESS'],'coordenada_x':raw['CO_T3_X'],'coordenada_y':raw['CO_T3_Y']})
locais_escola = pd.DataFrame(data={'id_pessoa':raw['ID_PESS'],'coordenada_x':raw['CO_ESC_X'],'coordenada_y':raw['CO_ESC_Y']})

#criando uma coluna de localização através da coordenada x e y
nedded_data = locais_origem.append(locais_destino)
nedded_data['loc'] = nedded_data['coordenada_x'].apply(str) + ',' + nedded_data['coordenada_y'].apply(str)

print(nedded_data)

#gerando o dataframe do grafo, e colocando quais colunas serão usadas 
pessoas = pd.unique(nedded_data['id_pessoa'])
grafo = pd.DataFrame(columns={'pessoa','contatos','grau'})


#Esse loop gera o grafo e calcula o grau de cada nó, para cada nó presente no array de pessoas 
#Criando um grafo que guarda como vetor os contatos que o nó tem, usando a representação em vetor dos grafos
for pessoa in pessoas:
    local = pd.unique(nedded_data[nedded_data['id_pessoa'] == pessoa]['loc'])[0]

    contatos = pd.unique(nedded_data[nedded_data['loc'] == local]['id_pessoa'])
    linha = pd.DataFrame(data={'pessoa':int(pessoa),'contatos':[contatos],'grau':len(contatos)})
    grafo = grafo.append(linha)


#Nesse momento realizo o agrupamento de nós de mesmo grau, contando quantos nós possuem o mesmo grau
vert_grau = grafo.groupby(by='grau').count()
vert_grau = vert_grau.drop(index=[25100],columns=['contatos'])

#realizo a renomeação da coluna para melhor compreensão do plot
vert_grau = vert_grau.rename(columns={"pessoa":"nós"})
print(vert_grau)

img = sns.barplot(x=vert_grau.index,y=vert_grau['nós'])
plt.show()
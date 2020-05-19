import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

def profundidade(grafo,vertice,contador,visitado):

    visitado = visitado.append(pd.Series(vertice))

    for vizinho in grafo[grafo.index == vertice]['contatos']:
        for each in vizinho:
            if each not in visitado:
                profundidade(grafo,each,contador,visitado)
                contador = contador + 1

    return contador
#importando o csv com as informações necessárias

raw = pd.read_csv('grafo.csv')
raw = raw.drop(columns=['Unnamed: 0'])
grafo = raw
grafo.index = raw['pessoas']
grafo = grafo.drop(columns=['grau','pessoas'])

grafo['contatos'] = raw['contatos']
grafo['contatos'] = grafo['contatos'].str.replace('[','')
grafo['contatos'] = grafo['contatos'].str.replace(']','')
grafo['contatos'] = grafo['contatos'].str.split(' ')

print(grafo)

resultados = pd.Series(['0'])
for vertice in grafo.index:

    visitado = pd.Series(['0'])
    contador = 0
    contador = profundidade(grafo,vertice,contador,visitado)
    resultados = resultados.append(pd.Series(contador))

resultados = pd.read_csv("result.csv")
Pessoa_por_profundidade = resultados.groupby("Profundidade").count()

Pessoa_por_profundidade.to_csv("Pessoas_por_profundidade.csv")



# -*- coding: utf-8 -*-
"""filmes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gLVEx2V7iqifEBUHxWYGnJ6ITaZku6zB
"""

!pip install seaborn==0.9.0

import pandas as pd

uri_filmes = 'https://raw.githubusercontent.com/oyurimatheus/clusterirng/master/movies/movies.csv'

filmes = pd.read_csv(uri_filmes)

filmes.columns = ['filme_id', 'titulo', 'generos']

filmes.head()

generos = filmes.generos.str.get_dummies()
dados_dos_filmes = pd.concat([filmes, generos], axis=1)
dados_dos_filmes.head()

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
generos_escalados = scaler.fit_transform(generos)

generos_escalados

from sklearn.cluster import KMeans

modelo = KMeans(n_clusters=3)

modelo.fit(generos_escalados)

print(f'Grupos {modelo.labels_}')

print(generos.columns)
print(modelo.cluster_centers_)

grupos = pd.DataFrame(modelo.cluster_centers_,
            columns=generos.columns)

grupos

grupos.transpose().plot.bar(subplots=True,
               figsize=(25, 25),
               sharex=False)

grupo = 0

filtro = modelo.labels_ == grupo

dados_dos_filmes[filtro].sample(10)

from sklearn.manifold import TSNE

tsne = TSNE()

visualizacao = tsne.fit_transform(generos_escalados)
visualizacao

import seaborn as sns

sns.set(rc={'figure.figsize': (13, 13)})



sns.scatterplot(x=visualizacao[:, 0],
               y=visualizacao[:, 1],
               hue=modelo.labels_,
               palette=sns.color_palette('Set1', 3))

modelo = KMeans(n_clusters=20)

modelo.fit(generos_escalados)

grupos = pd.DataFrame(modelo.cluster_centers_,
            columns=generos.columns)

grupos.transpose().plot.bar(subplots=True,
               figsize=(25, 50),
               sharex=False,
               rot=0)

grupo = 2

filtro = modelo.labels_ == grupo

dados_dos_filmes[filtro].sample(10)

def kmeans(numero_de_clusters, generos):
  modelo = KMeans(n_clusters=numero_de_clusters)
  modelo.fit(generos)
  return [numero_de_clusters, modelo.inertia_]

kmeans(20, generos_escalados)

kmeans(3, generos_escalados)

resultado = [kmeans(numero_de_grupos, generos_escalados) for numero_de_grupos in range(1, 41)]
resultado

resultado = pd.DataFrame(resultado, 
            columns=['grupos', 'inertia'])
resultado

resultado.inertia.plot(xticks=resultado.grupos)

modelo = KMeans(n_clusters=17)
modelo.fit(generos_escalados)

grupos = pd.DataFrame(modelo.cluster_centers_,
            columns=generos.columns)

grupos.transpose().plot.bar(subplots=True,
               figsize=(25, 50),
               sharex=False,
               rot=0)

grupo = 16

filtro = modelo.labels_ == grupo

dados_dos_filmes[filtro].sample(10)
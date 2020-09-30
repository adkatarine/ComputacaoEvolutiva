# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 11:01:18 2020

@author: Adlla Katarine
"""

import pandas as pd
import random

# Lendo o dataframe.
df = pd.read_csv('.\\dataset\\breast-cancer.csv')

'''***************************************** PRÉ-PROCESSAMENTO DOS DADOS *****************************************'''

# Renomeando as colunas.
df.rename(columns={'1000025': 'Sample code number', '5': 'Clump Thickness', '1': 'Uniformity of Cell Size',
                   '1.1': 'Uniformity of Cell Shape', '1.2': 'Marginal Adhesion', '2': 'Single Epithelial Cell Size',
                   '1.3': 'Bare Nuclei', '3': 'Bland Chromatin', '1.4': 'Normal Nucleoli',
                   '1.5': 'Mitoses', '2.1': 'Class'}, inplace=True)

# Verificando se existe valores nulos em cada coluna.
df.loc[pd.isnull(df['Sample code number'])]
df.loc[pd.isnull(df['Clump Thickness'])]
df.loc[pd.isnull(df['Uniformity of Cell Size'])]
df.loc[pd.isnull(df['Uniformity of Cell Shape'])]
df.loc[pd.isnull(df['Marginal Adhesion'])]
df.loc[pd.isnull(df['Single Epithelial Cell Size'])]
df.loc[pd.isnull(df['Bare Nuclei'])]
df.loc[pd.isnull(df['Bland Chromatin'])]
df.loc[pd.isnull(df['Normal Nucleoli'])]
df.loc[pd.isnull(df['Mitoses'])]
df.loc[pd.isnull(df['Class'])]

# Verificando a quantidade de '?'.
print(df['Bare Nuclei'].loc[df['Bare Nuclei'] == '?'].count())

# Atribuindo um valor aleatório entre 1 à 10 aos valores faltantes da coluna 'Bare Nuclei'.
df.loc[df['Bare Nuclei'] == '?', 'Bare Nuclei'] = str(random.randint(1,10))

# Separando os dados em previsores (entradas) e classe (saída)
previsores = df.iloc[:, 1:10].values
classe = df.iloc[:, 10].values


'''***************************************************************************************************************'''

'''***************************************** CLASSIFICAÇÃO - REDES NEURAIS ARTIFICIAIS *****************************************'''

from sklearn.model_selection import train_test_split #Função do pacote sklearn que divide automaticamente dados teste e dados de treinamento
from sklearn.neural_network import MLPClassifier #Importação do algoritmo e sua classe MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, mean_absolute_error

#Dividindo os dados entre 70% para treinamento e 30% para teste.
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, 
                                                                        classe, test_size=0.3, random_state=0)


#Criando a Rede Neural.
mlpC = MLPClassifier(random_state=0, learning_rate_init=0.01, max_iter=100, activation='logistic')

mlpC.fit(previsores_treinamento, classe_treinamento) #Treina o algoritmo.
resultado = mlpC.predict(previsores_teste) #Testa os dados para achar sua taxa de acerto.

accuracy = accuracy_score(classe_teste, resultado)
print('Acurácia: ' + str(accuracy))

mean_error = mean_absolute_error(classe_teste, resultado)
print('Taxa de erro: ' + str(mean_error))


#Cria uma matriz para comparação de dados dos dois atributos 
matriz = confusion_matrix(classe_teste, resultado)
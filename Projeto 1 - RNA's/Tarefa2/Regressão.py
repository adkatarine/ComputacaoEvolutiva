# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 14:40:39 2020

@author: Adlla Katarine
"""

import pandas as pd
import random
import math

'''***************************************** GERANDO DATASET *****************************************'''

lista_X = []
lista_Y = []
a = 3 # Constante da equação.

# Valores x e y do dataset são gerados.
for i in range(400):
    x = random.randint(0,400)
    lista_X.append(x)
    
    # Equação que retorna o valor de y a partir dos valores de x e a.
    y = math.sqrt(abs((2*(math.sqrt(abs((a**3)*(a + 2*x)))) ) + (2*(a**2)) + (2*a*x) - (x**2)))
    lista_Y.append(y)

data = {'x': lista_X, 'y': lista_Y} # Um dicionário é criado com os valores de x e y.
df = pd.DataFrame(data, columns=['x','y']) # Dataset é criado.


df.to_csv('.\\dataset\\dataset_XY.csv',index = False) # Dataset é salvo.

'''***************************************************************************************************************'''

# Lendo o dataframe.
df = pd.read_csv('.\\dataset\\dataset_XY.csv')

# Separando os dados em previsores (entradas) e classe (saída)
previsores = df.iloc[:, 0].values.reshape(-1, 1)
classe = df.iloc[:, 1].values.reshape(-1, 1)



'''***************************************** REGRESSÃO - REDES NEURAIS ARTIFICIAIS *****************************************'''

from sklearn.model_selection import train_test_split #Função do pacote sklearn que divide automaticamente dados teste e dados de treinamento
from sklearn.neural_network import MLPRegressor #Importação do algoritmo e sua classe MLPClassifier
from sklearn.metrics import mean_absolute_error

# Dividindo os dados entre 70% para treinamento e 30% para teste.
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, 
                                                                        classe, test_size=0.3, random_state=0)


mlpR = MLPRegressor(random_state=1, max_iter=300, solver='lbfgs', activation='identity')
mlpR.fit(previsores_treinamento, classe_treinamento) #Treina o algoritmo.
resultado = mlpR.predict(previsores_teste) #Testa os dados para achar sua taxa de acerto.

resultadoScore = mlpR.score(previsores_teste,classe_teste) # Acurácia
print('Score: ' + str(resultadoScore))

mean_error = mean_absolute_error(classe_teste, resultado) # Taxa de erro
print('Taxa de erro: ' + str(mean_error))

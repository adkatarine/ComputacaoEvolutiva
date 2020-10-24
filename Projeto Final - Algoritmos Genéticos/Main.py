# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:20:34 2020

@author: adlla
"""

from Jogo import Jogo
import pandas as pd

listaJogos = []
listaJogos.append(Jogo("Mesa de Sinuca", 0.751, 999.90, 5))
listaJogos.append(Jogo("Máquina de Pinball", 0.199, 2911.12, 2))
listaJogos.append(Jogo("Pebolim", 0.400, 1346.99, 3))
listaJogos.append(Jogo("Pingue-Pongue", 0.390, 2999.90, 3))
listaJogos.append(Jogo("Mesa de Jogo Poker/Truco", 0.300, 1999.00, 5))
listaJogos.append(Jogo("Mesa de Hockey", 0.350, 2499.90, 3))
listaJogos.append(Jogo("Mesa de Xadrez", 0.596, 499.90, 4))
listaJogos.append(Jogo("Mesa de Futebol de Botão", 0.0499, 508.66, 1))
listaJogos.append(Jogo("Máquina de Fliperama", 0.0599, 429.90, 4))
listaJogos.append(Jogo("Mesa Arcade", 0.319, 499.29, 2))
listaJogos.append(Jogo("Boliche", 0.835, 849.00, 4))

espacos = []
valores = []
precos = []
nomes = []

for jogo in listaJogos:
    nomes.append(jogo.nome)
    espacos.append(jogo.espaco)
    valores.append(jogo.valor)
    precos.append(jogo.preco)

data = {'Nome': nomes, 'Espaço (m²)': espacos, 'Preço (R$)': precos, 'Valor': valores} # Um dicionário é criado com os valores de x e y.
df = pd.DataFrame(data, columns=['Nome','Espaço (m²)', 'Preço (R$)', 'Valor']) # Dataset é criado.
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 10:41:47 2020

@author: adlla
"""
from Individuo import Individuo
from Jogo import Jogo

class Populacao():
    
    def __init__(self, numPopulacao, limiteEspacos, gastoMaximo):
        self.listaDeIndividuos = []
        self.listaJogos = []
        self.mediaPopulacao = 0
        self.limiteEspacos = limiteEspacos
        self.gastoMaximo = gastoMaximo
        
        self.criarListaJogos()
        descricaoJogo = []
        descricaoJogo = self.copiarAtributosJogos()
        # Cria uma população de individuos. a quantidade de individuos é recebida por parâmetro.
        for i in range(numPopulacao):
            self.listaDeIndividuos.append(Individuo(descricaoJogo[0], descricaoJogo[1], descricaoJogo[2], len(self.listaJogos)))
        self.avaliar()
        self.ordernarPopulacao()
    
    
    def criarListaJogos(self):
        self.listaJogos.append(Jogo("Mesa de Sinuca", 0.751, 999.90, 5))
        self.listaJogos.append(Jogo("Máquina de Pinball", 0.199, 2911.12, 2))
        self.listaJogos.append(Jogo("Pebolim", 0.400, 1346.99, 3))
        self.listaJogos.append(Jogo("Pingue-Pongue", 0.390, 2999.90, 3))
        self.listaJogos.append(Jogo("Mesa de Jogo Poker/Truco", 0.300, 1999.00, 5))
        self.listaJogos.append(Jogo("Mesa de Hockey", 0.350, 2499.90, 3))
        self.listaJogos.append(Jogo("Mesa de Xadrez", 0.596, 499.90, 4))
        self.listaJogos.append(Jogo("Mesa de Futebol de Botão", 0.0499, 508.66, 1))
        self.listaJogos.append(Jogo("Máquina de Fliperama", 0.0599, 429.90, 4))
        self.listaJogos.append(Jogo("Mesa Arcade", 0.319, 499.29, 2))
        self.listaJogos.append(Jogo("Boliche", 0.835, 849.00, 4))
        

    '''  '''
    def copiarAtributosJogos(self):
        espacos = []
        valores = []
        precos = []
        descricaoJogo = []
        for jogo in self.listaJogos:
            espacos.append(jogo.espaco)
            valores.append(jogo.valor)
            precos.append(jogo.preco)
        descricaoJogo.append(espacos)
        descricaoJogo.append(precos)
        descricaoJogo.append(valores)
        return descricaoJogo
            
    ''' Compara o melhor indivíduo da geração atual com o melhor indivíduo das gerações anteriores e retorna
    o melhor entre os dois. '''
    def melhorIndividuo(self, melhorSolucao):
        if self.listaDeIndividuos[0].getFitness() > melhorSolucao.fitness:
            melhorSolucao = self.listaDeIndividuos[0]
        return melhorSolucao
    
    
    def setListaDeIndividuos(self, listaDeIndividuos):
        self.listaDeIndividuos = listaDeIndividuos
    
    
    def ordernarPopulacao(self):
        self.setListaDeIndividuos(sorted(self.listaDeIndividuos, key = Individuo.getFitness, reverse=True))

    
    def avaliar(self):
        for individuo in self.listaDeIndividuos:
            individuo.avaliar(self.limiteEspacos, self.gastoMaximo)


    def printPopulacao(self):
        for individuo in self.listaDeIndividuos:
            individuo.printCromossomo()
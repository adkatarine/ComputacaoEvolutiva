# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 10:41:36 2020

@author: adlla
"""

from random import randint
from random import random

class Individuo():
    
    def __init__(self, qtdJogos, geracao=0):
        #self.espacos = espacos
        #self.valores = valores
        #self.limiteEspacos = limiteEspacos # limite mínimo e máximo que poderá ser usado
        self.fitness = 0
        self.espacoUsado = 0
        self.precoTotal = 0
        self.geracao = geracao
        self.cromossomo = []
        
        for i in range(qtdJogos):
            if random() < 0.5:
                self.cromossomo.append('0')
            else:
                self.cromossomo.append('1')
                
    def setCromossomo(self, cromossomo):
        self.cromossomo = cromossomo

    
    def setEspacoUsado(self, espacoUsado):
        self.espacoUsado = espacoUsado
    
    def setPrecoTotal(self, precoTotal):
        self.precoTotal = precoTotal
    
    def setFitness(self, fitness):
        self.fitness = fitness
    
    def getFitness(self):
        return self.fitness
    
    ''' Atualiza a geração do individuo. '''
    def setGeracao(self, geracao):
        self.geracao = geracao + 1
    
    
    ''' Faz a mutação(ou não) do cromossomo a partir da taxa de mutação. '''
    def mutarBit(self, taxaMutacao, qtdJogos):
        if(random() < taxaMutacao):
            i = randint(0, qtdJogos-1)
            if self.cromossomo[i] == '1':
                self.cromossomo[i] = '0'
            else:
                self.cromossomo[i] = '1'
    
    def printCromossomo(self):
        print('Cromossomo: {}  Fitness: {} Espaço Usado: {} Valor Gasto: {}'. format(self.cromossomo,
                                                                  self.fitness, self.espacoUsado, self.precoTotal))
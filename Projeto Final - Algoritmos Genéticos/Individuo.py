# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 10:41:36 2020

@author: adlla
"""

from random import randint
from random import random

class Individuo():
    
    def __init__(self, espacos, precos, valores, qtdJogos, geracao=0):
        self.espacos = espacos
        self.valores = valores
        self.precos = precos
        self.fitness = 0
        self.espacoUsado = 0
        self.precoTotal = 0
        self.geracao = geracao
        self.cromossomo = []
        
        for i in range(qtdJogos):
            if random() < 0.5:
                self.cromossomo.append(0)
            else:
                self.cromossomo.append(1)
                
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
    
    ''' Função de avaliação do indivíduo. Calcula o fitness atual e verifica se os limites de espaço e valor
    máximo gasto para compra foram ultrapassados. Caso tenha sido o valor do fitness será 1.'''
    def avaliar(self, limiteEspacos, gastoMaximo):
        fitness = 0
        espacoUsado = 0
        precoTotal = 0
        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] == 1:
                    fitness += self.valores[i]*self.espacos[i]
                    espacoUsado += self.espacos[i]
                    precoTotal += self.precos[i]
                    
        if ((espacoUsado < limiteEspacos[0] or espacoUsado > limiteEspacos[1]) or precoTotal > gastoMaximo):
            fitness = 1
        self.fitness = fitness
        self.espacoUsado = espacoUsado
        self.precoTotal = precoTotal
    
    ''' Faz a mutação(ou não) do cromossomo a partir da taxa de mutação. '''
    def mutarBit(self, taxaMutacao, qtdJogos):
        if(random() < taxaMutacao):
            i = randint(0, qtdJogos-1)
            if self.cromossomo[i] == 1:
                self.cromossomo[i] = 0
            else:
                self.cromossomo[i] = 1
    
    def printCromossomo(self):
        print('Cromossomo: {}  Fitness: {} Espaço Usado: {} Valor Gasto: {}'. format(self.cromossomo,
                                                                  self.fitness, self.espacoUsado, self.precoTotal))